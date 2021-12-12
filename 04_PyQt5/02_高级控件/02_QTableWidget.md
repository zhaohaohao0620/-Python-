# QTableWidget (QTableView的子类) 

## QTableWidget 方法

| 方法 | 描述 |
|:-----:|:-----:|
| setRowCount(int row) | 设置QTableWidget表格控件的行数 |
| setColumnCount(int col) | 设置QTableWidget表格控件的列数 |
| setHorizontalHeaderLabels() | 设置QTableWidget表格控件的水平标签 |
| setVerticalHeaderLabels() | 设置QTableWidget表格控件的垂直标签 |
| setItem(int ,int ,QTableWidgetItem) | 在QTableWidget表格控件的每个选项的单元控件内添加控件 |
| horizontalHeader() | 获得QTableWidget表格控件的表格头，以便执行隐藏 |
| setSpan(int row,int column,int rowSpanCount,int columnSpanCount) | 合并单元格，要改变单元格的第row行，column列，<br>要合并rowSpancount行数和columnSpanCount列数 |
|  | row：要改变的行数 |
|  | column：要改变的列数 |
|  | rowSpanCount：需要合并的行数 |
|  | columnSpanCount：需要合并的列数 |
| rowCount() | 获得QTableWidget表格控件的行数 |
| columnCount() | 获得QTableWidget表格控件的列数 |
| setShowGrid() | 在默认情况下表格的显示是有网格的，可以设置True或False用于是否显示，默认True |
| setColumnWidth(int column,int width) | 设置单元格行的宽度 |
| setRowHeight(int row,int height) | 设置单元格列的高度 |
| setEditTriggers(EditTriggers triggers) | 设置表格是否可以编辑，设置表格的枚举值 |
| setSelectionBehavior | 设置表格的选择行为 |
| setTextAlignment() | 设置单元格内文本的对齐方式 |


## 编辑规则的枚举值类型(setEditTriggers)

| 选项 | 值 | 描述 |
|:-----:|:-----:|:-----:|
| QAbstractItemView.NoEditTriggers0No | 0 | 不能对表格内容进行修改 |
| QAbstractItemView.CurrentChanged1Editing | 1 | 任何时候都能对单元格进行修改 |
| QAbstractItemView.DoubleClicked2Editing | 2 | 双击单元格|
| QAbstractItemView.SelectedClicked4Editing | 4 | 单击已经选中的内容 |
| QAbstractItemView.EditKeyPressed8Editing | 8 | 当修改键按下时修改单元格 |
| QAbstractItemView.AnyKeyPressed16Editing | 16 | 按任意键修改单元格 |
| QAbstractItemView.AllEditTriggers31Editing | 31| 包括以上所有条件 |


## 表格选择行为的枚举值(setSelectionBehavior)

| 选项 | 值 | 描述 |
|:-----:|:-----:|:-----:|
| QAbstractItemView.SelectItems0Selecting	 | 0 | 选中单个单元格 |
| QAbstractItemView.SelectRows1Selecting | 1 | 选中一行 |
| QAbstractItemView.SelectColumns2Selecting | 2 | 选中一列|

## 水平方向对齐

| 方法 | 描述 |
|:-----:|:-----:|
| Qt.AlignLeft | 将单元格内的内容沿单元格的左边缘对齐 |
| Qt.AlignRight | 将单元格内的内容沿单元格的右边缘对齐 |
| Qt.AlignHCenter | 在可用空间中，居中显示在水平方向上 |
| Qt.AlignJustify| 将文本在可用空间内对齐，默认从左到右 |


## 垂直方向对齐

| 方法 | 描述 |
|:-----:|:-----:|
| Qt.AlignTop | 与顶部对齐 |
| Qt.AlignBottom | 与底部对齐 |
| Qt.AlignVCenter | 在可用空间中，居中显示在垂直方向上 |
| Qt.AlignBaseline| 与基线对齐 |

## 信号

| 信号 | 含义 |
|:-----:|:----:|
| doubleClicked | 双击信号

```
    self.table.doubleClicked.connect(self.ShowDatas)
    def ShowDatas(self,index):
        row = index.row()
        item = self.table.item(row,1).text()
```