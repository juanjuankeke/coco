import requests
import json
from common import get_path
from conf.conf1 import ConFig
http = ConFig().get_conf('http', 'url')
class request:
    def __init__(self):
        self.session=requests.sessions.session()     #实例化一个session对象，存取cookies
    def requests(self,method,url,data):
        url=http+url
        print(url)
        method=method.upper()
        if method=='GET':
            resp=self.session.request(method=method, url=url,params=data)     #get方法使用params
            return resp     #返回的resp是一个对象
        else:
            resp = self.session.request(method=method, url=url,data=data)     #post方法使用data
            return resp

if __name__ == '__main__':

    t=request()
    #to=t.requests('get','/member/register',{"mobilephone":13999997779,"pwd":"123456"})
    to=t.requests('get','/member/login',{"mobilephone":13799997779,"pwd":"123456"})      #管理员登录
    to=t.requests('get','/loan/add',{'repaymemtWay': 11, 'loanTerm': 6, 'amount': 4000,
                                     'loanRate': '18.0', 'memberId': '1114926', 'loanDateType': 0, 'biddingDays': 10, 'title': '钱'})     #加标
    #to1=t.requests('get','/loan/audit',{"id":11642,"status":4})
    to2=t.requests('get','/member/login',{"mobilephone":13999997779,"pwd":"123456"})   #投资人登录
    to3=t.requests('get','/member/bidLoan',{"memberId":1116896,"password":"123456","loanId":"11642","amount":400})

    print('哈哈哈哈',to.text)
    print(to.content)
    print(to.status_code)                 #状态码
    print(to.cookies)
    #print(to1.text)
    print(to3.text)
    print(to2.text)

