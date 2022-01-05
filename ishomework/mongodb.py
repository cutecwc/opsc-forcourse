import csv

from pymongo import MongoClient

connection = MongoClient('localhost')

db = connection.config

emp = db.res

file1 = open('C:\Downloads\opsc-forcourse-main\ishomework\islist0.csv', 'r', encoding="utf-8")
#csv中提供DictReader函数将列表格式以字典格式读取出来
file = csv.DictReader(file1)

for each in file:
    print(each)
    eachline = json.loads(each)
    emp.insert(eachline)
file.close()

