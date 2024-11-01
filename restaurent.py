from typing import Any

class Restaurent:
    def __init__(self, name: str, order_date: str):
        self._name = name
        self.order_date = order_date
        self.item = None

    def order(self, item: str) -> None:
        self.item = item

    def show_order(self) -> Any:
        return self.item if self.item is not None else "No Order"
    
    
    

rest = Restaurent(name='Ravi', order_date='12/04/2020')
print(rest.show_order())
rest.order('Burger')
print(rest.show_order())
print(rest._name)

