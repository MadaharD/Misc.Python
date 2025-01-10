class CafeItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def total_price(user_items: list[CafeItem]) -> float:
    total: float = 0.0

    for item in user_items:
        total += item.price

    return total

user_items: list[CafeItem] = []
    
for i in range(3):
    user_intent : str = input("Would you like to order something, [y]es or [n]o: ").lower()

    if user_intent == 'yes' or user_intent == 'y':
        print("the options are: coffee, sandwich, bagel, oatmeal, and salad")
        user_order : str = input("what would you like to order?: ").lower()

        if user_order == "coffee":
            user_items.append(CafeItem("coffee", 2.00))
        elif user_order == "sandwich":
            user_items.append(CafeItem("sandwich", 5.00))
        elif user_order == "bagel":
            user_items.append(CafeItem("bagel", 1.95))
        elif user_order == "oatmeal":
            user_items.append(CafeItem("oatmeal", 3.45))
        elif user_order == "salad":
            user_items.append(CafeItem("salad", 2.67))
        else:
            print("that's not a valid option")
            continue

        print("got it!")

    elif user_intent == "no" or user_intent == "n":
        print("bye!")
        break

    else:
        print('that is not a valid option!')

print("your total is: $" + str(total_price(user_items)))
