# 一、 pip install 相关
>>### 1、生成requirements.txt文件
>>>> pip freeze > requirements.txt
>> ### 2、安装requirements.txt依赖
>>>>pip install -r requirements.txt  
>>>>sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt	加镜像
>> ### 3、删除已安装的包
>>>>pip uninstall package_name
>> ### 4、下载wheel文件 
>>>>https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib




# 二、windows下的常用命令
>>### 1、查询进程信息
>>>>tastlist 查询所有的进程信息  
>>>>tasklist | findstr "java" 查找进程名包含“java”的所有进程，详细使用方式使用tasklist | ?查看。
>>### 2、查看指定端口的连接信息
>>>>使用netstat -ano | findstr "8080"，在"|"前面的命令执行结果作为后一个命令执行的输入。


### 三、运行中一些bug解决方法
>>### 1、python3 UnicodeEncodeError
>>>>Python3中遇到UnicodeEncodeError: 'ascii' codec can't encode characters in ordinal not in range(128)  
>>>>解决办法：PYTHONIOENCODING=utf-8 python xxxx.py


# 四、Linux下的常用命令
>>### 1、某个进程查看详情 
>>>>ps -ef | grep 14708  
>>### 2、Linux启动某个程序将日志输出到文件
>>>>nohup java -jar ./packages/alarm/alarm.jar --server.port=21515 > ./packages/moduleLogs/alarm.log 2>&1 &  
>>### 3、查看端口号
>>>>lsof -i:(端口号)  
>>>>netstat -apn | grep 3306  
>>>>netstat -na | grep 53100  对端口号的查询  
>>### 4、根据端口号杀死某个进程
```
kill -9 $(netstat -tlnp | grep :8889 | awk '{print $7}' | awk -F '/' '{print $1}')
kill -9 $(lsof -i tcp:8889 -t)  root权限 常用
kill -9 $(sudo lsof -i tcp:8889 -t)  非root权限
```
>>### 5、tar在Linux上是常用的打包、压缩、加压缩工具
```
他的参数很多，这里仅仅列举常用的压缩与解压缩参数
参数：
-c ：create 建立压缩档案的参数；

-x ： 解压缩压缩档案的参数；

-z ： 是否需要用gzip压缩；

-v： 压缩的过程中显示档案；

-f： 置顶文档名，在f后面立即接文件名，不能再加参数

举例： 一，将整个/home/www/images 目录下的文件全部打包为 /home/www/images.tar

 tar -cvf /home/www/images.tar /home/www/images ← 仅打包，不压缩

 tar -zcvf /home/www/images.tar.gz /home/www/images ← 打包后，以gzip压缩


在参数f后面的压缩文件名是自己取的，习惯上用tar来做，如果加z参数，则以tar.gz 或tgz来代表gzip压缩过的tar file文件

1 将tgz文件解压到指定目录

tar   zxvf    test.tgz  -C  指定目录

比如将/source/kernel.tgz解压到  /source/linux-2.6.29 目录

tar  zxvf  /source/kernel.tgz  -C /source/ linux-2.6.29


2 将指定目录压缩到指定文件

比如将linux-2.6.29 目录压缩到  kernel.tgz

 tar czvf kernel.tgz linux-2.6.29
```
>>### 6、查看gpu信息
>>>>nvidia-smi -l 1  (一秒刷新一次)
>>### 7、对文件权限的修改
>>>>chmod -R 777 restart.sh
>>### 8、xxx.sh文件运行报错
```
chmod -R 777 restart.sh (赋予权限，默认-rw-rw-r--没有可执行权限，不赋予权限脚本运行不了)
执行玩chmod之后，权限已经改变-rwxrwxrwx

Syntax error : end of file unexpected (expecting “then”)  
解决方法在vim下，文件结尾 输入：set fileformat=unix 修改ubuntu 和linux服务器、 dos等非图形界面冲突  wq保存   解决
```
# 五、docker
>>### 1、在私有仓库中拉取镜像，并生成容器
```
docker pull 192.168.4.125:5000/pgy_common
docker run -itd --privileged=true --net="host"  --restart unless-stopped -v /package:/package  --name agent  192.168.4.125:5000/pgy_common  /bin/bash
```
>>### 2、进入到docker容器里
>>>>docker exec -it agent_test /bin/bash  
>>### 3、根据docker官方Redis镜像生成带密码的Redis容器
>>>>docker run --name redis -p 6379:6379 -d --restart=always redis --requirepass "tianxiao"  
# 六、在Ubuntu16.04下创建只有python3的虚拟环境
```
用 virtualvenvwrapper 创建的虚拟环境里 既有 py2 还有 py3 ，pip啥的也是乱七八糟的，有脏东西，改用 python3 自带的 venv 创建纯净的，只有 python3 ，pip也只对应 python3 的虚拟环境
安装 python3-venv：apt-get install python3-venv
创建虚拟环境 ,mxonline 为虚拟环境所在的文件夹的名称：~/Documents# python3 -m venv mxonline
mxonline/bin 里的 python 和 python3 全都是 python3.5 
使用 pip 安装的 包也都是对应 python 3.5的
~/Documents/mxonline/bin# ls
activate  activate.csh  activate.fish  easy_install  easy_install-3.5  pip  pip3  pip3.5  python  python3
激活虚拟环境 source activate：~/Documents/mxonline/bin# source activate
退出虚拟环境 deactivate
```

# 七、scrapy
>>## 1、
>>>>在开始爬取之前，必须创建一个新的Scrapy项目。进入自定义的项目目录中，运行下列命令：  
>>>>scrapy startproject mySpider
>>### 2、
>>>>在当前目录下输入命令，将在mySpider/spider目录下创建一个名为itcast的爬虫，并指定爬取域的范围：  
>>>>scrapy genspider itcast "itcast.cn"

>>### 3、scrapy genspider -l  查询有哪些模板

>>### 4、通过下面的命令可以快速创建 CrawlSpider模板 的代码：
```
scrapy genspider -t crawl tencent tencent.com  
将start_urls的值修改为需要爬取的第一个url
start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)
scrapy crawl itcast
```

>>### 5、scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，，命令如下：
```
# json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json
# json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonl
# csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv
# xml格式
scrapy crawl itcast -o teachers.xml
```



















