import re


def find_url(string):
    url_patern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]'
                            r'|[$-_@.&+]|[!*\\(\\),]|?:%[0-9a-fA-F]'
                            r'[0-9a-fA-F]+')
    urls = re.findall(url_patern, string)
    return urls


text = "Visit my website at https://www.example.com or check out"
+"http://google.com for more information."
found_url = find_url(text)

if found_url:
    print("found the urls")
    for url in found_url:
        print(url)
else:
    print("No urls")
