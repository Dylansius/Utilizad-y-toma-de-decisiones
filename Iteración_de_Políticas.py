import random

# Define tu MDP (Proceso de Decisi�n de Markov) con estados, acciones, recompensas y probabilidades de transici�n
# En este ejemplo, usaremos un MDP simple con 2 estados y 2 acciones.

# Estados
states = ["State1", "State2"]

# Acciones
actions = ["Action1", "Action2"]

# Recompensas (diccionario de diccionarios R[state][action])
rewards = {
    "State1": {"Action1": -1, "Action2": 2},
    "State2": {"Action1": 1, "Action2": -1}
}

# Probabilidades de transici�n (diccionario de diccionarios T[state][action][next_state])
# Cada celda contiene la probabilidad de transici�n desde un estado al siguiente dado una acci�n.
transitions = {
    "State1": {
        "Action1": {"State1": 0.2, "State2": 0.8},
        "Action2": {"State1": 0.4, "State2": 0.6}
    },
    "State2": {
        "Action1": {"State1": 0.7, "State2": 0.3},
        "Action2": {"State1": 0.1, "State2": 0.9}
    }
}

# Descuento
discount_factor = 0.9

# Inicializa la pol�tica de manera aleatoria (cada acci�n es igualmente probable)
policy = {}
for state in states:
    policy[state] = random.choice(actions)

# Realiza la iteraci�n de pol�ticas
num_iterations = 1000  # N�mero m�ximo de iteraciones
for _ in range(num_iterations):
    delta = 0  # Delta para verificar la convergencia de la pol�tica
    for state in states:
        old_action = policy[state]
        action_values = {}
        for action in actions:
            action_value = 0
            for next_state in states:
                action_value += transitions[state][action][next_state] * (rewards[state][action] + discount_factor * delta)
            action_values[action] = action_value
        policy[state] = max(action_values, key=action_values.get)
        delta = max(delta, abs(rewards[state][old_action] + discount_factor * delta - rewards[state][policy[state]]))

# Imprime la pol�tica �ptima
for state in states:
    print(f"Politica optima en {state}: {policy[state]}")
