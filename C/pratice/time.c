#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>


/* struct tm {
  int tm_sec;			//秒[0-59]
  int tm_min;			//分[0-59]
  int tm_hour;			//时[0-23]
  int tm_mday;			//日[1-31]
  int tm_mon;			//月份[0-11]，0代表一月
  int tm_year;			//年份，需要加上1900
  int tm_wday;			//星期[0-6]，0代表星期天
  int tm_yday;			//从每年1月1日开始的天数[0-365]，0代表1月1日
}; */


int main()
{
    // timestamp
    struct timeval t1,t2;
    double useTime = 0.0;

    gettimeofday(&t1, NULL);
    sleep(1);
    gettimeofday(&t2, NULL);

    useTime=(t2.tv_sec - t1.tv_sec) + (t2.tv_usec - t1.tv_usec);//秒
    printf("time_use is %.4f\n",useTime);
 
    // date
    time_t  seconds;
    struct tm *date;
    time(&seconds);
    date = gmtime(&seconds);
 

    printf("%d-%02d-%02d %d:%d:%d:\n",
            date->tm_year + 1900,
            date->tm_mon + 1,
            date->tm_mday,
            date->tm_hour,
            date->tm_min,
            date->tm_sec);
 
    return 0;
}
