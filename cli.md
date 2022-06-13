
## python源
 - pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple

## window设置永久源
 - pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

## github 项目
 - https://github.com/DjangoPeng/keras-101.git
 - https://github.com/zhaohaohao0620/-Python-.git

## git 配置

### install
 - sudo apt install git
 - git config --global user.name "xxx"
 - git config --global user.email "xxx@gmail.com"

### github
 - ssh-keygen 
 - cat ~/.ssh/id_rsa.pub
 - ssh -T git@github.com

### 本地git
 - git init 
 - git clone git@github.com:zhaohaohao0620/git-zhao.git

### 常用命令
 - git commit -m “提交信息”。
 - git push -f origin main
 - git pull --rebase origin main

### 设置代理
 - git config --global http.proxy http://127.0.0.1:1080
 - git config --global https.proxy http://127.0.0.1:1080

### 取消代理
 - git config --global --unset http.proxy
 - git config --global --unset https.proxy

### fatal错误
 - git config --global -l
 - env|grep -i proxy




## shell

**chmod +x ./test.sh  使脚本具有执行权限**