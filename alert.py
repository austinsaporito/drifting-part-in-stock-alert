#!/usr/local/bin/python3

import requests
import yagmail
from bs4 import BeautifulSoup as bs

def main():

    sender="hotboi0269@gmail.com"
    receiver="austincsp15@gmail.com"
    password="odxubsrpeliikrlu"

    subject = 'PARTS IN STOCK'
    url="https://carbonfiberhoods.com/modelodrive-frp-ori-t3-50mm-fenders-front-gt-nissan-240sx-s14-1995-1996-113160.html"
    request = requests.get(url)
    soup = bs(request.text,"html.parser")
    #print(soup.text)
    if "Out of stock" in soup.text:
        print("boi")
   # for line in soup:
    #  print(line)
      



    content = ['mail body content']

   # with yagmail.SMTP(sender, password) as yag:
    #    yag.send(receiver, subject, content)
    #    print('Sent email successfully')

if __name__ == "__main__":
    main()