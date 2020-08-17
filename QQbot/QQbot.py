import win32gui
import win32con
import win32clipboard as w
import time
import datetime

def set_name(name):
    #确定窗口名称
    namelist = [name]
    #同时开启多个会话时也可以识别
    for i in range(1,10):
        namelist.append(name + '等' + str(i) + '个会话')
    return namelist

def send_msg(msg,namelist,gap=5):
    #将msg中的内容发送到粘贴板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()

    for item in namelist:
        #试图定位聊天窗口
        handle = win32gui.FindWindow(None, item)
        if handle:
            #找到窗口 发送信息
            win32gui.SendMessage(handle, 770, 0, 0)
            win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            time.sleep(gap)
        else:
            continue

def creat_quad():
    char_list=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
    for i in char_list:
        

def main():
    name='学习资料分享中心'
    namelist = set_name(name)
    for i in range(1,16):
            
        msg = ('你不是组长？')
        send_msg(msg, namelist,15)

if __name__ == '__main__':
    main()
