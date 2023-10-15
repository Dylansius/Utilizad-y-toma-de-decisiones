import random

# Definición de un POMDP simple para el Problema del Ladrón
# Estados: {Afuera, Adentro}
# Acciones: {Esconderse, Robar}
# Observaciones: {Nada, Ruido}

# Probabilidades de transición estado a estado
P = [[0.8, 0.2], [0.3, 0.7]]

# Modelo de observación (probabilidades de observación dado el estado y la acción)
O = [[[0.1, 0.9], [0.8, 0.2]], [[0.6, 0.4], [0.1, 0.9]]]

# Recompensas (recompensa por estado y acción)
R = [[-5, -1], [-50, 10]]

# Horizonte de tiempo
T = 10

# Estado inicial
initial_state = 0  # Afuera

# Simulación del POMDP
state = initial_state
for t in range(T):
    print(f"Tiempo {t}:")
    print("Estado actual:", "Afuera" if state == 0 else "Adentro")

    # Selección de acción (política ingenua)
    action = max((R[state][a], a) for a in range(2))[1]
    print("Accion seleccionada:", "Esconderse" if action == 0 else "Robar")

    # Observación
    observation_probabilities = O[state][action]
    observation = random.choices([0, 1], observation_probabilities)[0]
    print("Observacion:", "Nada" if observation == 0 else "Ruido")

    # Transición de estado
    state_probabilities = P[state]
    state = random.choices([0, 1], state_probabilities)[0]
    print("Nuevo estado:", "Afuera" if state == 0 else "Adentro")
    print()

print("Simulacion completada.")
