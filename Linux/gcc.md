
## gcc

### suod apt install gcc

1. gcc -E hello.c -o hello.i
2. gcc -S hell.i - o hello.s
3. gcc -c hello.s -o hello.o
4. gcc hello.o -o hello

**gcc hello.c  -l /include -o hello**

### gcc 总体选项

| 扩展名 | 含义 |
| ------ | :-----:|
| -E | 预处理 |
| -S | 编译 |
| -c | 汇编 |
| -g | 在可执行文件中包含调试信息 |
| -o file | 输出文件到file |
| -v | 打印编译器内部编译过程中的命令信息和编译器的版本 |
| -I dir | 搜索头文件路径 |
| -L dir | 搜索库文件路径 |
| -static | 链接静态库 |
| -llibrary | 链接库文件 |

### gcc告警项和出错选项列表

| 扩展名 | 含义 |
| ------ | :-----:|
| -ansi | 支持符合ANSI标准的C程序 |
| -pedantic | ANSI C的告警 |
| -pedantic-error | ANSI C的错误 |
| -w | 关闭所有告警 |
| -Wall | 提供有用的告警信息 |
| -werror | 所有告警转换未错误信息,出现告警时停止编译 |
