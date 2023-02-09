

#putting it all together
import csv 
from bs4 import BeautifulSoup
from selenium import webdriver
from html import escape
#Getting the next page
def get_url(search_term):
    template="https://www.amazon.com/s?k={}&ref=nb_sb_noss_1"
    search_term=search_term.replace(' ','+')
    #add term query to url
    url=template.format(search_term)
    #add page query place holder
    url =url+'&page{}'
    return url


#ERROR HANDLING
def extract_record(item):
    atag=item.h2.a
    description =atag.text.strip()
    url='https://www.amazon.com'+atag.get('href')
    

    #text_url = "https://www.example.com"
    #link = f"<a href='{escape(url)}'>{escape(url)}</a>"
    #print(link)
    try:
        price_parent = item.find('span','a-price')
        price=price_parent.find('span','a-offscreen').text
    except(AttributeError):
        return 
    try:
        rating=item.i.text
        review=(item.find('span',{'class':'a-size-base','dir':'auto'}))
    except(AttributeError):
        rating=''
        review=''
    results=(description,price,rating,review,url)
    return results


def main(search_term):
    #Run main program routine
    #startup the web driver
    driver=webdriver.Firefox()

    records = []
    url=get_url(search_term)

    for page in range(1,2):
        driver.get(url.format(page))
        Soup=BeautifulSoup(driver.page_source, 'html.parser')
        result=Soup.find_all('div',{'data-component-type':'s-search-result'})
        for item in result:
            record=extract_record(item)
            if record:
                records.append(record)
    driver.close()

#SAVE DATA TO CSV FILE
    with open('data.csv','w',newline='\n',encoding='utf-8') as f:
        writer =csv.writer(f)
        writer.writerow(['description','price','rating','review','url'])
        writer.writerows(records)

