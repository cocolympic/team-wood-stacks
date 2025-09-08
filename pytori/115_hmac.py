import hmac
import hashlib

# 秘密鍵とメッセージ
key = b"my_secret_key"
message = b"Hello, HMAC!"

# HMACを生成
hmac_code = hmac.new(key, message, hashlib.sha256)

# 結果を表示（16進数表現）
print("HMAC:", hmac_code.hexdigest())
