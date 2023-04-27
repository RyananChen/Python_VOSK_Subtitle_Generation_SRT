#!/usr/bin/env python3

import subprocess
import sys
import os

from vosk import Model, KaldiRecognizer, SetLogLevel
SAMPLE_RATE = 16000
SetLogLevel(-1)

# 如果你要自己填写绝对路径，注意python用的是反斜杠
# model = Model(lang="en-us")
# model = Model("./model")
# 我试过了转码，或者别的什么，短时间没找到解决这一行中文error的办法，其他地方都可以中文
# ############模型必须放在没有中文的路径下#########
# 获取当前脚本所在路径
script_dir = os.path.dirname(os.path.realpath(__file__))
# 通过拼接，得出模型文件的绝对路径,此处默认.py脚本和模型文件在同一个文件夹下。
# 如果要更改英文模型，写为model_path = os.path.join(script_dir, "model")
model_path = os.path.join(script_dir, "model_cn")
# 把model的路径作为参数填入Model，创建模型对象
model = Model(model_path)


rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

result = []

with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                            sys.argv[1],
                            "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                            stdout=subprocess.PIPE).stdout as stream:

    # print(rec.SrtResult(stream))
    result.append(rec.SrtResult(stream).strip())

print(result)
output = open(sys.argv[1]+'.srt','w')
output.write("\n".join(result))
output.close()
#写入文件