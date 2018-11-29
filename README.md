# Learn_Django
Django学习

## Linux环境下使用Git

1. Github新建仓库
2. 创建SSH Key 看在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件
3. 没有/home/xxx/.ssh
ssh-keygen -t rsa -C "youremail@example.com"
4. 添加SSH Key到github
5. makedir mygit  
   cd mygit  
   git init  
   git add xxx(文件或目录)  
   git commit -m "文字说明"  
   git remote add origin git@github.com:xxx/xxx.git  
   git fetch/ git pull origin master  
   git push -u origin master (first time)  
   git push origin master (next times)     

## Ubuntu安装虚拟环境

Sudo pip install virtualenv  
Sudo pip install virtualenvwrapper  

若出现 sudo pip 找不到命令，则更换 /etc/apt/sources.list 的内容为清华源 
> https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

Python pip： https://pypi.tuna.tsinghua.edu.cn/simple 

sudo apt-get update  
sudo apt-get install python-pip / sudo apt-get install python3-pip  

安装对应的pip
再重复上述安装虚拟环境

### 创建虚拟环境管理目录

mkdir ~/.virtualenvs

打开.bashrc

sudo vim ~/.bashrc

在.bashrc的末尾增加下面内容

export WORKON_HOME=$HOME/.virtualenvs  # 所有虚拟环境存储的目录  
source /usr/local/bin/virtualenvwrapper.sh  

### 启用配置文件

source ~/.bashrc

### 虚拟环境操作

    + 创建虚拟环境
    mkvirtualenv env_name # env_name为你要创建的虚拟环境的名字，创建虚拟环境需要联网
    + 创建指定python版本的虚拟环境
    mkvirtualenv -p /usr/bin/python3 env_name
    mkvirtualenv -p /usr/bin/python2 env_name
    +  运行环境
    workon env_name
    workon + 两次tab键可以显示所有的虚拟环境
    + 退出虚拟环境
    deactivate
    + 删除虚拟环境
    rmvirtualenv env_name

