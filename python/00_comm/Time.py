from datetime import datetime, timedelta
from time import sleep
from pytz import timezone
from os.path import getmtime


start = datetime.now()
sleep(3)
end = datetime.now()
cost_time = str((end - start).seconds) + 's' + str((end - start).microseconds // 1000) + 'ms'
print(cost_time)

print(start.strftime('%Y-%m-%d %H:%M:%S.%f'))

now = '2022-02-22 22:22:22'
print(datetime.strptime(now, '%Y-%m-%d %H:%M:%S'))

after_three_days = (start + timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
print(after_three_days)

utc = timezone('Asia/Shanghai')
datetime.fromtimestamp(getmtime('./../files/test.csv'), utc).strftime('%Y-%m-%d %H:%M:%S')

def costTime(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        cost_time = str((end - start).seconds) + 's' + str((end - start).microseconds // 1000) + 'ms'
        print(f'func:{func.__name__}--{cost_time}')

        return func(*args)

    return wrapper()