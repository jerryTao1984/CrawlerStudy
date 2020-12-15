import requests
import re
from common import FileUtil
import os
if __name__ == '__main__':
    ruhnnFileU = FileUtil.FileUtil()
    dirname='./qiutulibs'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    url='https://www.qiushibaike.com/imgrank/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    pageText=requests.get(url=url,headers=header).text

    ex='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    imgsrc=re.findall(ex,pageText,re.S)
    for src in imgsrc:
        src='https:'+src
        imgdate=requests.get(url=src,headers=header).content
        imgName=dirname+'/'+src.split('/')[-1]
        print(src)
        ruhnnFileU.saveBToFile(imgName,imgdate)