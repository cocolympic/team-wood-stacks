def make_counter():
    count = 0  # 外側の関数の変数

    def increment():
        nonlocal count  # 外側の count を参照・更新
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # → 1
print(counter())  # → 2
print(counter())  # → 3