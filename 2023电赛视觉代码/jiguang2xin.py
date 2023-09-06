import sensor,image,lcd,time
from machine import UART
from board import board_info
from fpioa_manager import fm
#from modules import ybserial

#fm.register(15, fm.fpioa.UART1_RX, force=True)
#fm.register(17, fm.fpioa.UART1_TX, force=True)

fm.register(6,fm.fpioa.UART2_TX)
fm.register(8,fm.fpioa.UART2_RX)


#serial = ybserial()
yb_uart = UART(UART.UART2, 115200, 8, 0, 1, timeout=1000, read_buf_len=4096)
#常用初始化
lcd.init()

sensor.reset()                      #复位摄像头

sensor.set_pixformat(sensor.RGB565) #设置像素格式 RGB565
sensor.set_framesize(sensor.QVGA)   #设置帧尺寸 QVGA (320x240)
sensor.skip_frames(time = 2000)     #跳过不稳定画面

sensor.run(1)
#阈值
red_threshold   = (56, 100, 45, 127, -128, 127)



#寻色函数定义
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob

while True:
    img=sensor.snapshot()
    blobs = img.find_blobs([red_threshold],merge=True)#把拍摄的一张图片里满足的色块纳入集合中

    if blobs:
            max_blob = find_max(blobs)#调用函数，返回最大色块
            img.draw_circle(80,60,5,color=200)
            img.draw_circle(max_blob.cx(),max_blob.cy(),10,color=200)
            img.draw_rectangle((max_blob.x(),max_blob.y(),max_blob.w(),max_blob.h()),color=(255,0,0))#用红色框出最大色块
            img.draw_string(0,0, "(x,y) =")
            img.draw_string(max_blob.x()+40,max_blob.y(), str(max_blob.cx()))
            img.draw_string(max_blob.x()+60,max_blob.y(), str(max_blob.cy()))#在框图显示色块的中心坐标
            img.draw_string(40,0, str(max_blob.cx()))
            img.draw_string(60,0, str(max_blob.cy()))#在框图左上角显示色块的中心坐标

            print(max_blob.cx(),end=',')
            print(max_blob.cx(),end='\n')
            coordinate_str = "({}, {})".format(str(max_blob.cx()), str(max_blob.cy()))
            print(coordinate_str)
    lcd.display(img)
