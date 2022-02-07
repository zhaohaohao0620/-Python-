## QDialog 常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setWindowTitle() | 设置对话框标题 |
| setWindowModality() | 设置窗口模态 |
| | Qt.NonModal:非模态，可以和程序的其他窗口进行交互 |
| | Qt.WindowModal:窗口模态，程序在未处理玩当前对话框时，将阻止和对话框的父窗口进行交互 |
| | Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互 |
| | QSlider.TicksBelow:在滑块的（水平）下方绘制刻度线 |
| | QSlider.TicksLeft:在滑块的（垂直）左侧绘制刻度线 |
| | QSlider.TicksRight,在滑块的（垂直）右侧绘制刻度线 |

## QMessageBox 常用方法

| 方法 | 描述 | 
|-----|:-----:|
| information(QWdiget parent,title,text,buttons,defaultButton)| 设置对话框标题 |
| | parent：指定的父窗口控件 |
| | title：对话框标题 |
| | text：对话框文本 |
| | buttons：多个标准按钮，默认为ok按钮 |
| | defaultButton：默认选中的标准按钮，默认选中第一个标准按钮 |
| question（QWidget parent,title,text,buttons,defaultButton） | 弹出问答对话框 |
| warning（QWidget parent,title,text,buttons,defaultButton） | 弹出警告对话框 |
| critical（QWidget parent,title,text,buttons,defaultButton） | 弹出严重错误对话框 |
| about（QWidget parent,title,text） | 弹出关于对话框 |
| setTitle() | 设置标题 |
| setText() | 设置正文消息 |
| setIcon() | 设置弹出对话框的图片 |

## QMessageBox 标准按钮

| 类型 | 描述 | 
|-----|:-----:|
| QMessage.Ok | 同意操作 |
| QMessage.Cancel | 取消操作 |
| QMessage.Yes | 同意操作 |
| QMessage.No | 取消操作 |
| QMessage.Abort | 终止操作 |
| QMessage.Retry | 重试操作 |
| QMessage.Ignore | 忽略操作 |

## QInputDialog 提供的方法

| 方法 | 描述 | 
|-----|:-----:|
| getint() | 从控件中获得标准整数输入 |
| getDouble() | 从控件中获得标准浮点数输入 |
| getText() | 从控件中获得标准字符串的输入 |
| getItem() | 从控件中获得列表里的选项输入 |

## QFileDialog 提供的方法

| 方法 | 描述 | 
|-----|:-----:|
| getOpenFileName() | 返回用户所选择文件的名称 |
| getSaveFileName() | 使用用户选择的文件名保存文件 |
| setFileMode() | 可以选择的文件类型 |
|  | QFileDialog.AnyFile:任何文件 |
|  | QFileDialog.ExistingFile:已存在的文件 |
|  | QFileDialog.Directory:文件目录 |
|  | QFileDialog.ExistingFiles:已经存在的多个文件 |
| setFilter() | 设置过滤器, 只显示过滤器允许的文件类型 |
