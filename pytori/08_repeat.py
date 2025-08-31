import itertools

test_object = {
  "language": "python",
  "game": "pytori",
}

for item in itertools.repeat(test_object, 3):
  print(item)