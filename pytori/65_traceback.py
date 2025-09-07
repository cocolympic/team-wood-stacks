import traceback

try:
    x = 1 / 0
except Exception as e:
    print("エラーが発生しました")
    traceback.print_exc()