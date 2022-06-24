## gdb

1. gdb 编译后文件
2. l (查看文件内容) 
3. b 行号 (设置断点)
4. info b
5. r (运行)
6. p 变量名 (查看变量名)
7. n （跳过函数）
8. s （进入函数）
9. c （恢复运行程序）


### 工作环境相关命令
| 命令格式 | 含义 |
| ----- |:------:|
| set args | 指定运行的参数 set args 2 |
| show args |  |
| path dir | 设置程序运行路径 |
| show paths |  |
| set enVironment var [=value] | 设置环境变量 |
| show enVironment [var] |  |
| cd dir |  |
| pwd |  |

### 断点
| 命令格式 | 含义 |
| ----- |:------:|
| info b | 查看所设断点 |
| break 行号或函数名 <条件表达式> | 设置断点 |
| tbreak 行号或函数名 <条件表达式> | 临时断点,到达后自动删除 |
| delete [断点号] | 删除指定断点 |
| disable [断点号] | 停止指定断点 |
| enable [断点号] | 激活制定断定 |
| condition [断点号] <条件表达式> | 修改对应断点的条件爱你 |
| delete [断点号] <num> | 忽略对应断点num次 |
