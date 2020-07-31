# >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

# >>> r.status_code
# 200

# >>> r.headers['content-type']
# 'application/json; charset=utf8'

# >>> r.encoding
# 'utf-8'

# >>> r.text
# u'{"type":"User"...'

# >>> r.json()
# {u'disk_usage': 368627, u'private_gists': 484, ...}

################################################################################
# html = response.content.decode("UTF-8")

# soup.title
# # <title>The Dormouse's story</title>

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


    a = urllib.request.urlopen(url).geturl()
    unquote(a)
    html = urllib.request.urlopen(a).read()
    response = requests.get(url)
    html = response.content.decode("UTF-8")

    import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()


################################################################################

Old shit:
def get_reference_url2(url):
    # http_response = urllib.request.urlopen(url)
    # return http_response.geturl()

    # return urllib.request.urlopen(url).read()

    a = urllib.request.urlopen(url).geturl()
    print('before', a)
    unquote(a)
    print(a)

    # html = urllib.request.urlopen(a).read()
    response = requests.get(a)
    html = response.content.decode("UTF-8")


    soup = BeautifulSoup(html, 'html.parser')
    return soup
    # new_links = []

    # for link in soup.find_all('a'):
    #     new_link = link.get('href')
    #     if new_link and not new_link.startswith('#'):
    #         if new_link.startswith('/'):
    #             new_link = url + new_link[1:]
    #         if new_link.startswith('./'):
    #             pass
    #         print('NEW_LINK: ', new_link)
    #         new_links.append(new_link)
    # return new_links



def idk2(url):
    response = requests.get(url)
    html = response.content.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')
    return soup
    # new_links = []

    # for link in soup.find_all('a'):
    #     new_link = link.get('href')
    #     if new_link and not new_link.startswith('#'):
    #         if new_link.startswith('/'):
    #             new_link = url + new_link[1:]
    #         if new_link.startswith('./'):
    #             pass
    #         print('NEW_LINK: ', new_link)
    #         new_links.append(new_link)
    # return new_links


    
def links_in_site(url, visited=None):
    if visited is None:
        visited = []

    response = requests.get(url)
    response_url = response.url
    visited.append(response_url)
    print('MAIN URL: ', response_url) # no

    html = response.content.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')

    new_links = []

    for link in soup.find_all('a'):
        new_link = link.get('href')
        if new_link and new_link not in visited and not new_link.startswith('#'):
            new_link = urljoin(url, new_link)
            # if new_link.startswith('/'):
            #     new_link = url + new_link[1:]
            # if new_link.startswith('./'):
            #     pass
            print('NEW_LINK: ', new_link)
            visited.append(new_link)
            new_links.append(new_link)

    return (visited, new_links)

           # except HTTPError as http_err:
            #     print(f'HTTP error occurred: {http_err}')

# class UrlModel():
#     def __init__(self, url_id, url, add_all_children):
#         self.url_id = url_id
#         self.url = url
#         self.add_all_children = add_all_children