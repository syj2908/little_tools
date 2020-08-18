import os
import re

#删除文件夹中相同的图片
file_path = r'E:\Desktop\游戏截图\PS4\SHARE\Screenshots\FINAL FANTASY VII REMAKE'
#这条路径依据存放图片的文件夹位置而定
def delete_same_images(path):
    filenames = os.listdir(path)
    count = 0
    for filename in filenames:
        if re.match(r'.*_.*_.*.jpg', filename):
            #匹配到重复的图片
            os.remove(os.path.join(file_path,filename))
            print('Delete same image : ' + filename + '\n')
            count += 1
    if count != 0:
        print(str(count) + r'image(s) have been deleted.')
    else:
        print('No same image !')


if __name__ == '__main__':
    delete_same_images(file_path)