import json

import requests


class FileUtil(object):

    def __init__(self):
        super().__init__()
        self.__header__ = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

    #保存字符串到文件
    def saveTxtToFile(self, fileName, result):
        with open(fileName, 'w', encoding='utf-8') as fp:
            fp.write(result)

    #保存json格式到指定文件
    def saveJsonToFile(self,fileName, jsonResult):
        with open(fileName, 'a', encoding='utf-8') as fp:
            json.dump(jsonResult, fp=fp, ensure_ascii=False)

    #写入byte到文件
    def saveBToFile(self, fileName, result):
        with open(fileName, 'wb') as fp:
            fp.write(result)
    #下载网页写入文件
    def downLoadToFile(self,url,fileName):
        bimgdata = requests.get(url=url, headers=self.__header__).content
        with open(fileName, 'wb') as fp:
            fp.write(bimgdata)