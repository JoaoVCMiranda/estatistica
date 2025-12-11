#estatistica 
# Estatística Descritiva

É a linguagem que se fala em estatística, inclusive para a população

Nesse capítulo não é relevante se está sendo falado da amostra ou da população

> Dispondo dos dados, organizaremos os resultados.

É  preciso ter as características que gostaríamos de analisar bem definidas

## Variáveis 
Tratando apenas de variáveis de interesse unidimensionais
## Qualitativas
São classificadas,  por exemplo:

Escolha um conjunto de coisas e e mapeie-as para categorias com base em critérios

De todos os moradores de um bairro(==população==) qual o tipo de moradia (==variável==) ? Apartamento, Casa, Kitnet,... 

## Quantitativas
Numéricas, praticamente iguais...
### Discretas
De todos os moradores de um bairro(==população==) qual a idade *(em anos inteiros)* dos moradores (==variável==) ? 
(Valores geralmente por contagem)
### Contínuas
De todos os moradores de um bairro(==população==) qual a idade dos moradores (==variável==) ? 
(Valores geralmente por medição*)
#### Amplitude de classe
É a largura da barra, se não estiver explicitada é a precisão dos valores dados
> precisão: metade da menor divisão

(caso a amplitude seja definida à parte podemos ter valores *diferentes* que entram na mesma classe) 
$$k = \frac{max(dados) - min(dados)}{h}$$
(onde $k\in \mathbb{Z}$ é o número de classes)
(OBS: esse é um assunto controverso, cada autor falar de um jeito)

Portanto, só agrupar se for necessário e/ou conveniente.
## Descrição Gráfica 
Uso de tabelas, diagramas e etc para apresentação dos dados

### Frequência
É a contagem de quantas ocorrências temos do mesmo valor em todas as  [[#Variáveis]]
Por definição
$$
\sum_{i=1}^{k}f_i=n
$$
Onde $f_i$ é a frequência que o valor associado com a posição $i$
Ex.
Plantas (Uva, Manga, Abacaxi) -> Uva=1, Manga=2, Abacaxi=3

Não faz muito sentido ter frequência para variáveis contínuas, sem considerar um intervalo.

## Diagrama de barras
Colocam-se os valores das variáveis no eixo x e as frequências no eixo y
![](media/Pasted%20image%2020251208202038.png)

## Polígono de frequências
Semelhante ao diagrama de barras, mas faz linhas unindo os valores médios
Obs: os valores médios não estão alinhados como deveriam na imagem 
![](media/Pasted%20image%2020251208202201.png)

### Agrupamento
Para fazer o polígono, as vezes é interessante agrupar os valores, existem os limites aparentes, que são os números de fato que são tratados(valor médio) e temos os limites reais que são utilizados para categorizar os dados($\pm\frac{h}{2}$ )


> Curiosidade: Puericultura é o cuidado das crianças e adolescentes de 0 a 19 anos em postos de saúde.


O agrupamento é muito importante ao tratar com dados contínuos, pode ser útil inclusive fazer uma função agrupe dados contínuos em dados discretos para usar as mesmas funções feitas antes...

## Características Numéricas
> medidas de distribuição das frequências

### Média aritimética

$$
\bar x = \frac{\sum_{i=0}^{n}x_i}{n}
$$

> Em analogia com a física, seria o centro de massa do objeto


### Mediana

É o ponto médio da distribuição

> Pode ser calculada tanto com os dados brutos como com a distribuição de frequências

É usada em geral de forma obrigatória nos casos que as distribuições tem valores nos extremos dados por "menor que" e "maior que"

Além disso, pode ser interpretada como o ponto que divide o histograma em duas áreas iguais.

*Generalização: Quartis e fractis*(frações como quartis)


### Moda ($m_o$) 

Pode ser uma só ou várias para um conjunto de dados, para os valores que mais aparecem...

Para o caso de uma discretização, podemos ter *classe modal* que é a classe que mais aparece,
E supondo uma distribuição uniforme, podemos demonstrar a segunite equação

$$
m_0 = L_i + \frac{d_1}{d_1+d_2}h
$$

Para uma mesma amplitude h em todos as classes e sendo d as distâncias entre as classes adjacente e subjacente

---
Há uma relação empírica entre essas 3 medidas na maioria dos casos...
Diz assim
$$
\bar x - m_o = 3(\bar x - md)
$$

### Medidas de dispersão

#### Amplitude
é a diferença entre o máximo e o mínimo dos dados

#### Variância(s²)

Não confundir com "desvio padrão"

$$
S^2(X) = S^2_X = \frac{\sum{(x_i - \bar x)^2}}{n-1}
$$

Note que só há variância quando temos pelo menos 2 dados

Essa é uma variância de amostra, pois perde um grau de liberdade dos dados.(vira $n-1$)
Caso fosse a variância da população, ==DIVIDIR POR n ao invés de n-1==

Tem um cara o Sheppard que fez umas corresções sobre isso, mas quando for amostra comum, usar n-1

Outras formas de calcular a variancia...

$$
S^2_X = \sum{x_i^2} - \frac{(\sum{x_i})^2}{n} = \sum{x_i^2} - n(\bar x^2)
$$

#### Coeficiente de variação
Ninguém usa ?
Mas ele faz sentido!

É a razão entre o desvio e a média, quando menor, mais preciso

E isso está relacionado com as medidas de achatamento, ou "largura das caudas" das distribuições





==Lendo...==
