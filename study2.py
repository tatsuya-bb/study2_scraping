from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chromeを起動する関数
def set_driver(headless_flg):

    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
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

def main():
    search_keyword = "高収入"

    # driverを起動
    driver = set_driver(True)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(1)
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(1)
    except:
        pass

    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    driver.find_element_by_class_name("topSearch__button").click()


    exp_name_list = []

    name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
    for name in name_list:
        print(name.text)
        exp_name_list.append(name.text)

    df = pd.DataFrame(exp_name_list,columns=["企業名"])
    df.to_csv("study2-5.csv")

if __name__ == "__main__":
    main()
