# -*-coding:utf-8 -*-
import os
#获取当前目录文件
list = os.listdir(os.getcwd())
#for a in list:
	#打开cmd,运行collada2gltf.exe shu1.dae语句
	os.system("collada2gltf.exe "+"shu1.dae")