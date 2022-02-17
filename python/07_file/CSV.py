from csv import reader, writer


def read(file_name):
    with open(file_name, 'r', newline='') as f:
        csv_datas = reader(f, delimiter=',')
        for d in csv_datas:
            print(d)

def write(file_name):
    out = [
        ['name', 'age'],
        ['zhao', '25'],
    ]

    with open(file_name, 'w', newline='') as f:
        w = writer(f)
        w.writerows(out)


if __name__ == "__main__":
    read('./../files/test.csv')
    write('./../files/out.csv')

