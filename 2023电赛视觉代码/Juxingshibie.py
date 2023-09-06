import sensor
import image
import time
import lcd
#from machine import UART
#from board import board_info
#from fpioa_manager import fm
from modules import ybserial



# 初始化摄像头
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.run(1)
sensor.skip_frames()
sensor.skip_frames(time = 2000)     #跳过不稳定画面
# 初始化串口
serial = ybserial()


clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
# 自定义函数：识别矩形
# 在图像中寻找矩形
    for r in img.find_rects(threshold = 10000):
        # 判断矩形边长是否符合要求
        if r.w() > 20 and r.h() > 20:
            # 在屏幕上框出矩形
            img.draw_rectangle(r.rect(), color = (255, 0, 0), scale = 4)
            # 获取矩形角点位置
            corner = r.corners()
            # 在屏幕上圈出矩形角点
            img.draw_circle(corner[0][0], corner[0][1], 5, color = (0, 0, 255), thickness = 2, fill = False)
            img.draw_circle(corner[1][0], corner[1][1], 5, color = (0, 0, 255), thickness = 2, fill = False)
            img.draw_circle(corner[2][0], corner[2][1], 5, color = (0, 0, 255), thickness = 2, fill = False)
            img.draw_circle(corner[3][0], corner[3][1], 5, color = (0, 0, 255), thickness = 2, fill = False)

        # 打印四个角点坐标, 角点1的数组是corner[0], 坐标就是(corner[0][0],corner[0][1])
        # 角点检测输出的角点排序每次不一定一致，矩形左上的角点有可能是corner0,1,2,3其中一个
            corner1_str = corner[0][0],corner[0][1]
            corner2_str = corner[1][0],corner[1][1]
            corner3_str = corner[2][0],corner[2][1]
            corner4_str = corner[3][0],corner[3][1]

            corner1_str = "({}, {})".format(corner[0][0], corner[0][1])
            corner2_str = "({}, {})".format(corner[1][0], corner[1][1])
            corner3_str = "({}, {})".format(corner[2][0], corner[2][1])
            corner4_str = "({}, {})".format(corner[3][0], corner[3][1])

            output_str = corner1_str + ", " + corner2_str + ", " + corner3_str + ", " + corner4_str+ "\n"


            #lcd.draw_string(0, 0, corner1_str, lcd.WHITE, lcd.BLACK)
            #lcd.draw_string(0, 20, corner2_str, lcd.WHITE, lcd.BLACK)
            #lcd.draw_string(0, 40, corner3_str, lcd.WHITE, lcd.BLACK)
            #lcd.draw_string(0, 60, corner4_str, lcd.WHITE, lcd.BLACK)
            #while True:
                #time.sleep_ms(1000)
            num = serial.send(output_str)

                #print("num:%d, count:%d" % (num, count))

    lcd.display(img)




