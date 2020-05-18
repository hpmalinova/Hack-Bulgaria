import requests
from bs4 import BeautifulSoup


def print_links_in_site(url):
    response = requests.get(url)
    html = response.content.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        new_link = link.get('href')
        if new_link and not new_link.startswith('#'):
            print(new_link)


# BFS
def find_all_urls(master_url):
    queue = [master_url]
    visited = [master_url]

    while queue:
        url = queue.pop()

        print('MAIN URL: ', url)

        response = requests.get(url)
        html = response.content.decode("UTF-8")
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):
            new_link = link.get('href')
            if new_link and new_link not in visited and not new_link.startswith('#'):
                if new_link.startswith('/'):
                    new_link = url + new_link[1:]
                    print('NEW_LINK: ', new_link)
                    queue.append(new_link)
                    visited.append(new_link)


url = 'https://register.start.bg/'
# print_links_in_site(url)
print_links_in_site('http://link.php?id=59518')
# find_all_urls(url)
