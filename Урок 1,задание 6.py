revenue = int(input("Введите сумму выручки компании за прошедший месяц:"))
costs = int(input("Введите сумму издержек компании:"))
profit = revenue-costs
loss = costs-revenue
profitability = profit/revenue
print("Рентабельность выручки Вашей фирмы составляет:{a}".format(a=profitability))
number_of_employees = int(input("Введите количество сотрудников Вашей фирмы:"))
salary = profit/number_of_employees
print("Результат работы каждого сотрудника в среднем составил:{a}".format(a=salary))