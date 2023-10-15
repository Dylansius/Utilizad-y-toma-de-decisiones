import random

# Definición de un MDP simple
# Estados: S1, S2, S3
# Acciones: A, B
# Recompensas: Tabla de recompensas (state, action, next_state)
# Probabilidades de transición: Tabla de probabilidades (state, action, next_state)

# Definición de estados, acciones, recompensas y probabilidades de transición
states = ["S1", "S2", "S3"]
actions = ["A", "B"]
rewards = {
    ("S1", "A", "S1"): 0,
    ("S1", "A", "S2"): 5,
    ("S1", "B", "S1"): 2,
    ("S2", "A", "S1"): 1,
    ("S2", "A", "S2"): 0,
    ("S2", "B", "S2"): 4,
    ("S3", "A", "S3"): 10,
    ("S3", "B", "S3"): -1,
}
transitions = {
    ("S1", "A"): {"S1": 0.8, "S2": 0.2},
    ("S1", "B"): {"S1": 0.4, "S2": 0.6},
    ("S2", "A"): {"S1": 0.3, "S2": 0.7},
    ("S2", "B"): {"S2": 1.0},
    ("S3", "A"): {"S3": 0.9, "S1": 0.1},
    ("S3", "B"): {"S3": 0.5, "S2": 0.5},
}

# Inicialización de valores
V = {state: 0 for state in states}
gamma = 0.9  # Factor de descuento

# Iteración de valor
num_iterations = 100
for _ in range(num_iterations):
    new_V = V.copy()
    for state in states:
        max_value = float("-inf")
        for action in actions:
            action_value = sum(
                transitions.get((state, action), {}).get(next_state, 0) * (
                    rewards.get((state, action, next_state), 0) + gamma * V.get(next_state, 0)
                )
                for next_state in states
            )
            max_value = max(max_value, action_value)
        new_V[state] = max_value
    V = new_V

# Resultados finales
print("Valores de estado optimos:")
for state, value in V.items():
    print(f"{state}: {value}")
