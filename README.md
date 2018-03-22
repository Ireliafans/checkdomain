# Checkdomain

基于对爆破出的众多子域名进行有选择筛选的探测工具



## 要求

- python 2.7
- 读取子域名的文件中间空格断开，推荐搭配lijiejie的
  subdoamin生成

## 使用

1. `git clone https://github.com/Imanfeng/checkdomain.git`
2. `cd checkdomain`
3. `选择端口:-p 80,8080...(默认端口：80) `
4.     python checkDomain.py -h
       
        ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
       ██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
       ██║     █████╔╝ ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
       ██║     ██╔═██╗ ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
       ╚██████╗██║  ██╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
        ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
       
       
                       V-2.0 # Coded By Imanfeng
       
       usage: checkDomain.py [-h] [-p] [-f] [-o]
       
       checkDomain v 1.0 to check a txt subdoamins which is open port.
       
       OPTIONS:
         -h, --help       show this help message and exit
         -p , --port      choose a port or ports
         -f , --file      choose a subdomain txt
         -o , --outfile   save a file
   
## 版本
- v-1.0 支持读取指定格式子域名文件，指定单端口单线程扫描，默认文件输出
- v-2.0 支持读取制定格式子域名文件，多端口多线程扫描扫描，默认输出为out.xxx.txt
