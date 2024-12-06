import open3d as o3d


def find_overlapped_cloud(cloud1, cloud2):
    overlapped_cloud_indices = []
    octree = o3d.geometry.Octree(max_depth=4)
    octree.convert_from_point_cloud(cloud1, size_expand=0.01)
    min_pt = octree.get_min_bound()
    max_pt = octree.get_max_bound()
    for point in cloud2.points:
        if point[0] < min_pt[0] or point[1] < min_pt[1] or point[2] < min_pt[2] or \
                point[0] > max_pt[0] or point[1] > max_pt[1] or point[2] > max_pt[2]:
            continue
        else:
            leaf_node, leaf_info = octree.locate_leaf_node(point)
            if leaf_info is not None:
                indices = leaf_node.indices
                for indice in indices:
                    overlapped_cloud_indices.append(indice)

    return cloud1.select_by_index(overlapped_cloud_indices)


if __name__ == '__main__':
    "read cloud"
    cloud1 = o3d.io.read_point_cloud("11.pcd")
    cloud2 = o3d.io.read_point_cloud("22.pcd")
    "find overlapped cloud"
    overlapped_cloud1 = find_overlapped_cloud(cloud2, cloud1)
    overlapped_cloud2 = find_overlapped_cloud(cloud1, cloud2)
    "save cloud"
    o3d.io.write_point_cloud("33.pcd", overlapped_cloud1)
    o3d.io.write_point_cloud("44.pcd", overlapped_cloud2)
