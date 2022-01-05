import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def area_Dis():
    pr = pd.read_csv('isSplited.csv')
    print("统计面积分布：")
    print()
    area = []
    for i in pr['areas']:
        area.append(i)
    print(area)
    area1=[]
    area2=[]
    area3=[]
    area4=[]
    area5=[]
    for i in area:
        if 50<=i.rstrip('平米')<75:
            area1.append(i)
        elif 75<=i.rstrip('平米')<100:
            area2.append(i)
        elif 100<=i.rstrip('平米')<125:
            area3.append(i)
        elif 125<=i.rstrip('平米')<150:
            area4.append(i)
        else:
            area5.append(i)

    index=['50~75','75~100','100~125','125~150','others']
    values=[len(area1),len(area2),len(area3),len(area4),len(area5)]
    plt.bar(index,values)
    plt.show()

if __name__=="__main__":
    area_Dis()
