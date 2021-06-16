from spider import spider


def main():
    # init
    # url = "https://www.bigdata-expo.cn/"
    url0 = "http://www.cbdio.com/node_2570.htm"  # info
    url1 = "http://www.cbdio.com/node_2568.htm"  # cases
    url2 = "http://www.cbdio.com/node_2782.htm"  # reports
    # bigdata_expo_paper = newspaper.build(url, language=language, memoize_articles=False)
    # cbdio_paper = newspaper.build(url0, language=language, memoize_articles=False)
    spider(url0, "cbdio_info")
    spider(url1, "cbdio_cases")
    spider(url2, "cbdio_reports")


if __name__ == "__main__":
    main()
