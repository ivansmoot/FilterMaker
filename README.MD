# 滤镜生成工具
#### 给运营用的
### 用PyQt写的一个小工具,运营可以选择图片,给图片添加一些滤镜效果,<br>工具的作用就是进行一些JSON处理和文件处理,<br>因为滤镜本身也只是一个压缩包,符合协议即可
#### 关于PyQt的学习,可以参考这个
`https://mp.weixin.qq.com/s/Wy1iTYoX7_O81ChMflXXfg`

###关键是Pyinstaller,用这玩意打包巨坑
`pip install pipenv`
<br>
一定要用3.7.6以下的python版本,请不要头铁
<br>
`pipenv install --python 3.7`<br>
`pipenv shell`<br>
`pipenv install `
<br>
Pyinstaller也请不要用高版本的
<br>
`pip3 install Pyinstaller==3.4`
<br>
PyQt5也请不要用高版本的,就是这么操蛋
<br>
`pip3 install PyQt5==5.9.2`
<br>
请一定要加上 -p ../../ 让spec文件里的pathex有这个路径,否则找不到根目录文件夹,巨特么坑
<br>
如果要加-i设置图标,要和-w一起,但是亲测不好使,最好也别头铁了
<br>
pyinstaller  -n 'filterMaker' -p ../../ -F ./mainUI.py
