

## QButton提供的状态

| 状态 | 描述 | 
|-----|:-----:|
| isDown() | 提示按钮是否已按下 |
| isChecked() | 提示按钮是否已经标记 |
| isEnable() | 提示按钮是否可以被用户点击 |
| isCheckAble() | 提示按钮是否为可标记的 |
| setAutoRepeat() | 设置按钮是否在用户长按时可以自动重复执行 |

## QButton提供的信号

| 信号 | 描述 | 
|-----|:-----:|
| Pressed | 当鼠标指针在按钮上并按下左键时触发该信号 |
| Released | 当鼠标左键被释放时触发该信号 |
| Clicked | 当鼠标左键被按下然后释放时 |
| Toggled | 当按钮的标记状态发生改变时触发该信号 |

## QPushButton常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setCheckable() | 设置按钮是否已经被选中 |
| toggle() | 在按钮状态之间进行切换 |
| setIcon() | 设置按钮上的图标 |
| setEnabled() | 设置按钮是否可以使用 |
| isChecked() | 返回按钮的状态 |
| setDefault() | 设置按钮的默认状态 |
| setText() | 设置按钮的显示文本 |
| text() | 返回按钮的显示文本 |

## QRadioButton常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setCheckable() | 设置按钮是否已经被选中 |
| isChecked() | 返回按钮的状态 |
| setText() | 设置按钮的显示文本 |
| text() | 返回按钮的显示文本 |

## QCheckBox常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setCheckable() | 设置按钮是否已经被选中 |
| isChecked() | 返回按钮的状态 |
| setText() | 设置按钮的显示文本 |
| text() | 返回按钮的显示文本 |
| setTriState() | 设置复选框为一个三态复选框 |
| setCheckState() | 三态复选框的状态设置，具体设置可以见下表 |

### 三态复选框

| 名称 | 值 | 含义 |
|-----|:-----:|:-----:|
| Qt.Checked | 2 |组件没有被选中（默认） |
| Qt.PartiallyChecked | 1 | 组件被半选中 |
| Qt.Unchecked | 0 | 组件被选中 |
