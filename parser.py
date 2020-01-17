import requests
import bs4 as BeautifulSoup
import re

class WikiParser:
    URL = "https://en.wikipedia.org/w/api.php"
    S = requests.Session()

    def getPage(self, name):
        print("getting page : " + name)
        PARAMS = {
            "action": "parse",
            "page": name,
            "format": "json"
        }
        R = self.S.get(url=self.URL, params=PARAMS)
        DATA = R.json()
        return DATA["parse"]["text"]["*"]

    def getLinksFromPage(self, page):
        soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
        links = soup.find_all("a", href=lambda x: x and x.startswith('/wiki/'), class_=False)
        titles = []
        for link in links:
            title = link.attrs['title']
            # beginnings to avoid: Help: Wikipedia: Special: Category: Template: User talk:
            if ':' not in title:
                titles.append(title)
        return titles



if __name__ == "__main__":
    wikiParser = WikiParser()
    page = wikiParser.getPage("Pet door")
    links = wikiParser.getLinksFromPage(page)
    for link in links:
        print(link)