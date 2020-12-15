import requests
from lxml import etree
if __name__ == '__main__':
    url='https://hz.58.com/ershoufang/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=header).text
    tree_58=etree.HTML(page_text)
    li_58=tree_58.xpath('//ul[@class="house-list-wrap"]/li')
    with open('./58.txt','w',encoding='utf-8') as fp:
        for li in li_58:
            name=li.xpath('.//div[2]/h2/a/text()')[0]#.表示当前指向的
            fp.write(name+'\n')