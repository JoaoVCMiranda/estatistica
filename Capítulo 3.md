# Amostragem

É tirar dados de um população(conjunto universo)
Porém deve ser significativa: os dados retirados devem representar a população


## Probabilística
### Casual Simples
Apenas uma medição ao acaso
### Sistemática
O primeiro termo é ao acaso
Os demais, serão medidos seguindo um padrão de escolha, sem correlação ou viés com os dados
### Conglomerados
Define-se (intencionalmente) grupos para análise, e em cada grupo faz-se uma nova amostragem
(Espera-se que cada conglomerado tenha uma característica distinta)
### Estratificada
Para ter representatividade dos dados, sem ter que colher muitas amostras, vale a penas utilizar dos estratos(subpopulações)
Que informam sobre as característica da população em um certo contexto, no qual é possível fazer a analise independentemente das demais e depois juntá-las

## Não-probabilística
### Amostragem à esmo
Aleatório da nossa cabeça(é a que geralmente acontece)

## Distribuições Amostrais
> Ponte entre estatística descritiva e indutiva

### Distribuição Amostral da Média
Quando se tem um população e se faz uma medição aleatória $x_i$ (ou várias) podemos calcular a média dessas medições, 

Média Calculada
$$\bar x$$
Média "Real" da população
$$
\mu
$$
$$
\langle \bar x \rangle = \langle \frac{\sum_{i=1}^{n}{x_i}}{n} \rangle =\frac{1}{n}(\langle x_1 \rangle + \langle x_2 \rangle +\langle x_3 \rangle + ... +\langle x_n \rangle) = \frac{1}{n} (n\mu)= \mu
$$
Ou seja, a média para amostragens aleatórias, também será uma variável aleatória...
E o valor esperado dessa variável $\bar x$ será a média real.

#### Variância
$$
Var(X) = \int_{-\infty}^{\infty} dx p(x)x^2
$$
Onde $x$ é o valor medido da variável aleatória e $p(x)$ é a probabilidade de obtê-lo(p.d.f.)
##### Propriedades

$$
Var(kX) = \int_{-\infty}^{\infty} dx p(x)(kx)^2 = k^2 \int_{-\infty}^{\infty} dx p(x)x^2 = k^2Var(X)
$$
$$
Var(X_1+X_2) = Var(X_1) + Var(X_2) 
$$
Então, a variância dessa nova v.a. $\bar x$ é 
$$
Var(\bar x ) = Var( \frac{\sum_{i=1}^{n}{x_i}}{n}) =\frac{1}{n^2}Var(\sum_{i=1}^{n}{x_i})= \frac{1}{n^2}\sum_{i=1}^{n}Var({x_i})=\frac{1}{n^2}\sum_{i=1}^{n}\sigma^2=\frac{1}{n^2}n\sigma^2 = \frac{\sigma^2}{n} = \sigma_{\bar x}
$$
Note que quanto maior a amostra, menor a variância... Quando temos uma amostra "infinita" a variância vai para zero! Pois a se for infinita, a média será certeira!

Já no caso finito, e sem reposição, temos o *fator da população finita*
$$
\sigma_{\bar x}=\frac{\sigma^2}{n}.(\frac{N-n}{N-1})
$$
Onde 
$N$ é o tamanho da população
$n$ é o tamanho da amostra

Quando se considera *normal* a distribuição, implicitamente assumimos que a população é infinita

### Distribuição Amostral da Frequência(relativa ou não)

Modela-se a frequência como uma distribuição binomial, a média e variância seguem desse princípio, veja que:
O valor esperado a frequência de uma certa característica será:
$$
\langle f \rangle = np
$$
> Veja que a frequência relativa está muito relacionada(são o mesmo valor) com a probabilidade de "sucesso"

### Variância
$$
Var(f) = n(p(1-p))
$$
Veja que para chegar nos resultados para a frequência relativa, basta dividir por $n$ e usar as propriedades

### Graus de Liberdade de uma estatística
Variáveis livres, são aquelas que você precisa saber para calcular uma certa estatística.

Porém, no desvio padrão, já temos calculada a média da amostra, isso reduz uma dimensão dessa estatística,(pois basta saber n-1 parâmetros e a média e saberemos todos!)
Por isso n-1 é usado na variância!


### Distribuição Amostral da Variância

Segue uma distribuição $\chi ^2$  com n-1 graus de liberdade
Tem até uma aproximação para ela que podemos usar...

Faz-se uma distribuição normal reduzida, para chegar na $\chi ^2$ e a vantagem é que isso faz surgir tanto o desvio padrão quanto a variância da amostra.


A distribuição $\chi^2$ usa uma normal reduzida, e elevada ao quadrado.
> Lembre-se que como a variância tem n-1 graus de liberdade assim também será na chi quadrado

### t-student
Parece muito com a normal só não é pois usa a raiz da variância(que é apenas um estimador do desvio-padrão)
### F de Snedecor

É a mesma coisa que fizemos para a distribuição amostral da variância, mas agora reduzimos a chi quadrado, para poder fazer comparações sobre as distribuições de valores das variâncias.



