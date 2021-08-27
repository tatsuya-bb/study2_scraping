name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")
def kimetsu(word):

  if word in name:
      print("{}は存在します".format(word))
  else:
      print("{}は存在しません".format(word))


kimetsu("ぜんいつ")
