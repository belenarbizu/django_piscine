import requests
import json
import dewiki
import sys


def api_search(string):
    url = "https://en.wikipedia.org/w/api.php"
    # extracts - texto del articulo
    # explaintext - texto plano sin HTML/wiki markup
    params = {
        "action": "query",
        "prop": "extracts",
        "format": "json",
        "explaintext": True,
        "titles": string,
        "redirects": True
    }
    headers = {
        "User-Agent": "request an API (barbizu-@student.42malaga.com)"
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        pages = data["query"]["pages"]

        if not pages:
            print("No results found")
            sys.exit(1)

        for _, value in pages.items():
            if "extract" in value:
                filename = string.replace(" ", "_") + ".wiki"
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(dewiki.from_string(value["extract"]))
                return

        print("No results found")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    args = sys.argv
    if len(args) != 2 or not args[1].strip():
        print("Usage: python3 ./request_wikipedia [string]")
        sys.exit(1)
    api_search(args[1])


if __name__ == '__main__':
    main()
