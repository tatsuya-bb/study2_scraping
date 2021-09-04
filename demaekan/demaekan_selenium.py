from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Chromeを起動する関数
def set_driver(headless_flg):


  # Chromeドライバーの読み込み
  options = ChromeOptions()

  # ヘッドレスモード（画面非表示モード）をの設定
  if headless_flg == True:
    options.add_argument('--headless')

  # 起動オプションの設定
  options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
  # options.add_argument('log-level=3')
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--ignore-ssl-errors')
  options.add_argument('--incognito')          #シークレットモードの設定を付与

  # ChromeのWebDriverオブジェクトを作成する。
  return Chrome(ChromeDriverManager().install(), options=options)

def main():

  start = 3164000
  end = 3164010
  df = pd.DataFrame()
  for i in range(start, end):
   try:
    driver = set_driver(True)

    # Webサイトを開く
    driver.get(f"https://demae-can.com/shopDetail/{i}/")
    time.sleep(3)


    #店舗名を取得
    name = driver.find_element_by_css_selector("#shop_info_area h1").text
    idx = name.find("の店舗詳細")
    print(name[:idx])

    #住所を取得
    address = driver.find_element_by_xpath("//h3[contains(text(), '住所')]/following-sibling::p[1]").text
    print(address)

    #最低注文条件を取得
    order = driver.find_element_by_xpath("//h3[contains(text(), '最低注文条件')]/following-sibling::p[1]").text
    print(order)

    #送料を取得
    postage = driver.find_element_by_xpath("//h3[contains(text(), '送料')]/following-sibling::p[1]").text
    print(postage)

    #ページ移動
    driver.find_element_by_css_selector("[data-id='shop_review']").click()
    time.sleep(1)

    #レビューを取得
    star = driver.find_element_by_css_selector(".shop_star").text
    star_rate = star[:star.find("(")].strip()
    print(star_rate)

    #レビュー数を取得
    review_number = star[star.find("(")+1:-1].strip()
    print(review_number)

   except:
    pass


   df = df.append({
        "店舗名": name[:idx],
        "住所": address,
        "最低注文条件": order,
        "送料": postage,
        "評価": star_rate,
        "評価数": review_number
        }, ignore_index=True)
   df.to_csv("./test.csv", mode='w', encoding='utf-8')

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
  main()
