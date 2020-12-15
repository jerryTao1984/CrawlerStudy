import json
class FileUtil(object):
    def __init__(self):
        super().__init__()

    #保存字符串到文件
    def saveTxtToFile(self, fileName, result):
        with open(fileName, 'w', encoding='utf-8') as fp:
            fp.write(result)

    #保存json格式到指定文件
    def saveJsonToFile(self,fileName, jsonResult):
        with open(fileName, 'a', encoding='utf-8') as fp:
            json.dump(jsonResult, fp=fp, ensure_ascii=False)