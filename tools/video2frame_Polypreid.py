import cv2
import glob
import os
from datetime import datetime


def video_to_frames(video_path, files):
    path = video_path + files
    videoCapture = cv2.VideoCapture()
    videoCapture.open(path)
    # 帧率
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    # 总帧数
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))

    files_name = files.split('.')[0]
    for i in range(int(frames)):
        ret, frame = videoCapture.read()
        frame_cut = frame[:, :, :] # 将这部分代码移植到息肉检测中时，需要把矩形框坐标放在这里

        # fold 0: 前21位病例划为train
        # frame_path = '/home/chenqingzhong/data/chenqingzhong/Data/zhongshan_endoscope/Polyp-reID/bounding_box_train/' + files_name + '_f' + str(format(i, "07")) + '.jpg'

        # 将后6位病例的帧按7: 1划分测试病例为test和query。
        if i % 8 == 0:
            frame_path = '/home/chenqingzhong/data/chenqingzhong/Data/zhongshan_endoscope/Polyp-reID/query/' + files_name + '_f' + str(format(i, "07")) + '.jpg'
        else:
            frame_path = '/home/chenqingzhong/data/chenqingzhong/Data/zhongshan_endoscope/Polyp-reID/bounding_box_test/' + files_name + '_f' + str(format(i, "07")) + '.jpg'
        cv2.imwrite(frame_path, frame_cut)
        # fold 0: 前21位病例划为train，将后6位病例的帧按7:1划分测试病例为test和query。
    return


if __name__ == '__main__':
    video_path = '/home/chenqingzhong/data/chenqingzhong/Data/zhongshan_endoscope/Polyp-reID/video/'
    for files in sorted(os.listdir(video_path)):
        video_to_frames(video_path, files)