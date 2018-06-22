import sys

def judge(mystr, correctStr):
    if(mystr == correctStr):        # ふたつの文字列が完全に一致する場合、IDENTICALをreturn
        return("IDENTICAL")
    else:
        miss = 0                    # 誤差の数をカウントする
        mystrList = mystr.split('"')
        correctStrList = correctStr.split('"')
        if(len(mystrList)!=len(correctStrList)):
            return("DIFFERENT")
        for i in range(min(len(mystrList), len(correctStrList))):
            if(i%2==0):             # ""で囲まれていない部分について
                if(mystrList[i]!=correctStrList[i]): # 一致しない場合
                    return("DIFFERENT")
            else:                   # ""で囲まれている部分について
                if(mystrList[i]!=correctStrList[i]):    # 一致しない場合
                    miss += 1
                    if(miss > 1):   # missが複数になった場合はdifferent
                        return("DIFFERENT")
        if(miss == 1):
            return("CLOSE")

#------------------
while(True):
    str1 = input()
    if str1 == '.': # 終了の記号'.'が入力された場合、プログラムを終了
        sys.exit()
    str2 = input()

    print(judge(str1, str2))

