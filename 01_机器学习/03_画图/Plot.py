import matplotlib.pyplot as plt


x = [1, 2, 3]
y = x

plt.plot(x, y)
## 旋转角度
plt.yticks(rotation = 45)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X-Y')
plt.show()

## 多图
fig = plt.figure()
ax = fig.add_subplot(221)
plt.show()

## 一张图多条线

for i in range(3):
    plt.plot(x, y, c = 'color', lable = '11')


##　标识图像, best自动放置位置
plt.legend(loc = 'best')

fig, axs = plt.subplots(2 , 2, figsize = (5, 5))
ax[0, 0].hist(X)  ## 柱状图
ax[1, 0].scatter(X, Y)  ## 散点图图
ax[0, 1].plot(X)  ## 折线图
ax[1, 1].hist2d(X)  ## 矩阵图
