def divide(a, b):
    if b == 0:
        raise ValueError("ゼロでは割り算できません")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"エラー: {e}")
