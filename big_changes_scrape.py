from bs4 import BeautifulSoup
from lxml import etree
import requests


  
def biggest_changers(input, n_returns):
    #input is losers or gainers
    #n_returns is the number of stocks to be returned
    
    if input == "losers":
        URL = "https://finance.yahoo.com/losers"
    elif input == "gainers":
        URL = "https://finance.yahoo.com/gainers"
    else:
        URL = input
    
    
    #Get webpage
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    
    count = 0
    stock_array = []
    
    while len(stock_array) < n_returns:
        
        XPATH_string = '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(count+1)+']/td[1]/a'
        stock_name = dom.xpath(XPATH_string)[0].text
        if option_check(stock_name) == 'y':
            count+=1
            stock_array.append(stock_name)
        else:
            count+=1
            
    return stock_array
        
    
    #print(dom.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a')[0].text)
    
def option_check(stock_name):
    URL = "https://finance.yahoo.com/quote/"+stock_name+"/options"
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    XPATH_string = '//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr[1]/td[1]/a'
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    try: 
        (dom.xpath(XPATH_string)[0].text) #verify options available
        return 'y'
    except:
        return 'n'
