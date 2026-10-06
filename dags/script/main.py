import json
import requests
import hashlib

from bs4 import BeautifulSoup
from preprocessing import preprocessing, ingestion

def main():
    index = get_index()
    
    articles = []
    for url in index[:2]:
        page = get_page(url)
        ingestion(page)
        # articles.append(page)
    
    # print(articles)
    
    # with open("result.json", "w", encoding="utf-8") as f:
    #     json.dump(articles, f, indent=4)
    
def get_index():
    base_url = "https://gizmologi.id"
    max_page = 2
    
    links = []
    for i in range(max_page):
        url = f"{base_url}/blog/page/{i}/?s=+"
        soup = request(url)

        for link in soup.select("a.p-url"):
            links.append(link.get("href"))
            
    return links 

def get_page(url):
    soup = request(url)
    
    paragraph = [text.get_text() for text 
                    in soup.select("p.wp-block-paragraph")]

    # add urlhash, tag 
    temp = {
        "urlhash": hashlib.md5(url.encode('utf-8')).hexdigest(),
        "author": 
            soup.select_one("a.meta-author-url").get_text()
            if soup.select_one("a.meta-author-url") is not None
            else soup.select_one("meta[name='twitter:data1']").get("content"),
        "tag":[tag.get_text() for tag in soup.select("a[rel='tag']")],
        "url": 
            url,
        "title": 
            soup.select_one("title").get_text(),
        "published_date": 
            "" if soup.select_one("meta[property='article:published_time']") is None
                else soup.select_one("meta[property='article:published_time']").get("content"),
        "content": preprocessing(".".join(paragraph))
    }
    
    return temp
    
def request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    return soup    

if __name__ == '__main__':  
    main()