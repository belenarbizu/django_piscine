import sys
import requests
from bs4 import BeautifulSoup


def api_search(string):
    string_url = string.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{string_url}"

    headers = {
        "User-Agent": "request an API (barbizu-@student.42malaga.com)"
    }
    pages = []
    visited = []
    found = False
    pages.append(string)
    visited.append(url)
    try:
        while url != "https://en.wikipedia.org/wiki/Philosophy":
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                all_p = soup.find_all("p")
                for p in all_p:
                    if p.text.strip():
                        first_paragraph = p
                        break
                for link in first_paragraph.find_all("a"):
                    href = link.get("href")
                    if not href or not href.startswith("/wiki/") or ":" in href or link.find_parent("i"):
                        continue
                    url = f"https://en.wikipedia.org{href}"
                    if url not in visited:
                        visited.append(url)
                        found = True
                    else:
                        print("It leads to an infinite loop !")
                        sys.exit(1)
                    pages.append(link.text)
                    break
                if not found:
                    print("It leads to a dead end !")
                    sys.exit(1)
        if url == "https://en.wikipedia.org/wiki/Philosophy":
            for page in pages:
                print(page)
            print(f"{len(pages)} roads from {string} to philosophy !")

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