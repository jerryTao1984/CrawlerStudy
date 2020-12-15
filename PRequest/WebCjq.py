# coding:utf-8
import requests
if __name__ == '__main__':
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url='https://www.sogou.com/web'
    kw=input('输入参数')
    param={
        'query':kw
    }
    response=requests.get(url=url,params=param,headers=header)
    with open(kw+'.html','w',encoding='utf-8') as fp:
        fp.write(response.text)