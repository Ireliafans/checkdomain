#/usr/bin/env python
#coding:utf-8
import argparse
import sys
import os
import re
import urllib2
import requests
import threading
import datetime



def banner():
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    print("""%s

 ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║     █████╔╝ ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║     ██╔═██╗ ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
╚██████╗██║  ██╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
                                                                 %s%s

                V-1.0 # Coded By Imanfeng 
        """ % (R, W, Y))


def parse_args():#命令定义
    parser = argparse.ArgumentParser(description='checkDomain v 1.0 to check a txt subdoamins which is open port.')
    parser.error=parse_error
    parser._optionals.title='OPTIONS'
    parser.add_argument('-p','--port',metavar="",default='80',help='choose a port or ports')
    parser.add_argument('-f','--file',metavar="",default='',help='choose a subdomain txt')
    parser.add_argument('-o','--outfile',metavar="",default='',help='save a file')
    return parser.parse_args()


def parse_error(errormsg):#传参报错
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errormsg)
    sys.exit()


def open_file(filename):#读取域名文件
    try:
        files = open(filename,'r')
    except IOError, e:
        print "could not open file:",e
        sys.exit(1)
    subdomain = []
    for eachline in files:
        #print eachline
    	line1,line2 = re.split('\s\s+|\t',eachline.strip())
        subdomain.append(line1)
        subdomain.append(line2)
    return subdomain


def check_state(i,port,subdomain_ip):#检查主机状态
    ports = port.split(",")
    for port in ports:
        url = "http://%s:%s"%(subdomain_ip,port)
        try:
            r = requests.get(url,timeout=4)
            status = r.status_code
            if status in {200,301}:
                print "\033[91m[Interesting]:{}:{}".format(subdomain_ip,port)
                intersting.append(subdomain_ip)
        except:
            print "\033[0m[Down]:{}:{}".format(subdomain_ip,port)


def write(ip,infilename,filename):#写进文件
    filename == ''
    filename = 'out.'+infilename
    file = open(filename,'w')
    for i,this_ip in enumerate(ip):
        file.writelines(['%d-----------%s\n' % (i+1,this_ip)])
    file.close()


def go_threading(nums,port,subdomain_ip):#调用多线程
    global intersting
    intersting = []
    threads = []
    for i in nums:
        t = threading.Thread(target=check_state,args=(i,port,subdomain_ip[i]))
        threads.append(t)
    print '\033[1;32m[STRAT..]\n'
    for i in nums:
        threads[i].start()
    for i in nums:
        threads[i].join()
    print '\n\033[1;32m[DONE..]'


def main(port,infile,outfile): 
    subdomain_ip = open_file(infile)
    subdomain_ip = list(set(subdomain_ip))#去重ip/域名
    nums = range(len(subdomain_ip))
    go_threading(nums,port,subdomain_ip)
    write(intersting,infile,outfile)


if __name__ == '__main__':
    banner()
    args = parse_args()
    port = args.port
    infile = args.file
    outfile = args.outfile
    main(port,infile,outfile)
    
    
