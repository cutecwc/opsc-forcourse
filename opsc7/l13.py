# 数据可视化
# 流萤漫天花共舞，闲蝉栖柳风奏湖
# pip install pyecharts
import pyecharts
import pandas
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

np.random.seed(19680801)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
# plt.rcParams['savefig.dpi'] = 400 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
font2 = {'color':'darkred','size':5}
# 数据读取测试
def tst():
    fname='opsc7\opsc7_r\isAnalys.csv'
    binding=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    # fname,encoding='utf-8',header=None,skiprows=num,nrows=1,usecols=[0]
    # df.iloc[0]['title']
    df = pandas.read_csv(fname,encoding='utf-8',names=binding,header=None,delimiter='$')
    runs(df)

# # 数组和
# fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
def listca(df,strs):
    li=[]
    #               0           1           2           3       4           5       6       7       8       9       0
    fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
    lca=None
    if (strs==fieldnames[0] or strs==fieldnames[1] or strs==fieldnames[5] or strs==fieldnames[6] or strs==fieldnames[8]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            li.append(lca)
    elif (strs==fieldnames[2] or strs==fieldnames[3] or strs==fieldnames[7] or strs==fieldnames[9] or strs==fieldnames[10]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            if(lca==''):
                lca=0
            else:
                lca=int(lca)
            li.append(lca)
    elif (strs==fieldnames[4]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            if(lca==''):
                lca=0
            else:
                lca=float(lca)
            li.append(lca)
    return li

# 楼房类型 分布 板楼塔楼，板塔楼结合，其它
def typstest(df):
    li=listca(df,strs='typs')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 板楼'):
            numb+=1
        elif(li[num]==' 塔楼'):
            numc+=1
        elif(li[num]==' 板塔结合'):
            numd+=1
        else:
            others+=1
    xlist=[' 板楼',' 塔楼',' 板塔结合',' 其他']
    ylist=[numb,numc,numd,others]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房类型分布')
    plt.savefig('opsc7\photos\ps1.png',dpi = 400)
    plt.show()

def typstest2(df):
    li=listca(df,strs='typs')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 板楼'):
            numb+=1
        elif(li[num]==' 塔楼'):
            numc+=1
        elif(li[num]==' 板塔结合'):
            numd+=1
        else:
            others+=1
    xlist=[' 板楼',' 塔楼',' 板塔结合',' 其他']
    numb=float(format(numb/2400,'.2f'))
    numc=float(format(numc/2400,'.2f'))
    numd=float(format(numd/2400,'.2f'))
    others=(1-numb-numc-numd)
    pslist=[numb,numc,numd,others]
    a1=int(numb*100)
    a2=int(numc*100)
    a3=int(numd*100)
    a6=100-a1-a2-a3
    a1=xlist[0]+str(a1)+'%'
    a2=xlist[1]+str(a2)+'%'
    a3=xlist[2]+str(a3)+'%'
    a6=xlist[3]+str(a6)+'%'
    xlists=[a1,a2,a3,a6]
    ylist=np.array(pslist)
    plt.pie(ylist,labels=xlists,colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
    plt.title('楼房类型分布(饼状图)')
    plt.savefig('opsc7\photos\ps2.png',dpi = 400)
    plt.show()

# v1.0
def areatest1(df):
    li=listca(df,strs='areas')
    # 50 70 90 110 130 150
    num1=0
    num2=0
    num3=0
    num4=0
    num5=0
    num6=0
    num7=0
    num0=0
    for num in range(0,2400):
        if(li[num]==0):
            num0+=1
        elif(li[num]<50.0 and li[num]>0):
            num1+=1
        elif(li[num]>=50.0 and li[num]<70.0):
            num2+=1
        elif(li[num]>=70.0 and li[num]<90.0):
            num3+=1
        elif(li[num]>=90.0 and li[num]<110.0):
            num4+=1
        elif(li[num]>=110.0 and li[num]<130.0):
            num5+=1
        elif(li[num]>=130.0 and li[num]<150.0):
            num6+=1
        else:
            num7+=1
    xlist=['未知','0~50','50~70','70~90','90~110','110~130','130~150','>150']
    ylist=[num0,num1,num2,num3,num4,num5,num6,num7]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房面积分布(柱状图)')
    plt.savefig('opsc7\photos\ps3.png',dpi = 400)
    plt.show()

# 楼房面积改进版
# 参考:https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
def areatest2(df):
    li=listca(df,strs='areas')
    numlist=[]
    counters=0
    c1=0
    c2=0
    # 50--70--90--110--130--150
    for num in range(0,2400):
        if li[num]<=50:
            c1+=1
        elif li[num]>200:
            c2+=1
        else:
            continue
    numlist.append(c1)
    for s in range(50,200,10):
        counters=0
        for num in range(0,2400):
            if(li[num]>s and li[num]<=(s+10)):
                counters+=1
            else:
                continue
        numlist.append(counters)
    numlist.append(c2)
    xlist=['0~50','50~60','60~70','70~80','80~90','90~100','100~110','110~120','120~130','130~140','140~150','150~160','160~170','170~180','180~190','190~200','>200']
    resp=plt.bar(xlist, numlist,0.5,edgecolor='grey',alpha=0.8)  # 横放条形图函数 barh
    plt.title('楼房面积分布(柱状图2)')
    ##############################设置xy轴字体大小
    plt.xticks(fontproperties = 'Times New Roman', size = 4)
    plt.yticks(fontproperties = 'Times New Roman', size = 5)
    ##############################设置数据标签
    for a,b in zip(xlist,numlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    ##############################
    plt.savefig('opsc7\photos\ps4.png',dpi = 400)
    plt.show()

# 楼房类型 分布 板楼塔楼，板塔楼结合，其它
def decoratetest(df):
    li=listca(df,strs='decorates')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 精装 '):
            numb+=1
        elif(li[num]==' 简装 '):
            numc+=1
        elif(li[num]==' 毛坯 '):
            numd+=1
        else:
            others+=1
    xlist=[' 精装',' 简装',' 毛坯',' 其他']
    ylist=[numb,numc,numd,others]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房装饰方式分布(条形图)')
    plt.savefig('opsc7\photos\ps5.png',dpi = 400)
    plt.show()

def decoratetest2(df):
    li=listca(df,strs='decorates')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 精装 '):
            numb+=1
        elif(li[num]==' 简装 '):
            numc+=1
        elif(li[num]==' 毛坯 '):
            numd+=1
        else:
            others+=1
    xlist=[' 精装',' 简装',' 毛坯',' 其他']
    numb=float(format(numb/2400,'.2f'))
    numc=float(format(numc/2400,'.2f'))
    numd=float(format(numd/2400,'.2f'))
    others=(1-numb-numc-numd)
    pslist=[numb,numc,numd,others]
    a1=int(numb*100)
    a2=int(numc*100)
    a3=int(numd*100)
    a6=100-a1-a2-a3
    a1=xlist[0]+str(a1)+'%'
    a2=xlist[1]+str(a2)+'%'
    a3=xlist[2]+str(a3)+'%'
    a6=xlist[3]+str(a6)+'%'
    xlists=[a1,a2,a3,a6]
    # xlists=[xlist[0]+str(others*100)[0]+str(others*100)[1]+str(others*100)[2]+str(others*100)[3]+'%',xlist[1]+str(numb*100)[0]+str(numb*100)[1]+str(numb*100)[2]+str(numb*100)[3]+'%',xlist[2]+str(numc*100)[0]+str(numc*100)[1]+str(numc*100)[2]+str(numc*100)[3]+'%',xlist[3]+str(numd*100)[0]+str(numd*100)[1]+str(numd*100)[2]+str(numd*100)[3]+'%']
    ylist=np.array(pslist)
    plt.pie(ylist,labels=xlists,colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
    plt.title('楼房装饰方式分布(饼状图)')
    plt.savefig('opsc7\photos\ps6.png',dpi = 400)
    plt.show()

# ========================================================================================================== #
# 晓来雨过，遗踪何在？一池萍碎。春色三分，二分尘土，一分流水。细看来，不是杨花，点点是离人泪。
# 2022/1/5 数据分析
# 对价格的分析
# ========================================================================================================== #
def pricetest(df):
    li=listca(df,strs='price')
    ylist=[]
    counter=0
    ca=0
    cb=0
    numlist=[]
    for num in range(0,2400):
        if li[num]<=40000:
            ca+=1
        elif li[num]>120000:
            cb+=1
        else:
            continue
    numlist.append(ca)
    for s in range(40000,120000,10000):
        counters=0
        for num in range(0,2400):
            if(li[num]>s and li[num]<=(s+10000)):
                counters+=1
            else:
                continue
        numlist.append(counters)
    numlist.append(cb)
    xlist=['<4','4~5','5~6','6~7','7~8','8~9','9~10','10~11','11~12','>12']
    resp=plt.bar(xlist, numlist,0.5,edgecolor='red',alpha=0.8)  # 横放条形图函数 barh
    plt.title('楼房单位面积的价格分布(柱状图)')
    ##############################设置xy轴字体大小 left
    plt.xticks(fontproperties = 'Times New Roman', size = 4)
    plt.yticks(fontproperties = 'Times New Roman', size = 5)
    plt.xlabel('单位面积（万元）')
    plt.ylabel('统计数目')
    ##############################设置数据标签
    for a,b in zip(xlist,numlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    ##############################
    plt.savefig('opsc7\photos\ps7.png',dpi = 400)
    plt.show()

# 对建成时间的分析
# ========================================================================================================== #
def everstest(df):
    li=listca(df,strs='evers')
    ca=0
    cb=0
    numlist=[]
    cnt=0
    for num in range(0,20):
        if li[num]<1985:
            ca+=1
        elif li[num]>=2015:
            cb+=1
        else :
            continue
    numlist.append(ca)
    for s in range(1985,2015,5):
        counters=0
        for num in range(0,2400):
            if(li[num]>=s and li[num]<(s+5)):
                counters+=1
            else:
                continue
        numlist.append(counters)
    numlist.append(cb)
    xlist=['before 1985','after 1985','after 1990','after 1995','after 2000','after 2005','after 2010','after 2015']
    resp=plt.bar(xlist, numlist,0.5,edgecolor='red',alpha=0.8)  # 横放条形图函数 barh
    plt.title('楼房建筑起始年分布(柱状图)')
    ##############################设置xy轴字体大小 left
    plt.xticks(fontproperties = 'Times New Roman', size = 4)
    plt.yticks(fontproperties = 'Times New Roman', size = 5)
    plt.xlabel('建成年份')
    plt.ylabel('统计数目')
    ##############################设置数据标签
    for a,b in zip(xlist,numlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    ##############################
    plt.savefig('opsc7\photos\ps8.png',dpi = 400)
    plt.show()

def floorstest(df):
    li=listca(df,strs='floors')
    numb=0
    numc=0
    numd=0
    nume=0
    numf=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 高楼层'):
            numb+=1
        elif(li[num]==' 中楼层'):
            numc+=1
        elif(li[num]==' 低楼层'):
            numd+=1
        elif(li[num]==' 顶层'):
            nume+=1
        elif(li[num]==' 底层'):
            numf+=1
        else:
            others+=1
    xlist=[' 高楼层',' 中楼层',' 低楼层',' 顶层',' 底层','未指定']
    numb=float(format(numb/2400,'.2f'))
    numc=float(format(numc/2400,'.2f'))
    numd=float(format(numd/2400,'.2f'))
    nume=float(format(nume/2400,'.2f'))
    numf=float(format(numf/2400,'.2f'))
    others=(1-numb-numc-numd-nume-numf)
    pslist=[numb,numc,numd,nume,numf,others]
    a1=int(numb*100)
    a2=int(numc*100)
    a3=int(numd*100)
    a4=int(nume*100)
    a5=int(numf*100)
    a6=100-a1-a2-a3-a4-a5
    a1=xlist[0]+str(a1)+'%'
    a2=xlist[1]+str(a2)+'%'
    a3=xlist[2]+str(a3)+'%'
    a4=xlist[3]+str(a4)+'%'
    a5=xlist[4]+str(a5)+'%'
    a6=xlist[5]+str(a6)+'%'
    xlists=[a1,a2,a3,a4,a5,a6]
    ylist=np.array(pslist)
    plt.pie(ylist,labels=xlists,colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9","#253fad","#3fda4d"])
    plt.title('楼房所在楼层高度分布(饼状图)')
    plt.savefig('opsc7\photos\ps9.png',dpi = 400)
    plt.show()

# ========================================================================================================== #
# 公无渡河，公竟渡河！渡河而死，其奈公何？
# 组合图
# 关注人数与单位面积的价格
# ========================================================================================================== #
def cbchart1(df):
    xli=listca(df,strs='price')
    yli=listca(df,strs='followers')
    xarr=np.array(xli)
    yarr=np.array(yli)
    colorlist=np.random.rand(2400)
    plt.scatter(xarr,yarr,s=0.3,c=colorlist,alpha=0.8)
    plt.xlabel('每单位面积(元)')
    plt.ylabel('关注人数(人)')
    plt.title('单位面积的价格与关注人数（散点图）展示')
    plt.savefig('opsc7\photos\ps10.png',dpi = 400)
    plt.show()

# ========================================================================================================== #
# 有酒湑我，无酒酤我。坎坎鼓我，蹲蹲舞我。迨我暇矣，饮此湑矣。
# 面积与关注人数
# ========================================================================================================== #
def cbchart2(df):
    '''
    advertistitle    格局方正 采光好 保持的很干净 业主自住
    locationa                     新华联家园南区
    locationb                          果园
    configs                         3室2厅
    areas                       119.18平米#
    directs                        南 西 北
    decorates                         精装#
    floors                      中楼层(共7层)#
    evers                         2002年建#
    typs                               板楼#
    price                       44,052元/平#
    followers                      47人关注
    publish                       1个月以前发布
    '''
    xlis=listca(df,strs='areas')
    ylis=listca(df,strs='followers')
    xli=[]
    yli=[]
    cnt=0
    for num in range(0,2400):
        if(xlis[num]<150.0):
            xli.append(xlis[num])
            yli.append(ylis[num])
            cnt+=1
        else:
            continue
    xarr=np.array(xli)
    yarr=np.array(yli)
    colorlist=np.random.rand(cnt)
    plt.scatter(xarr,yarr,s=0.3,c=colorlist,alpha=0.8)
    plt.xlabel('每单位面积(元)')
    plt.ylabel('关注人数(人)')
    plt.title('面积(all)与关注人数（散点图）展示')
    ###########################
    # https://www.pythonf.cn/read/61655
    z1=np.polyfit(xarr,yarr,1)
    p1=np.poly1d(z1)
    yvals=p1(xarr)
    plot2=plt.plot(xarr, yvals, 'r',label='polyfit values',linewidth=0.1)
    np.polyfit(xarr, yarr, 2, rcond=None, full=False, w=None, cov=False)
    plt.show()

def cbcharts3(df):
    '''
    resp=plt.bar(xlist, numlist,0.5,edgecolor='red',alpha=0.8)  # 横放条形图函数 barh
    ##############################设置数据标签
    for a,b in zip(xlist,numlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    '''
    xli=listca(df,strs='price')
    yli=listca(df,strs='followers')
    numlist=[]
    flrlist=[]
    c1=0
    c2=0
    for num in range(0,2400):
        if xli[num]>=170000:
            c1+=1
            c2+=yli[num]
        else:
            continue
    for s in range(10000,170000,10000):
        counters=0
        flcnt=0
        for num in range(0,2400):
            if(xli[num]>=s and xli[num]<(s+10000)):
                counters+=1
                flcnt+=yli[num]
            else:
                continue
        numlist.append(counters)
        flrlist.append(flcnt)
    numlist.append(c1)
    flrlist.append(c2)
    xlists=['1~2','2~3','3~4','4~5','5~6','6~7','7~8','8~9','9~10','10~11','11~12','12~13','13~14','14~15','15~16','16~17','>17']
    resp=plt.bar(xlists, flrlist,0.5,edgecolor='grey',alpha=0.8)  # 条形图函数 bar
    # plt.plot(xarr,yarr,s=0.3,alpha=0.8)
    plt.title('单位面积的价格与关注人数（直方图）展示')
    ##############################设置xy轴字体大小 left
    plt.xticks(fontproperties = 'Times New Roman', size = 4)
    plt.yticks(fontproperties = 'Times New Roman', size = 5)
    plt.xlabel('单位面积（万元）')
    plt.ylabel('统计数目(人数)')
    ##############################设置数据标签
    for a,b in zip(xlists,flrlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    ##############################
    # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
    # sns.distplot(flrlist,color="r",bins=17,kde=True)
    plt.savefig('opsc7\photos\ps12.png',dpi = 400)
    plt.show()

# 在runs中修改调用的函数名，以调用不同函数
# fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
def runs(df):
    cbcharts3(df)
    
def main():
    tst()

if __name__=='__main__':
    main()