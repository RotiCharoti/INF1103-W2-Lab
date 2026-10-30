from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        if download_size < 0:
            raise ValueError("Download size cannot be less than 0.")

        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        return (
            f"{super().display_information()} | "
            f"Download Size: {self._download_size:.2f} MB"
        )

    def get_fulfilment_info(self):
        return "This product will be delivered digitally."
