def menu_select(menulist, etc):
  order = {}

  print(f'<{etc}를 선택해주세요>')

  for name, price in menulist.items():
    print(f'{name}({price:,})원')

  while True:
    menu_name = input('메뉴 이름을 입력하세요(종료: exit) >>')

    if menu_name == 'exit':
      break
    elif menu_name in menulist:
      count = int(input('수량을 입력하세요: '))
      order[menu_name] = count
      print('주문완료')

  return order

def money_calc(order, menu):
    totprice = 0
    for k in order.keys():
        if k in menu.keys():
            price = order[k] * menu[k]
            print(f'{k}: {menu[k]}원 * {order[k]} = {price:,}원')
        totprice = totprice + price
    print(f'전체금액 : {totprice:,}원')
    
    return totprice

# #main()

# pizza_menu = {'페퍼로니' : 3000, '치즈' : 3200, '콤비네이션' : 3500,
#               '불고기' : 3600, '해산물' : 3800}

# drink_menu = {'콜라':1500, '사이다': 1500, '생수': 1000}

# # 피자 주문
# order_pizza = menu_select(pizza_menu, '피자')
# # 음료 주문
# order_drink = menu_select(drink_menu, '음료')


# # 계산
# pizza_money = money_calc(order_pizza, pizza_menu)
# drink_money = money_calc(order_drink, drink_menu)

# print(f'전체금액: {pizza_money + drink_money}원')