"""
Paquet `gestio_erp` per gestionar clients, comandes i productes en un sistema ERP.

Aquest paquet inclou:
- Gestió de clients: Crear i gestionar clients amb les seves dades i comandes.
- Gestió de comandes: Crear i gestionar comandes amb els seus productes i estats.
- Gestió de productes: Definir i gestionar productes del sistema.
- Gestió d'errors: Classes específiques per gestionar i tractar errors habituals.
"""

from .clients import Client
from .orders import Order
from .products import Product
from .exceptions import (
    ERPException,
    ClientNotFoundException,
    OrderNotFoundException,
    ProductAlreadyExistsException,
    ProductNotFoundException,
)

__all__ = [
    "Client",
    "Order",
    "Product",
    "ERPException",
    "ClientNotFoundException",
    "OrderNotFoundException",
    "ProductAlreadyExistsException",
    "ProductNotFoundException",
]
