# Tsygankov_HW3_1
import shutil
from pathlib import Path
import argparse

COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))

def copy_and_sort(source_dir: Path, dest_dir: Path) -> None:
    for item in source_dir.iterdir():
        if item.is_dir():
            copy_and_sort(item, dest_dir)
        else:
            extension = item.suffix[1:]
            destination = dest_dir / extension
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, destination)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy and sort files.")
    parser.add_argument("source", help="Path to the source directory.")
    parser.add_argument("destination", nargs="?", default="dist", help="Path to the destination directory (default: dist).")
    args = parser.parse_args()

    source_path = Path(args.source)
    dest_path = Path(args.destination)

    if not source_path.exists():
        print(f"Error: Source directory '{source_path}' does not exist.")

    copy_and_sort(source_path, dest_path)
    print(f"Files copied and sorted. Destination directory: {dest_path}")
    display_tree(dest_path)

