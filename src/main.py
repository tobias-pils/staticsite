import sys
import os
import shutil
from markdown.conversion import generate_page

STATIC_PATH = "static"
CONTENT_PATH = "content"
TEMPLATE_PATH = "template.html"
PUBLIC_PATH = "docs"

def clear_public_dir():
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)

def copy_static_files(sub_path=""):
    path = os.path.join(STATIC_PATH, sub_path)
    if os.path.exists(path):
        filenames = os.listdir(path)
        for filename in filenames:
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                copy_static_files(os.path.join(sub_path, filename))
            else:
                dest_dir = os.path.join(PUBLIC_PATH, sub_path)
                if not os.path.exists(dest_dir):
                    print(f"make dir {dest_dir}")
                    os.mkdir(dest_dir)
                print(f"copy file {filename}")
                shutil.copy(file_path, os.path.join(dest_dir, filename))

def generate_pages(base_path, sub_path=""):
    path = os.path.join(CONTENT_PATH, sub_path)
    if os.path.exists(path):
        filenames = os.listdir(path)
        for filename in filenames:
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                generate_pages(base_path, os.path.join(sub_path, filename))
            else:
                dest_filename = filename.removesuffix(".md") + ".html"
                dest_dir = os.path.join(PUBLIC_PATH, sub_path)
                generate_page(base_path, file_path, TEMPLATE_PATH, os.path.join(dest_dir, dest_filename))


def main():
    base_path = "/"
    if (len(sys.argv) > 2):
        raise Exception("Usage: main.py [basepath]")
    if (len(sys.argv) == 2):
        base_path = sys.argv[1]

    clear_public_dir()
    copy_static_files()
    generate_pages(base_path)

if __name__ == "__main__":
    main()
