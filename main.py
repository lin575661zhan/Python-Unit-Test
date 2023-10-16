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