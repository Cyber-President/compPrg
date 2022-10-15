import sys
import itertools


def main():
    """
    :return: None
    """
    # 入力層
    n = int(input())
    products = [int(x) for x in input().rstrip().split()]
    products.sort()
    # 定義層
    cnt = 0

    # 実行層
    # 全パターン
    for p in itertools.permutations(products):
        # tuple -> list
        p = list(p)
        print(p)
        # p[i] p[i-1]を比較
        # p[i] < p[i-1] 一回だけ許容
        # カウント増加
        pass

    # 出力層
    ans = cnt % 100003
    print(ans)

    return


if __name__ == '__main__':
    main()
