import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from lxml import html

def main():

  start = 3164000
  end = 4000000
  df = pd.DataFrame()
  for i in range(start, end):
    try:
      # Webサイトを開く
      url=f"https://demae-can.com/shopDetail/{i}/"
      res = requests.get(url)
      if not(300 > res.status_code >= 200):
        print(f"fetch store review error | number :{i}")
        continue
      soup = bs(res.text, "html.parser")

      #店舗名を取得
      name = soup.select_one("#shop_info_area h1").text
      idx = name.find("の店舗詳細")
      print(name[:idx])

      #住所を取得
      lxml_data = html.fromstring(res.text)

      address = lxml_data.xpath("//h3[contains(text(), '住所')]/following-sibling::p[1]")[0].text
      print(address)

      #最低注文条件を取得
      order = lxml_data.xpath("//h3[contains(text(), '最低注文条件')]/following-sibling::p[1]")[0].text
      print(order)

      #送料を取得
      postage = lxml_data.xpath("//h3[contains(text(), '送料')]/following-sibling::p[1]")[0].text
      print(postage)

      #レビューを取得
      res = requests.get("https://demae-can.com/shopDetail/{}/?review=1".format(i))
      if not(300 > res.status_code >= 200):
        print(f"fetch store review error | number :{i}")
        continue
      soup = bs(res.text, "html.parser")
      try:
        star = soup.select_one(".shop_star").text
        star_rate = star[:star.find("(")].strip()
        print(star_rate)

        #レビュー数を取得
        review_number = star[star.find("(")+1:-1].strip()
        print(review_number)
      except:
        print("review not found")
        star_rate = 0.0
        review_number = 0

      df = df.append({
        "店舗番号": {i},
        "店舗名": name[:idx],
        "住所": address,
        "最低注文条件": order,
        "送料": postage,
        "評価": star_rate,
        "評価数": review_number
        }, ignore_index=True)
      df.to_csv("./test.csv", mode='w', encoding='utf-8')
      print(f"success number: {i}")

    except Exception as e:
      import traceback
      print(f"error number: {i} | {traceback.print_exc()}")
    time.sleep(1)

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
  main()
