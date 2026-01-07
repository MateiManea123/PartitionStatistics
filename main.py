#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import platform

from chart_generator import generate_charts
from path_traverser import traverse_path
from row_builder import build_rows, top_with_other, print_phase2_table
from safe_utils import normalize_root, validate_root_exists, safe_text
TOP_N = 10


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_or_drive>")
        print("mac examples:")
        print("  python main.py ~")
        print("  python main.py /Users/yourname")
        print("  python main.py /Volumes/MyDisk")
        print("windows examples:")
        print("  python main.py D")
        print("  python main.py D:\\")
        sys.exit(1)

    try:
        root = normalize_root(sys.argv[1])
        validate_root_exists(root)
    except Exception as e:
        print(f"Error: {safe_text(e)}")
        sys.exit(2)

    print(f"Platform: {platform.system()} ({os.name})")
    print(f"Root path: {safe_text(root)}")

    total_dirs, total_files, stats, errors = traverse_path(root)

    print(f"Total directories: {total_dirs}")
    print(f"Total files:       {total_files}")
    print("\nSkipped/Errors summary:")
    print(f"  Unreadable directories skipped: {errors['dir_skips']}")
    print(f"  Walk errors (os.walk onerror):  {errors['walk_errors']}")
    print(f"  File size read errors:          {errors['file_size_errors']}")

    rows, _ = build_rows(stats, total_files)

    data_by_count = top_with_other(rows, key_name="count", top_n=TOP_N)
    data_by_size  = top_with_other(rows, key_name="size",  top_n=TOP_N)

    print_phase2_table(data_by_count, "Phase 2 (sorted by count)")
    print_phase2_table(data_by_size,  "Phase 2 (sorted by size)")

    print("\nGenerating charts into ./charts ...")
    generate_charts(data_by_count, data_by_size)

if __name__ == "__main__":
    main()
