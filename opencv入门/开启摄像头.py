# 导入opencv-python
import cv2
# 获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# 打开cap
cap.open(0)

# 循环
while cap.isOpened():
    # 获取画面
    flag, frame = cap.read()

    cv2.imshow('my_window', frame)

    # 获取键盘上按下哪个键
    key_pressed = cv2.waitKey(60)
    print('键盘上被按下的键是: ',key_pressed)
    # 如果按下esc键，退出
    if key_pressed ==27:
        break

# 关闭摄像头
cap.release()
# 关闭摄像窗口
cv2.destroyAllWindows()