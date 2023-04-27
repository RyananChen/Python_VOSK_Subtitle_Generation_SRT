# **一键批量**生成**多个视频**的**中英文字幕**
* * *
## **用处**
> 基于python的vosk语言模型，进行**一键批量**的生成**多个视频**的**字幕**，中英文都可以。中文识别率不高。  
**做来倍速播放视频用的** 
> >GitHub项目链接：
> >[GitHub链接](https://github.com/RyananChen/Python_VOSK_Subtitle_Generation_SRT)  
> >有帮助的话可以给个**star**
> >所有文件打包**下载链接**  
> > 国内:  
> > GitHub:  
* * *
## **使用说明**
---------

### **来源**  
> vosk项目地址  
> https://alphacephei.com/vosk/models    

> **参考**  **感谢**  
> 有什么软件可以自动生成视频字幕？ - CycleUser的回答 - 知乎
> https://www.zhihu.com/question/397207300/answer/2806069443
> 
下面部分摘抄**CycleUser**的文章  
首先安装好**python**，不做详细说了。   
最新的3.11.3版本python [官网下载链接](https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe  )  
 
然后从终端上安装两个需要的包  

对于 macOS 用户来说，使用 brew 和 pip3:
> brew install ffmpeg  
> pip3 install vosk   

对于 Windows 用户来说，使用 winget 和 pip3:
> winget install ffmpeg  
> pip3 install vosk
  

* * *
### **环境安装好后，配置文件**  
---------
首先，把压缩包解压，把解压出来的文件夹放在**没有中文**的路径中，如果不清楚就放在**d盘c盘根目录**。    

* * *
**修改**文件夹中的.bat文件  
- 【复制我】到【中文视频文件夹】双击打开.bat 
- 【复制我】到【英文视频文件夹】双击打开.bat  
**右键编辑**，打开他们，把第六行的路径**改为你解压缩的路径**，
``` dos
set "model_py_dir=D:\dailyexe\1python_VOSK"
rem 把D:\dailyexe\1python_VOSK   改为你解压缩的路径，也就是test_srt_cn.py的路径
rem 比如model的路径在D:\1python_VOSK\model，
rem 此时test_srt_cn.py的路径在D:\1python_VOSK，那么路径应该写为
set "model_py_dir=D:\1python_VOSK"
```

根据自己的中文还是英文的需求，**复制**文件夹中的.bat文件  
- 【复制我】到【中文视频文件夹】双击打开.bat 
- 【复制我】到【英文视频文件夹】双击打开.bat  

>将这两个文件的其中之一，**复制**到你**需要批量生成字幕的mp4文件**旁边，要在**同一个目录**下。  
>比如你的中文视频**路径**在**C:\Users\Public\Videos\视频.mp4**  
>把【复制我】到【中文视频文件夹】双击打开.bat 拷贝到**C:\Users\Public\Videos**  
>然后**双击**.bat文件运行它，它就会开始跑了。
* * *
> # 一定要复制出来用，不然可能不小心把自己model给删了
* * *
### **运行结束**
---------
运行结束后会弹窗，*弹窗提示是否删除文件*，因为我们是**复制出来运行**的，所以推荐是**点删除**。这样文件不会太乱。  
虽然可以静默删除，不过这个弹窗的本意是**提示转换完成**。


* * *
## 杂七杂八的使用说明
---------
注意点：
- 第一步安装python，注意环境变量
- winget install ffmpeg  
  - 此处报错了，解决办法是去Microsoft store里面更新“应用安装程序”
- 右键cmd的标题栏，属性（默认值），关闭**快速编辑模式**
  - 对cmd卡住的情况有帮助。有时候会卡住，按以下键盘就好了。
  - 也可以在cmd里面这样
``` dos
 @echo off
 reg add HKEY_CURRENT_USER\Console /v QuickEdit /t REG_DWORD /d 00000000 /f
```
- 懒得写了 就这样吧
