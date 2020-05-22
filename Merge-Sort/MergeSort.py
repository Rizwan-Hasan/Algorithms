import os
os.system('clear')


class MergeSort:
    def __init__(self, arr: list):
        self.__arr: list
        self.__mergeSort(arr)

    def getArray(self):
        return self.__arr

    def __mergeSort(self, arr: list):
        if len(arr) > 1:
            mid: int = len(arr) // 2
            left: int = arr[:mid]
            right: int = arr[mid:]

            # Recursive call on each half
            self.__mergeSort(left)
            self.__mergeSort(right)

            # Two iterators for traversing the two halves
            i, j = 0, 0

            # Iterator for the main list
            k: int = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    # The value from the left half has been used
                    arr[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            self.__arr: list = arr


if __name__ == "__main__":
    arr: list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(MergeSort(arr).getArray())
