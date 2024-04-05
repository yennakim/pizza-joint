class Pizza:
# the self argument is the instance of the class that you created
  def __init__(self):
    # Establish the properties of each book
    # with a default value
    self.size = 0
    self.style = ""
    self.toppings = []

  def add_topping(self, topping):
    self.toppings.append(topping)

  def print_order(self):
    toppings_str = " and ".join(self.toppings)
    print(f"I would like a {self.size}-inch, {self.style} pizza with {toppings_str}.")

    
meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "deep-dish"
meat_lovers.add_topping("pepperoni")
meat_lovers.add_topping("olives")
meat_lovers.print_order()
