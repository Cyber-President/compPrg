"""
n行の読み取り
n
1
2
3
"""
n = int(input())
rcs = [int(input()) for i in range(n)]

"""
n個の空白区切り読み取り→降順並び替え
n
1 2 3 4
"""
cards = [int(x) for x in input().rstrip().split()]

"""
要素がわかっている時の読み取り
a b c
"""
a, b, c = [int(x) for x in input().rstrip().split()]

"""
リスト要素の連結
"""
list.append(''.join(map(str, list)))

"""
降順
"""
cards.sort(reverse=True)

"""
重複削除
"""
set(list)
