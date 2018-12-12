# Learn_Django
Django学习

## Linux环境下使用Git

参考
   
[廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)  

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

## Windows环境下使用Git

https://git-scm.com/downloads 下载

### 下载 git 的安装包
Git-2.19.2-64-bit.exe

能打开 git bash 命令行界面即安装成功

设置输入 名字、email     git config --global      表示这台机器上所有Git仓库都使用此配置  

```
git config --global user.name "Your Name"  
git config --global user.email “email@example.com”

git config --global core.autocrlf false       禁止自动转换为crlf
```

### 新建一个空目录，将其变成Git可以管理的仓库

git init 之后当前目录下会有 .git（版本库）  
```
mkdir mygit   
cd mygit    

git init
```


### 写一个文件添加到Git仓库

```
Vi readme.txt

git add readme.txt  # add可以多次添加  
git commit -m “test readme”  # 添加提交说明  
```

### Git区域

Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

![工作区与版本库](https://cdn.liaoxuefeng.com/cdn/files/attachments/001384907702917346729e9afbf4127b6dfbae9207af016000/0 "工作区与版本库")

需要提交的文件修改通通放到暂存区，然后，一次性提交暂存区的所有修改

### Git基本命令

```
git status                           # 查看当前仓库状态  
git diff readme.txt                  # 查看修改的部分  
git diff HEAD -- readme.txt          # 命令可以查看工作区和版本库里面最新版本的区别  
git log                              # 查看最近到最远的提交日志  
git reset --hard HEAD^               # 回退到上一个版本 HEAD表示当前版本 HEAD^表示上一个 HEAD^^表示上上个，前一百个表示：HEAD~100  
git reset --hard commit_id           # 回到某个版本id对应的版本  
git reflog                           # 查看记录的每一次版本命令 可以从中找到之前版本的id 回退到该版本  
git checkout -- readme.txt           # 意思就是，把readme.txt文件在工作区的修改全部撤销；若修改之后还提交到了暂存区（add），分两步 git reset HEAD file 再使用 checkout  
rm readme.txt                        # 删除当前工作区文件  
git rm readme.txt    git commit -m “remove”                  # 删除版本库中文件 并提交  
git rm readme.txt    git commit -m “remove”     git push     # 删除远程仓库中的文件 并提交  
git push origin master                                       # 把本地master分支推送到远程库  
git clone (ssh…)                                             # 克隆远程到本地  
```

### Git 添加远程仓库

用户主目录下没有.ssh 目录的话，需要创建SSH Key：

`ssh-keygen -t rsa -C “youremail@example.com”`

可以在GitHub的settings 中添加 id_rsa.pub 中的内容

#### 添加远程仓库
（Git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快）

若远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令
```
git remote add origin “git@github.com:michaelliao/learngit.git“   # origin 为远程库名字 后面跟的是GitHub对应仓库的ssh  
git push -u origin master                                         # 推送本地库中所有内容至远程库  
```
#### 若已经有远程仓库
则可以克隆一个到本地库

git clone “git@github.com:michaelliao/gitskills.git”              # 克隆远程库到本地

---

#### 若已有远程库，新建了本地库想要推送至远程，按上述添加远程库后会出现

```
Warning: Permanently added 'github.com,13.250.177.223' (RSA) to the list of known hosts.
To github.com:joelYing/All_Spider.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:joelYing/All_Spider.git'
```

**的问题，并提示你 git pull**

```
$ git pull
warning: no common commits
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 23 (delta 7), reused 9 (delta 2), pack-reused 0
Unpacking objects: 100% (23/23), done.
From github.com:joelYing/All_Spider
 * [new branch]      master     -> origin/master
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> master
```

**尝试 git pull origin master**

```
$ git pull origin master
Warning: Permanently added the RSA host key for IP address '13.229.188.59' to the list of known hosts.
From github.com:joelYing/All_Spider
 * branch            master     -> FETCH_HEAD
fatal: refusing to merge unrelated histories
```

参考 [git-出现-fatal-refusing-to-merge-unrelated-histories-错误](https://www.centos.bz/2018/03/git-%E5%87%BA%E7%8E%B0-fatal-refusing-to-merge-unrelated-histories-%E9%94%99%E8%AF%AF/)

**git pull 失败 ,提示：fatal: refusing to merge unrelated histories**

其实这个问题是因为 两个 根本不相干的 git 库， 一个是本地库， 一个是远端库， 然后本地要去推送到远端， 远端觉得这个本地库跟自己不相干， 所以告知无法合并

具体的方法， 一个种方法： 是 从远端库拉下来代码 ， 本地要加入的代码放到远端库下载到本地的库， 然后提交上去 ， 因为这样的话， 你基于的库就是远端的库， 这是一次update了

第二种方法：
使用这个强制的方法

**git pull origin master --allow-unrelated-histories**

后面加上 --allow-unrelated-histories ， 把两段不相干的 分支进行强行合并后出现

```
Merge branch 'master' of github.com:joelYing/All_Spider

# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
```

**：wq 回车即可**

```
$ git pull origin master --allow-unrelated-histories
From github.com:joelYing/All_Spider
 * branch            master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 README.md            |   2 +
 Weixin_Article1      | 156 +++++++++++++++++++++++++++++++++++++++++++++
 Weixin_Article2      | 176 +++++++++++++++++++++++++++++++++++++++++++++++++++
 YuanTong_tousu       |  94 +++++++++++++++++++++++++++
 headerstool.py       |  21 ++++++
 twitter_2022_test.py | 139 ++++++++++++++++++++++++++++++++++++++++
 twitter_user.py      | 154 ++++++++++++++++++++++++++++++++++++++++++++
 7 files changed, 742 insertions(+)
 create mode 100644 README.md
 create mode 100644 Weixin_Article1
 create mode 100644 Weixin_Article2
 create mode 100644 YuanTong_tousu
 create mode 100644 headerstool.py
 create mode 100644 twitter_2022_test.py
 create mode 100644 twitter_user.py
```

**后面再push就可以**


```
$ git push -u origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 735 bytes | 735.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:joelYing/All_Spider.git
   1d03d2c..ef53313  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

**Success**

---

### Git 分支管理
git branch dev  git checkout dev         # 创建并切换到分支dev
git checkout -b dev                     # 创建并切换到分支dev
git branch                             # 查看分支 带 \* 号的是当前分支
git merge dev                          # 把dev 分支上的工作合并到 master  先切换到master，把指定分支合并到当前分支上
git branch -d dev                       # 合并之后删除分支 dev

在dev提交完修改后切换到master 再在master上修改之后提交，此时两个分支上都有新的提交

![分支冲突](https://cdn.liaoxuefeng.com/cdn/files/attachments/001384909115478645b93e2b5ae4dc78da049a0d1704a41000/0 "分支冲突")

这种情况下 Git 无法快速合并，会有冲突，解决冲突的办法就是把Git合并失败的文件手动编辑为我们希望的内容，再提交
```
git log --graph                                   # 看分支合并图  
git log --graph --pretty=oneline --abbrev-commit  # 分支合并图  
```

### 多人协作

```
git remote                                 # 查看远程仓库信息  
git remote -v                              # 显示详细信息  
```

### 从远程仓库获取最新代码合并到本地分支--推荐

```
//查询当前远程的版本
$ git remote -v
//获取最新代码到本地(本地当前分支为[branch]，获取的远端的分支为[origin/branch])
$ git fetch origin master  [示例1：获取远端的origin/master分支]
$ git fetch origin dev [示例2：获取远端的origin/dev分支]
//查看版本差异
$ git log -p master..origin/master [示例1：查看本地master与远端origin/master的版本差异]
$ git log -p dev..origin/dev   [示例2：查看本地dev与远端origin/dev的版本差异]
//合并最新代码到本地分支
$ git merge origin/master  [示例1：合并远端分支origin/master到当前分支]
$ git merge origin/dev [示例2：合并远端分支origin/dev到当前分支]
```


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

