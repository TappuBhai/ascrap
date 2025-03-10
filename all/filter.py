from bs4 import BeautifulSoup
import json

def filter_response(html)-> dict:
    '''Filter the HTML body and make it to a default output'''
    soup = BeautifulSoup(html,'html.parser')
    data = {
        "title": soup.title.string,
        "attributes_links": [a["href"] for a in soup.find_all("a",href=True)],
        "links": [l["href"] for l in soup.find_all("link",href=True)],
        "img_src": [i["src"] for i in soup.find_all("img",src=True)]
    }

    return json.dumps(data)

def css()->dict:

    pass 

print(f"\n")