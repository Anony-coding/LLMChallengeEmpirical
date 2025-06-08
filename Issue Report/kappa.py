from collections import Counter
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa


def compute_fleiss_kappa(data):
    # 1. 获取所有出现过的标签
    all_labels = set(label for sample in data for label in sample)
    all_labels = sorted(list(all_labels))  # 保证顺序一致
    label_to_index = {label: idx for idx, label in enumerate(all_labels)}
    num_labels = len(all_labels)

    # 2. 构建矩阵：每一行是每个数据点的标签分布
    rating_matrix = np.zeros((len(data), num_labels), dtype=int)
    for i, sample in enumerate(data):
        counter = Counter(sample)
        for label, count in counter.items():
            rating_matrix[i, label_to_index[label]] = count

    # 3. 计算 Fleiss' Kappa
    kappa_score = fleiss_kappa(rating_matrix)
    return kappa_score


