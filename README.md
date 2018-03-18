Checkdomain

基于对爆破出的众多子域名进行有选择筛选的探测工具



要求

- python 2.7
- 读取子域名的文件推荐搭配生成lijiejie
  

使用

1. git clone https://github.com/Imanfeng/checkdomain.git
2. cd checkdomain
3. 默认端口：80 
4.     python checkDomain.py -h
       
        ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
       ██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
       ██║     █████╔╝ ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
       ██║     ██╔═██╗ ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
       ╚██████╗██║  ██╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
        ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
       
       
                       V-1.0 # Coded By Imanfeng
       
       usage: checkDomain.py [-h] [-p] [-f] [-o]
       
       checkDomain v 1.0 to check a txt subdoamins which is open port.
       
       OPTIONS:
         -h, --help       show this help message and exit
         -p , --port      choose a port or ports
         -f , --file      choose a subdomain txt
         -o , --outfile   save a file
   
