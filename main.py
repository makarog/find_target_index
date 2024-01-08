import sys


def main():
    input_data = sys.stdin.readline().rstrip()

    sorted_array = list(map(int, input_data.split()))

    target = int(sys.stdin.readline().rstrip())

    def find_element(sorted_numbers, element):
        left = 0

        right = len(sorted_array)

        result = 0

        while left < right:
            mid = (left + right) // 2
            if sorted_numbers[mid] == element:
                result = mid
                right = mid

            if sorted_numbers[mid] < element:
                left = mid + 1
                result = mid + 1
            if sorted_numbers[mid] > element:
                right = mid
                result = mid

        return result

    target_index = find_element(sorted_array, target)
    print(target_index)


if __name__ == '__main__':
    main()
