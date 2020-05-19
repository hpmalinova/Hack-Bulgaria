import gateway
from collections import deque


# class UrlModel():
#     def __init__(self, url_id, url, add_all_children):
#         self.url_id = url_id
#         self.url = url
#         self.add_all_children = add_all_children

def get_all_urls_as_set():  # {url1, url2, url3}
    raw_urls = gateway.get_all_urls()
    url_set = set()
    for raw_url in raw_urls:
        url_set.update(raw_url)
    return url_set


def get_urls_with_no_children_in_db_as_deque():
    raw_urls = gateway.get_urls_with_no_children_in_db()
    url_deque = deque()
    for raw_url in raw_urls:
        url_deque.append(raw_url)
    return url_deque


def update_url_add_all_children(url):
    gateway.update_url_add_all_children(url)


def add_url(url):
    gateway.add_url(url)
