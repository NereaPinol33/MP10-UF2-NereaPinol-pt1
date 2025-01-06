from gestio_erp.clients import Client
from gestio_erp.orders import Order
from gestio_erp.products import Product
from gestio_erp.exceptions import ProductAlreadyExistsException

# Funció per crear productes
def create_products():
    return {
        "bicicleta": Product("bicicleta"),
        "casc": Product("casc"),
        "guants": Product("guants"),
        "maillot": Product("maillot"),
        "roda": Product("roda"),
        "pantalons": Product("pantalons")
    }

# Funció per crear clients
def create_clients():
    return {
        "anna": Client(1, "Anna", "anna@example.com"),
        "pere": Client(2, "Pere", "pere@example.com"),
        "joan": Client(3, "Joan", "joan@example.com")
    }

# Funció per crear comandes
def create_orders_for_client(client, products):
    order_1 = Order(101)
    order_1.add_product(products["bicicleta"], 1)
    order_1.add_product(products["casc"], 2)

    order_2 = Order(102)
    order_2.add_product(products["guants"], 1)

    client.add_order(order_1)
    client.add_order(order_2)

def create_orders_for_pere(client, products):
    order_3 = Order(103)
    order_3.add_product(products["maillot"], 1)
    order_3.add_product(products["roda"], 2)

    order_4 = Order(104)
    order_4.add_product(products["guants"], 2)

    client.add_order(order_3)
    client.add_order(order_4)

# Funció per mostrar les comandes dels clients
def print_orders_for_clients(clients):
    print("COMANDES DELS CLIENTS:")
    for client in clients.values():
        print(f"\nComandes del client {client.name}: {len(client.list_orders())}")
        for order in client.list_orders():
            print(order.summary())
        if not client.list_orders():
            print("El client no té cap comanda.")

# Funció per provar els errors de productes
def test_product_errors(order, product, quantity):
    try:
        order.add_product(product, quantity)
    except ProductAlreadyExistsException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"El producte {product} no existeix a la comanda.")

# Funció per modificar les comandes
def modify_orders(order, products):
    order.add_product(products["casc"], 2)
    order.add_product(products["pantalons"], 1)
    order.modify_status(Order.SENT)

def main():
    # Crear productes i clients
    products = create_products()
    clients = create_clients()

    # Crear comandes per a Anna i Pere
    create_orders_for_client(clients["anna"], products)
    create_orders_for_pere(clients["pere"], products)

    # Mostrar informació inicial
    print_orders_for_clients(clients)

    # Provar errors amb productes
    test_product_errors(clients["anna"].list_orders()[0], products["bicicleta"], 1)  # Producte ja existent
    test_product_errors(clients["anna"].list_orders()[0], products["guants"], 1)  # Producte inexistent

    # Modificar estat i productes de les comandes d'Anna
    modify_orders(clients["anna"].list_orders()[0], products)

    # Mostrar informació actualitzada de les comandes
    print("\nCOMANDES DELS CLIENTS (ACTUALITZADES):")
    print_orders_for_clients(clients)

# Per executar el main
if __name__ == "__main__":
    main()
