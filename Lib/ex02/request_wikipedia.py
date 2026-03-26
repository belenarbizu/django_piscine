import requests
import json
import dewiki
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 ./request_wikipedia [string]")

if __name__ == '__main__':
    main()