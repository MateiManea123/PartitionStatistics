# Disk File Analysis Tool

## Overview
This project is a Python-based tool for analyzing the contents of a disk, partition, or directory.
It recursively traverses the filesystem, collects statistics about files and directories, and presents both textual and visual summaries of file-type distribution.

The tool is designed to be **robust**, **cross-platform**, and safe to run on real systems with restricted permissions.

---

## Features
- Recursive directory traversal
- Counts total files and directories
- Groups files by extension (case-insensitive)
- Uses `<no-ext>` for files without extensions
- Calculates relative proportions by file count and total size
- Aggregates minor file types into an `Other` category
- Generates visual charts using Matplotlib
- Gracefully handles permission errors, long paths, and encoding issues

---

## Requirements
- Python 3.8 or newer
- Matplotlib

Install dependency:
```bash
pip install matplotlib
```

---

## Usage
Run the script by providing a path to analyze:

```bash
python analize_partition.py <path>
```

### Examples (macOS / Linux)
```bash
python analize_partition.py ~
python analize_partition.py /Users/username/Documents
python analize_partition.py /Volumes/ExternalDisk
```

### Windows
```bash
python analize_partition.py D
```

---

## Implementation Phases

### Phase 1 — Traversal & Raw Metrics
The program recursively walks the directory tree using `os.walk`, counting files and directories while collecting raw statistics per file extension.

### Phase 2 — Data Aggregation & Proportions
Raw metrics are converted into relative percentages.
Results are sorted and minor file types are grouped into an `Other` category for improved readability.

### Phase 3 — Chart Generation
The tool generates four charts:
- Pie chart showing file distribution by count
- Pie chart showing file distribution by total size
- Bar chart for top file types by count
- Bar chart for top file types by size (logarithmic scale)

All charts are displayed interactively and saved as PNG files in the `charts/` directory.

### Phase 4 — Error Handling & Validation
The program validates input paths before scanning and safely skips inaccessible directories or files.
Symbolic links are ignored to prevent infinite recursion, and non-UTF8 filenames are handled without interrupting execution.

---

## Output
Console summary with formatted percentages and totals.

Generated chart files are saved in:
```
charts/
 ├── pie_count.png
 ├── pie_size.png
 ├── bar_count.png
 └── bar_size.png
```
