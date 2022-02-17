from array import array
from os.path import getsize
from struct import unpack


def read1(file_name):
    datas = array('i')

    n = getsize(file_name) // 4
    with open(file_name, 'rb') as f:
        datas.fromfile(f, n)


def read2(file_name):
    n = getsize(file_name) // 4
    with open(file_name, 'rb') as f:
        tmp = '>' + str(n) + 'i'
        data = f.read()
        datas = list(unpack(tmp, data))

    return datas


def write(file_name, data):
    datas = array('i', data)

    with open(file_name, 'wb') as f:
        datas.tofile(f)
