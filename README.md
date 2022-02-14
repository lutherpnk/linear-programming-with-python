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
