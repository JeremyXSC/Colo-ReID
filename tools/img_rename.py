# 可视化时需要对应图片序号，因此给gallery和test都加了序号
# import cv2
import os


def walkFile(file):
    i = 1
    for files in sorted(os.listdir(file)):
        print(files, i)
        id = str(format(int(i), "04"))
        os.rename(file + files, file + id + '_' + files)
        i += 1


if __name__ == '__main__':
    walkFile('/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r1/fold3/dukemtmc/DukeMTMC-reID/query_index/')
