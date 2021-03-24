# 滤镜生成工具
#### 给运营用的
### 用PyQt写的一个小工具,运营可以选择图片,给图片添加一些滤镜效果,<br>工具的作用就是进行一些JSON处理和文件处理,<br>因为滤镜本身也只是一个压缩包,符合协议即可
#### 关于PyQt的学习,可以参考这个
`https://mp.weixin.qq.com/s/Wy1iTYoX7_O81ChMflXXfg`

###关键是Pyinstaller,用这玩意打包巨坑
`pip install pipenv`  
一定要用3.7.6以下的python版本,请不要头铁  
`pipenv install --python 3.7`  
`pipenv shell`  
`pipenv install `  
Pyinstaller也请不要用高版本的  
`pip3 install Pyinstaller==3.4`  
PyQt5也请不要用高版本的,就是这么操蛋  
`pip3 install PyQt5==5.9.2`  
请一定要加上 -p ../../ 让spec文件里的pathex有这个路径,否则找不到根目录文件夹,巨特么坑  
如果要加-i设置图标,要和-w一起,但是亲测不好使,最好也别头铁了  
pyinstaller  -n 'filterMaker' -p ../../ -F ./mainUI.py  
  
关于windows  
如果遇到了TypeError: expected str, bytes or os.PathLike object, not NoneType  
将  
```
 pydll = 'python%d%d.dll' % sys.version_info[:2]
        if pydll in PYDYLIB_NAMES:
            filename = getfullnameof(pydll)
            return filename
```
            
添加到
venv/Lib/site-packages/PyInstaller/depend/bindepend.py
的函数  
get_python_library_path里  
在if is_unix:的上面  
参考`https://www.jianshu.com/p/71b1c4aaf06d`  
然后执行  
`pyinstaller -n filterMaker -p ../../ -F -w -i ../../res/images/main.ico ./mainUI.py`  
这张图由于有点大,在小图标的情况下不显示,这个问题就先不解决了  
  
喜大普奔,windows尝试新版本的PyInstaller和Pyqt5,没报错,也不需要修改venv的文件  
垃圾MAC
pyinstaller 4.2  
PyQt5 5.15.4
Python仍然是3.7.6,下次用新版本Python再试一下
