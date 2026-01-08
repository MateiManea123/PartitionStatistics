import os

def safe_text(s: object) -> str:

    try:
        return str(s)
    except Exception:
        return repr(s)

def normalize_root(arg: str) -> str:

    a = arg.strip()
    if not a:
        raise ValueError("Empty path/drive argument.")

    a = os.path.expanduser(a)

    if os.name == "nt":
        if len(a) == 1 and a.isalpha():
            a = a + ":\\"
        elif len(a) == 2 and a[1] == ":":
            a = a + "\\"

    return os.path.normpath(a)

def validate_root_exists(root: str) -> None:
    if not os.path.exists(root):
        raise FileNotFoundError(f"Path does not exist: {safe_text(root)}")
    if not os.path.isdir(root):
        raise NotADirectoryError(f"Not a directory: {safe_text(root)}")
