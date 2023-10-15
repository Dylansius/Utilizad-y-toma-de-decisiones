from pydecision import InfluenceDiagram, DecisionNode, UtilityNode, ChanceNode

influence_diagram = InfluenceDiagram()

decision = DecisionNode("Tomar sombrilla", ["Si", "No"])
chance = ChanceNode("Lluvia", ["Si", "No"])
utility = UtilityNode("Utilidad")

influence_diagram.add_node(decision)
influence_diagram.add_node(chance)
influence_diagram.add_node(utility)

influence_diagram.add_edge(chance, decision)
influence_diagram.add_edge(decision, utility)
influence_diagram.add_edge(chance, utility)

# Define las probabilidades y utilidades según tu problema.
# influence_diagram.set_probabilities(...)
# influence_diagram.set_utility_function(...)

# Resuelve el problema de decisión
result = influence_diagram.solve()

print("Tomar sombrilla:", result[decision])
print("Utilidad:", result[utility])

