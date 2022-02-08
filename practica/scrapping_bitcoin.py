from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#The below url contains an html table with data about colors and color codes.
url = "https://www.coingecko.com/es"


#Before proceeding to scrape a web site, you need to examine the contents,
# and the way data is organized on the website. 
# Open the above url in your browser and check 
# how many rows and columns are there in the color table.

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
# in html table is represented by the tag <table>
BTC_pr = soup.find('td',{"class":"no-wrap"})['data-price-previous']



print(BTC_pr)
    