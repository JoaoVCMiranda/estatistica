# Estimação de Parâmetros

> Começando com a estatística indutiva de verdade

O objetivo é entender as populações e fazer boas decisões

As distribuições teóricas da probabilidade, precisam de parâmetros bem definidos.
Porém na vida real não temos esses parâmetros de antemão. Portanto eles devem ser estimados a partir dos dados

Só escolher o modelo, já é, implicitamente um tipo de processo de estimação (Veja mais sobre em [Problema da Especificação de Fisher](https://estatisticafacil.org/glossario/o-que-e-erro-de-especificacao-glossario-estatistico/))

## Estimador e Estimativa

Estimador é calculado em função dos parâmetros da amostra

Estimativa é o valor que o estimador assume

E é sempre uma estimativa a respeito de um parâmetro, que tem um valor real que a estimativa deve ser aproximar e pode ser categorizada de acordo com os seguintes critérios

### Justeza
O estimador é justo quando de fato na média, é o valor que ele gostaria de ser
### Consistência 
É consistente quando quando maior o tamanho da amostra, mais próximo do valor desejado ele se torna
> Outra forma de dizer que a variância tende a zero quando $n\rightarrow \infty$

#### Eficiência

Para um mesmo tamanho de amostra, a média da diferença quadrática (Variância da distância até o valor real) quanto menor essa variância mais eficiente é o estimador

#### Suficiência

Se o estimador contém o máximo possível de informação que se poderia ter em relação ao parâmetro que quer estimar...


### Critérios para escolha de estimadores
(pulei)

### Estimativas de parâmetros

#### Média da população
A melhor estimativa é a média da amostra
#### Variância da população
Existem alguns detalhes sobre o cálculo da variância de uma população...

Se a média $\mu$ for conhecida, então faz-se
$$
s^2 = \frac{\sum(x_i-\mu)^2}{n} = \frac{\sum x_i^2}{n}-\mu^2 
$$

Caso a média seja apenas uma estimativa $\bar x$...
$$
s^2 = \frac{\sum(x_i-\bar x)^2}{n-1} = \frac{\sum x_i^2}{n-1}-\bar x^2 
$$
Isso acontece para ter um estimador justo, da variância(e não do desvio padrão $\sigma$)
#### Desvio padrão da população $\sigma$

> O desvio padrão só é a raiz quadrada da variância quando temos amostras grandes(quase sempre) para amostras menores, existe uma constante de correção para usar...
$$
S'_x=\frac{1}{c'_2}\sqrt{\frac{\sum(x_i-\bar x)^2}{n-1}}
$$

Mas na prática considerar $c'_2 = 1$

#### Proporção populacional
O melhor estimador é a [frequência relativa](Capítulo%202.md#Frequência%20Relativa)!
É um estimador justo, consistente e etc.

#### Com base em muitas amostras

Supondo diferentes medições de um mesmo parâmetro(com mesma média e variância) em momentos diferentes, se você quiser juntá-los depois para ter uma melhor estimativa pode fazer:
##### Média ponderada
Onde os pesos são os tamanhos das amostras
##### Variância "ponderada"
Onde os pesos são os graus de liberdade 
$$
S_p^2 = \frac{(n_1-1)s_1^2+(n_2-1)s_2^2 +... + (n_k-1)s_k^2}{(n_1-1)+(n_2-1)+...+(n_k-1)}
$$


### Estimação por intervalo

Agora que as coisas começam a ficar emocionantes, eu percebi que, nesse tópico tem as informações de intervalo de confiança e etc, geralmente eu pulava pois achava simples, mas não entendia como aplicar o I.C.


Como estamos tratando de variáveis aleatórias é impossível certeza do valor, já que precisaríamos de precisão infinita então surge a ideia de estimar por intervalos e calcular a probabilidade de estar certo.

Como o desvio padrão é calculado também a partir de variáveis aleatórias ele vai seguir uma distribuição...

Com base nisso, podemos estimar um fator que redimensiona o intervalo de confiança para os dados obtidos.

### Intervalo de Confiança

Dentro do intervalo de confiança caem $1-\alpha$ dos resultados

#### Para média com Desvio padrão $\sigma$ conhecido
Esse é o intervalo de confiança para a média real da população $\mu$ ao nível de confiança de $1-\alpha$ 
$$
\bar x \pm z_{\frac{\alpha}{2}} \frac{\sigma}{\sqrt{n}}
$$
O valor que  $\bar x$ estima $\mu$, como a distribuição das médias amostrais é normal, faz-se um redimensionamento do intervalo de confiança (além do próprio desvio da distribuição) para o grau de significância desejado.

#### Para média com Desvio padrão $\sigma$ desconhecido

Como há também a distribuição dos possíveis valores do desvio padrão, pois ele é estimado com base nos dados fornecidos.
A distribuição desse também deve ser levada em consideração.

Lembre que a diferença entre a distribuição normal e a [t-student](Capítulo%203.md#t-student) é apenas o parâmetro de espalhamento ($\sigma$ ou $s_x$)
$$
\bar x \pm t_{\frac{\alpha}{2}} \frac{\sigma}{\sqrt{n}}
$$

#### Para variância
Deve-se usar a distribuição [chi quadrado](Capítulo%203.md#Distribuição%20$\chi^2$) para tratar da distribuição amostral da variância

Como as normais reduzidas internas tem valor esperado 1, assim também será a distribuição chi quadrado, porém como ela tem $v$ graus de liberdade o valor esperado é $1v=v$
Com algumas manipulações algébricas chega-se em

$$
\frac{\sum_{i=1}^n(x_i-\bar x)^2}{\chi^2_{n-1;\frac {\alpha}{2}}}
=
\sigma^2
=
\frac{\sum_{i=1}^n(x_i-\bar x)^2}{\chi^2_{n-1;1-\frac {\alpha}{2}}}
$$

#### Para o desvio padrão
Tem um jeitinho de fazer o intervalo de confiança para amostras grandes $n>30$

$$
s \pm = z_{\alpha/2} \frac{s}{\sqrt{2(n-1)}}
$$


