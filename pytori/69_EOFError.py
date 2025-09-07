try:
    data = input("何か入力してください")
    print("入力された内容:", data)
except EOFError:
    print("EOFErrorが発生しました(入力が終了しました)")