import sys
import os
import re
import settings


def read_file(file_name: str) -> str:
    try:
        if not os.path.exists(file_name):
            print("File does not exist")
            sys.exit(1)
        if not file_name.endswith('.template'):
            print("File name must end with .template")
            sys.exit(1)
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def get_content(match: re.Match) -> str:
    #re.sub() sends an object called match which is {name}
    #group(1) returns only name without {}
    key = match.group(1)
    if hasattr(settings, key):
        return str(getattr(settings, key))
    else:
        return ''


def change_content(content: str) -> str:
    line = re.sub(r'\{(\w+)\}', get_content, content)
    return line


def save_file(content: str) -> None:
    with open('file.html', 'w') as file:
        file.write(content)


def main():
    args = sys.argv
    if len(args) == 2:
        file = read_file(args[1])
        changed_file = change_content(file)
        save_file(changed_file)
    

if __name__ == '__main__':
    main()