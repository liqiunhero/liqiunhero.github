import FindFile
import cv2
import numpy as np
import time
import os

video_container = r'/Users/liqiuheng/Documents/downie/03.函数/04.函数的奇偶性'
cap = cv2.VideoCapture(video_container)  # 读取视频文件，参数设置为0表示从摄像头获取图像

_, frame1 = cap.read()
#img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)  # 将图片转为灰度图，第一个返回值表示是否转换成功，第二个返回值就是灰度图了
start = time.time()
time.sleep(2)


class Activity_Detect:
    video_path_list: list = []
    save_path_list: list = []
    each_video_path: str = ''
    each_save_path: str = ''
    capture = 0
    frame1: object
    frame2: object
    suc1: bool = False
    suc2: bool = False
    is_change: bool = False
    is_next: bool = False
    index: int = 0

    def __init__(self):
        global video_container
        filesys = FindFile.FileSystem(video_container)

        self.video_path_list = filesys.video_file_path_list
        self.save_path_list = filesys.save_container_path_list

        filesys.create_captue_container()
        print(self.video_path_list)

    def Judge_Change(self):
        global start
        global end
        global video_container
        length = len(self.video_path_list)
        while self.index < length:
            self.each_video_path = self.video_path_list[self.index]
            self.each_save_path = self.save_path_list[self.index]
            self.capture = cv2.VideoCapture(self.each_video_path)

            end = time.time()
            print("end - start,", end - start)
            if end - start > 1:  # 每隔2秒拍一幅图，比较前后两幅图的差异
                print("end - start,", end - start)
                start = time.time()
                self.suc1, self.frame1 = self.capture.read()
                print("suc1,", self.suc1)
            self.suc2, self.frame2 = self.capture.read()
            print("suc2,", self.suc2)

            while self.suc1 != 0 and self.suc2 != 0:
                cv2.imshow("output", self.frame2)

                img1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
                img2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2GRAY)
                grey_diff = cv2.absdiff(img1, img2)  # 计算两幅图的像素差
                self.is_change = np.average(grey_diff)
                print("is_change:", self.is_change)
                if self.is_change > 0.01:
                    newPath = self.each_save_path + "/" + str(int(end)) + ".jpg"
                    cv2.imencode('.jpg', self.frame1)[1].tofile(newPath)

                end = time.time()
                if end - start > 1:  # 每隔2秒拍一幅图，比较前后两幅图的差异
                    start = time.time()
                    self.suc1, self.frame1 = self.capture.read()

                self.suc2, self.frame2 = self.capture.read()


            else:
                self.index += 1
                print("index,", self.index)
                print("length,", length)
                if self.index == length:
                    print("已经全部截图结束！")
                    break
                else:
                    self.Judge_Change()
            break


def test():
    global video_container
    ad = Activity_Detect()
    print(ad.Judge_Change())


test()
