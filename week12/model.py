import gateway
from collections import deque


def get_all_urls_as_set():
    raw_urls = gateway.get_all_urls()
    url_set = set()
    for raw_url in raw_urls:
        url_set.add(raw_url[0])
    return url_set


def get_urls_with_no_children_in_db_as_deque():
    raw_urls = gateway.get_urls_with_no_children_in_db()
    url_deque = deque()
    for raw_url in raw_urls:
        url_deque.append(raw_url[0])
    return url_deque


def update_all_children_now_added(url):
    gateway.update_all_children_now_added(url)


def add_url(url):
    gateway.add_url(url)
