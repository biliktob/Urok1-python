revenue = int(input("Введите сумму выручки компании за прошедший месяц:"))
costs = int(input("Введите сумму издержек компании:"))
profit = revenue-costs
loss = costs-revenue
if revenue > costs:
    print("Компания работает с положительным финансовым результатом, прибыль составила:{a}".format(a=profit))
elif revenue < costs:
    print("Компания работает с отрицательным финансовым результатом, убыток составил:{a}".format(a=loss))
else:print("Результат компании без изменений")

