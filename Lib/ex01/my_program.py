from local_lib.path import Path


if __name__ == "__main__":
    dir_path = Path("new_folder").mkdir_p()
    file = "file.txt"
    full_path = dir_path / file
    with open(full_path, 'w') as f:
        f.write('Hello World!')
    with open(full_path, 'r') as f:
        print(f.read())