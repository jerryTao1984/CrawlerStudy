import requests
# 爬取搜狗首页
if __name__ == '__main__':
    # 指定url
    url='https://www.sogou.com/'
    # 发起请求
    # 获取响应数据
    response=requests.get(url=url)
    page_text=response.text
    print(page_text)
    with open('./sogou.html','w',encoding='utf-8') as  fp:
        fp.write(page_text)