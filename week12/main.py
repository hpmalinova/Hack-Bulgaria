import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# from requests.exceptions import HTTPError


# BFS
def find_all_urls(url):
    try:
        response = requests.get(url, timeout=5)
        url = response.url
    except Exception as err:
        print(f'Other error occurred: {err}')

    queue = [url]
    visited = [url]
    # Add url to BD

    while queue:
        url = queue.pop()

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
                        print('NEW_LINK: ', new_link)
                        visited.append(new_link)
                        # ADD url to BD
                        queue.append(new_link)
            # except HTTPError as http_err:
            #     print(f'HTTP error occurred: {http_err}')
            except Exception:
                pass


url = 'https://register.start.bg/'
url2 = 'https://www.fmi.uni-sofia.bg/'
url3 = 'https://about.google/'
find_all_urls(url)
