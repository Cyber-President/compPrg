import sys


def main():
    """

    :return:
    """
    n = int(input())
    nums = [int(x) for x in input().rstrip().split()]

    min_nums = min(nums)
    max_nums = max(nums)

    nums.sort()
    result = ''.join(map(str, nums))

    print(min_nums, max_nums)
    print(result)
    return


if __name__ == '__main__':
    main()
