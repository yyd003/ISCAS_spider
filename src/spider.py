import newspaper
from newspaper import ArticleException

from buildTable import buildTable
from single import getNews


def spider(url, fr0m):
    papers = None
    if "cbdio" in url:
        papers = newspaper.Source("http://www.cbdio.com")
        print(papers.size())
        papers.add_categories(url)
        str_list = list(url)
        str_list.insert(-4, "_2")
        a_b = ''.join(str_list)
        papers.add_categories(a_b)
        str_list = list(url)
        str_list.insert(-4, "_3")
        a_b = ''.join(str_list)
        papers.add_categories(a_b)
        papers.download_categories()
        papers.parse_categories()
        papers.generate_articles()

        print(papers.size())
        for category in papers.category_urls():
            print(category)

        print("---------------")

        news_list = []
        for article in papers.articles:
            print(article.url)
            try:
                article.download()
                article.parse()
                news_list.append(getNews(article.url, article.html, fr0m))
            except ArticleException:
                print('***FAILED TO DOWNLOAD, SKIP!***')
                continue

        buildTable(news_list, fr0m)
        pass
    elif "bigdata-expo" in url:
        # Todo
        pass
    else:
        print("Not Support for this site")