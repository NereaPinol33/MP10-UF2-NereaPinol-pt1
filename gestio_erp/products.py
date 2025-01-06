class Product:
    """
    Representa un producte en el sistema ERP.

    Atributs:
        - name (str): Nom del producte.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
