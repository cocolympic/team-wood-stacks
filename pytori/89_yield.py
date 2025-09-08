def count_up():
    for i in range(1, 6):
        yield i

for num in count_up():
    print(num)