import pandas as pd
PATH="./study1-4.csv"


def search():

    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    df=pd.read_csv(PATH)
    source=list(df["name"])

    if word in source:
        print("{}は存在します".format(word))
    else:
        print("{}は存在ましません".format(word))
        add_flg = input("{}を追加しますか？>>(0:する　1:しない)".format(word))
        if add_flg == "0":
            print("{}を追加しました".format(word))
            source.append(word)
        else:
            pass

        df = pd.DataFrame(source,columns=["name"])
        df.to_csv(PATH,encoding="utf_8-sig")
        
if __name__ == "__main__":
    search()
