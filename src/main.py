import os
import shutil

STATIC_PATH = "static"
PUBLIC_PATH = "public"

def clear_public_dir():
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

def main():
    clear_public_dir()
    copy_static_files()

if __name__ == "__main__":
    main()
