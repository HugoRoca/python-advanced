from typing import List, NoReturn, Optional
from models import Product, BaseProduct


class Cart(object):
    products: List[Product] = []
    id_maker: int = 1

    def add_to_cart(self, product: BaseProduct) -> NoReturn:
        new_product = Product(id=self.id_maker, **product.dict())
        self.products.append(new_product)
        self.id_maker += 1

    def get_cart(self, id: Optional[int] = None):
        if id:
            for product in self.products:
                if id == product.id:
                    return product

        return self.products

    def edit_cart(self, old_product: Product, new_product: BaseProduct) -> NoReturn:
        position = self.products.index(old_product)
        self.products[position] = old_product.copy(update=new_product.dict())

    def delete_product(self, product: Product) -> NoReturn:
        self.products.remove(product)