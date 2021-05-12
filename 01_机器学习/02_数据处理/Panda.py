## 数据处理
import pandas as pd

info = pd.read_csv('**.csv', encoding = 'gbk')


## 读数据方法,默认前5条
info.head()
info.tail()

info.columns
info.shape

## 获取指定行数据
info.loc[i]
info.loc[i : n]

## 指定列
info['1']
info[['1', '2']]

## 处理空值
pd.isnull(info['1'])

info['1'][pd.isnull(info['1']) == False]

## 分组
info.pivot_table(index = 'sex', values = 'money', aggfunc = np.sum)