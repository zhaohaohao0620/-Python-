## QComboBox 常用方法

| 方法 | 描述 | 
|-----|:-----:|
| addItem() | 添加一个下拉选项 |
| addItems() | 从列表中添加下拉选项 |
| clear() | 删除下拉选项集合中的所有选项 |
| count() | 返回下拉选项集合中的数目 |
| currentText() | 返回选中选项的文本 |
| itemText(i) | 获取索引为i的item的选项文本 |
| currentIndex() | 返回选中项的索引 |
| setItemText(int index,text) | 改变序列号为index的文本 |

## QComboBox 提供的信号

| 信号 | 描述 | 
|-----|:-----:|
| activated | 当用户选中一个下拉选项时发射该信号，同下个信号 |
| currentIndexChanged | 当下拉选项的索引发生改变时发射该信号 |
| highlighted | 鼠标一放上，发射该信号 |

