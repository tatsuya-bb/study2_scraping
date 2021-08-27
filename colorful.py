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

    for i in range(5):
        address = "sdf@gmail.com"
        message = "暴力、詐欺求人はやめよう。"

        # driverを起動
        driver = set_driver(True)
        # Webサイトを開く
        driver.get("https://www.colorful2005.com/%E6%8E%A1%E7%94%A8%E6%A1%88%E5%86%85")
        time.sleep(5)

        # 検索窓に入力
        driver.find_element_by_css_selector("#input_comp-kpjrq7kn").send_keys(address)
        driver.find_element_by_css_selector("._1VWbH.has-custom-focus").send_keys(message)
        # 検索ボタンクリック
        driver.find_element_by_class_name("_1Qjd7").click()

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
