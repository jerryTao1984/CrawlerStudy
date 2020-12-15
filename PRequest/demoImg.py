import requests
from common import FileUtil



if __name__ == '__main__':
    ruhnnFileU = FileUtil.FileUtil()
    url='https://pic.qiushibaike.com/system/pictures/12387/123875223/medium/AE2GQ0JD5GYMJY8E.jpg'
    imgdate=requests.get(url=url).content
    ruhnnFileU.saveBToFile('./img.jpg',imgdate)