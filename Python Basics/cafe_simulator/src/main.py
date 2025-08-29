from menu_items import Drink, Food
from customer import Customer

def run_simulation():
    ## Initialize food and dring instances
    latte = Drink("Latte", 120, "hot")
    iced_tea = Drink("Iced Tea", 90, "cold")
    pizza = Food("Pizza", 350, False)
    salad = Food("Salad", 280, True)

    # Customer places an order
    customer = Customer("Andrusha")
    order = customer.create_order([latte, pizza, salad, iced_tea])

    # Process the order
    order.process_order()


if __name__ == "__main__":
    run_simulation()