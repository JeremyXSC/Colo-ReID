import shutil
import os

seed = 5

for fold in range(4):
    i = 0
    source_path = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r{}/fold{}/dukemtmc/DukeMTMC-reID/bounding_box_test/'.format(seed, fold)
    target_path = '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID/r{}/fold{}/dukemtmc/DukeMTMC-reID/query/'.format(seed, fold)
    if not os.path.exists(target_path):
        os.makedirs(target_path)  # 创建路径
    for files in sorted(os.listdir(source_path)):
        if i % 9 == 0:
            shutil.move(source_path + files, target_path + files)
        i += 1