import sys
import requests
from bs4 import BeautifulSoup


def remove_parantheses(p):
    count = 0
    result = ""
    for char in p:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        elif count == 0:
            result += char
    return result


def api_search(string):
    string_url = string.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{string_url}"

    headers = {
        "User-Agent": "request an API (barbizu-@student.42malaga.com)"
    }
    pages = []
    visited = []
    found = False
    visited.append(url)
    try:
        while url != "https://en.wikipedia.org/wiki/Philosophy":
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                redirect = soup.find(class_="mw-redirectedfrom")
                if redirect:
                    a_name = redirect.find("a")
                    if a_name:
                        title = a_name.get("title")
                        url_redirect = f"https://en.wikipedia.org/wiki/{title}"
                    if url_redirect not in visited:
                        visited.append(url_redirect)
                    print(title)
                    pages.append(title)

                main_title = soup.find(class_="mw-page-title-main")
                if main_title:
                    pages.append(main_title.text)
                    print(main_title.text)

                content_text = soup.find(id="mw-content-text")
                context_ltr = content_text.find(class_="mw-content-ltr")
                all_p = context_ltr.find_all("p")

                for p in all_p:
                    if p.text.strip():
                        first_paragraph = p
                        break
                
                clean_paragraph = remove_parantheses(first_paragraph.text)


                for link in first_paragraph.find_all("a"):
                    href = link.get("href")
                    if not href or not href.startswith("/wiki/") or ":" in href or link.find_parent("i") or link.text not in clean_paragraph:
                        continue
                    url = f"https://en.wikipedia.org{href}"
                    if url not in visited:
                        visited.append(url)
                        found = True
                    else:
                        print("It leads to an infinite loop !")
                        sys.exit(1)
                    break
                if not found:
                    print("It leads to a dead end !")
                    sys.exit(1)

        if url == "https://en.wikipedia.org/wiki/Philosophy":
            pages.append("Philosophy")
            print("Philosophy")
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