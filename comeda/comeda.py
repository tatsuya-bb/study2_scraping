import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from lxml import html

def main():

  start=1
  end=1000
  df=pd.DataFrame()

  for i in range(start,end):

    try:
      url=f"http://www.komeda.co.jp/search/shopdetail.php?id={i}"
      res = requests.get(url)
      if not(300 > res.status_code >= 200):
        print(f"fetch store review error | number :{i}")
      soup = bs(res.text, "html.parser")

      #店舗名を取得
      name = soup.select_one(".shop.mt20 h3").text
      print(name)

      postage=soup.select(".shop.mt10 p")[0].text
      print(postage)

      address=soup.select(".shop.mt10 p")[1].text
      print(address)

      tel=soup.select_one(".d-inline-b").text
      print(tel)

      df = df.append({
            "店舗名": name,
            "郵便番号": postage,
            "住所": address,
            "電話番号":tel
            }, ignore_index=True)
      df.to_csv("./test.csv", mode='w', encoding='utf-8')
      print(f"success number: {i}")
    except Exception as e:
      import traceback
      print(f"error number: {i} | {traceback.print_exc()}")



if __name__ == "__main__":
  main()
