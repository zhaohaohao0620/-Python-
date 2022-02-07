import numpy as np

## 从文件读数据 np.genfromtxt
npData = np.genfromtxt('E:/python项目/01_机器学习/矩阵/numpy/1.txt', delimiter = ',', dtype = int)
print(npData)

## 切片
print(npData[0:1]) #行
print(npData[:,2]) #列
print(npData[:,0:2]) #多行多列

## 值比较 
## 矩阵每一个值都与某个数值比较, 相等返回True

print(npData[npData[:,1] == 2,:])  #如果有的数与2相等， 打印整行

## 类型转换
print(npData.astype(float))

## 矩阵变换
print(np.arange(15).reshape(3, 5))

## 矩阵维度
npData.ndim

## 矩阵大小
npData.size

## 矩阵初始化
np.zeros((3, 5))
np.ones((3, 5))
np.random.random((3, 5))  ## random 生成0-1数
print(np.linspace(1, np.pi, 50))  ## 从1-3.1415  取50个数

## 矩阵其它操作
a = np.floor(np.random.random((3, 5)) * 10)
b = a.ravel() ## 变成一行
a.shape = (2, -1)  ## 变成2行

## e**a
np.exp(a) 
np.sqrt(4) ## 开根号

## 特征值分解  必须是方阵
a, b = np.linalg.eig(np.random.random((3, 3)))  ## at特征值， b特征向量