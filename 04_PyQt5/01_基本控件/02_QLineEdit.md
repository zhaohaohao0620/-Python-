

## QLineEdit常用方法

| 方法 | 描述 | 
|-----|:-----:|
| setAlignment() | 对齐 |
|  | Qt.AlignLeft：水平方向靠左对齐 |
|  | Qt.AlignRight:水平方向靠右对齐 |
|  | Qt.AlignCenter：水平方向居中对齐 |
|  | Qt.AlignJustify：水平方向调整间距两端对齐 |
|  | Qt.AlignTop：垂直方向靠上对齐 |
|  | Qt.AlignBottom：垂直方向靠下对齐 |
|  | Qt.AlignVCenter：垂直方向居中对齐 |
| setEchoMode() | 设置文本框的显示格式， 常用于密码输入 |
|  | QLineEdit.Normal：正常显示所输入的字符, 默认 |
|  | QLineEdit.NoEcho：不显示任何输入的字符，且长度保密 |
|  | QLineEdit.Password：显示与平台相关的密码掩饰字符，而不是实际输入的字符 |
|  | QLineEdit.PasswordEchoOnEdit：在编辑时显示字符，负责显示密码类型的输入 |
| setValidator() | 设置文本框的验证器（验证规则），将限制任意可能输入的文本 |
|  | QIntValidator：限制输入整数 |
|  | QQDoubleValidator：限制输入浮点数 |
|  | QRegexpValidator：检查输入是否符合正则表达式 |
| text() | 获取文本内容 |
| setText() | 设置文本内容 |
| setPlaceholderText() | 设置文本框显示文字 |
| setMaxLength() | 设置文本框所允许输入的最大字符数 |
| setReadOnly() | 设置文本为只读 |
| setDragEnable() | 设置文本框是否接受拖动 |
| selectAll() | 全选 |
| setFocus() | 得到焦点 |
| setInputMask() | 设置掩码 |

## 信号
| 方法 | 描述 | 
|-----|:-----:|
| selectionChanged | 只要选择改变了，这个信号就会发射 |
| textChanged | 当修改文本内容时，这个信号就会发射 |
| editingFinished | 当编辑文本结束时，这个信号就会发射 |
