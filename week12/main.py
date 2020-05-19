import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from db import create_tables
from model import (get_all_urls_as_set, get_urls_with_no_children_in_db_as_deque,
                   update_all_children_now_added, add_url)


def build():
    create_tables()


# BFS
def find_all_urls(url):
    deque = get_urls_with_no_children_in_db_as_deque()  # deque([url1, url2, ..])
    visited = get_all_urls_as_set()  # {url1, url2, url3, ..}

    try:
        response = requests.get(url, timeout=5)
        url = response.url
    except Exception as err:
        print(f'Other error occurred: {err}')

    if url not in visited:
        deque.append(url)
        visited.add(url)

    while deque:
        url = deque.popleft()

        try:
            response = requests.get(url, timeout=5)
            print('MAIN URL: ', url)  # no
        except Exception as err:
            print(f'Other error occurred: {err}')

        html = response.content.decode("UTF-8")
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):
            try:
                new_link = link.get('href')

                if new_link and not new_link.startswith('#'):
                    new_link = urljoin(url, new_link)
                    if new_link not in visited:
                        if 'link.php?id=' in new_link:
                            new_link = requests.get(new_link, timeout=5).url
                        add_url(new_link)
                        print('NEW_LINK: ', new_link)
                        deque.append(new_link)
                        visited.add(new_link)
            except Exception as err:
                print(f'Other error occurred: {err}')

        update_all_children_now_added(url)


def main():
    url = 'https://register.start.bg/'
    url2 = 'https://www.fmi.uni-sofia.bg/'
    # url3 = 'https://about.google/'
    find_all_urls(url2)


if __name__ == '__main__':
    build()
    main()
