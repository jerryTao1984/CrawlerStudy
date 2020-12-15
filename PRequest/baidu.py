from common import FileUtil
import requests
from requests.models import Response

if __name__ == '__main__':
    ruhnnFileU= FileUtil.FileUtil()
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url='https://fanyi.baidu.com/sug'
    kw=input('kw:')
    paramdata={
        'kw':kw
    }
    response=requests.post(url=url,data=paramdata,headers=header)
    jsonResponse=response.json()
    ruhnnFileU.saveJsonToFile('./百度翻译.json',jsonResponse)
    # print(jsonResponse)
    #with open('./kw.json','w',encoding='utf-8') as fp:
    #    json.dump(jsonResponse,fp=fp,ensure_ascii=False)

    fy=jsonResponse['data']
    for item in fy:
        print(item['k'],item['v'])