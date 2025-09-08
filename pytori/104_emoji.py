import emoji

# 名前で絵文字を表示
print(emoji.emojize("Python is fun! :snake: :rocket:", use_aliases=True))

# 絵文字の名前を取得
text = "I love Python! 🐍"
emoji_list = emoji.emoji_list(text)
print(emoji_list)
