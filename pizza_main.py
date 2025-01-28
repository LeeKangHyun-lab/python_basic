# import pizza_order as po #이렇게 하면 po.을 붙여야 한다.
from pizza_order import *; #이렇게 하면 po.을 안붙여도 된다.

pizza_menu = {'페퍼로니' : 3000, '치즈' : 3200, '콤비네이션' : 3500,
              '불고기' : 3600, '해산물' : 3800}

drink_menu = {'콜라':1500, '사이다': 1500, '생수': 1000}

# 피자 주문
order_pizza = menu_select(pizza_menu, '피자')
# 음료 주문
order_drink = menu_select(drink_menu, '음료')


# 계산
pizza_money = money_calc(order_pizza, pizza_menu)
drink_money = money_calc(order_drink, drink_menu)

print(f'전체금액: {pizza_money + drink_money}원')