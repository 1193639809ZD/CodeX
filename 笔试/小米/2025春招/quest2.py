"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-12 20:58:57
lastModified:  2025-03-12 20:58:59

公司需要采购一批汽车，保证可以载人X，载货Y，经过调研有n种汽车，对第i种汽车，价值为m_i， 有k_i种选配方案，默认方案承载x_i人，载货y_i，第j中选配方案需要金额变化为m_ij，载人变化值为x_ij，载货变化量为y_ij，
每辆车只能选择一种选配方案，或者默认方案。可以采购多种汽车的多种选配方案，希望花销最少。

输入说明：
第一行为X, Y, n，取值范围在[1, 200]
下面是n组数据
第i组数据第一行包括四个整数，m_i, x_i, y_i, k_i，其中选配方案k_i可能为0
接下来k_i行，包括3个整数，m_ij, x_ij, y_ij, 变化值可能为负数
数据保证k_i之和小于200-n，价格，载人和载货量均为正值

输入样例：
10 20 2
100 2 6 1
20 1 1
80 5 1 1
10 -1 2

输出：390

"""
