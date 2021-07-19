import xlsxwriter as xlwt
import datetime


def buildTable(lines, fr0m):
    wb = xlwt.Workbook(str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(datetime.datetime.now().day) +
                       str(fr0m) + '_news.xlsx')

    # 新增两个表单页
    sh1 = wb.add_worksheet('news')
    sh2 = wb.add_worksheet('about')

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一个sheet
    sh1.write(0, 0, '标题')
    sh1.write(0, 1, '图片URL')
    sh1.write(0, 2, '正文')
    sh1.write(0, 3, '正文URL')
    sh1.write(0, 4, '时间')
    sh1.write(0, 5, '作者')
    sh1.write(0, 6, '来源')
    sh1.write(0, 7, '标题图')
    sh1.write(0, 8, '摘要')
    for idx, line in enumerate(lines):
            sh1.write(idx + 1, 0, line.title)
            sh1.write(idx + 1, 1, line.images)
            sh1.write(idx + 1, 2, line.content)
            sh1.write(idx + 1, 3, line.url)
            sh1.write(idx + 1, 4, line.publish_time)
            sh1.write(idx + 1, 5, line.author)
            sh1.write(idx + 1, 6, line.sources)
            sh1.write(idx + 1, 7, line.media_thumb)
            sh1.write(idx + 1, 8, line.description)

    sh2.write(0, 0, "build time")
    sh2.write(0, 1, "build amount")
    try:
        sh2.write(1, 1, str(idx))
    except UnboundLocalError:
        sh2.write(1, 1, "0")
    sh2.write(1, 0, str(datetime.datetime.now()))
    # 最后保存文件即可
    wb.close()
