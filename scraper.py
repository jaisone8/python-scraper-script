import requests
from bs4 import BeautifulSoup
import smtplib
import time
currency_symbols = [ "₹", "," ] 

#I took an example of an amazon product
URL = 'https://www.amazon.in/AMD-Ryzen-3700X-Processor-100000071BOX/dp/B07SXMZLPK/ref=sr_1_3?crid=1TLXJ4BNVIX2U&dchild=1&keywords=ryzen+7+3700x&qid=1599154843&sprefix=ryzen+7+%2Caps%2C312&sr=8-3'

headers = {"USer-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    
    #This will parse all the data from the given URL
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    for i in currency_symbols : 
        price = price.replace(i, '')
    converted_price = int(float(price))
    
    #this will print present price 
    print(converted_price)
    #this will print product name
    print(title.strip())

    if(converted_price < #desired price):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    #this is making our server secure
    server.starttls()
    server.ehlo()

    server.login('#Email from which you want to send', '#password of that email')
    
    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.in/AMD-Ryzen-3700X-Processor-100000071BOX/dp/B07SXMZLPK/ref=sr_1_3?crid=1TLXJ4BNVIX2U&dchild=1&keywords=ryzen+7+3700x&qid=1599154843&sprefix=ryzen+7+%2Caps%2C312&sr=8-3' 

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '#Sender E-mail',
        '#Reciever E-mail',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


check_price()
