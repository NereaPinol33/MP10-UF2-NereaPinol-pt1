class ERPException(Exception):
    """
    Classe base per a les excepcions del sistema ERP.
    """
    pass


class ClientNotFoundException(ERPException):
    """
    Error llançat quan un client no es troba.
    """
    def __init__(self, client_id):
        super().__init__(f"El client amb ID {client_id} no existeix.")


class OrderNotFoundException(ERPException):
    """
    Error llançat quan una comanda no es troba.
    """
    def __init__(self, order_id):
        super().__init__(f"La comanda amb ID {order_id} no existeix.")


class ProductAlreadyExistsException(ERPException):
    """
    Error llançat quan un producte ja està a una comanda.
    """
    def __init__(self, product_name):
        super().__init__(f"El producte {product_name} ja existeix a la comanda.")


class ProductNotFoundException(ERPException):
    """
    Error llançat quan un producte no es troba a una comanda.
    """
    def __init__(self, product_name):
        super().__init__(f"El producte {product_name} no existeix a la comanda.")
