import sys


def main():
    """
    :return:　None
    """
    # 標準入力
    line = input()
    # 定義層
    img, doc = 'img', 'doc'
    # 実行層
    if img in line:
        if doc in line:
            print('presentation')
        else:
            print('image')
    elif doc in line:
        print('document')
    else:
        print('other')

    return


if __name__ == '__main__':
    main()
