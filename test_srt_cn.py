import subprocess
import sys
import os


from pathlib import Path
from vosk import Model, KaldiRecognizer, SetLogLevel
SAMPLE_RATE = 16000
SetLogLevel(-1)
# 如果你要自己填写绝对路径，注意python用的是反斜杠
# model = Model(lang="en-us")
# model = Model("./model")
# 我试过了转码，或者别的什么，短时间没找到解决路径中文error的办法，其他地方都可以中文
# ############模型必须放在没有中文的路径下#########
# 获取当前脚本所在路径
script_dir = os.path.dirname(os.path.realpath(__file__))
# 通过拼接，得出模型文件的绝对路径,此处默认.py脚本和模型文件在同一个文件夹下。
# 如果要更改英文模型，写为model_path = os.path.join(script_dir, "model")
model_path = os.path.join(script_dir, "model_cn") 
# model_path = model_path.replace('\\', '/') #python自带的路径转移函数,不需要用,model里面带了转义.用了也解决不了中文的问题
# 联网下载用的参数，想改自己改，链接在https://alphacephei.com/vosk/models/model-list.json，从这里得知的D:\dailyexe\1python3.11\Lib\site-packages\vosk__init__.py
model_name1 = "vosk--cn-0.1-lgraph"
lang1 = "cn"


# 执行model = Model(model_name=model_name1, lang=lang1) ，逻辑是
# 先在本地路径上找，没找到就下载，所以我这边先判断本地这几个路径有没有文件，
# 没有的话就先执行我们配置的路径，有的话说明路径配置失败了，下载过一次了，那就用下载的
# 定义默认模型model下载文件夹的路径
dirs = [Path("/usr/share/vosk"), Path.home() / "AppData/Local/vosk", Path.home() / ".cache/vosk"]

# 遍历文件夹路径列表，检查每个文件夹是否存在文件
files_exist = any(dir.exists() and any(dir.glob("*")) for dir in dirs)
dirs_with_files = [str(dir) for dir in dirs if dir.exists() and any(dir.glob("*"))]
dirs_with_files_str = "\n".join(dirs_with_files)


# 根据检查结果执行不同语句，如果有下载的，就用下载的，如果没有下载的，就用我们自己配置的model_cn
if files_exist:
    # 执行语句1
    print("##############################################################") 
    print("##############################################################") 
    print("请注意，此时你在用联网下载的模型: " + model_name1 + "\n文件路径在在" + dirs_with_files_str) 
    print("如果你想运行自己下载的模型，请做到以下两点") 
    print("1. 清空这几个文件夹的所有模型：/usr/share/vosk，  AppData/Local/vosk，   .cache/vosk \n"+ "    1.1    " + dirs_with_files_str) 
    print("2. 确保你的模型文件路径没有中文和特殊符号，并和.py脚本在同一路径，命名为model_cn") 
    print("##############################################################") 
    print("##############################################################") 
    try: 
        model = Model(lang=lang1) 
    except Exception as e: 
        print("##############################################################") 
        print("##############################################################") 
        print("执行出错了，这是异常信息：", e) 
        print("##############################################################") 
        print("##############################################################") 
else:
    try: 
        print("【你在用自己配置正确路径的model】") 
        # 把model的路径作为参数填入Model，创建模型对象
        model = Model(model_path) 
    except Exception as e: 
        print("##############################################################") 
        print("##############################################################") 
        print("执行出错了，这是异常信息：", e) 
        print("【路径可能有问题】，\n请确认路径中【没有中文】，或者【特殊符号】，\n比如感叹号!或者&等等，\n你可以选择【继续执行】，将会【联网下载一个最小的model】，\n【效果不会太好】\n或者【手动】把路径调整到中文和特殊符号的位置，【再次运行】") 
        print("##############################################################") 
        print("##############################################################") 
        print("【推荐【手动】改好路径，只要没有中文和特殊符号就不会有问题】") 
        choice = input("是否继续执行，联网下载model？（Y/N）") 
        if choice.lower() == 'y': 
                model = Model(lang=lang1) 
                # model = Model(model_name=model_name1, lang=lang1) 
        else: 
            raise







rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

result = []

# 把视频文件的完整路径和文件名赋值给input_path，
input_path = sys.argv[1]
# 用os.path.basename()方法获取文件名部分，用os.path.splitext()方法分离出文件名和扩展名。用os.path.dirname()方法获取输入视频文件的路径
# 最后用os.path.join()方法拼接新的字幕文件路径。这样就能正确地生成字幕文件名,并且避免路径包含特殊符号&就报错的情况。
output_path = os.path.join(os.path.dirname(input_path), os.path.splitext(os.path.basename(input_path))[0]) + '.srt'

# 转换生成字幕的主要部分，可以封装成函数，写在另一个py文件了。
with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i", input_path,
                        "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                        stdout=subprocess.PIPE).stdout as stream:
     # print(rec.SrtResult(stream))
    result.append(rec.SrtResult(stream).strip())

# 生成完毕了，输出
print("\n##############################################################################")  
print(result)
print("\n##############################################################################")   
print("这是" + output_path + "生成字幕文件的内容")   
print("########################################") 
output = open(output_path,'w')
output.write("\n".join(result))
output.close()
#写入文件