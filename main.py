from bs4 import BeautifulSoup
from lxml import etree
import requests
from crr import CRR
from big_changes_scrape import biggest_changers
from options_scrape import options_scrape



"""n = 1001                  # Number of steps
Spot = 150.35              # Spot Price
K = 145.0                 # Strike Price
T = 0.0082                   # Years to maturity
q = 0.0058
r = 0.0356                    # Risk-Free Rate
v = 0.25 """

#print(CRR(101,150.35,145.0,.0082,0.0058,0.0356,0.25, "Call"))

    
if __name__ == "__main__":
    #options_scrape('AAPL',101,2)
    n = 101 #number of steps
    
    #Get risk free rate
    URL = "https://www.cnbc.com/quotes/US10Y"
    
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5','referer':'https://www.google.com/'})
    
    webpage = requests.get(URL, headers=HEADERS)
    
    XPATH_string = '//*[@id="quote-page-strip"]/div[3]/div/div[2]/span[1]'
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    risk_rate = dom.xpath(XPATH_string)[0].text
    r = float(risk_rate.strip('%'))/100
    options_scrape('AAPL',101,r)
    
    stock_list = biggest_changers('losers',15)
    
    for stock in stock_list:
        print(stock)
        options_scrape(stock,n,r)
        
    stock_list = biggest_changers('gainers',15)
    
    for stock in stock_list:
        print(stock)
        options_scrape(stock,n,r)
    


    