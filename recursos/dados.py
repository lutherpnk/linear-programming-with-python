import numpy as np


# Dados
num_empresas = 12
num_ofertantes = 9

# Custo da matriz
custo_matriz = np.array([[8, 32, 29, 25, 10, 12, 19, 10, 0],
                        [28, 35, 20, 30, 9, 30, 26, 18, 0],
                        [14, 22, 25, 24, 24, 9, 9, 25, 0],
                        [30, 15, 12, 18, 29, 9, 27, 21, 0],
                        [13, 13, 11, 31, 25, 13, 24, 23, 0],
                        [29, 10, 32, 9, 33, 22, 33, 19, 0],
                        [31, 13, 16, 8, 21, 34, 35, 26, 0],
                        [16, 22, 21, 23, 11, 19, 23, 19, 0],
                        [18, 10, 28, 31, 14, 11, 9, 27, 0],
                        [19, 26, 12, 27, 26, 27, 26, 33, 0],
                        [22, 23, 12, 12, 34, 16, 33, 27, 0],
                        [29, 20, 22, 10, 10, 19, 21, 34, 0]])

# Custo de Demanda e Oferta
custo_demanda = np.array([3280, 1650, 3830, 6180, 6600, 5990, 4510, 6410, 3680, 6390, 5560, 5410])
custo_oferta = np.array([8100, 7500, 6300, 5100, 7200, 7000, 9700, 6300, 2290])