from local_lib import Path


if __name__ == "__main__":
    path = Path("new_folder").mkdir(exist_ok=True)
    file = "file.txt"
    full_path = path / file
    with open(full_path, 'w') as f:
        f.write('Hello World!')
    with open(full_path, 'r') as f:
        print(f.read())