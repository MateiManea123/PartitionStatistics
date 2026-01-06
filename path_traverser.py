import os

NO_EXT = "<no-ext>"


def get_extension_key(filename: str) -> str:
    base = os.path.basename(filename)

    if base.startswith(".") and base.count(".") == 1:
        return NO_EXT

    _, ext = os.path.splitext(base)
    if not ext:
        return NO_EXT

    return ext[1:].lower()

def traverse_path(root_path: str):

    total_dirs = 0
    total_files = 0
    stats = {}

    errors = {
        "dir_skips": 0,
        "file_size_errors": 0,
        "walk_errors": 0,
    }

    def on_walk_error(err):
        errors["walk_errors"] += 1

    for dirpath, dirnames, filenames in os.walk(
        root_path,
        topdown=True,
        followlinks=False,
        onerror=on_walk_error
    ):
        kept = []
        for d in dirnames:
            full = os.path.join(dirpath, d)
            try:
                os.listdir(full)
                kept.append(d)
            except (PermissionError, FileNotFoundError, OSError):
                errors["dir_skips"] += 1
        dirnames[:] = kept

        total_dirs += len(dirnames)

        for name in filenames:
            total_files += 1
            full_path = os.path.join(dirpath, name)
            ext_key = get_extension_key(name)

            try:
                size = os.path.getsize(full_path)
            except (PermissionError, FileNotFoundError, OSError):
                size = 0
                errors["file_size_errors"] += 1

            if ext_key not in stats:
                stats[ext_key] = [0, 0]

            stats[ext_key][0] += 1
            stats[ext_key][1] += size

    return total_dirs, total_files, stats, errors