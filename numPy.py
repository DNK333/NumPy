import numpy as np

sales = np.array([
    [120, 150, 180, 200],
    [90, 130, 160, 170],
    [200, 220, 250, 280]
])

print(sales.shape)
print(sales.ndim)
print(sales.size)

print(sales[0])
print(sales[:, -1])

print(sales[-2:])

sales[1, 0] = 100

print(sales.reshape(2, 6))

bonus = np.array([10, 20, 30, 40])
sales_with_bonus = sales + bonus
print(sales_with_bonus)

print(sales.sum())
print(sales.mean())
print(sales.min())
print(sales.max())

print(sales.sum(axis=1))

print(sales[sales > 180])

print(np.count_nonzero(sales > 180))

sales[sales < 100] = 100
print(sales)
