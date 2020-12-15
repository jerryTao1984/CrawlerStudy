import requests
from lxml import etree
import os
from common import FileUtil

if __name__ == '__main__':
    dirname = './4k'
    ruhnnFileU = FileUtil.FileUtil()
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    url='http://pic.netbian.com/4kqiche/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response=requests.get(url=url, headers=header)
    #response.encoding='utf-8'
    page_text=response.text
    tree_4k=etree.HTML(page_text)
    li_4k=tree_4k.xpath('//div[@class="slist"]//li')
    for li in li_4k:
        src=li.xpath('.//a/img/@src')[0]#.表示当前指向的
        src='http://pic.netbian.com/'+src
        sname = li.xpath('.//a/img/@alt')[0] + '.jpg'  # .表示当前指向的
        sname = sname.encode('iso-8859-1').decode('gb2312')
        ruhnnFileU.downLoadToFile(src,dirname+'/'+sname)

        # bimgdata=requests.get(url=src,headers=header).content
        # ruhnnFileU.saveBToFile(dirname+'/'+sname,bimgdata)