import math

def binarySearch(arr: list, n: int):
    L = 0
    R = len(arr) - 1
    index: int = -1
    while L <= R:
        mid: int = math.floor((L + R) / 2)
        if arr[mid] < n:
            L = mid + 1
        elif arr[mid] > n:
            R = mid - 1
        else:
            index = mid
            break
    return index

def main():
    arr: list = [i for i in range(10000)]
    print('{0} found in index {0}'.format(256, binarySearch(arr, 256)))

if __name__ == '__main__':
    main()
