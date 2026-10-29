class Inventory:
    """Responsibility: manage a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a product. Returns False if the ID already exists."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the matching Product, or None if not found."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()

    def get_products(self):
        """Return a copy of the product list so callers can't alter ours."""
        return list(self.__products)
