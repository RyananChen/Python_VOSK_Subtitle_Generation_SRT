CHCP 65001
@echo off
setlocal enabledelayedexpansion

rem 只有这个需要设置，这是test_srt_cn.py的路径。填进去即可。
set "model_py_dir=D:\dailyexe\1python_VOSK_Github"

rem 如果要用英文字幕生成，把下一行的【test_srt_cn.py】改为【test_srt.py】
set "py_script=%model_py_dir%\test_srt.py"

set "input_dir=%~dp0"
set "file_names=%input_dir%\视频目录.txt"
set source="%model_py_dir%\弹窗提示完成.vbs"
set destination="%~dp0弹窗提示完成.vbs"
rem 把弹窗提示完成.vbs复制过来，用来删除脚本运行后的bat和txt文件。并起到提醒完成的作用
rem
echo 正在从 "%source%" 复制到 "%destination%"...
copy %source% %destination%
echo 弹窗提示脚本，已拷贝到工作目录下

rem 这一段注释掉，这一段是用来仅仅转换和bat同一个目录下视频用的。
rem 下一段是转换和bat同一个目录下以及所有子目录下的视频用的。
goto start
rem 将同一个目录下的所有mp4文件批量添加进同一目录下的file_names.txt
(for %%f in ("%input_dir%\*.mp4") do echo %%~nxf) > "%file_names%"
rem 开始一个一个转换.
for /f "tokens=*" %%f in (%file_names%) do (
    echo 请不要关闭此窗口,正在转换 %%f ...
    python "%py_script%" "%%~nxf"
)
:start

rem 添加所有同目录以及子目录的，mp4文件的绝对路径，到TXT文件中
pushd "%input_dir%"
(for /r %%f in (*.mp4) do echo %%~dpnxf) > "%file_names%"
popd

rem 开始一个一个转换.
for /f "tokens=*" %%f in (%file_names%) do (
    echo 请不要关闭此窗口,正在转换 %%f ...
    python "%py_script%" "%%~dpnxf"
)

echo Done.

cscript /nologo 弹窗提示完成.vbs
del /f /q 视频目录.txt
pause
