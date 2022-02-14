from pulp import *
from recursos.dados import num_empresas, num_ofertantes, custo_matriz, custo_demanda, custo_oferta
from recursos.utilidades import converter_lista, coletar_custo, obter_indice_x_custo, obter_resultado_por_variavel,obter_produto_do_custo, obter_resultado_por_empresa, tratamento_resultado_final
from time import sleep
import numpy as np


def analise_dos_dados():    
    print('[>] Resolução do estudo de caso: Distribuição de Energia Elétrica.')
    sleep(2)

    # Iniciando o modelo da biblioteca PulP
    modelo = LpProblem("Distribuição-de-Energia-Elétrica", LpMinimize)
    print('[>] Criando modelo através dos dados em "recursos/dados.py".')
    sleep(2)

    # Identificando a localização dos valores na matriz
    print('[>] Identificando a localização dos valores na matriz.')
    sleep(2)
    converter_indice_custo = [str(i)+str(j) for j in range(1, num_ofertantes + 1) for i in range(1, num_empresas + 1)]
    lista_indice_tratada = converter_lista(converter_indice_custo)
    variaveis_dos_indices = LpVariable.matrix("X", lista_indice_tratada, cat="Integer", lowBound=0)
    localizacoes_dos_indices_tratado = np.array(variaveis_dos_indices).reshape(12,9)
    objetos_do_modelo = lpSum(localizacoes_dos_indices_tratado * custo_matriz)
    modelo +=  objetos_do_modelo

    # Custo da demanda e da oferta - Restrições
    print('[>] Obtendo custo da demanda e da oferta (Restrições).')
    sleep(2)
    for i in range(num_empresas):
        modelo += lpSum(localizacoes_dos_indices_tratado[i][j] for j in range(num_ofertantes)) <= custo_demanda[i] , "Custo da demanda" + str(i)
    for j in range(num_ofertantes):
        modelo += lpSum(localizacoes_dos_indices_tratado[i][j] for i in range(num_empresas)) >= custo_oferta[j] , "Custo da oferta " + str(j)

    # Resolvendo o problema
    print('[>] Todos os dados estão prontos.')
    sleep(1)
    print('[>] Resolvendo o caso.')
    modelo.solve()
    sleep(2)
    # Obtendo resultados
    print('[>] Obtendo resultados.')
    sleep(2)
    lista_custo = coletar_custo(custo_matriz)
    custo_e_indice = obter_indice_x_custo(lista_custo, variaveis_dos_indices)

    # Resultados
    resultado_por_variavel = obter_resultado_por_variavel(modelo.variables(), variaveis_dos_indices)
    resultado_do_produto = obter_produto_do_custo(resultado_por_variavel, custo_e_indice)
    resultado_por_empresa = obter_resultado_por_empresa(num_empresas, localizacoes_dos_indices_tratado, num_ofertantes)
    resultado_final = {'Resultado Final': {
        'Custo Total': modelo.objective.value(),
        'Resultado por variável': resultado_por_variavel,
        'Resultado por variável multiplicado': resultado_do_produto,
        'Resultado por empresa': resultado_por_empresa
    }}
    tratamento_resultado_final(resultado_final)
    print('[>] Resultados obtidos. Gerando arquivo CSV.')
    sleep(1.5)
    print('[>] "Resultado Final.csv" gerado com sucesso! Você poderá localizá-lo na pasta raiz do script.')
    sleep(1)
    print('[>] Obrigado!')
    sleep(1.5)


if __name__ == '__main__':
    analise_dos_dados()
