#!/usr/bin/env python3
"""validate_sandbox.py: structural integrity gate for VibesSandbox (v0.0.9, hardened).

What it enforces (errors fail the run; warnings are reported):
  1. Required directories and files exist and are not empty, including the root registry.yaml.
  2. Everything the root registry.yaml names (top_level, directories, key_artifacts) exists.
  3. Maintenance entries MAINT-69.. are contiguous (no gaps, no duplicates), each non-empty,
     each starting with a heading that names its own id.
  4. MAINT_INDEX.md reconciles with the entries/ directory in BOTH directions: every `entries/`
     row has a file and every file has a row. Rows whose home is a frozen log (LOG-1028, LOG-1029)
     are historical and are not required to have an entry file.
  5. Every .zip under Maintenance/ opens, passes its CRC check, and has no unsafe member path;
     the required release archive is present. (Warning: a zip the registry does not list.)
  6. Every zip name the root README mentions exists under Maintenance/.
  7. Relative Markdown links in the root documents and the Maintenance records resolve.
  8. STATE.md carries a "Last updated: DATE (MAINT-N)" line (warning if N is not the highest entry).
  9. Decision briefs and Audits/ are present.

It always prints what it did NOT inspect. Exit codes: 0 no errors, 1 problems found, 2 usage error.
Standard library only.

Usage:
    python3 tools/validate_sandbox.py [--root PATH]
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

VERSION = "0.0.9"
FIRST_ENTRY = 69          # entries/ holds MAINT-69 onward; earlier ids live in the frozen logs
MIN_ZIP_BYTES = 10_000
MIN_BRIEFS = 10
MIN_ENTRY_BYTES = 100

REQUIRED_DIRS = ["Audits", "Maintenance", "Maintenance/entries", "Proposals",
                 "Astroid-miner-AstroidMinerV0.07", "tools", "tests"]
REQUIRED_FILES = ["README.md", "PKC_Ruling_List.md", "registry.yaml",
                  "Maintenance/STATE.md", "Maintenance/STATE_History.md", "Maintenance/MAINT_INDEX.md",
                  "Maintenance/MAINT_LOG_2026-10-28.md", "Maintenance/MAINT_LOG_2026-10-29.md",
                  "Astroid-miner-AstroidMinerV0.07/registry.yaml", "Astroid-miner-AstroidMinerV0.07/README.md"]
REQUIRED_ZIPS = ["Maintenance/LazarusForge-1.38.Alpha.zip"]
LINK_FILES = ["README.md", "CO_AUTHOR_MANDATE.md", "PKC_Ruling_List.md",
              "Maintenance/STATE.md", "Maintenance/MAINT_INDEX.md"]

NOT_INSPECTED = [
    "contents of the nested project archives beyond opening, CRC and path safety (each project has its own tests)",
    "the inside of the Astroid-miner snapshot (its own tests and registry are separate)",
    "whether any entry's text is correct, ratified, or consistent with LazarusForge doctrine",
    "external URLs and the live GitHub repositories",
    "semantic staleness in prose (only zip names and relative links are checked)",
]


class Result:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: dict[str, object] = {}

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def parse_registry(text: str):
    """Minimal reader for the registry's three lists. No YAML library needed."""
    top, dirs, arts = [], [], []
    section = None
    for line in text.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_]+):\s*$", line)
        if m:
            section = m.group(1)
            continue
        if re.match(r"^[A-Za-z_]+:", line):
            section = None
            continue
        if section == "top_level":
            m = re.match(r"^\s+-\s+(\S.*?)\s*$", line)
            if m:
                top.append(m.group(1).strip("\"'"))
        elif section == "directories":
            m = re.match(r"^\s+([^\s:][^:]*?):\s", line)
            if m:
                dirs.append(m.group(1).strip("\"'"))
        elif section == "key_artifacts":
            m = re.match(r"^\s+-\s+path:\s*(\S.*?)\s*$", line)
            if m:
                arts.append(m.group(1).strip("\"'"))
    return top, dirs, arts


def check_structure(root: Path, r: Result):
    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            r.err(f"MISSING DIR: {d}")
    for f in REQUIRED_FILES:
        p = root / f
        if not p.is_file():
            r.err(f"MISSING FILE: {f}")
        elif p.stat().st_size == 0:
            r.err(f"EMPTY FILE: {f}")


def check_registry(root: Path, r: Result):
    p = root / "registry.yaml"
    if not p.is_file():
        return
    top, dirs, arts = parse_registry(read(p))
    if not (top or dirs or arts):
        r.err("registry.yaml: no top_level, directories or key_artifacts could be read")
    for t in top:
        if not (root / t).exists():
            r.err(f"registry.yaml top_level names a path that does not exist: {t}")
    for d in dirs:
        if not (root / d).is_dir():
            r.err(f"registry.yaml directories names a directory that does not exist: {d}")
    for a in arts:
        if not (root / a).exists():
            r.err(f"registry.yaml key_artifacts names a path that does not exist: {a}")
    r.info["registry_artifacts"] = set(arts)


def check_entries_and_index(root: Path, r: Result):
    entries_dir = root / "Maintenance" / "entries"
    index_path = root / "Maintenance" / "MAINT_INDEX.md"
    on_disk: dict[int, Path] = {}
    if entries_dir.is_dir():
        for f in sorted(entries_dir.glob("MAINT-*.md")):
            m = re.fullmatch(r"MAINT-(\d+)\.md", f.name)
            if not m:
                r.err(f"entries/ file with an unexpected name: {f.name}")
                continue
            n = int(m.group(1))
            on_disk[n] = f
            if f.stat().st_size < MIN_ENTRY_BYTES:
                r.err(f"entries/{f.name}: file is empty or nearly empty ({f.stat().st_size} bytes)")
                continue
            first = next((ln for ln in read(f).split("\n") if ln.strip()), "")
            if not re.match(rf"^#{{1,2}}\s*MAINT-{n}\b", first):
                r.err(f"entries/{f.name}: first line does not name MAINT-{n}: {first[:60]!r}")
    if not on_disk:
        r.err("entries/ contains no MAINT-*.md files")
        return
    lo, hi = min(on_disk), max(on_disk)
    if lo != FIRST_ENTRY:
        r.err(f"entries/ should start at MAINT-{FIRST_ENTRY}; lowest is MAINT-{lo}")
    gaps = [i for i in range(lo, hi + 1) if i not in on_disk]
    if gaps:
        r.err("entries/ has gaps: " + ", ".join(f"MAINT-{i}" for i in gaps))
    r.info["entries"] = len(on_disk)
    r.info["highest_entry"] = hi

    if index_path.is_file():
        text = read(index_path)
        indexed = [int(m) for m in re.findall(r"^\| MAINT-(\d+) \| entries/ \|", text, re.M)]
        dup = sorted({n for n in indexed if indexed.count(n) > 1})
        if dup:
            r.err("MAINT_INDEX.md lists entries/ rows more than once: " + ", ".join(f"MAINT-{n}" for n in dup))
        idx = set(indexed)
        if not idx:
            r.err("MAINT_INDEX.md has no `entries/` rows")
        missing_files = sorted(idx - set(on_disk))
        missing_rows = sorted(set(on_disk) - idx)
        if missing_files:
            r.err("MAINT_INDEX.md lists entries/ rows with no file: " + ", ".join(f"MAINT-{n}" for n in missing_files))
        if missing_rows:
            r.err("entries/ files with no MAINT_INDEX.md row: " + ", ".join(f"MAINT-{n}" for n in missing_rows))
        r.info["index_rows"] = len(idx)


def check_zips(root: Path, r: Result):
    maint = root / "Maintenance"
    if not maint.is_dir():
        return
    for z in REQUIRED_ZIPS:
        if not (root / z).is_file():
            r.err(f"MISSING NESTED ZIP: {z}")
    listed = r.info.get("registry_artifacts", set())
    zips = sorted(maint.glob("*.zip"))
    r.info["zips"] = len(zips)
    for z in zips:
        rel = z.relative_to(root).as_posix()
        if z.stat().st_size < MIN_ZIP_BYTES:
            r.err(f"{rel}: too small to be a release archive ({z.stat().st_size} bytes)")
            continue
        try:
            with zipfile.ZipFile(z) as zf:
                bad = zf.testzip()
                if bad:
                    r.err(f"{rel}: CRC failure in member {bad}")
                for n in zf.namelist():
                    parts = n.replace("\\", "/").split("/")
                    if n.startswith("/") or ".." in parts:
                        r.err(f"{rel}: unsafe member path {n!r}")
        except (zipfile.BadZipFile, OSError) as e:
            r.err(f"{rel}: cannot be opened as a zip ({e})")
        if listed and rel not in listed:
            r.warn(f"{rel}: not listed in registry.yaml key_artifacts")


def check_readme_zip_names(root: Path, r: Result):
    p = root / "README.md"
    if not p.is_file():
        return
    names = set(re.findall(r"`([^`\s/]+\.zip)`", read(p)))
    for n in sorted(names):
        if not (root / "Maintenance" / n).is_file():
            r.err(f"README.md names an archive that is not under Maintenance/: {n}")


def check_links(root: Path, r: Result):
    for rel in LINK_FILES:
        p = root / rel
        if not p.is_file():
            continue
        for m in re.findall(r"\]\(([^)\s]+)\)", read(p)):
            if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:|#", m):
                continue
            target = m.split("#")[0]
            if target and not (p.parent / target).resolve().exists():
                r.err(f"{rel}: broken relative link: {m}")


def check_state(root: Path, r: Result):
    p = root / "Maintenance" / "STATE.md"
    if not p.is_file():
        return
    m = re.search(r"^Last updated:\s*(\d{4}-\d{2}-\d{2})\s*\(MAINT-(\d+)\)", read(p), re.M)
    if not m:
        r.err('Maintenance/STATE.md has no "Last updated: YYYY-MM-DD (MAINT-N)" line')
        return
    hi = r.info.get("highest_entry")
    if hi is not None and int(m.group(2)) != hi:
        r.warn(f"STATE.md says it was last updated at MAINT-{m.group(2)}, but the highest entry is MAINT-{hi}")


def check_misc(root: Path, r: Result):
    briefs = list(root.glob("Decision_Brief_*.md"))
    r.info["briefs"] = len(briefs)
    if len(briefs) < MIN_BRIEFS:
        r.err(f"too few Decision_Brief_*.md files: found {len(briefs)}, expected at least {MIN_BRIEFS}")
    a = root / "Audits"
    if a.is_dir() and not any(a.iterdir()):
        r.err("Audits/ is empty")


def validate(root: Path) -> Result:
    r = Result()
    check_structure(root, r)
    check_registry(root, r)
    check_entries_and_index(root, r)
    check_zips(root, r)
    check_readme_zip_names(root, r)
    check_links(root, r)
    check_state(root, r)
    check_misc(root, r)
    return r


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="VibesSandbox structural validation")
    ap.add_argument("--root", default=None, help="repository root (default: the parent of tools/)")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2
    r = validate(root)
    ok = not r.errors
    print(f"VibesSandbox structural validation {'PASSED' if ok else 'FAILED'} (validate_sandbox {VERSION})")
    for e in r.errors:
        print(f"  ERROR   {e}")
    for w in r.warnings:
        print(f"  warning {w}")
    print(f"  {len(r.errors)} error(s), {len(r.warnings)} warning(s)")
    print(f"  entries {r.info.get('entries', 0)} (MAINT-{FIRST_ENTRY}..{r.info.get('highest_entry', '?')}), "
          f"index rows {r.info.get('index_rows', 0)}, nested zips {r.info.get('zips', 0)}, decision briefs {r.info.get('briefs', 0)}")
    print("  Not inspected:")
    for n in NOT_INSPECTED:
        print(f"    - {n}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
