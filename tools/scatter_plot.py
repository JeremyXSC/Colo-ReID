import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import cv2
import os

def read_and_resize_image(image_path, target_size):
    image = cv2.imread(image_path)
    image = cv2.resize(image, target_size)
    return image

def load_dataset(dataset_path, target_size):
    features = []
    for image_file in os.listdir(dataset_path):
        image_path = os.path.join(dataset_path, image_file)
        image = read_and_resize_image(image_path, target_size)
        # 提取图像特征（这里以简单地展平图像作为示例）
        feature = image.reshape(-1)
        features.append(feature)
    return np.array(features)

dataset_paths = ['/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold0/dukemtmc/DukeMTMC-reID/query/', '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold1/dukemtmc/DukeMTMC-reID/query/', '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold2/dukemtmc/DukeMTMC-reID/query/', '/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold3/dukemtmc/DukeMTMC-reID/query/']

target_size = (256, 256)  # 设置目标图像尺寸

all_features = []
for dataset_path in dataset_paths:
    features = load_dataset(dataset_path, target_size)
    all_features.extend(features)

all_features = np.array(all_features)

# 使用t-SNE进行降维
tsne = TSNE(n_components=2, random_state=42)
reduced_features = tsne.fit_transform(all_features)

# 绘制散点图
num_samples_per_dataset = [len(os.listdir(dataset_path)) for dataset_path in dataset_paths]
color_idx = 0
start_idx = 0
for i, num_samples in enumerate(num_samples_per_dataset):
    end_idx = start_idx + num_samples
    plt.scatter(reduced_features[start_idx:end_idx, 0], reduced_features[start_idx:end_idx, 1], label='Dataset {}'.format(i+1))
    start_idx = end_idx
    color_idx += 1

plt.legend()
plt.show()




# import torch
# import torchvision
# from torchvision import transforms
# from sklearn.manifold import TSNE
# import matplotlib.pyplot as plt
#
# # 设置每个数据集的路径
# dataset1_path = "/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold0/dukemtmc/DukeMTMC-reID/query/"
# dataset2_path = "/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold1/dukemtmc/DukeMTMC-reID/query/"
# dataset3_path = "/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold2/dukemtmc/DukeMTMC-reID/query/"
# dataset4_path = "/home/chenqingzhong/data/chenqingzhong/Data/dukemtmc/DukeMTMC-reID（息肉）/r1/fold3/dukemtmc/DukeMTMC-reID/query/"
#
# # 定义数据预处理步骤
# transform = transforms.ToTensor()
#
# # 加载并预处理数据集
# dataset1 = torchvision.datasets.ImageFolder(root=dataset1_path, transform=transform)
# dataset2 = torchvision.datasets.ImageFolder(root=dataset2_path, transform=transform)
# dataset3 = torchvision.datasets.ImageFolder(root=dataset3_path, transform=transform)
# dataset4 = torchvision.datasets.ImageFolder(root=dataset4_path, transform=transform)
#
# # 将所有数据集合并
# all_datasets = torch.utils.data.ConcatDataset([dataset1, dataset2, dataset3, dataset4])
#
# # 创建数据加载器
# batch_size = 64
# data_loader = torch.utils.data.DataLoader(all_datasets, batch_size=batch_size, shuffle=True)
#
# # 提取特征向量
# features = []
# labels = []
#
# model = torchvision.models.resnet18(pretrained=True)  # 使用预训练的ResNet模型
# model.fc = torch.nn.Identity()  # 去除最后一层分类器，保留特征提取部分
#
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = model.to(device)
#
# model.eval()  # 设置为评估模式，不进行梯度计算
#
# with torch.no_grad():
#     for images, batch_labels in data_loader:
#         images = images.to(device)
#         features_batch = model(images)
#         print(features_batch.shape)  # 打印特征向量的维度
#         features.append(features_batch.cpu())
#         labels.append(batch_labels)
#
# features = torch.cat(features, dim=0)
# labels = torch.cat(labels, dim=0)
#
# # 使用 t-SNE 进行特征映射
# tsne = TSNE(n_components=2, random_state=42)
# embedded_features = tsne.fit_transform(features)
#
# # 绘制散点图
# plt.scatter(embedded_features[:, 0], embedded_features[:, 1], c=labels, cmap='viridis')
# plt.colorbar()
#
# # 设置图例、标题和坐标轴标签
# plt.legend(['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4'])
# plt.title('Differentiation between Image Datasets')
# plt.xlabel('t-SNE Dimension 1')
# plt.ylabel('t-SNE Dimension 2')
#
# # 显示图形
# plt.show()
