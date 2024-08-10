import random
import os
import shutil
from glob import glob

# 二选一A：固定单一seed
# seed = 7 #每次只需要修改seed！
# 二选一B：使用固定范围内的seed
for seed in range(5, 6):
    random.seed(seed)

    patient_list = [1, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    random.shuffle(patient_list)
    print(patient_list)
    fold_0_list = patient_list[0:7]
    fold_1_list = patient_list[7:14]
    fold_2_list = patient_list[14:21]
    fold_3_list = patient_list[21:27]
    print(fold_0_list)
    print(fold_1_list)
    print(fold_2_list)
    print(fold_3_list)

    # r52
    # patient_list = [9, 6, 15, 17, 14, 18, 31, 29, 23, 30, 5, 7, 22, 20, 26, 8, 24, 10, 19, 12, 21, 25, 27, 16, 28, 1, 4]
    # r53
    # patient_list = [9, 15, 7, 17, 14, 18, 31, 29, 23, 30, 5, 6, 22, 20, 26, 12, 4, 10, 19, 1, 21, 25, 27, 16, 28, 8, 24]

    img_path = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/all/'

    def mycopyfile(srcfile, dstpath):  # 复制函数
        if not os.path.isfile(srcfile):
            print("%s not exist!" % (srcfile))
        else:
            fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)  # 创建路径
            shutil.copy(srcfile, dstpath + fname)  # 复制文件
            print("copy %s -> %s" % (srcfile, dstpath + fname))

    src_dir = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/all/'
    dst_dir = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r{}/'.format(seed)  # 目的路径记得加斜杠

    for i in range(27):
        if i <= 6:
            patient_num = patient_list[i]
            src_file_list = glob(src_dir + '%04d_*' % patient_num)
            for srcfile in src_file_list:
                mycopyfile(srcfile, dst_dir + 'fold0/dukemtmc/DukeMTMC-reID/bounding_box_test/')
                mycopyfile(srcfile, dst_dir + 'fold1/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold2/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold3/dukemtmc/DukeMTMC-reID/bounding_box_train/')
        elif i <= 13:
            patient_num = patient_list[i]
            src_file_list = glob(src_dir + '%04d_*' % patient_num)
            for srcfile in src_file_list:
                mycopyfile(srcfile, dst_dir + 'fold0/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold1/dukemtmc/DukeMTMC-reID/bounding_box_test/')
                mycopyfile(srcfile, dst_dir + 'fold2/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold3/dukemtmc/DukeMTMC-reID/bounding_box_train/')
        elif i <= 20:
            patient_num = patient_list[i]
            src_file_list = glob(src_dir + '%04d_*' % patient_num)
            for srcfile in src_file_list:
                mycopyfile(srcfile, dst_dir + 'fold0/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold1/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold2/dukemtmc/DukeMTMC-reID/bounding_box_test/')
                mycopyfile(srcfile, dst_dir + 'fold3/dukemtmc/DukeMTMC-reID/bounding_box_train/')
        else:
            patient_num = patient_list[i]
            src_file_list = glob(src_dir + '%04d_*' % patient_num)
            for srcfile in src_file_list:
                mycopyfile(srcfile, dst_dir + 'fold0/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold1/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold2/dukemtmc/DukeMTMC-reID/bounding_box_train/')
                mycopyfile(srcfile, dst_dir + 'fold3/dukemtmc/DukeMTMC-reID/bounding_box_test/')
