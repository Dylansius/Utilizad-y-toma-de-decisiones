# Definir las estrategias de los jugadores
# Variables de decisión de los jugadores
x = 0  # Estrategia del jugador 1
y = 0  # Estrategia del jugador 2

# Funciones de utilidad de los jugadores
utility_player_1 = 2 * x + y
utility_player_2 = x + 2 * y

# Definir las estrategias de los jugadores
strategies_player_1 = [0, 1, 2]  # Estrategias del jugador 1
strategies_player_2 = [0, 1, 2]  # Estrategias del jugador 2

# Matriz de recompensas
# En este ejemplo, utilizamos una matriz de recompensas simple
rewards = [
    [3, 0],
    [1, 2],
    [2, 1]
]

# Encontrar el equilibrio de Nash
equilibrium_found = False
for s1 in strategies_player_1:
    for s2 in strategies_player_2:
        player_1_utility = rewards[s1][1]
        player_2_utility = rewards[s2][0]
        
        if player_1_utility >= rewards[s1][1] and player_2_utility >= rewards[s2][0]:
            equilibrium_found = True
            print("Equilibrio de Nash encontrado:")
            print(f"Jugador 1 elige la estrategia {s1}")
            print(f"Jugador 2 elige la estrategia {s2}")
            break
    if equilibrium_found:
        break

if not equilibrium_found:
    print("No se encontro un equilibrio de Nash en este juego.")
