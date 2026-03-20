from decimal import Decimal, getcontext
from fractions import Fraction

prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

getcontext().prec = 28

float_sum = sum(prices)
float_discounted = float_sum * (1 - 0.07)
float_with_vat = float_discounted * (1 + 0.20)
float_part = float_with_vat / 3

decimal_prices = [Decimal(str(price)) for price in prices]
decimal_sum = sum(decimal_prices)
decimal_discounted = decimal_sum * Decimal('0.93')
decimal_with_vat = decimal_discounted * Decimal('1.20')
decimal_part = decimal_with_vat / Decimal('3')

fraction_prices = [Fraction(str(price)) for price in prices]
fraction_sum = sum(fraction_prices)
fraction_discounted = fraction_sum * Fraction(93, 100)
fraction_with_vat = fraction_discounted * Fraction(6, 5)
fraction_part = fraction_with_vat / 3


print(f"{'Тип':<10} {'Итоговая сумма':<20} {'Одна треть':<20}")
print(f"{'float':<10} {float_with_vat:<20.15f} {float_part:<20.15f}")
print(f"{'Decimal':<10} {decimal_with_vat:<20} {decimal_part:<20}")
print(f"{'Fraction':<10} {float(fraction_with_vat):<20.15f} {float(fraction_part):<20.15f} (как float)")
print(f"{'Fraction':<10} {fraction_with_vat:<20} {fraction_part:<20} (как дробь)")
