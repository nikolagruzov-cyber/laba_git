import sys
dann=[7,"30.10.2026","Васьков"]
zakaz=[101,102,103,104]
yeszakaz={101,104}
zm={101:"ул.Ленина 2", 102:"ул.Управленческая 3", 103:"ул.Предовая 4", 104:"ул.Чехова 10"}
new_zakaz=105
zakaz.append(new_zakaz)
print(dann)
zm[new_zakaz]=input("Введите адрес:")
print("Новый список заказов:",zakaz)
check_zakaz=int(input("Введите номер заказа для проверки:"))
if check_zakaz in yeszakaz:
    print("Этот заказ уже доставлен")
else:
    print("Этот заказ еще не доставлен")
search_adress_zakaz=int(input("Введите номер заказа для просмотра адреса:"))
print("Адрес доставки для этого заказа:",zm[search_adress_zakaz])
