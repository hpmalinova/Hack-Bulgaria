from db import Url, session_scope


def add_url(url):
    with session_scope() as session:
        new_url = Url(url=url, add_all_children='False')
        session.add(new_url)


def update_all_children_now_added(url):
    with session_scope() as session:
        session.query(Url)\
               .filter(Url.url == url)\
               .update({'add_all_children': 'True'})


def get_all_urls():
    with session_scope() as session:
        raw_urls_dict = []
        raw_urls = session.query(Url.url).all()
        for raw_url in raw_urls:
            raw_urls_dict.append(raw_url)

        return raw_urls_dict


def get_urls_with_no_children_in_db():
    with session_scope() as session:
        raw_urls_dict = []
        raw_urls = session.query(Url.url).filter(Url.add_all_children == 'False').all()
        for raw_url in raw_urls:
            raw_urls_dict.append(raw_url)

        return raw_urls_dict

# def find_url(url):
#     with session_scope() as session:
#         found_url = session.query(Url.url_id)\
#                            .filter(Url.url == url)\
#                            .first()
#         return True if found_url else False
