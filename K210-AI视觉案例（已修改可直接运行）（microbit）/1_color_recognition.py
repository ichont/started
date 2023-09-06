import sensor, image, time, lcd

from modules import ybserial
import time

serial = ybserial()

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 100)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

print("Hold the object you want to track in front of the camera in the box.")
print("MAKE SURE THE COLOR OF THE OBJECT YOU WANT TO TRACK IS FULLY ENCLOSED BY THE BOX!")

# Capture the color thresholds for whatever was in the center of the image.
# 50x50 center of QVGA.
r = [(320//2)-(50//2), (240//2)-(50//2), 50, 50]
for i in range(50):
    img = sensor.snapshot()
    img.draw_rectangle(r)
    lcd.display(img)

print("Learning thresholds...")
threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values.
for i in range(50):
    img = sensor.snapshot()
    hist = img.get_histogram(roi=r)
    lo = hist.get_percentile(0.01) # Get the CDF of the histogram at the 1% range (ADJUST AS NECESSARY)!
    hi = hist.get_percentile(0.99) # Get the CDF of the histogram at the 99% range (ADJUST AS NECESSARY)!
    # Average in percentile values.
    threshold[0] = (threshold[0] + lo.l_value()) // 2
    threshold[1] = (threshold[1] + hi.l_value()) // 2
    threshold[2] = (threshold[2] + lo.a_value()) // 2
    threshold[3] = (threshold[3] + hi.a_value()) // 2
    threshold[4] = (threshold[4] + lo.b_value()) // 2
    threshold[5] = (threshold[5] + hi.b_value()) // 2
    for blob in img.find_blobs([threshold], pixels_threshold=100, area_threshold=100, merge=True, margin=10):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        img.draw_rectangle(r, color=(0,255,0))
    lcd.display(img)

print("Thresholds learned...")
print("Start Color Recognition...")
while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([threshold], pixels_threshold=100, area_threshold=100, merge=True, margin=10):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        x = str(blob.x())
        y = str(blob.y())
        w = str(blob.w())
        h = str(blob.h())
        #print(threshold)
    if len(x)<3 :
       i_flag = 3-len(x)
       x = "0"*i_flag + x
    if len(y)<3 :
       i_flag = 3-len(y)
       y = "0"*i_flag + y
    if len(w)<3 :
       i_flag = 3-len(w)
       w = "0"*i_flag + w
    if len(h)<3 :
       i_flag = 3-len(h)
       h = "0"*i_flag + h

    send_data ="$"+"01"+ x+','+ y+','+ w+','+ h+','+"#"
    serial.send(send_data)
    #print(send_data)
    #for i in range(1,5):
        #serial.send(send_data)

    time.sleep_ms(5)
    lcd.display(img)
    #print(clock.fps())
