#include <stdio.h>


/* 1in = 2.54cm */
#define IN_TO_CM        2.54

int main()
{
    float in = 0.0;
    float out = 0.0;

    while (1)
    {
        printf("input inch:");
        scanf("%f", &in);

        out = in * IN_TO_CM;
        printf("output cm:%f\n", out);
    }

    return 0;
}