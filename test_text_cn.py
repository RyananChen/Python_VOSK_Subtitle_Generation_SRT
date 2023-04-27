#!/usr/bin/env python3

import sys
import json
import os

from vosk import Model, KaldiRecognizer

script_dir = os.path.dirname(os.path.realpath(__file__))
# 如果要更改模型，写为model_path = os.path.join(script_dir, "model")
model_path = os.path.join(script_dir, "model_cn")
# 把model的路径作为参数填入Model，创建模型对象
model = Model(model_path)

# Large vocabulary free form recognition
rec = KaldiRecognizer(model, 16000)

# You can also specify the possible word list
#rec = KaldiRecognizer(model, 16000, "zero oh one two three four five six seven eight nine")
result= []
with open(sys.argv[1], "rb") as wf:
    wf.read(44) # skip header

    while True:
        data = wf.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print(res["text"])
            result.append((res["text"]))

    res = json.loads(rec.FinalResult())
    print(res["text"])   
    result.append((res["text"]))


result = '\n'.join(result)
output = open(sys.argv[1]+'.txt','w')
output.write(result )
output.close()
#写入文件
