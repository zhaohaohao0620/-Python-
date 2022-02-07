
## QDateTimeEdit 类中常用方法
| 方法 |	描述 |
|:-----:|:-----:|
| setDisplayFormat() | 设置日期的时间格式 |
|  | yyyy：代表年份，用4为数表示 |
|  | MM：代表月份，取值范围01-12 |
|  | dd：代表日，取值范围01-31 |
|  | HH：代表小时，取值范围00-23 |
|  | mm：代表分钟，取值范围00-59 |
|  | ss：代表秒，取值范围00-59 |
| setMinimumDate() | 设置控件的最小日期 |
| setMaximumDate() | 设置控件的最大日期 |
| time() | 返回编辑的时间 |
| date() | 返回编辑的日期 |


## QDateTimeEdit 类中常用信号

| 信号 |	含义 |
|:-----:|:-----:|
| dateChanged | 当日期改变时发射此信号 |
| dateTImeChanged | 当日期时间改变时发射此信号 |
| timeChanged | 当时间发生改变时发射此信号 |