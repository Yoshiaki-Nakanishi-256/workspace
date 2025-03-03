#ライブラリを取り込む
import openpyxl as excel

#新規ワークブックを作る
book = excel.Workbook()

#アクティブなワークシートを得る
sheet = book.active

#A1のセルに値を設定
sheet["A1"]="こんにちは"

#ファイルを保存
book.save("hello.xlsx")

#テスト

#テスト2

#test3

#test4

#test5

#test6

#test7