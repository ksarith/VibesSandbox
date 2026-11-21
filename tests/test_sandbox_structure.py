#!/usr/bin/env python3
"""Tests for tools/validate_sandbox.py (v0.0.9).

Run with the standard runner:  python3 -m unittest discover -s tests
Most tests build a small disposable repository, break one thing, and check that the validator
notices. One integration test runs the validator on the real repository.
"""
import io
import shutil
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate_sandbox as vs  # noqa: E402

ZIPS = ["LazarusForge-1.38.Alpha.zip", "AuditBot-V_0_0_3.zip"]
LAST = 80


def make_zip(path, member="Proj/README.md"):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as z:
        z.writestr(member, "x" * 12000)


def make_repo(tmp: Path, last=LAST):
    for d in vs.REQUIRED_DIRS:
        (tmp / d).mkdir(parents=True, exist_ok=True)
    (tmp / "Audits" / "a.md").write_text("audit\n", encoding="utf-8")
    for i in range(vs.MIN_BRIEFS):
        (tmp / f"Decision_Brief_2026-11-{i + 1:02d}.md").write_text("brief\n", encoding="utf-8")
    rows = ["| MAINT-3 | LOG-1028 | 2026-10-28 | historical |", "| MAINT-3 | LOG-1029 | 2026-10-29 | historical |"]
    for n in range(vs.FIRST_ENTRY, last + 1):
        (tmp / "Maintenance" / "entries" / f"MAINT-{n}.md").write_text(
            f"# MAINT-{n}: entry\n\n" + "body " * 40 + "\n", encoding="utf-8")
        rows.append(f"| MAINT-{n} | entries/ | 2026-11-01 | summary |")
    (tmp / "Maintenance" / "MAINT_INDEX.md").write_text("# index\n\n| ID | Home | Date | Summary |\n|---|---|---|---|\n" + "\n".join(rows) + "\n", encoding="utf-8")
    (tmp / "Maintenance" / "MAINT_LOG_2026-10-28.md").write_text("log\n", encoding="utf-8")
    (tmp / "Maintenance" / "MAINT_LOG_2026-10-29.md").write_text("log\n", encoding="utf-8")
    (tmp / "Maintenance" / "STATE_History.md").write_text("history\n", encoding="utf-8")
    (tmp / "Maintenance" / "STATE.md").write_text(f"# STATE\n\nLast updated: 2026-11-18 (MAINT-{last})\n\nSee [index](MAINT_INDEX.md).\n", encoding="utf-8")
    for z in ZIPS:
        make_zip(tmp / "Maintenance" / z)
    (tmp / "README.md").write_text("# VibesSandbox\n\nArchives: `LazarusForge-1.38.Alpha.zip`. See [state](Maintenance/STATE.md).\nNot LazarusForge doctrine.\n", encoding="utf-8")
    (tmp / "PKC_Ruling_List.md").write_text("pkc\n", encoding="utf-8")
    (tmp / "CO_AUTHOR_MANDATE.md").write_text("mandate\n", encoding="utf-8")
    ast = tmp / "Astroid-miner-AstroidMinerV0.07"
    (ast / "registry.yaml").write_text("x: 1\n", encoding="utf-8")
    (ast / "README.md").write_text("astroid\n", encoding="utf-8")
    arts = "".join(f"  - path: Maintenance/{z}\n    role: archive\n" for z in ZIPS)
    (tmp / "registry.yaml").write_text(
        "package:\n  name: VibesSandbox\n\ntop_level:\n  - README.md\n  - PKC_Ruling_List.md\n\n"
        "directories:\n  Audits: \"audits\"\n  Maintenance: \"records\"\n\nkey_artifacts:\n"
        "  - path: Maintenance/STATE.md\n    role: state\n" + arts, encoding="utf-8")


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_validate(self):
        return vs.validate(self.tmp)

    def errors(self):
        return " || ".join(self.run_validate().errors)

    def warnings(self):
        return " || ".join(self.run_validate().warnings)


class Baseline(Base):
    def test_clean_fixture_passes(self):
        r = self.run_validate()
        self.assertEqual(r.errors, [])
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.info["entries"], LAST - vs.FIRST_ENTRY + 1)

    def test_real_repository_passes(self):
        r = vs.validate(ROOT)
        self.assertEqual(r.errors, [], "\n".join(r.errors))


class MaintenanceRecords(Base):
    def test_deleting_any_entry_is_caught(self):
        """v0.0.8 only spot-checked MAINT-85/90/95/100, so deleting 101 or 150 passed."""
        for n in (vs.FIRST_ENTRY, 75, 80):
            (self.tmp / "Maintenance" / "entries" / f"MAINT-{n}.md").unlink()
            self.assertIn(f"MAINT-{n}", self.errors(), n)
            make_repo(self.tmp)

    def test_deleting_the_highest_entry_is_caught_by_the_index(self):
        (self.tmp / "Maintenance" / "entries" / f"MAINT-{LAST}.md").unlink()
        self.assertIn(f"lists entries/ rows with no file: MAINT-{LAST}", self.errors())

    def test_gap_is_named(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-75.md").unlink()
        self.assertIn("gaps: MAINT-75", self.errors())

    def test_empty_entry_is_caught(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-72.md").write_text("", encoding="utf-8")
        self.assertIn("MAINT-72.md: file is empty", self.errors())

    def test_heading_must_name_its_own_id(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-72.md").write_text("# MAINT-73: wrong\n" + "x" * 200, encoding="utf-8")
        self.assertIn("MAINT-72.md: first line does not name MAINT-72", self.errors())

    def test_both_heading_levels_are_accepted(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-72.md").write_text("## MAINT-72: ok\n" + "x" * 200, encoding="utf-8")
        self.assertEqual(self.run_validate().errors, [])

    def test_unindexed_file_is_caught(self):
        idx = self.tmp / "Maintenance" / "MAINT_INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("| MAINT-77 | entries/ | 2026-11-01 | summary |\n", ""), encoding="utf-8")
        self.assertIn("files with no MAINT_INDEX.md row: MAINT-77", self.errors())

    def test_duplicate_index_row_is_caught(self):
        idx = self.tmp / "Maintenance" / "MAINT_INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8") + "| MAINT-77 | entries/ | 2026-11-01 | again |\n", encoding="utf-8")
        self.assertIn("more than once: MAINT-77", self.errors())

    def test_historical_log_rows_need_no_entry_file(self):
        self.assertEqual(self.run_validate().errors, [])

    def test_entries_must_start_at_69(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-69.md").unlink()
        idx = self.tmp / "Maintenance" / "MAINT_INDEX.md"
        idx.write_text(idx.read_text(encoding="utf-8").replace("| MAINT-69 | entries/ | 2026-11-01 | summary |\n", ""), encoding="utf-8")
        self.assertIn("should start at MAINT-69", self.errors())

    def test_unexpected_entry_name(self):
        (self.tmp / "Maintenance" / "entries" / "MAINT-X.md").write_text("x", encoding="utf-8")
        self.assertIn("unexpected name", self.errors())

    def test_empty_index_is_caught(self):
        (self.tmp / "Maintenance" / "MAINT_INDEX.md").write_text("# nothing here\n", encoding="utf-8")
        self.assertIn("no `entries/` rows", self.errors())


class RegistryAndStructure(Base):
    def test_missing_root_registry_is_caught(self):
        (self.tmp / "registry.yaml").unlink()
        self.assertIn("MISSING FILE: registry.yaml", self.errors())

    def test_registry_naming_a_missing_artifact_is_caught(self):
        reg = self.tmp / "registry.yaml"
        reg.write_text(reg.read_text(encoding="utf-8") + "  - path: Maintenance/Ghost.zip\n    role: x\n", encoding="utf-8")
        self.assertIn("key_artifacts names a path that does not exist: Maintenance/Ghost.zip", self.errors())

    def test_registry_naming_a_missing_top_level_file_or_directory(self):
        reg = self.tmp / "registry.yaml"
        reg.write_text(reg.read_text(encoding="utf-8").replace("  - PKC_Ruling_List.md\n", "  - PKC_Ruling_List.md\n  - Ghost.md\n").replace('  Maintenance: "records"\n', '  Maintenance: "records"\n  Ghostdir: "x"\n'), encoding="utf-8")
        e = self.errors()
        self.assertIn("top_level names a path that does not exist: Ghost.md", e)
        self.assertIn("directories names a directory that does not exist: Ghostdir", e)

    def test_unreadable_registry_is_caught(self):
        (self.tmp / "registry.yaml").write_text("nonsense\n", encoding="utf-8")
        self.assertIn("no top_level, directories or key_artifacts could be read", self.errors())

    def test_missing_required_directory_and_empty_file(self):
        shutil.rmtree(self.tmp / "Proposals")
        (self.tmp / "PKC_Ruling_List.md").write_text("", encoding="utf-8")
        e = self.errors()
        self.assertIn("MISSING DIR: Proposals", e)
        self.assertIn("EMPTY FILE: PKC_Ruling_List.md", e)

    def test_too_few_briefs_and_empty_audits(self):
        for f in list(self.tmp.glob("Decision_Brief_*.md"))[:3]:
            f.unlink()
        (self.tmp / "Audits" / "a.md").unlink()
        e = self.errors()
        self.assertIn("too few Decision_Brief_*.md", e)
        self.assertIn("Audits/ is empty", e)


class Archives(Base):
    def test_truncated_zip_is_caught(self):
        z = self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip"
        z.write_bytes(z.read_bytes()[:11000])
        self.assertIn("cannot be opened as a zip", self.errors())

    def test_crc_corruption_is_caught(self):
        z = self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip"
        data = bytearray(z.read_bytes())
        data[100] ^= 0xFF           # inside the stored member data
        z.write_bytes(bytes(data))
        self.assertIn("CRC failure", self.errors())

    def test_junk_file_named_zip_is_caught(self):
        (self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip").write_bytes(b"x" * 20000)
        self.assertIn("cannot be opened as a zip", self.errors())

    def test_unsafe_member_path_is_caught(self):
        make_zip(self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip", member="../evil.txt")
        self.assertIn("unsafe member path", self.errors())

    def test_tiny_zip_is_caught(self):
        with zipfile.ZipFile(self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip", "w") as z:
            z.writestr("a", "b")
        self.assertIn("too small", self.errors())

    def test_required_release_archive_must_exist(self):
        (self.tmp / "Maintenance" / "LazarusForge-1.38.Alpha.zip").unlink()
        self.assertIn("MISSING NESTED ZIP: Maintenance/LazarusForge-1.38.Alpha.zip", self.errors())

    def test_every_zip_is_checked_not_just_the_release(self):
        (self.tmp / "Maintenance" / "AuditBot-V_0_0_3.zip").write_bytes(b"x" * 20000)
        self.assertNotIn("LazarusForge", self.errors())
        self.assertIn("AuditBot-V_0_0_3.zip", self.errors())

    def test_unlisted_zip_is_a_warning_not_an_error(self):
        make_zip(self.tmp / "Maintenance" / "Other-V1.zip")
        r = self.run_validate()
        self.assertEqual(r.errors, [])
        self.assertIn("Other-V1.zip: not listed in registry.yaml", " ".join(r.warnings))


class DocumentsAndState(Base):
    def test_readme_naming_a_missing_archive_is_caught(self):
        """The stale 1.33/1.34 references that survived into v0.0.8."""
        readme = self.tmp / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "Also `LazarusForge-1.33.Alpha.zip`.\n", encoding="utf-8")
        self.assertIn("names an archive that is not under Maintenance/: LazarusForge-1.33.Alpha.zip", self.errors())

    def test_broken_relative_link_is_caught(self):
        readme = self.tmp / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "[gone](Nope/Missing.md)\n[web](https://example.com/x.md)\n[anchor](#top)\n", encoding="utf-8")
        e = self.errors()
        self.assertIn("README.md: broken relative link: Nope/Missing.md", e)
        self.assertNotIn("example.com", e)
        self.assertNotIn("#top", e)

    def test_link_with_anchor_resolves_by_file(self):
        readme = self.tmp / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "[s](Maintenance/STATE.md#top)\n", encoding="utf-8")
        self.assertEqual(self.run_validate().errors, [])

    def test_state_without_last_updated_line_is_caught(self):
        (self.tmp / "Maintenance" / "STATE.md").write_text("garbage\n", encoding="utf-8")
        self.assertIn("no \"Last updated", self.errors())

    def test_state_behind_the_highest_entry_is_a_warning(self):
        (self.tmp / "Maintenance" / "STATE.md").write_text("Last updated: 2026-11-10 (MAINT-70)\n", encoding="utf-8")
        r = self.run_validate()
        self.assertEqual(r.errors, [])
        self.assertIn(f"highest entry is MAINT-{LAST}", " ".join(r.warnings))


class Cli(Base):
    def run_cli(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = vs.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_exit_codes(self):
        code, out, _ = self.run_cli(["--root", str(self.tmp)])
        self.assertEqual(code, 0)
        self.assertIn("PASSED", out)
        (self.tmp / "Maintenance" / "entries" / "MAINT-75.md").unlink()
        code, out, _ = self.run_cli(["--root", str(self.tmp)])
        self.assertEqual(code, 1)
        self.assertIn("FAILED", out)
        self.assertIn("ERROR", out)
        code, _, err = self.run_cli(["--root", str(self.tmp / "nope")])
        self.assertEqual(code, 2)

    def test_report_always_lists_what_was_not_inspected(self):
        _, out, _ = self.run_cli(["--root", str(self.tmp)])
        self.assertIn("Not inspected:", out)
        self.assertIn("live GitHub repositories", out)


class Discovery(unittest.TestCase):
    def test_the_standard_runner_finds_these_tests(self):
        loaded = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
        self.assertGreater(loaded.countTestCases(), 25)


if __name__ == "__main__":
    unittest.main()
