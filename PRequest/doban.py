import json
from common import FileUtil
import requests
from requests.models import Response
if __name__ == '__main__':
    ruhnnFile=FileUtil.FileUtil()
    url='https://movie.douban.com/j/search_subjects'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    param={
        'type':'movie',
        'sort': 'recommend',
        'tag':'%E7%83%AD%E9%97%A8',
        'page_start': '0',
        'page_limit': '20',
    }
    responses=requests.get(url=url,params=param,headers=header)
    list_data=responses.json()
    ruhnnFile.saveJsonToFile('./douban.json',list_data)