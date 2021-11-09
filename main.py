import requests
from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url="https://www.flipkart.com/ahana-women-printed-a-line-kurta/p/itmec50e31f25f9e?pid=KTAG7FGDF2QCHPDJ&lid=LSTKTAG7FGDF2QCHPDJ6OK4JU&marketplace=FLIPKART&q=kurtas+kurtis&store=clo%2Fcfv%2Fcib%2Frkt&srno=s_2_48&otracker=search&fm=SEARCH&iid=3809eaaf-eb10-4e20-892f-c832d8f6915c.KTAG7FGDF2QCHPDJ.SEARCH&ppt=browse&ppn=browse&ssid=kr0eipebr40000001635862918663&qH=5985e3313e9e348f"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
cprice=soup.find("div",class_="_30jeq3 _16Jk6d")
aprice=soup.find("div",class_="_3I9_wc _2p6lqe")
p1=cprice.text
p2=aprice.text
current_pr=int(re.search(r'\d+',p1).group())
actual_pr=int(re.search(r'\d+',p2).group())
if(current_pr < actual_pr):
    fromaddr = 'priyamandhane121995@gmail.com'
    toaddrs ='nikinayak53@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = "The Price of Product is dropped.....Go & Check...."

    body = "https://www.flipkart.com/ahana-women-printed-a-line-kurta/p/itmec50e31f25f9e?pid=KTAG7FGDF2QCHPDJ&lid=LSTKTAG7FGDF2QCHPDJ6OK4JU&marketplace=FLIPKART&q=kurtas+kurtis&store=clo%2Fcfv%2Fcib%2Frkt&srno=s_2_48&otracker=search&fm=SEARCH&iid=3809eaaf-eb10-4e20-892f-c832d8f6915c.KTAG7FGDF2QCHPDJ.SEARCH&ppt=browse&ppn=browse&ssid=kr0eipebr40000001635862918663&qH=5985e3313e9e348f"
    msg.attach(MIMEText(body, 'plain'))
    username = 'priyamandhane121995@gmail.com'
    password = 'Psm12@1995'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    text = msg.as_string()
    server.login(username, password)

    if (True):
        server.sendmail(fromaddr,toaddrs,text)
        print("Email sent")
    else:
        print("Email not sent")
    server.quit()
else:
    print("price is greater than ",actual_pr)
