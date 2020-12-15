from lxml import etree

if __name__ == '__main__':
    tree = etree.parse('test.html')
    # //表示多个层级
    # div = tree.xpath('/html/body/div')
    # //表示多个层级
    # div = tree.xpath('/html//div')
    # //表示所有的
    # p = tree.xpath('//div[@id="itownetPage"]/p[1]')
    # print(p[0].text)
    p = tree.xpath('//div[@id="itownetPage"]/p[1]//text()')
    # 获取属性
    img = tree.xpath('//div[@id="itownetPage"]/img/@src')
    print(img)
