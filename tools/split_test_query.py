import shutil
import os

# 二选一A：固定单一seed
# seed = 7 #每次只需要修改seed！
# 二选一B：使用固定范围内的seed
for seed in range(5, 6):
    for i in range(4):
        src_dir = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r{}/fold{}/dukemtmc/DukeMTMC-reID/bounding_box_test/'.format(seed, i)
        dst_dir = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r{}/fold{}/dukemtmc/DukeMTMC-reID/query/'.format(seed, i)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        j = 0
        for files in sorted(os.listdir(src_dir)):
            if j % 9 == 0:
                shutil.move(src_dir + files, dst_dir + files)
            j += 1