seconds = int(input("Введите время в секундах:"))
hours = seconds//3600
minutes = seconds//60
print("Вы задали время в секундах:{s}, что в формате чч:мм:сс составляет:{h}:{m}:{s}".format(s=seconds, h=hours, m=minutes))
