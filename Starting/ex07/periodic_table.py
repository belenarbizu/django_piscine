import sys


def create_list(content):
    split_name = []
    split_info = []
    for item in content:
        split_name.append(item.split(' = '))
    for item in split_name:
        split_info.append(item[1].split(', '))
    for info in split_info:
        for element in info:
            element = element.split(':')[1]
        info = info
    final_list = []
    # for name, info in zip(split_name, split_info):
    #     final_list.append([name[0], info[1]])
    #print(final_list)


def main():
    try:
        with open('periodic_table.txt') as f:
            content = f.read().strip().split('\n')
        create_list(content)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()