k = 4

x = [1, 4, 2, 10, 2, 3, 1, 0, 20]

window = x[0:k]

window_sum = sum(window)

movement = len(x) - k

maximum = window_sum

for i in range(movement):
    window_sum = window_sum - x[i] + x[i + k]
    if window_sum > maximum:
        maximum = window_sum

print(maximum)