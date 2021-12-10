## QDrag 拖曳

### MimeData类函数允许检测和使用方便的MIME类型

| 判断函数 | 获取函数 | 设置函数 | MIME类型 |
| hasText() | text() | setText() | text/plain |
| hasHtml() | html() | setHtml() | text/html |
| hasUrls() | urls() | setUrls() | text/url-list |
| hasImage() | imageData() | setImageData() | image/* |
| hasColor() | colorDta() | setColorData() | application/x-color |

### 常用拖曳事件

| 事件 | 描述 |
| dragEnterEvent | 进入控件时触发 |
| dragMoveEvent | 在拖曳操作进行时会触发该事件 |
| dragLeaveEvent | 当执行一个拖曳操作，并且鼠标指针离开该控件时，这个事件被触发 |
| dropEvent | 放入时控件时触发 |




