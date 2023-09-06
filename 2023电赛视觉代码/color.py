import sensor, image, time,math,pyb
from pyb import UART,LED
import json
import ustruct

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_windowing((240, 240))
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
red_threshold_01=(10, 100, 127, 32, -43, 67)
#red_threshold_01=(86, 64, -128, -17, -128, 127)
clock = time.clock()

uart = UART(3,115200)   #定义串口3变量
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

def find_max(blobs):    #定义寻找色块面积最大的函数
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
            return max_blob


def sending_data(cx,cy,cw,ch):
    global uart;
    data = ustruct.pack("<bbhhhhb",      #格式为俩个字符俩个短整型(2字节)
                   0x2C,                      #帧头1
                   int(cx), # up sample by 4   #数据1
                   int(cy), # up sample by 4    #数据2
                   0x5B)
    uart.write(data);   #必须要传入一个字节数组


while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([red_threshold_01])
    max_b = find_max(blobs)
    cx=0;cy=0;
    img.draw_cross(120, 120, size = 5, color = (255, 255, 255))
    if blobs:
            #如果找到了目标颜色
            cx=max_b[5]
            cy=max_b[6]
            img.draw_rectangle(max_b[0:4]) # rect
            img.draw_cross(max_b[5], max_b[6]) # cx, cy
            FH = bytearray([0x2C,cx,cy,0x5B])
            uart.write(FH)
            print(cx,cy)
