import csv
from collections import Counter
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType

with open("islist0.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    column = [row[2] for row in reader]
    # print (column)
    result = Counter(column)
    # print (result)
    words = result.items()

def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("二手房所在地区词云", words, word_size_range=[20, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="二手房所在地区词云"))
    )
    return c

def main():
    wd = wordcloud_base()
    wd.render()

if __name__=='__main__':
    main()