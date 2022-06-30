#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>

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
