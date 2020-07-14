import os
import requests
import time
download_urls=[]
current_dir=os.path.dirname(__file__)
def visual_studio_code():
    print("visual_code下载开始")
    res=requests.get("https://vscode.cdn.azure.cn/stable/d5e9aa0227e057a60c82568bf31c04730dc15dcd/VSCodeUserSetup-x64-1.47.0.exe")
    with open(os.path.join(current_dir,"VSCodeUserSetup-x64-1.47.0.exe"),"wb")as f:
        f.write(res.content)
    pass
def notepad_add():
    print("notepad++下载开始")
    res=requests.get("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.8/npp.7.8.8.Installer.exe")
    with open(os.path.join(current_dir,"npp.7.8.8.Installer.exe"),"wb")as f:
        f.write(res.content)
    pass
def git():
    print("git下载开始")
    res=requests.get("https://npm.taobao.org/mirrors/git-for-windows/v2.27.0.windows.1/Git-2.27.0-32-bit.exe")
    with open(os.path.join(current_dir,"Git-2.27.0-32-bit.exe"),"wb")as f:
        f.write(res.content)
def torisorgit():
    print("torisorgit下载开始")
    res=requests.get("https://download.tortoisegit.org/tgit/2.10.0.0/TortoiseGit-2.10.0.2-32bit.msi")
    with open(os.path.join(current_dir,"TortoiseGit-2.10.0.2-32bit.msi"),"wb")as f:
        f.write(res.content)
    pass
#帮助doc
def help():
    print("欢迎来到帮助页面 首先你可以修改json文件来修改下载链接, 你也可以添加自己的新的开发工具的下载地址 \n 注意必须是直链 不然不行")
    pass
#读取json配置文件
def read_config():

    pass
#主方法
def main():
    print("请输入选项")
    print("输入1一键下载安装vs_code,notepad++,git,torisorgit")
    print("输入help来获得帮助")
    print("你可以手动编写json文件来修改下载地址")
    print("输入0退出")
    usr_in=input()
    if usr_in=="1":
        print("即将开始下载")
        visual_studio_code()
        notepad_add()
        git()
        torisorgit()
    if usr_in=="0":
        print("退出！0")
        pass
    if usr_in=="help":
        help()
        pass
    pass

main()