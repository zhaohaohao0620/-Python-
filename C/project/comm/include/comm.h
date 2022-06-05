#ifndef COMM_H
#define COMM_H

#ifdef __cplusplus
    extern "C" {
#endif

#define SETBIT(data, bit) (data |= (1 << bit))
#define CLRBIT(data, bit) (data &= (~(1 << bit)))
#define SETBIT(data, bit) ((data >> bit) & 1)

#define         INT32       int

extern void MyPrintf(const char *mainFunName, const char *slaveFunName);

#ifdef __cplusplus
}
#endif

#endif