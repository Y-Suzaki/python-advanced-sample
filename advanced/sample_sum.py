# 1～10までの合計値を出したい
# for文でも可能だが、sum関数が標準で用意されている
print(sum(range(1, 11)))

# 1～20までの合計値を出したい
# ただし、偶数の場合だけ足すことにする
sum_num = 0
for i in range(1, 20):
    if i % 2 == 0:
        sum_num += i
print(sum_num)

# 1行で記載することが可能（リスト内表記）
# 速度は速いが、全配列をメモリ上に保持してしまう
print(sum([i for i in range(1, 20) if i % 2 == 0]))

# リスト内表記を使わない場合（ジェネレータ）
# 速度は遅めだが、メモリは少量で済む
print(sum(i for i in range(1, 20) if i % 2 == 0))
