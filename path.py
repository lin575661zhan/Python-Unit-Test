
"""
測試目標: Edge-Pair coverage
總共 Edge-Pair: 123, 129, 234, 345, 346, 467, 468, 672, 682, 723, 729, 823, 829

test case 1 (測試案例 1)
1) Input values(測試時候需要控制資料的值): arr = [1, 2, 3, 4, 5], target = 3
2) expected result(正確的 結果): 2
3) test program's result(程式執行後的結果): 2
4) criteria analysis(測試目標的分析)
Edge-Pair coverage:   測試案例涵蓋的 Edges: 12345: 123, 234, 345

test case 2 (測試案例 2)
1) Input values(測試時候需要控制資料的值): arr = [2, 4, 6, 8, 10, 12, 14, 16], target = 11
2) expected result(正確的 結果): -1
3) test program's result(程式執行後的結果): -1
4) criteria analysis(測試目標的分析) 
Edge-Pair coverage: 測試案例涵蓋的 Edges: 123467234682346729: 123, 234, 346, 467, 672, 723, 468, 682, 823, 729

Test case 3 (測試案例 3)
1) Input values(測試時候需要控制資料的值): arr = [50, 100], target = 25
2) expected result(正確的 結果): -1
3) test program's result(程式執行後的結果): -1
4) criteria analysis(測試目標的分析) 
Edge-Pair coverage: 測試案例涵蓋的 Edges: 12346829: 123, 234, 346, 468, 682, 829

Test case 4 (測試案例 4)
1) Input values(測試時候需要控制資料的值): arr = [], target = 10
2) expected result(正確的 結果): -1
3) test program's result(程式執行後的結果): -1
4) criteria analysis(測試目標的分析) 
Edge-Pair coverage: 測試案例涵蓋的 Edges: 129

案例總共涵蓋總共 Edge-Pair:	 123, 129, 234, 345, 346, 467, 468, 672, 682, 723, 729, 823, 829
Edge-Pair coverage: 100%
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
    
    def testCase3(self):
        arr = [50, 100]
        target = 25
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)
    
    def testCase4(self):
        arr = []
        target = 10
        result = binarySearch(arr, target)
        self.assertEqual(-1, result)

if __name__ == '__main__':
    unittest.main()