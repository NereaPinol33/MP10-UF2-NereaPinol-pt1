from gestio_erp.exceptions import ProductNotFoundException

class Order:
    """
    Representa una comanda en el sistema ERP.

    Atributs:
        - order_id (int): Identificador únic de la comanda.
        - products (dict): Diccionari de productes i les seves quantitats.
        - status (str): Estat de la comanda ("Pendent" o "Enviada").

    Funcionalitats:
        - Afegir productes a la comanda.
        - Modificar la quantitat d'unitats d'un producte.
        - Eliminar productes de la comanda.
        - Modificar l'estat de la comanda.
        - Obtenir un resum de la comanda.
    """
    PENDING = "Pendent"
    SENT = "Enviada"

    def __init__(self, order_id, initial_products=None):
        self.order_id = order_id
        self.products = initial_products if initial_products else {}
        self.status = self.PENDING

    def add_product(self, product, quantity=1):
        """
        Afegeix un producte a la comanda o incrementa la seva quantitat.

        :param product: Nom del producte.
        :param quantity: Quantitat del producte a afegir (per defecte 1).
        """
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def modify_status(self, new_status):
        """
        Modifica l'estat de la comanda.

        :param new_status: Nou estat de la comanda.
        """
        self.status = new_status

    def increase_quantity(self, product, quantity=1):
        """
        Incrementa la quantitat d'un producte existent a la comanda.

        :param product: Nom del producte.
        :param quantity: Quantitat a incrementar (per defecte 1).
        :raises ProductNotFoundException: Si el producte no existeix a la comanda.
        """
        if product in self.products:
            self.products[product] += quantity
        else:
            raise ProductNotFoundException(product)
        
    def remove_product(self, product, quantity=None):
        """
        Elimina un producte de la comanda o redueix-ne la quantitat.

        :param product: Nom del producte.
        :param quantity: Quantitat a eliminar. Si no es proporciona, s'elimina el producte completament.
        """
        if product in self.products:
            if quantity is None or self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity

    def summary(self):
        """
        Retorna un resum de la comanda.

        :return: Una cadena amb el resum de la comanda.
        """
        product_details = ", ".join(
            f"{product}: {quantity}" for product, quantity in self.products.items()
        )
        return f"Comanda {self.order_id} [{self.status}]: {product_details or 'Cap producte'}"

    def __str__(self):
        return self.summary()
