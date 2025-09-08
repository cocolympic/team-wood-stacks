import emoji

text = "Hello, world! 🌍👋"
clean_text = emoji.replace_emoji(text, replace="")
print(clean_text)
