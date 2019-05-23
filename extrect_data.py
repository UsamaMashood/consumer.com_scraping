from fake_useragent import UserAgent
import requests

ua = UserAgent()

link = 'https://www.consumerreports.org/cro/a-to-z-index/products/index.htm'
data = requests.get(link,headers={'user-agent' : ua.chrome}, timeout = 3).text

with open('consumer.txt', 'w',encoding='UTF-8') as file:
        file.write(data)
