class Client:
    """
    Representa un client del sistema ERP.

    Atributs:
        - client_id (int): Identificador únic del client.
        - name (str): Nom del client.
        - email (str): Correu electrònic del client.
        - orders (list): Llista de comandes associades al client.

    Funcionalitats:
        - Afegir noves comandes al client.
        - Consultar el llistat de comandes associades al client.
    """
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        """
        Afegeix una nova comanda al client.

        :param order: Objecte Order a afegir.
        """
        self.orders.append(order)

    def list_orders(self):
        """
        Retorna una llista de les comandes associades al client.
        """
        return self.orders

    def __str__(self):
        return f"Client({self.client_id}, {self.name}, {self.email})"
