import datetime

import numpy as np
from plyfile import PlyData
from scipy.spatial.distance import cdist


# 在Python中，对比两个PLY格式的点云文件可以通过读取文件、
# 处理点数据以及计算点之间的差异来完成。为了实现这个功能，
# 我们可以使用plyfile库来读取PLY文件，然后使用一些简单的几何操作来进行比较。


# 在这个示例中，我们首先读取两个PLY文件并提取点云数据。然后，我们计算每个点云的中心点，并计算这两个中心点之间的距离。
# 接着，我们通过遍历每个点云中的点，并检查它们是否在设定的距离阈值内找到匹配点，来计算匹配点的数量。最后，我们计算每个点云中独特点的数量。
# 请注意，这个方法提供了一个基本的比较框架，实际应用中可能需要根据点云数据的特点和具体需求进行调整和优化。例如，可能需要考虑点云的预处理（如去噪、下采样等），以及更复杂的相似性度量方法和变换（如旋转、平移等）来更准确地比较两个点云。
def compare_ply_point_clouds(ply_path1, ply_path2):
    # 读取两个PLY文件
    point_cloud1 = PlyData.read(ply_path1)
    point_cloud2 = PlyData.read(ply_path2)

    # 提取点云数据
    points1 = np.vstack((point_cloud1['vertex']['x'], point_cloud1['vertex']['y'], point_cloud1['vertex']['z'])).T
    points2 = np.vstack((point_cloud2['vertex']['x'], point_cloud2['vertex']['y'], point_cloud2['vertex']['z'])).T

    # points3 = trimesh.load_mesh(ply_path1)
    # points4 = trimesh.load_mesh(ply_path2)
    # print(points3)
    # print(points4)

    print("点云1" + str(len(points1)))
    print("点云1" + str(len(points2)))
    # 计算两个点云的中心点
    # center1 = np.mean(points1, axis=0)
    # center2 = np.mean(points2, axis=0)

    # 计算点云之间的距离
    distance_threshold = 5  # 设定一个阈值，用于判断点是否相似
    # dist1_to_2 = np.linalg.norm(center1 - center2)
    # print(f"两点云中心之间的距离为: {dist1_to_2}")

    # 计算匹配点和独特点的数量
    matching_points = 0
    unique_points1 = 0
    unique_points2 = 0

    start_time = datetime.datetime.now()
    print(start_time)
    for point1 in points1:
        _result = cdist([point1], points2, 'euclidean')

        # _result2 = np.linalg.norm(point1 - points2[0])
        result1 = _result[_result < distance_threshold]
        print(result1)
        if result1.size > 0:
            matching_points += 1

    end_time = datetime.datetime.now()
    print(start_time, end_time)
    print("遍历处理数据")
    if matching_points > 0:
        unique_points1 = points1.shape[0] - matching_points
        unique_points2 = points2.shape[0] - matching_points

    print(f"匹配点: {matching_points}")
    print(f"点云中的唯一点 1: {unique_points1}")
    print(f"点云中的唯一点 2: {unique_points2}")


# 使用示例
compare_ply_point_clouds("11.ply", "22.ply")
