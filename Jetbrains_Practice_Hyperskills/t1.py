pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingrediant=input().strip()
if(pasta.__contains__(ingrediant)):
    print('pasta time')
if(apple_pie.__contains__(ingrediant)):
    print('apple pie time')
if(ratatouille.__contains__(ingrediant)):
    print('ratatouille time')
if(chocolate_cake.__contains__(ingrediant)):
    print('chocolate cake time')
if(omelette.__contains__(ingrediant)):
    print('omelette time')
