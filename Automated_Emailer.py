import requests
import bs4
import email
import smtplib
import datetime

url = "https://quotes.toscrape.com/page/{}/"

def random_quote(url):
    quotes = []
    for num in range(1,11):
        res = requests.get(url.format(str(num)))
        soup = bs4.BeautifulSoup(res.text,"lxml")
        
        
        quotelist = soup.select(".text")

        for item in quotelist:
            quotes.append(item.getText())
    num = str(datetime.date.today())[-2:]
    return quotes[int(num)]

quote = random_quote(url)

smtp_object = smtplib.SMTP_SSL("smtp.gmail.com",465)
smtp_object.ehlo()

user = "YOUR_EMAIL_ADDRESS"
password = "YOUR_EMAIL_PASSWORD"
smtp_object.login(user,password)
from_address = "YOUR_EMAIL_ADDRESS"
to_address = "RECIPIENT_EMAIL_ADDRESS"
subject = "Quote of the Day!"
body = quote
msg = "Subject: "+subject+"\n"+body

smtp_object.sendmail(from_address,to_address,msg.encode("utf-8"))
smtp_object.close()

