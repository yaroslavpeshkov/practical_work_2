import ru_local as ru

income = float(input(ru.INCOME))
profit = income / 100 * 19
print(f'{ru.PROFIT}: {round(profit, 2)}')
