import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from lxml import html

def main():

  df = pd.DataFrame()

  # Webサイトを開く
  url="https://www.interphex.jp/ja-jp/about.html"
  res = requests.get(url)
  if not(300 > res.status_code >= 200):
    print(f"fetch store review error")
  soup = bs(res.text, "html.parser")


  #開催展名を取得
  lxml_data = html.fromstring(res.text)
  name = lxml_data.xpath("//b[contains(text(), '【開催展名】')]/following-sibling::text")[0].text
  print(name)



  df = df.append({
    "開催展名": name
    }, ignore_index=True)
  df.to_csv("./test.csv", mode='w', encoding='utf-8')

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
  main()
