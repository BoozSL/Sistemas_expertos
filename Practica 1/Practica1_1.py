###################################### Representación del mapa de calles como grafo
calles = {
    "Casa": ["Tienda", "Plaza"],
    "Tienda": ["Escuela", "Plaza"],
    "Escuela": ["Parque"],
    "Plaza": ["Parque"],
    "Parque": []
}

##################### Destino a llegar
destino = "Parque"

def dfs(calle, visitados, camino):
    camino.append(calle)
    print(f" Caminando por: {calle}")
    
    if calle == destino:
        print(" ¡Llegué al Parque!")
        print("Ruta encontrada:", " → ".join(camino))
        return True
    
    visitados.add(calle)
    
    for vecino in calles[calle]:
        if vecino not in visitados:
            if dfs(vecino, visitados, camino):
                return True
    
    ################################################# Si no hay salida, backtracking 
    camino.pop()
    return False


########### Inicio 
print(" Buscando una ruta desde Casa hasta Parque.......\n")
encontrado = dfs("Casa", set(), [])

if not encontrado:
    print(" No encontre ruta.")
