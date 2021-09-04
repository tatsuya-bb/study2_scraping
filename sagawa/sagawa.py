import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import eel

# Chromeを起動する関数
def set_driver(headless_flg):

    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == False:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(ChromeDriverManager().install(), options=options)

# main処理
def main():
    #task1
    path="佐川フォーマット.xlsx"
    df=pd.read_excel(path)
    sagawa_code=list(df["問い合わせ番号"])


    #task2
    # driverを起動
    driver = set_driver(True)
    # Webサイトを開く
    driver.get("https://k2k.sagawa-exp.co.jp/p/sagawa/web/okurijoinput.jsp")
    time.sleep(5)
    # 検索窓に入力
    toiawase_no_elms = driver.find_elements_by_class_name("toiban-dt1")
    for elm, toiawase_no in zip(toiawase_no_elms, sagawa_code):elm.send_keys(toiawase_no)
    # 検索ボタンクリック
    driver.find_element_by_css_selector(".btn_basic.btn_level01").click()


    #task3
    exp_stock_list=[]
    exp_number_list=[]


    stock_list = driver.find_elements_by_class_name("state")
    for stock in stock_list:
        exp_stock_list.append(stock.text)

    number_list=driver.find_elements_by_css_selector(".number.nowrap")
    for number in number_list:
        exp_number_list.append(number.text)

    #CSVに出力
    df=pd.DataFrame({"お問い合わせNO":exp_number_list,"最新荷物状況":exp_stock_list})
    df.to_csv("./sagawa.csv",mode="w",encoding="utf-8")

if __name__ == "__main__":
    main()
