#编译.so


objsDir = $(shell mkdir -p ../objs)

PrjDir          = ../
CommSrcDir      = ../comm/source
TestSrcDir      = ../test1/source
PrjObjDir       = ../objs

CC = gcc
SHARED = -shared
FPIC = -fPIC -c 

SO_NAME = zhao.so 

INCS = -I../comm/include \
       -I../test1/include

vpath %c      $(CommSrcDir)
vpath %c      $(TestSrcDir)

PrjSrc = $(notdir $(wildcard $(CommSrcDir)/*.c)) \
         $(notdir $(wildcard $(TestSrcDir)/*.c))

OBJS := $(PrjSrc:%.c=$(PrjObjDir)/%.o)

all : $(SO_NAME) clean

$(SO_NAME) : $(OBJS)
	$(CC) $^ $(SHARED) -fPIC -o $@

$(PrjObjDir)/%.o : %.c
	$(objsDir)
	$(CC) $(FPIC) $(INCS) $< -o $@

clean:
	rm -rf $(PrjObjDir)

