#/usr/bin/env python
#coding:utf-8
import argparse
import sys
import os
import re
import urllib2
import requests

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
    parser.add_argument('-o','--outfile',metavar="",default='out.txt',help='save a file')
    #parser.add_argument('-t','--threads',metavar="",default=16,help='thread count')
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


def check_state(subdomain_ip,port):#检查主机状态
    print '\033[92m'+'[STRAT..]'
    intersting=[]
    for i,this_ip in enumerate(subdomain_ip):
        url="http://{}:{}".format(this_ip,port)
        #print url 
        try:
            r = requests.get(url)
            status = r.status_code
            if status in {200,301}:
                print ("\033[91m")
                print "Interesting:{}".format(this_ip)
                intersting.append(this_ip)

        except:
            print '\033[0m'
            print "Down:{}".format(this_ip)
            pass
    return intersting


def write(ip,filename):
    file = open(filename,'w')
    for i,this_ip in enumerate(ip):
        file.writelines(['%d-----------%s\n' % (i+1,this_ip)])
    file.close()


def main(port,infile,outfile):
    subdomain_ip = open_file(infile)
    subdomain_ip = list(set(subdomain_ip))#去重ip/域名
    intersting = check_state(subdomain_ip,port)
    write(intersting,outfile)


if __name__ == '__main__':
    banner()
    args = parse_args()
    port = args.port
    infile = args.file
    outfile = args.outfile
    #threads = args.threads
    main(port,infile,outfile)
    
    
