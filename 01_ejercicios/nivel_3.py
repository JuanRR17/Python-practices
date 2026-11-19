print("=== NIVEL 3 ===")

# Ejercicio 5: Sistema de pedidos
print("**** EJERCICIO 5: Sistema de pedidos ****")

pedidos = [
    {"id": 101, "cliente": "Empresa A","importe": 1500},
    {"id": 102, "cliente": "Empresa B","importe": 1000},
    {"id": 103, "cliente": "Empresa C","importe": 2500},
    {"id": 104, "cliente": "Empresa D","importe": 2000}
]


def main():
    while True:
        try:
            option = int(input("MENU:\n1. Ver pedidos\n2. Añadir pedido\n3. Buscar pedido\n4. Eliminar pedido\n5. Salir\n"))
            if option in range(1,6):
                print(f"Opción elegida: {option}. ", end="")
            else:
                print("Elige una opción entre 1 y 5.")
        except ValueError:
            print("Elige una opción entre 1 y 5.")
        match option:
            case 1:
                print("Ver pedidos")
                show()
            case 2:
                print("Añadir pedido")
                add_order()
            case 3:
                print("Buscar pedido")
                search_order()
            case 4:
                print("Eliminar pedido")
                delete_order()
            case 5:
                print("Salir")
                print("¡Hasta la próxima!")
                break

# 0. Mostrar un pedido
def show_order(id,client,amount):
    print(f"ID: {id} | Cliente: {client} | Importe: {amount:,.2f}€")

# 1. Ver pedidos
def show():
    print("Lista de pedidos actualizada:")
    for pedido in pedidos:
        # print(f"ID: {pedido["id"]} | Cliente: {pedido["cliente"]} | Importe: {pedido["importe"]:,.2f}€")
        show_order(pedido["id"],pedido["cliente"],pedido["importe"])

# 2. Añadir pedido
def add_order():
    #Initialize new order
    new_order = {"id": 0, "cliente": "", "importe": 0}
    
    #Create id automatically
    orders_reversed_sorted = sorted(pedidos, key=lambda x: x["id"], reverse=True)
    new_id = orders_reversed_sorted[0]["id"] + 1
    new_order["id"] = new_id

    #Add new Client
    new_client = input("Cliente: ")
    new_order["cliente"] = new_client

    while True:
        try:
            new_amount = int(input("Importe: "))
            new_order["importe"] = new_amount
            break
        except ValueError:
            print("Introduce una cantidad en números.")
        
    pedidos.append(new_order)
    show()

# 3. Buscar pedido
def search_order():
    order_id = None
    # Obtener un pedido válido del usuario
    while True:
        try:
            order_id = int(input("Introduce el ID del pedido que quiere ver: "))
            # Buscar el pedido
            valid = False
            for order in pedidos:
                if order["id"] == order_id:
                    valid = True
                    # print(order)
                    show_order(order["id"],order["cliente"],order["importe"])
            if not valid:
                print(f"El pedido con ID {order_id} no existe.")
            else:
                break
        except ValueError:
            print("El pedido introducido no existe. Pruebe otra vez con un número.")


# 4. Eliminar pedido
def delete_order():
    order_id = None
    # Obtener un pedido válido del usuario
    while True:
        try:
            order_id = int(input("Introduce el ID del pedido que quiere eliminar: "))

            # Buscar el pedido
            valid = False
            for order in pedidos:
                if order["id"] == order_id:
                    valid = True
                    pedidos.remove(order)
                    #new_pedidos = [pedido for pedido in pedidos if pedido["id"] != order_id]
                    show()

            if not valid:
                print(f"El pedido con ID {order_id} no existe.")
            else:
                break

        except ValueError:
            print("El pedido introducido no existe. Pruebe otra vez con un número.")

main()