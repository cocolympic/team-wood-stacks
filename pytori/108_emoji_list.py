import emoji

# 絵文字を含むテキスト
text = "I love Python! 🐍 and coding! 💻🚀"

# 絵文字をリストで取得
emoji_list = emoji.emoji_list(text)

# 結果を表示
print(emoji_list)
