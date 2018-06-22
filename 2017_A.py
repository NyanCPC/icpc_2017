import sys


def data_input():
    items = []
    n, m = map(int, input().split(" "))             # nは商品の個数、mは許容額を読み込む
    if n!=0 and m!=0:                               # 0 0(終了の合図がないとき)
        items = list(map(int, input().split(" ")))  # 商品のそれぞれの値段のリストを読み込む
        return [n, m, items]                         # 戻り値
    else:
        sys.exit()                                  # 終了の合図があったときはプログラム終了

def search_answer(n, m, itemList):
    sumList = []                                    # 合計値のリスト
    for i in range(n):
        for j in range(n):
            if(i!=j) and itemList[i]+itemList[j]<=m: # おなじ商品は買わない, 合計値がmを超えるものはスルー
                sumList.append(itemList[i] + itemList[j]) # 合計値のリストに追加していく
    if len(sumList) != 0:
        print(max(sumList))                              # 答えを表示
    else:
        print("NONE")                                    # 答えがないときはNoneを表示


for i in range(5000):
    data_l = data_input()
    search_answer(data_l[0], data_l[1], data_l[2])





