from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        if weight < 0:
            raise ValueError("Product weight cannot be less than 0.")

        super().__init__(product_id, name, price, stock)
        self._weight = weight

    def get_weight(self):
        return self._weight

    def display_information(self):
        return (
            f"{super().display_information()} | "
            f"Weight: {self._weight:.2f} kg"
        )

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self._weight * 2.00
