import os
import re

import newspaper
from lxml import etree
import gne
from src.newsClass import news


def main():
    url = r"http://www.cbdio.com/BigData/2021-01/11/content_6162221.htm"
    _id = re.findall(r"content_(.*)", url)
    print(_id[0])
    article = newspaper.Article(url)
    article.download()
    extractor = gne.GeneralNewsExtractor()
    result = extractor.extract(article.html)
    html = article.html.replace(r"../../../", r'http://www.cbdio.com/')
    article.parse()
    line = news()
    d1ct = {}
    tree = etree.HTML(html)
    meta = []
    if tree is not None:
        meta = tree.xpath("//meta[@name = 'description']/@content")
        line.description = meta[0]
        meta = tree.xpath("//meta[@name = 'biaotitu']/@content")
        line.media_thumb = "http://www.cbdio.com/image" + meta[0][5:]
    #     t = tree.xpath("//p[@class = 'cb-article-info']/span//text()")
    #     for i in t:
    #         key = i.split('：', 1)[0]
    #         try:
    #             value = i.split('：', 1)[1]
    #         except IndexError:
    #             value = ''
    #         d1ct[key] = value
    #
    #         try:
    #             line.author = d1ct["作者"]
    #         except KeyError:
    #             line.author = ""
    #         try:
    #             line.sources = d1ct["来源"]
    #         except KeyError:
    #             line.author = ""
    #
    #     t = tree.xpath("//div [@class = 'cb-article']")
    #     h1 = tree.xpath("//h1 [@class = 'cb-article-title']")
    #     info = tree.xpath("//p [@class = 'cb-article-info']")
    #     qrcode = tree.xpath("//p [@align = 'center']")
    #
    #     for i in h1:
    #         i.getparent().remove(i)
    #     for i in info:
    #         i.getparent().remove(i)
    #     try:
    #         qrcode[-1].getparent().remove(qrcode[-1])
    #     except IndexError:
    #         pass
    #     for i in t:
    #         line.content = _id[0]
    #     if not os.path.exists(os.path.abspath(r"../html/")):  # 判断是否存在文件夹如果不存在则创建为文件夹
    #         os.makedirs(os.path.abspath(r"../html/"))
    #     file = os.path.abspath(r"../html/"+_id[0])
    #     f = open(file, "wb+")
    #     f.write(etree.tostring(i, encoding='ISO-8859-1'))
    #     f.close()
    #
    # line.title = str(result['title'])
    # if result['images']:
    #     for image in result['images'][:-1]:
    #         if image[0:4] != 'http':
    #             image = image.replace(r"../", '')
    #             image = r'http://www.cbdio.com/' + image
    #             line.images += str(image)
    #             line.images += '\n'
    #
    # line.url = url
    # line.publish_time = result['publish_time'][:-3]
    print(line)


if __name__ == "__main__":
    main()
