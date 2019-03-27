# 結果はいずれも、[1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
numbers_1 = [x ** 2 for x in numbers]
# map関数は、第一引数に関数（Lambda式）、第二引数にIterableなObjectを受け取る
numbers_2 = map(lambda x: x ** 2, numbers)


# 結果はいずれも、[4, 16]
numbers_1 = [x ** 2 for x in numbers if x % 2 == 0]

# filter関数で絞り込んだ後で、mapに渡している
# filter関数もmap同様に、第一引数に関数（Lambda式）、第二引数にIterableなObjectを受け取る
numbers_2 = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
