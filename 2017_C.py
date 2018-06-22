import sys

while(True):
    d, w = map(int, input().split(" ")) #庭の奥行と幅を読み込む
    if (d==0 and w==0):
        sys.exit()
    e = [list(map(int, input().split(" "))) for i in range(d)] #内包表記(すごーい)
    gaishu_height = []
    pond_height = []


    for i in range(3,w):
        for j in range(3,d):
            for x in range(0,w-i):
                for y in range(0,d-j):
                    print(x,y)


    print(e)
