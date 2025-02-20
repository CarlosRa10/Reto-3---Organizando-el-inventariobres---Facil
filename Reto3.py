def organize_inventory(inventory):
    organized = {} # Diccionario vacío para almacenar el inventario organizado
    
    for item in inventory:
        category = item['category']
        name = item['name']
        quantity = item['quantity']
        # Si la categoría no existe en el diccionario, la creamos
        if category not in organized:
            organized[category] = {}
        # Si el nombre del juguete no existe en la categoría, lo inicializamos en 0
        if name not in organized[category]:
            organized[category][name] = 0
        
        organized[category][name] += quantity
    
    return organized

# Ejemplo 1
inventory1 = [
    {'name': 'doll', 'quantity': 5, 'category': 'toys'},
    {'name': 'car', 'quantity': 3, 'category': 'toys'},
    {'name': 'ball', 'quantity': 2, 'category': 'sports'},
    {'name': 'car', 'quantity': 2, 'category': 'toys'},
    {'name': 'racket', 'quantity': 4, 'category': 'sports'}
]

print(organize_inventory(inventory1))
# Resultado esperado:
# {
#   'toys': {'doll': 5, 'car': 5},
#   'sports': {'ball': 2, 'racket': 4}
# }

# Ejemplo 2
inventory2 = [
    {'name': 'book', 'quantity': 10, 'category': 'education'},
    {'name': 'book', 'quantity': 5, 'category': 'education'},
    {'name': 'paint', 'quantity': 3, 'category': 'art'}
]

print(organize_inventory(inventory2))
# Resultado esperado:
# {
#   'education': {'book': 15},
#   'art': {'paint': 3}
# }