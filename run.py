import os
import requests
import time
download_urls=[]
current_dir=os.path.dirname(__file__)
def visual_studio_code():
    print("下载开始")
    res=requests.get("https://vscode.cdn.azure.cn/stable/d5e9aa0227e057a60c82568bf31c04730dc15dcd/VSCodeUserSetup-x64-1.47.0.exe")
    with open(os.path.join(current_dir,"VSCodeUserSetup-x64-1.47.0.exe"),"wb")as f:
        f.write(res.content)
    pass
def notepad_add():
    requests.get("")
    pass
def git():
    requests.get()
    pass
def torisorgit():
    requests.get()
    pass
#帮助doc
def help():
    print("欢迎来到帮助页面 首先你可以修改json文件来修改下载链接, 你也可以添加自己的新的开发工具的下载地址 \n 注意必须是直链 不然不行")
    pass
def main():
    print("请输入选项")
    print("输入1一键下载安装vs_code,notepad++,git,torisorgit")
    print("输入help来获得帮助")
    print("你可以手动编写json文件来修改下载地址")
    print("输入0退出")
    print()
    usr_in=input()
    if usr_in=="1":
        visual_studio_code()
    if usr_in=="0":
        print("退出！0")
        pass
    if usr_in=="help":
        help()
        pass
    pass

main()