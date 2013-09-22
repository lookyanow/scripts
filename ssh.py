#!/usr/bin/python

import paramiko 
import sys


host = 'cyberdynesystems.no-ip.org'
user = 'ivan'
passwd = '120387'
port = 22

def ssh_con(host,user,passwd,port,com):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host, username=user, password=passwd, port=port)
	stdin, stdout, stderr = client.exec_command(com)
	data = stdout.read() + stderr.read()
	print data
	client.close()
ssh_con('cyberdynesystems.no-ip.org','ivan','120387',22,'ls -l')
	

