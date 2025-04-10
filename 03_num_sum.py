# Реализуйте функцию, которая находит количество способов
# разбить число n на сумму чисел, используя динамическое
# программирование

def count_partitions(n: int) -> int:
    if n <= 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]

    return dp[n]

n = 5
print(count_partitions(n))