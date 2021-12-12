## QSlider 常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setMinimum() | 设置滑动条控件的最小值 |
| setMaximum() | 设置滑动条控件的最大值 |
| setSingleStep() | 设置滑动条控件的步长 |
| setValue() | 设置滑动条控件的值 |
| value() | 获取滑动条控件的值 |
| setTickInterval() | 设置刻度间隔 |
| setTickPosition() | 设置刻度标记的位置，可以输入一个枚举值，这个枚举值指定刻度线想当与滑块和用户操作的位置，以下是可以输入的枚举值 |
| | QSlider.NoTicks:不绘制任何刻度线 |
| | QSlider.TicksBothSides：在滑块的两侧绘制刻度线 |
| | QSlider.TicksAbove:在滑块的（水平）上方绘制刻度线 |
| | QSlider.TicksBelow:在滑块的（水平）下方绘制刻度线 |
| | QSlider.TicksLeft:在滑块的（垂直）左侧绘制刻度线 |
| | QSlider.TicksRight,在滑块的（垂直）右侧绘制刻度线 |

## QSlider 提供的信号

| 信号 | 描述 | 
|-----|:-----:|
| valueChanged | 数字只要改变就发射信号 |
| sliderPressed | 当用户按下滑块时发射此信号 |
| sliderMoved | 当用户拖动滑块时发射此信号 |
| sliderReleased | 当用户释放滑块时发射此信号 |

