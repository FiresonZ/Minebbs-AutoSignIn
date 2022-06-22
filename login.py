import requests
from bs4 import BeautifulSoup
import datetime
import logging
import configparser
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO,
    filename='login.log',
    filemode='a')

cf = configparser.ConfigParser()
cf.read('config.ini')
cookie=cf.get('config','Cookie')
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Referer':'https://www.minebbs.com/',
'Cookie': cookie
}
res=requests.get("https://www.minebbs.com/",headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
pd = soup.find_all('span',class_="p-navgroup-linkText")
account = pd[0].text.split()
if(account[0]=='登录'):
    logging.warning("Cookie未填或过期！")
else:
    fid=soup.find_all('dl',class_="pairs pairs--justified fauxBlockLink")
    gold=fid[0].text.split()
    dia=fid[1].text.split()
    logging.info(gold)
    logging.info(dia)
