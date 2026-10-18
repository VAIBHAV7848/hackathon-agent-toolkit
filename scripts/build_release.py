#!/usr/bin/env python3
"""Build a deterministic ZIP release of the current toolkit directory."""
from __future__ import annotations
import argparse
import hashlib
import os
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".venv", "venv", "__pycache__", "dist", ".pytest_cache"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default=str(ROOT / "dist"), help="Output directory (default: ./dist)")
    args = parser.parse_args()
    version_file = ROOT / "VERSION"
    if not version_file.is_file():
        parser.error("VERSION file is missing")
    version = version_file.read_text(encoding="utf-8").strip()
    if not version or any(c not in "0123456789." for c in version):
        parser.error(f"Invalid numeric version: {version!r}")

    output = Path(args.output_dir).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    archive_path = output / f"hackathon-ai-toolkit-universal-v{version}.zip"
    root_name = f"hackathon-ai-toolkit-universal-v{version}"
    # A fixed date supports reproducible outputs for identical input bytes.
    # SOURCE_DATE_EPOCH is deliberately optional; use it only when a release
    # pipeline wants another stable timestamp.
    epoch = int(os.environ.get("SOURCE_DATE_EPOCH", "1792281600"))  # 2026-10-18 UTC
    import datetime
    dt = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc)
    zip_dt = (max(1980, dt.year), dt.month, dt.day, dt.hour, dt.minute, dt.second - dt.second % 2)

    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        if path.suffix in {".pyc", ".pyo"} or path.name == ".DS_Store":
            continue
        if path.resolve() == archive_path or output == path.parent:
            continue
        files.append((path, rel.as_posix()))
    files.sort(key=lambda item: item[1])

    tmp = archive_path.with_suffix(".zip.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9, strict_timestamps=True) as archive:
        for path, rel in files:
            info = zipfile.ZipInfo(f"{root_name}/{rel}", date_time=zip_dt)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            mode = path.stat().st_mode
            info.external_attr = ((mode & 0xFFFF) << 16) | 0x20
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    tmp.replace(archive_path)
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    sums = output / "SHA256SUMS"
    sums.write_text(f"{digest}  {archive_path.name}\n", encoding="utf-8")
    with zipfile.ZipFile(archive_path) as archive:
        corrupt = archive.testzip()
        if corrupt:
            archive_path.unlink(missing_ok=True)
            parser.error(f"ZIP integrity verification failed at {corrupt}")
    print(f"Built: {archive_path}")
    print(f"Files: {len(files)}")
    print(f"SHA-256: {digest}")
    print(f"Manifest: {sums}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
