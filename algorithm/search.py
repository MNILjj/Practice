#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# 时间: 2023-05-07
"""
查找算法：输入一个元素，在被查询的列表中搜索相同的元素并返回其索引。
查找算法包括顺序查找、二分查找等。不同的算法有不同的时间、空间复杂度。
"""

from debug.compute_time import run_time
from typing import Union


@run_time
def linear_search(li: list, val: Union[int, float, str]) -> Union[int, None]:
    """
    线性查找，也叫做顺序查找。方法是直接遍历列表，将列表元素与被查找元素进行对比，若循环到与被查找元素相同的元素时，
    返回该元素在列表中的索引，若遍历完后没有找到被查找元素，则返回None。

    需要注意的是：
    1. 若列表中存在别查找的元素，返回的索引是列表中第一个与被查找元素相同元素的位置，而不是找出列表中所有与被查找元素一样的元素。
    2. 本方法的时间复杂度是O(n)。

    python内置的查找算法： list.index()

    Args:
        li: 需要检索的列表。
        val: 需要查找的元素。

    Returns: 被查找元素的索引或者None。

    """

    id_ = 0
    for i in li:  # for i, v in enumerate(li):
        if i == val:
            return id_
        id_ += 1
    else:
        return None
@run_time
def binary_search(li: list, val: Union[int, float, str]) -> Union[int, None]:
    """
    二分查找，也叫折半查找。方法是先对输入的列表进行排序，然后取列表中间的元素与被查找元素比较，
    若是，则直接返回列表该位置的索引，若不是，则判断该元素与被查找元素之间的大小，比被查找元素小，
    则说明需要在列表中该元素右边去寻找，左边的舍弃，反之亦然。按照这个逻辑继续进行下去，直到在列表中
    找到这个元素后返回该元素在列表中的索引；若被查找元素不在列表中，返回None。

    需要注意的是：
    1. 二分查找输入的列表必须是有序的，如果是无序列表，必须先排序才能使用二分查找。
    2. 在列表有序的情况下，二分查找的时间复杂度是O(logn);若列表无序，则需要考虑排序算法的时间复杂度。

    Args:
        li: 需要检索的列表。
        val: 需要查找的元素。

    Returns: 被查找元素的索引或者None。

    """
    li.sort()

    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1  # 在if中已经知道了li[mid]不是val,所以从mid+1开始查找，可以减少重复次数。
        else:  # li[mid] > val:
            right = mid - 1
    return None

if __name__ == "__main__":
    li = list(range(102222))
    val = 6666

    # id = linear_search(li, val)

    id_ = binary_search(li, val)
    print(id_)