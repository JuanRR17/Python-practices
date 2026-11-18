# Ejercicio 1: Inventario de herramientas
print("**** EJERCICIO 1: Inventario de herramientas ****")
herramientas = [
    {"nombre": "Taladro", "stock":5},
    {"nombre": "Martillo", "stock": 12},
    {"nombre": "Destornillador", "stock": 2}
]

print("Mostrar todas las herramientas:")
def all_tools(tools):
    for tool in tools:
        print("Tool:",tool["nombre"])

all_tools(herramientas)
print(" ")

print("Buscar una herramienta por nombre:")
def tool(tools, tool_name):
    not_found = True
    tool_found = None
    for tool in tools:
        if tool["nombre"] == tool_name:
            not_found = False
            tool_found = tool["nombre"]
    if not_found:
        print("Tool Not Found")
    else: 
        print("Tool Found:", tool_found)

tool(herramientas, "Martillo")
print(" ")

print("Listar herramientas con stock inferior a 5:") 
def minus_5_stock(tools):
    #fewer_tools = []
    for tool in tools:
        if tool["stock"] < 5:
            #fewer_tools.append(tool)
            print(tool["nombre"])
    
minus_5_stock(herramientas)
print(" ")

print("Calcular el stock total:")
def total_stock(tools):
    stock = 0
    for tool in tools:
        stock += tool["stock"]
    print(stock)

total_stock(herramientas)
print(" ")

print("**** EJERCICIO 2: Gestión de empleados ****")
empleados = [
    {"nombre": "Juan", "departamento": "CAD", "salario": 32000},
    {"nombre": "Ana", "departamento": "Calidad", "salario": 35000},
    {"nombre": "Luis", "departamento": "CAD", "salario": 30000}
]

print("Calcular salario medio:")
def average_salary(employees):
    salaries = 0    
    for employee in employees:
        salaries += employee["salario"]
    return salaries / len(employees)

print(f"{average_salary(empleados):.2}")
print(" ")

print("Encontrar el empleado con salario más alto:") 
def best_payed_employee(employees):
    ordered = sorted(employees, key = lambda x: x["salario"])

    return ordered[-1]["nombre"]

print(best_payed_employee(empleados))

#Mostrar todos los empleados de un departamento.
#Contar empleados por departamento.