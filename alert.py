#!/usr/local/bin/python3

import requests
import yagmail
from bs4 import BeautifulSoup as bs
import datetime

def main():

    sender="hotboi0269@gmail.com"
    receiver="austincsp15@gmail.com"
    password="odxubsrpeliikrlu"

    subject = 'PARTS IN STOCK'
    urllist=[]

    url=""
    while 1:
        dt=datetime.datetime.now()
        url=input("add a url: ")
        if url:
            urllist.append(url)
            url=""
        else:
            print("empty")
        if urllist and dt.hour==12:
            for i in urllist:
                request = requests.get(i)
                soup = bs(request.text,"html.parser")
                if "Out of stock" in soup.text:
                    continue
                else:
                    content = ['A Car part is in stock.\n Link is attached',i]
                    with yagmail.SMTP(sender, password) as yag:
                        yag.send(receiver, subject, content)
                        print('Sent email successfully')
                    urllist.remove(i)

if __name__ == "__main__":
    main()