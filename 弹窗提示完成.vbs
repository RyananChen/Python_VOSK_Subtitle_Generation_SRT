Dim message, title, response, filesDeleted
message = "【字幕生成完毕，是否删除多余的脚本文件】" & vbCrLf & _
          "【请确保您已备份好】" & vbCrLf & _
          "【不想删除请点”否“。】"
title = "提示"
response = MsgBox(message, vbYesNo, title)
filesDeleted = ""

'创建最后用来打开vbs所在的路径的对象(也就是视频路径)
Set objShell = CreateObject("Shell.Application")

'如果点击了"是",那么就开始删除.
If response = vbYes Then
    Dim fso, folderPath, scriptPath, fileName
    folderPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
    Set fso = CreateObject("Scripting.FileSystemObject")

    ' 删除其他文件和文件夹
    On Error Resume Next
    fso.DeleteFolder folderPath & "\model_cn", True
    fileName = folderPath & "\model_cn"
    If Err.Number = 0 Then
        filesDeleted = "已删除文件夹：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


    fso.DeleteFolder folderPath & "\model", True
    fileName = folderPath & "\model"
    If Err.Number = 0 Then
        filesDeleted = "已删除文件夹：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

     fso.DeleteFolder folderPath & "\__MACOSX", True
    fileName = folderPath & "\__MACOSX"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件夹：" & fileName & vbNewLine
    Else
        Err.Clear
    End If



     fso.DeleteFile folderPath & "\【复制我】到【中文视频文件夹】双击打开.bat"
    fileName = folderPath & "\【复制我】到【中文视频文件夹】双击打开.bat"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

    
     fso.DeleteFile folderPath & "\【复制我】到【英文视频文件夹】双击打开.bat"
    fileName = folderPath & "\【复制我】到【英文视频文件夹】双击打开.bat"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

     fso.DeleteFile folderPath & "\方法2Ryan.py"
    fileName = folderPath & "\方法2Ryan.py"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\方法2运行这个[有问题].bat"
    fileName = folderPath & "\方法2运行这个[有问题].bat"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\test_srt.py"
    fileName = folderPath & "\test_srt.py"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\test_srt_cn.py"
    fileName = folderPath & "\test_srt_cn.py"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\test_text.py"
    fileName = folderPath & "\test_text.py"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\test_text_cn.py"
    fileName = folderPath & "\test_text_cn.py"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

     fso.DeleteFile folderPath & "\file_names.txt"
    fileName = folderPath & "\file_names.txt"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If


     fso.DeleteFile folderPath & "\视频目录.txt"
    fileName = folderPath & "\视频目录.txt"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

     fso.DeleteFile folderPath & "\拷贝模型到目标文件夹.vbs"
    fileName = folderPath & "\拷贝模型到目标文件夹.vbs"
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If

     ' 删除自身
    scriptPath = WScript.ScriptFullName
    fso.DeleteFile scriptPath
    fileName = scriptPath
    If Err.Number = 0 Then
        filesDeleted = filesDeleted & "已删除文件：" & fileName & vbNewLine
    Else
        Err.Clear
    End If
End If

'开头创建的对象,现在打开vbs所在的文件路径，用来展示生成的字幕文件
objShell.Explore Replace(WScript.ScriptFullName, WScript.ScriptName, "")
'完成弹窗.显示删除了哪些文件
MsgBox "完成" & vbNewLine & filesDeleted, vbOKOnly, "提示"
