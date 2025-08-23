def cal_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price

price = float(input('Enter price: '))
discount_percent = float(input('Enter discount percent: '))

print(cal_discount(price, discount_percent))
