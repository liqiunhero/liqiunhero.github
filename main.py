import cv2
import time
import numpy as np

video_path = "/Users/liqiuheng/Pictures/40.mp4"
save_path = "/Users/liqiuheng/Pictures/capturePhotos/40"

cap = cv2.VideoCapture(video_path)  # 读取视频文件，参数设置为0表示从摄像头获取图像

_, frame1 = cap.read()
img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)  # 将图片转为灰度图，第一个返回值表示是否转换成功，第二个返回值就是灰度图了
start = time.time()


def moving_detect(frame1, frame2, e):
    end = e
    img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    grey_diff = cv2.absdiff(img1, img2)  # 计算两幅图的像素差
    change = np.average(grey_diff)
    print("change:", change)

    if change > 0.001:  # 当两幅图的差异大于给定的值后，认为画面有物体在动
        cv2.putText(frame2, 'moving', (100, 30), 2, 1, (0, 255, 0), 2, cv2.LINE_AA)
        return change
    else:
        cv2.putText(frame2, 'quiet', (100, 30), 2, 1, (255, 0, 0), 2, cv2.LINE_AA)
        newPath = save_path + "/" + str(int(end)) + ".jpg"
        cv2.imencode('.jpg', frame1)[1].tofile(newPath)
        return change



    cv2.imshow("output", frame2)


change_new = 1
chane0 = 0
while True:

    f

    if change_new == change0:
        continue
    change_new = moving_detect(frame1, frame2, end)
    if cv2.waitKey(5) & 0xFF == ord('q'):  # 按下q停止运行程序
        break

# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()
