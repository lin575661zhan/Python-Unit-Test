"""
測試目標: Edge coverage
總共 Edges: 12, 23, 29, 34, 45, 46, 67, 68, 72, 82

test case 1 (測試案例 1)
1) Input values(測試時候需要控制資料的值): arr = [1, 2, 3, 4, 5], target = 3
2) expected result(正確的 結果): 2
3) test program's result(程式執行後的結果): 2
4) criteria analysis(測試目標的分析)
Edge coverage:   測試案例涵蓋的 Edges: 12, 23, 34, 45

test case 2 (測試案例 2)
1) Input values(測試時候需要控制資料的值): arr = [2, 4, 6, 8, 10, 12, 14, 16], target = 11
2) expected result(正確的 結果): -1
3) test program's result(程式執行後的結果): -1
4) criteria analysis(測試目標的分析) 
Edge coverage: 測試案例涵蓋的 Edges: 12, 23, 34, 46, 67, 72, 68, 82, 29

案例總共涵蓋總共 Edges:	12, 23, 29, 34, 45, 46, 67, 68, 72, 82
Edge coverage: 100%
"""

import unittest

def binarySearch(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        num = arr[mid]

        if num == target:
            return mid
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

class TestBinarySearch(unittest.TestCase):

    def testCase1(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        result = binarySearch(arr, target)
        self.assertEqual(2, result)

    def testCase2(self):
        arr = [2, 4, 6, 8, 10, 12, 14, 16]
        target = 11
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)

if __name__ == '__main__':
    unittest.main()