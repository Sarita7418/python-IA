# Definición de los países y sus adyacencias
paises = {
    'Argentina': ['Bolivia', 'Chile', 'Paraguay', 'Brasil', 'Uruguay'],
    'Bolivia': ['Argentina', 'Chile', 'Paraguay', 'Brasil', 'Perú'],
    'Brasil': ['Argentina', 'Bolivia', 'Perú', 'Guyana', 'Surinam', 'Venezuela'],
    'Chile': ['Argentina', 'Bolivia'],
    'Colombia': ['Venezuela', 'Perú', 'Ecuador'],
    'Ecuador': ['Colombia', 'Perú'],
    'Guyana': ['Brasil', 'Surinam'],
    'Paraguay': ['Argentina', 'Bolivia', 'Brasil'],
    'Perú': ['Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador'],
    'Surinam': ['Brasil', 'Guyana'],
    'Uruguay': ['Argentina'],
    'Venezuela': ['Colombia', 'Brasil'],
    'Guayana Francesa': ['Brasil', 'Surinam']
}

# Colores disponibles
colores = ['Rojo', 'Verde', 'Morado', 'Amarillo']

# Función para verificar si se puede asignar un color
def es_valido(pais, color, asignacion):
    for vecino in paises[pais]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Heurística de mínimos valores restantes
def mvr(paises, asignacion):
   
    no_asignados = {}
    
    for pais in paises:
        if pais not in asignacion: 
            no_asignados[pais] = len(paises[pais]) 
    
    pais_con_menos_colores = None
    menor_valor = 9999999  
    
    for pais in no_asignados:  
        cantidad = no_asignados[pais]  
        if cantidad < menor_valor: 
            menor_valor = cantidad
            pais_con_menos_colores = pais  
    
    return pais_con_menos_colores  


# Función para colorear el mapa
def colorear_mapa(paises, colores, asignacion=None):
    
    if asignacion is None:
        asignacion = {}
    
    if len(asignacion) == len(paises):
        return asignacion  
    
    pais = mvr(paises, asignacion)
    
    for color in colores:
        
        if es_valido(pais, color, asignacion):
            asignacion[pais] = color  
            
            
            resultado = colorear_mapa(paises, colores, asignacion)
            if resultado: 
                return resultado  
            
            del asignacion[pais]
    
    return None  


# Ejecución del algoritmo
asignacion_colores = colorear_mapa(paises, colores)

# Impresión de la asignación de colores en el formato deseado
for pais in asignacion_colores:
    color = asignacion_colores[pais]
    print(pais + ": " + color)

