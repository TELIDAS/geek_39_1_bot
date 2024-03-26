import requests
from parsel import Selector


# pip install lxml==4.9.4

class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    URL = 'https://www.prnewswire.com/news-releases/news-releases-list/'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    LINK_XPATH = '//div[@class="row newsCards"]//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'
    DESCRIPTION_XPATH = '//p[@class="remove-outline"]/text()'
    IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        titles = tree.xpath(self.TITLE_XPATH).getall()
        descriptions = tree.xpath(self.DESCRIPTION_XPATH).getall()
        imgs = tree.xpath(self.IMG_XPATH).getall()
        # for link in links:
        #     print(self.PLUS_URL + link)
        for img in imgs:
            print(img)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()
