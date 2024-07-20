import flet as ft
import matplotlib.pyplot as plt
import check_normal_distribution

def main(page: ft.Page):
   
    text_box = ft.TextField(label="数値を１行ごとに入力(貼り付け)してください", multiline=True, height=200)
    
    # 平均を表示するテキスト
    result_text = ft.Text(value="平均: ")

    # ボタンが押されたときの処理
    def calculate_average(e):
        try:
            # テキストボックスの値を取得し、行ごとに分割して数値に変換
            numbers = [float(line) for line in text_box.value.splitlines() if line.strip()]
            if numbers:
                result = check_normal_distribution.check_normal_distribution(numbers)
                average = sum(numbers) / len(numbers)
                result_text.value = f"結果: {result}"
            else:
                result_text.value = "数値を入力してください."
        except ValueError:
            result_text.value = "数値を入力してください."

        # ページを更新
        page.update()

    # ボタン
    calculate_button = ft.ElevatedButton(text="検定開始", on_click=calculate_average)

    page.add(text_box, calculate_button, result_text)

# アプリケーションを実行
ft.app(target=main)
