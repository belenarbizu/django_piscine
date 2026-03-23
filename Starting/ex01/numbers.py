def main():
    with open('numbers.txt') as file:
        content = file.read().strip().split(',')
        for number in content:
            print(number)

if __name__ == "__main__":
    main()