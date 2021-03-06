# -*- coding: UTF-8 -*-
# '''
# Created on 2017年3月8日
#
# @author: Administrator
# '''
import xlsxwriter
import database
import tools
import os


# 循环建立图表
def build_graph():
    rootdir = "./in/"                                  # 指明被遍历的文件夹
    for rd in os.listdir(rootdir):
        build_one_graph("in/"+rd, "out/"+rd.split(".txt")[0]+".xlsx")


# 建立图表
def build_one_graph(source_file, build_file):
    # 创建EXCEL工作簿
    workbook = xlsxwriter.Workbook(build_file)
    # 时间段活跃统计图
    time_set = database.get_time_set(source_file)
    # 排序
    time_tuple = sorted(time_set.items(), key=lambda e: e[0], reverse=False)
    # 写入工作簿
    tools.add_sheet_type(workbook, "时间段活跃", time_tuple, "时间", "活跃量")

    # 成员活跃图
    people_say_set = database.get_people_say_set(source_file)
    # 排序
    people_say_tuple = sorted(people_say_set.items(), key=lambda e: e[1], reverse=True)
    # 写入工作簿
    tools.add_sheet_type(workbook, "成员活跃", people_say_tuple, "成员", "活跃量")

    # 热词统计
    word_tuple = database.get_hot_noun_counts(source_file)
    # 写入工作簿
    tools.add_sheet_type(workbook, "热词统计", word_tuple, "词汇", "出现次数")

    # 关闭文档
    workbook.close()
