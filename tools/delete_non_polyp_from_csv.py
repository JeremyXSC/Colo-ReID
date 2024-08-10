import csv
import shutil

with open('/home/chenqingzhong/data/chenqingzhong/Data/HyperKvasir/hyper-kvasir-videos/video-annotations.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    i = 1
    for row in reader:
        line = row['videoID;finding']
        if 'polyp' in line:
            print(line)
            video_name = line.split(';')[0]
            video_path = '/home/chenqingzhong/data/chenqingzhong/Data/HyperKvasir/hyper-kvasir-videos/videos/' + video_name + '.avi'
            new_video_name = str(format(i, "04")) + '_c1'
            target_video_path = '/home/chenqingzhong/data/chenqingzhong/Data/HyperKvasir/hyper-kvasir-videos/polyp videos/' + new_video_name + '.avi'
            shutil.move(video_path, target_video_path)
            i += 1

