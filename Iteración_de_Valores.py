class Node:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        self.value = 0
        self.prev_value = 0

# Define tus nodos de decisión y utilidad
decision_A = Node("Decision A", [0, 1, 2])
decision_B = Node("Decision B", [0, 1])
utility_C = Node("Utility C", [3, 4, 5])

# Define las probabilidades asociadas a las decisiones
probabilities_A = [0.2, 0.4, 0.4]
probabilities_B = [0.7, 0.3]

# Configura las conexiones entre los nodos
decision_A.children = [utility_C]
decision_B.children = [utility_C]

# Define el epsilon para la convergencia
epsilon = 0.01

# Implementa la iteración de valores
while True:
    max_change = 0
    for decision in [decision_A, decision_B]:
        for i in range(len(decision.values)):
            expected_utility = 0
            for j in range(len(decision_A.values)):
                for k in range(len(decision_B.values)):
                    expected_utility += probabilities_A[j] * probabilities_B[k] * utility_C.value
            new_value = decision.values[i] + expected_utility
            change = abs(new_value - decision.value)
            decision.prev_value = decision.value  # Guarda el valor anterior
            decision.value = new_value
            if change > max_change:
                max_change = change

    if max_change < epsilon:
        break

# Imprime los resultados
print("Optimal Decision A:", decision_A.value)
print("Optimal Decision B:", decision_B.value)
