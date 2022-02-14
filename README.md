# Linear Programming - IFSEMG

## Solução de estudo de caso de distribuição de energia elétrica

"Uma Companhia de Distribuição de Energia (CDE) compra energia em leilões e a revende para empresas que contratam
seus serviços. A revenda garante aos compradores preços mais acessíveis, mas não garante que toda a demanda seja
atendida, uma vez que as ofertas de energia nos leilões são sazonais. Nesse caso, quando uma demanda do consumidor
de energia não é atendida, não há pagamento de multa, pois o consumidor irá usar a energia oferecida pelas operadoras
de energia elétrica.
Mensalmente a CDE recebe as demandas de seus clientes e adquire os pacotes de energia de acordo com as
disponibilidades de energia nos leilões. Nos leilões de energia, diversos fornecedores ofertam pacotes de energia e as
disputas entre compradores são acirradas. Assim, a CDE concorre pela energia e busca comprar energia para atender
suas demandas, no entanto, nem sempre isso pode ser garantido.
A partir da energia elétrica que terá para ofertar, a CDE organiza a logística de distribuição de energia, alugando as redes
de distribuição das operadoras de energia elétrica.
Sempre que a energia comprada não pode atender toda a demanda, cabe a CDE decidir que empresas serão
contempladas e que empresas não serão atendidas. Essa decisão é tomada com base nos custos de logística da
distribuição relacionado ao aluguel das redes de distribuição das operadoras de energia elétrica.
Para a gestão logística, a empresa realiza uma tomada de preço entre as operadoras de energia elétrica e com base
nessas informações, na oferta e na demanda de energia, ela decidirá como será realizada a distribuição da energia
contratada. Essa decisão deve ser tomada mensalmente, a cada nova contratação de serviços.
Para facilitar a tomada de decisão, a empresa deseja elaborar um programa que a auxilie na tomada de decisões,
decidindo quais as melhores estratégias de distribuição, de forma a minimizar os custos de logística, decidindo, também,
quais demandas deixarão de ser atendidas."

É possível obter a solução do caso utilizando de programação linear. A Programação Linear é basicamente um subconjunto da otimização. Programação linear ou otimização linear é uma técnica de otimização em que tentamos encontrar um valor ótimo para uma função objetivo linear para um sistema de restrições lineares usando um conjunto variável de variáveis de decisão.

O script faz uso da biblioteca PulP, conhecida por facilitar a solução de casos de otimização, que facilita a modelagem dos dados e retorna a solução do caso em funções simples.

Além de resolver o problema da Companhia de Distribuição de Energia, o script realiza a saída dos dados em uma planilha em formato CSV. Facilitando o usuário a visualização e manipulação dos dados já tratados pelo script.

## Instalação

Para fazer uso do script, é necessário instalar as bibliotecas usadas no desenvolvimento. Basta digitar no seu terminal:

`pip install -r requirements.txt`

Logo após a instalação das bibliotecas, execute o arquivo main.py.

## Electric power distribution case study solution

"A Energy Distribution Company (CDE) buys at auctions and resells it to companies that hire its services. In this case, when an energy supply is not met, there is no payment for energy, as the consumer uses the fine that the energy consumer receives. Thus, CDE competes for energy and seeks to meet its needs, when buying. , not always can be guaranteed. Based on the electric energy that it will have to offer, CDE organizes the energy distribution logistics, renting it as distribution networks from electric energy operators. Whenever the energy purchased cannot meet a demand, it is up to CDE decides which companies will be covered and which companies will not be served. This decision is made based on the distribution logistics costs related to the leasing of the operators' distribution networks those of electrical energy. For management, the company carries out a price assessment between the electric operators and based on them, on the supply and demand of energy information, it will decide how the distribution of energy will be carried out. This decision must be made monthly, with each new service contract. To facilitate decision-making, the company wants to develop a program to assist in decision-making, deciding on the best distribution strategies, in which ways to minimize logistics costs, also deciding on the demands to be met."

It's possible to obtain the solution of the case using linear programming. Linear Programming is basically a subset of optimization. Linear technical programming or linear optimization, is an optimization where we try to find a linear optimal value for an objectified linear function system for a set of linear functions we try to find a variable of decision variables.

The script makes use of the PulP library, known for facilitating the solution of optimization cases, which facilitates data modeling and returns the case solution in simple functions.

In addition to solving the problem of the Energy Distribution Company, the script outputs the data in a spreadsheet in CSV format. Facilitating the user to visualize and manipulate the data already treated by the script

## Installation

To make use of the script, it is necessary to install the libraries used in development. Just type in your terminal:

`pip install -r requirements.txt`

Right after installing the libraries, run the main.py file.

