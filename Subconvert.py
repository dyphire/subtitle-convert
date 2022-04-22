#! python3
# encoding: utf-8

import os
import sys
import time
import glob
import chardet

class Logger(object):
    logfile =""
    def __init__(self, filename=""):
        self.logfile = filename
        self.terminal = sys.stdout
        # self.log = open(filename, "a", encoding='utf-8')
        return
 
    def write(self, message):
        self.terminal.write(message)
        if self.logfile != "":
            try:
                self.log = open(self.logfile, "a", encoding='utf-8')
                self.log.write(message)
                self.log.close()
            except:
                pass
 
    def flush(self):
        pass

def read(path):
	sys.stdout = Logger("utf8_out.log")
	sys.stderr = Logger("utf8_err.log")
	
	for root_path,dir_name,file_name in os.walk(path):
		for file in file_name:
			ext = file.lower()
			# 设置要过滤的文件类型
			if(ext.endswith(".ass") or ext.endswith(".ssa") or ext.endswith(".srt")):
				ture_file = os.path.join(root_path,file)
				print(ture_file)
				with open(ture_file,'rb') as out_file:
					data = out_file.read()
					chr_res = chardet.detect(data)
					coding = chr_res.get('encoding')
					print(chr_res)
					try:
						# 忽略已经是 utf-8 或 UTF-8-SIG 编码的文件
						if chr_res['encoding'] != "utf-8" and chr_res['encoding'] != "UTF-8-SIG":
							if chr_res['encoding'] == "GB2312":
								data = data.decode("gbk")
							else:
								data = data.decode(chr_res['encoding'])
							with open(ture_file,'wb') as f:
								f.write(data.encode("utf-8"))
								print(" Done.")
						else:
							print(" Already "+"is " + coding + "!")
					except:
						print(" UnicodeDecodeError err%s"%ture_file)

def run():
    # 从控制台输入文件路径
    path = input("please input path: ")
    read(path)
run()
