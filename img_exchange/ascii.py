from PIL import Image
import argparse

#命令行参数处理
parser = argparse.ArgumentParser()
#添加参数(都是关键字参数)
parser.add_argument("file")
parser.add_argument("-o", "--output")
parser.add_argument("--width", type=int, default=100)
parser.add_argument("--height", type=int, default=80)

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#要用到的字符
ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

if __name__ == "__main__":
    im = Image.open(IMG)
    #调整图像大小 第二个参数表示输出低质量图片
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.convert('RGBA').getpixel((j, i)))
        txt += '\n'
    
    if not OUTPUT:
        with open("output.txt", 'w') as f:
            f.write(txt)
    else:
        with open(OUTPUT, 'w') as f:
            f.write(txt)  

    