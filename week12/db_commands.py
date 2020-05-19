from db import Url, session_scope


def add_url(url):
    with session_scope() as session:
        new_url = Url(url=url)
        session.add(new_url)


def find_url(url):
    with session_scope() as session:
        found_url = session.query(Url.url_id)\
                           .filter(Url.url == url)\
                           .first()
        return True if found_url else False
