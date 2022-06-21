
## python源
 - pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple

## window设置永久源
 - pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

## github 项目
 - https://github.com/DjangoPeng/keras-101.git
 - https://github.com/zhaohaohao0620/-Python-.git


## vscode 常用
 1. 默认固定窗口 ：输入enablePreview搜索，把Workbench>Editor: Enable Preview对勾打掉，就OK了
 2. Tab转空格
    - 检索 tab
    - 检查 Editor: Detect Indetation 是否勾选，如果选中，则将其勾掉，否则 tab 的空格数量将会随文件的不同而发生变化
    - 检查 Editor: Insert Spaces 是否勾选，如果未勾选，则将其选中，否则 tab 将不会转为空格
    - 检查 Editor: Tab Size, 并将其设置为 4，以保证 tab 的数量为 4 个空格
 3. 显示空格：搜索renderControlCharacters，然后选中勾选框。搜索 enderWhitespace，然后选择all。


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




