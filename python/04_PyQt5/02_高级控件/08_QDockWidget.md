
## QDockWidget 常用方法

| 方法 | 描述 |
|:-----:|:-----:|
| setWidget() | 在Dock窗口区域设置QWidget |
| setFloating() | 设置Dock窗口是否可以浮动，如果设置为True，则表示可以浮动 |
| setAllowedAreas() | 设置窗口可以停靠的区域 |
| | LeftDockWidgetArea:左侧停靠区域 |
| | RightDockWidgetArea:右侧停靠区域 |
| | TopDockWidgetArea:顶部停靠区域 |
| | BottomDockWidgetArea:底部停靠区域 |
| | NoDockWidgetArea:不显示Widget |
| setFearures() | 设置停靠窗口的功能属性 |
| | DockWidgetClosable:可关闭 |
| | DockWidgetMovable：可移动 |
| | DockWidgetFloatable：可漂浮 |
| | DockWidgetVerticalTitleBar：在左边显示垂直的标签栏 |
| | AllDockWidgetFeatures:具有前三种属性的所有功能 |
| | NoDockWidgetFeatures：无法关闭，不能悬浮，不能移动 |

