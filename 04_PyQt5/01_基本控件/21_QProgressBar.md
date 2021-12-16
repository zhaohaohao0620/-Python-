
## QProgressBar 方法

| 方法 | 描述 |
|:-----:|:----:|
| setRange() | 设置进度条的取值范围 |
| setMinimum() | 设置进度条的最小值 |
| setMaximum() | 设置进度条的最大值 |
| setValue() | 设置进度条的值 |
| setOrientation() | 设置进度条方向(水平: Qt.Horizontal, 垂直: Qt.Vertical) |
| setTextVisible() | 设置进度条的文本是否可见 |
| setTextDirection() | 设置文本方向，只对垂直进度条有效 |
| setInvertedAppearance() | 设置进度条的方向(True/False: 正反方向) |
| setFormat() | 设置文本字符串的格式(%p, 百分比显示,这是默认情况, %v: 当前进度, %m :总步数)。 |
| reset() | 让进度条重新回到开始位置 |


## QProgressBar 信号

| 信号 | 描述 |
|:-----:|:----:|
| valueChanged | 进度条的值发生改变时，发射此信号 |
