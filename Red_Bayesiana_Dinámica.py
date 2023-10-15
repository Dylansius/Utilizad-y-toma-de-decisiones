import random

# Definición de un DBN simple
# Estados: {Lluvia (0, 1), Tráfico (0, 1), Paraguas (0, 1)}

# Probabilidades de transición estado a estado
P_rain = [[0.8, 0.2], [0.3, 0.7]]
P_traffic = [[1, 0], [0.3, 0.7]]
P_umbrella = [[0.7, 0.3], [0.1, 0.9]]

# Función para simular una transición de estado
def transition(state, P):
    return random.choices([0, 1], P[state])

# Ejemplo de inferencia en el DBN
evidence = {'Rain_t0': 1, 'Traffic_t0': 1}  # Lluvia y Tráfico en el tiempo t0
query_variable = 'Rain_t1'  # Lluvia en el tiempo t1

# Realiza la inferencia mediante muestreo
num_samples = 10000
count = 0
for _ in range(num_samples):
    rain_t0 = evidence['Rain_t0']
    traffic_t0 = evidence['Traffic_t0']
    umbrella_t0 = transition(rain_t0, P_umbrella)
    
    rain_t1 = transition(rain_t0, P_rain)
    
    if rain_t1 == 1:
        count += 1

probability = count / num_samples
print("Probabilidad de lluvia en el siguiente paso de tiempo:", probability)
