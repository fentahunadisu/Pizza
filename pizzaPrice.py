import random
def p_price(size):
    pizza_size = ['S', 'M', 'L', 'XL']
    pizza_Pice = [40, 50, 60, 75]
    price = pizza_Pice[pizza_size.index(size)]
    return price


delivery_costB = 20
delivery_costO = 60
amount_extra = 0
age = int(input("please enter the age: "))
game = input("do you want play a game?\n if you play you will have discont y/n")
destination = input("enter your destination: ")
dic_persent = 0
total = 0
while age>18:
     size = input("please enter  the pizza size: ")
     extra = input("do you want extar? ")
     amount_slice = int(input("enter amount of slice you  need: "))
     if extra == "yes":
         sum = amount_extra(amount_slice)
         total+=sum
     if game != "no":
         chance1 = random.randint(1, 9)
         input("press enter to continue: ")
         print('chance1 value is ', chance1)
         chance2 = random.randint(1, 9)
         input("press enter to continue: ")
         print('chance2 value is ', chance2)
         dic_persent += (chance1 * chance2) / 100
         print(f'the persent you get discount is {dic_persent}')
     if destination == "beersheba":
         sum = p_price(size) + delivery_costB
         total+=sum
     else:
         sum = p_price(size) + delivery_costO
         total+=sum
     con = input("do you want continue: ")
     if con == "no":
         break
else:
    print("Sorry you can not get an access! good bay! ")
print(f'The total pyament is {total} ')
print(f'The total pyament with discount is {round(total * (1 - dic_persent))} ')