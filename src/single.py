import os
import re
from lxml import etree
import gne
from newsClass import news


def getNews(url, text, fr0m) -> news:
    extractor = gne.GeneralNewsExtractor()
    result = extractor.extract(text)
    tree = etree.HTML(text)
    line = news()
    if fr0m == "bigdata_expo":
        if tree is not None:
            t = tree.xpath("//div[@class = 'col-md-9 news-main ']/p/text()")
            out = "".join(str(t).split()) \
                .replace(u'\'', '').replace('\\xa0', '').replace('\\n', '').replace('\\t', '')
            sources = re.findall(r"来源:(.*)编辑:", out)
        # print("来源：", sources)
        line.title += str(result['title'])
        for image in result['images']:
            if image[0:4] != 'http':
                image = r'https://www.bigdata-expo.cn' + image
            line.images += str(image)
            line.images += '\n'
        line.content = result['content']
        line.url = url
        line.publish_time = result['publish_time']
        line.author = result['author']
        line.sources = sources
    elif "cbdio" in fr0m:
        html = text.replace(r"../../../", r'http://www.cbdio.com/')
        d1ct = {}
        tree = etree.HTML(html)
        if tree is not None:
            t = tree.xpath("//p[@class = 'cb-article-info']/span//text()")
            for i in t:
                key = i.split('：', 1)[0]
                try:
                    value = i.split('：', 1)[1]
                except IndexError:
                    value = ''
                d1ct[key] = value

                try:
                    line.author = d1ct["作者"]
                except KeyError:
                    line.author = ""
                try:
                    line.sources = d1ct["来源"]
                except KeyError:
                    line.author = ""

            t = tree.xpath("//div [@class = 'cb-article']")
            h1 = tree.xpath("//h1 [@class = 'cb-article-title']")
            info = tree.xpath("//p [@class = 'cb-article-info']")
            qrcode = tree.xpath("//p [@align = 'center']")
            meta = tree.xpath("//meta[@name = 'description']/@content")
            if len(meta) != 0:
                line.description = meta[0]
            meta = tree.xpath("//meta[@name = 'biaotitu']/@content")
            if len(meta) != 0:
                line.media_thumb = "http://www.cbdio.com/image" + meta[0][5:]

            for i in h1:
                i.getparent().remove(i)
            for i in info:
                i.getparent().remove(i)
            try:
                qrcode[-1].getparent().remove(qrcode[-1])
            except IndexError:
                pass
            for i in t:
                _id = re.findall(r"content_(.*)", url)
                line.content = _id[0]
                if not os.path.exists(os.path.abspath(r"./html/")):  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(os.path.abspath(r"./html/"))
                file = os.path.abspath(r"./html/" + _id[0])
                f = open(file, "wb+")
                f.write(etree.tostring(i, encoding='ISO-8859-1'))
                f.close()

        line.title = str(result['title'])
        if result['images']:
            for image in result['images'][:-1]:
                if image[0:4] != 'http':
                    image = image.replace(r"../", '')
                    image = r'http://www.cbdio.com/' + image
                    line.images += str(image)
                    line.images += '\n'

        line.url = url
        line.publish_time = result['publish_time'][:-3]
        pass
    else:
        print("Unknown source!")
        return None

    return line
