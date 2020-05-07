#! python3
import requests
from bs4 import BeautifulSoup as soup
import smtplib
def send_mail():
    mail_conn=smtplib.SMTP('smtp.gmail.com',587)#mail service,port
    mail_conn.ehlo()#initiate the transaction
    
    mail_conn.starttls()
    mail_conn.login('mail_id@gmail.com','yourpasskey')#maildif,passkey for the account from which mail is to be sent
    mail_conn.sendmail('source_mailid','target_mailid','Subject: Amazon Diadem Alert!\n\nAttention!\n\nThe Price of the Diadem has come down!\n\n')
    mail_conn.quit()
    print('notified')#for our convenience

def checkprice(count):
    #url target 
    target_url='https://www.amazon.in/24x7-eMall-Analogue-White-Pocket/dp/B01LZUFCWZ/ref=sr_1_1?dchild=1&keywords=watch&qid=1588829471&s=dvd&sr=1-1'
    #headers of request
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    #requests.get is a standard apache II based method to get content
    page_download=requests.get(target_url,headers=headers)
    #terminate script if request denied by server
    page_download.raise_for_status()
    #model the obtained content into a html doc
    page_parse=soup(page_download.content,'html.parser')
    #locate the required by inspecting the dom tree using the web browser
    info_container=page_parse.find('span',{'class','a-size-medium a-color-price priceBlockBuyingPriceString'})
    #goes in only if the request is success and the desired element/tag has been captured
    if info_container is not None:
                 count=count-1
                 #extraction of only numerical data for our comparison
                 container=info_container
                 cost_string=container.text
                 cost_string=cost_string.strip('₹\xa0')
                 cost_string=float(cost_string)
                 if cost_string < 400:
                         #condition success
                        send_mail()
    return count
count=2
while count!=0:
    count=checkprice(count)
    #send notifs only twice
#use task scheduler to schedule the running of this program during the active hours of your desktop/laptop
#creation of a .bat file is needed to run the script




