import sys


def main():
    """
    :return: None
    """
    # 入力層
    n, m, k = [int(x) for x in input().rstrip().split()]
    # 実行層
    if m * k <= n:
        print(k)
    elif m * k > n:
        if m * k - n > m:
            print(m)
        else:
            print(m - (n - (m * (k - 1))))

    return


if __name__ == '__main__':
    main()
