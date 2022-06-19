objsDir = $(shell mkdir -p ../objs)

PrjDir          = ../
MainSrcDir      = ../main/source
PrjObjDir       = ../objs

CC = gcc
CFLAGS = -Wall -c

LIB_NAME = zhao.so

INCS = -I../main/include

vpath %c      $(MainSrcDir)

PrjSrc = $(notdir $(wildcard $(MainSrcDir)/*.c))

OBJS := $(PrjSrc:%.c=$(PrjObjDir)/%.o)

all : main clean


# export LD_LIBRARY_PATH=./
main : $(OBJS)
	$(CC) $^ -L. $(LIB_NAME) -o $@

$(PrjObjDir)/%.o : %.c
	$(objsDir)
	$(CC) $(CFLAGS) $(INCS) $< -o $@

clean:
	rm -rf $(PrjObjDir)

