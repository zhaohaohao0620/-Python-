#编译.a


objsDir = $(shell mkdir -p ../objs)

PrjDir          = ../
CommSrcDir      = ../comm/source
TestSrcDir      = ../test1/source
PrjObjDir       = ../objs

CC = gcc
CFLAGS = -Wall -c
AR = ar rc

LIB_NAME = lib.a

INCS = -I../comm/include \
       -I../test1/include

#搜索源文件
vpath %c      $(CommSrcDir)
vpath %c      $(TestSrcDir)

#notdir 剥离文件的绝对路径，只保留文件名 wildcard 获取目录下所有.c文件
PrjSrc = $(notdir $(wildcard $(CommSrcDir)/*.c)) \
         $(notdir $(wildcard $(TestSrcDir)/*.c))

#将PrjSrc中以 .c结尾的文件都用PrjObjDir下的 .o替换 %$(var :a=b)
OBJS := $(PrjSrc:%.c=$(PrjObjDir)/%.o)

all : $(LIB_NAME) clean

$(LIB_NAME) : $(OBJS)
	$(AR) $@ $^

$(PrjObjDir)/%.o : %.c
	$(objsDir)
	$(CC) $(CFLAGS) $(INCS) $< -o $@

clean:
	rm -rf $(PrjObjDir)

