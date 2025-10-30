from datetime import datetime, timedelta

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}'
    
    def is_adult(self):
        return True if self.age >= 18 else False


class SalesPerson(Person):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.wage = wage
    
    def __str__(self):
        return f'Salesperson: {self.name}\nAge: {self.age}\nWage: {self.wage:.2f}'


class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.orders = []

    def register_order(self, order):
        if isinstance(order.salesperson, SalesPerson):
            self.orders.append(order)
        else:
            self.orders.append(Order(salesperson='Test', date=order.date, amount=order.amount))
    
    def get_last_order_date(self):
        return 'Last order: '+ datetime.strftime(self.orders[len(self.orders)-1].date, "%d/%m/%Y")
        

    def total_orders(self):
        tmp_total_amount = 0
        if self.orders:
            for item in self.orders:
                tmp_total_amount += item.amount

        return f'Total in orders: $ {tmp_total_amount:.2f}'
        

    def __str__(self):
        return f'Customer: {self.name}\nAge: {self.age}'
        


class Order:
    def __init__(self, salesperson, date, amount):
        self.salesperson = salesperson
        self.date = date
        self.amount = amount

    def __str__(self):
        return f'Salesperson: {self.salesperson.name}\nDate: {datetime.strftime(self.date, "%d/%m/%Y")}\nAmount: $ {self.amount:.2f}'   


test = Person('Tales', 33)
customer_a = Customer('Helio', 63)
customer_b = Customer('Cerli', 55)
salesperson_a = SalesPerson('Ray', 19, 1400)
salesperson_b = SalesPerson('Chris', 23, 1400)
order_1 = Order(salesperson_a, datetime.now(), 200)
order_2 = Order(salesperson_b, datetime(2025, 10, 10), 250)
order_3 = Order(customer_b, datetime.now(), 900)
customer_a.register_order(order_1)
customer_a.register_order(order_2)
customer_b.register_order(order_3)
print(customer_a.get_last_order_date())
print(customer_a.total_orders())
print(order_1)
print('')
print(order_2)
print('')
print(order_3)
print('')
print(customer_b.total_orders())
print(customer_b.get_last_order_date())
print((customer_b.orders)[0].salesperson    )


# print(customer_a)
# print('')
# print(salesperson_a)
