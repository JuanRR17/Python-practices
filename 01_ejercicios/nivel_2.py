print("=== NIVEL 2 ===")

# Ejercicio 3: Registro de incidencias
print("**** EJERCICIO 3: Registro de incidencias ****")

proyectos = [
    {"codigo": "PR001", "horas": 120, "estado": "abierto"},
    {"codigo": "PR002", "horas": 80, "estado": "cerrado"},
    {"codigo": "PR003", "horas": 150, "estado": "abierto"}
]

print("Obtener proyectos abiertos:")
def open_proj(projects):
    open = []
    for proj in projects:
        if proj["estado"] == "abierto":
            open.append(proj["codigo"])
    return open

print(open_proj(proyectos))
print(" ")

print("Sumar horas totales:")
def total_hours(projects):
    total = 0
    for proj in projects:
        total += proj["horas"]
    return total

print(total_hours(proyectos))
print(" ")

print("Encontrar proyecto con más horas:")
def biggest_proj(projects):
    hours = []
    for proj in projects:
        hours.append(proj["horas"])
    hours.reverse()

    return hours[0]

print(biggest_proj(proyectos))
print(" ")

print("Cambiar el estado de un proyecto:")
def change_status(project, projects):
    for proj in projects:
        if proj["codigo"] == project:
            if proj["estado"] == "abierto":
                proj["estado"] = "cerrado"
            elif proj["estado"] == "cerrado":
                proj["estado"] = "abierto"
            return proj

print(change_status("PR001", proyectos))
print(change_status("PR002", proyectos))
print(change_status("PR003", proyectos))

# Ejercicio 4: Registro de incidencias
print("**** EJERCICIO 4: Registro de incidencias ****")
incidencias = [
    {"id": 1, "prioridad": "alta", "resuelta": False},
    {"id": 2, "prioridad": "baja", "resuelta": True},
    {"id": 3, "prioridad": "media", "resuelta": False},
    {"id": 4, "prioridad": "baja", "resuelta": True}
]

print("Contar incidencias abiertas:")
def count_open(incidents):
    count = 0
    for inc in incidents:
        if not inc["resuelta"]:
            count += 1
    return count

print(count_open(incidencias))

print("Contar incidencias por prioridad:") 
def count_by_priority(incidents):
    #Create list of priorities
    priors = []
    for inc in incidents:
        if inc["prioridad"] not in priors:
            priors.append(inc["prioridad"])
    #Create dictionary of count by priority
    prior_count = {}
    for inc in incidents:
        #prior = {alta}
        prior = inc["prioridad"]
        if prior not in prior_count:
            prior_count[prior] = 1
        else:
            prior_count[prior] += 1
    return prior_count

print(count_by_priority(incidencias))

print("Resolver una incidencia buscando por ID:") 