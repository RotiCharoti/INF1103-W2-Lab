class Product:
    def __init__(self, product_id, name, price, stock):
        if price < 0:
            raise ValueError("Product price cannot be less than 0.")
        if stock < 0:
            raise ValueError("Stock quantity cannot be less than 0.")
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Update stock quantity 
    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock quantity cannot be less than 0.")
        self.__stock = quantity

    # Display information of the product 
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
