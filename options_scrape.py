from bs4 import BeautifulSoup
from lxml import etree
import requests
from crr import CRR
from helper_functions import day_to_year


def options_scrape(stock_name, n,r):
    
    #Relevant Variables
    #n             # Number of steps
    #Spot          # Spot Price
    #K             # Strike Price
    #T             # Years to maturity
    #q             # Dividend (continuous) Yield
    #r             # Risk-Free Rate
    #v             # Volitility
    
    #Stock Details NOT Option Details
    
    URL = "https://finance.yahoo.com/quote/" + stock_name
    
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(webpage, 'html.parser')
    XPATH_string_Spot = '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]'
    #soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    Spot = float((dom.xpath(XPATH_string_Spot)[0].text).replace(",",""))
    XPATH_string_div = '//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]'
    q_string = dom.xpath(XPATH_string_div)[0].text
    try:
        q = float(q_string.split('(')[1].split('%')[0])/100
    except:
        q = 0.0
    
    
    
    #Option Details
    
    URL = "https://finance.yahoo.com/quote/"+stock_name+"/options"
    
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(webpage, 'html.parser')
    dom = etree.HTML(str(soup))
    XPATH_string_date = '//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[1]/span[3]'
    #print(dom.xpath(XPATH_string_date))
    options_date = dom.xpath(XPATH_string_date)[0].text
    days = day_to_year(options_date)
    years = days/365
    
    """print('Classes of each table:')
    for table in soup.find_all('table'):
        print(table.get('class'))"""
    tables = soup.find_all('table')
    table = soup.find('table', class_='calls W(100%) Pos(r) Bd(0) Pt(0) list-options')
    
    for row in table.tbody.find_all('tr'):    
    # Find all data for each column
        columns = row.find_all('td')
        #print(columns[2].text)
        v = float(columns[10].text.replace("%", 'e-2').replace(",",''))
        
        if v == 0.0:
            pass
        else:
            if float((columns[5].text).replace(",","")) < CRR(n,Spot,float((columns[2].text.replace(",",""))),years,q,r,v,'Calls'):
                print(stock_name)
                print("Spot: ", Spot)
                print("Strike: ", float(columns[2].text))
                print("q: ", q)
                print("r: ", r)
                print("v: ", v)
                print("CCR")
                print(CRR(n,Spot,float(columns[2].text),years,q,r,v,'Calls'))
                print("ask:")
                print(float(columns[5].text))
                print("")
        #print(float(columns[2].text)+5)
        
        
        
        
        #print(type(columns[2]))
        
        
        
        
        """print(columns[2].text)
        print(columns[5].text)"""
    
    
    
    
    """URL = "https://finance.yahoo.com/quote/"+stock_name+"/options"
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(URL, headers=HEADERS)
    
    check = 'valid'
    count = 1
    while check == 'valid':
        XPATH_string = '//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr['+str(count)+']/td[3]/a'
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = etree.HTML(str(soup))
        #sdaad = dom.xpath(XPATH_string)[0].text
        
        
        try: 
            K = dom.xpath(XPATH_string)[0].text
            
            count +=1
            return 'valid'
        except:
            return 'not'
    
    
    
//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr[1]/td[3]/a
//*[@id="Col1-1-OptionContracts-Proxy"]/section/section[1]/div[2]/div/table/tbody/tr[2]/td[3]/a"""
