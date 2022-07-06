
#include <stdio.h>
#include <stdarg.h>
#include <time.h>

void vlog(char *format,...)
{
    time_t rawtime;
    struct tm *info;
    char buffer[80];
    char msg[100] = {0};

    va_list valist;

    /* 为 num 个参数初始化 valist */
    va_start(valist, format);

    /* 访问所有赋给 valist 的参数 */
    //va_arg(valist, int);

    vsprintf(msg, format, valist);

    /* 清理为 valist 保留的内存 */
    va_end(valist);

    time(&rawtime);
    info = localtime(&rawtime);

    strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", info);
    printf("[%s] %s\n", buffer, msg);
}

void WriteFrmtd(char *format, ...)
{
    va_list args;
    
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
}

int main ()
{
    WriteFrmtd("%d variable argument\n", 1);
    WriteFrmtd("%d variable %s\n", 2, "arguments");
    
    vlog("age:%d", 10);

    return(0);
}