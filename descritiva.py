import numpy as np

def get_frequencias(dados):
    conjunto = set(dados) # Sem repetições
    frequencias = {} 
    for c in conjunto:
        frequencias[c] = len([x for x in dados if x == c]) # contagens
    frequencias = dict(sorted(frequencias.items())) # ordem alfabética
    return frequencias

def get_frequencias_relativas(dados):
    frequencias = {}
    n = len(dados)
    for k, v in get_frequencias(dados).items():
        frequencias[k] = v/n
    return frequencias

def get_frequencias_relativas_acumuladas(dados):
    frequencias = {}
    acumulado = 0 
    for k,v in get_frequencias_relativas(dados).items():
        acumulado += v 
        frequencias[k] = acumulado
    return frequencias

def get_frequencias_acumuladas(dados):
    frequencias = {}
    acumulado = 0 
    for k,v in get_frequencias(dados).items():
        acumulado += v 
        frequencias[k] = acumulado
    return frequencias

def get_precisao(number):
    s = str(number)
    if '.' in s:
        return 10**(-len(s.split('.')[-1]))
    return 1

def media(dados):
    return sum(dados)/len(dados)

def media_frequencia(conjunto_dados, frequencias):
    """
    uso:
    L = get_frequencias(dados) 
    media_frequencia(L.keys(), L.values())
    """
    return np.dot(conjunto_dados, frequencias)/sum(frequencias)

def mediana(dados):
    n = len(dados)
    dados = sorted(dados)
    if(n==0):
        return 0
    if(n%2==1):
        return dados[n//2]
    else:
        return (dados[n//2-1] + dados[n//2]) / 2
    
def mediana_classes(classes, frequencias, h):
    n = sum(frequencias)
    acumulado = 0
    i = 0 
    
    while(acumulado<n/2):
        acumulado+=frequencias[i]
        i+=1
    # quando passou, volta um
    i-=1
    acumulado -= frequencias[i]
    
    # amplitude
    h_0 = 0
    if(type(h)==list):
        h = h[i]
        h_0 = h[0]
    else:
        h_0 = h

    print(classes[i]-h_0/2 , n/2 ,  acumulado, frequencias[i]*h)
    return (classes[i]-h_0/2) + ((n/2) - acumulado)/frequencias[i]*h

def moda(dados):
    frequencias = get_frequencias(dados)
    lista_frequencias = list(frequencias.values())
    i = lista_frequencias.index(max(lista_frequencias))
    lista_valores =  list(frequencias.keys())
    return lista_valores[i] 

def moda_classes(classes, frequencias, h):
    """
    h precisa ser único  
    """
    if(len(classes)!= len(frequencias)):
        Error("Tamanhos incompatíveis de classe/frequencia")
    i = frequencias.index(max(frequencias))
    d2 = frequencias[i] - frequencias[i+1] # já que a frequencia i é a maior sempre
    d1 = frequencias[i] - frequencias[i-1]

    print(classes[i] - h/2,   (d1),d2)

    return (classes[i] - h/2) + (d1)/(d1+d2)*h

def variancia(dados):
    m = media(dados)
    n = len(dados)
    return(sum([(x - m)**2 for x in dados])/(n-1))

def discretizar(dados, h=0):
    if(h==0):
        h = (min([get_precisao(i) for i in dados]))
    mn = min(dados)-h/2
    mx = max(dados)+h/2
    atual = min(dados)
    dados_discretizados = []
    while(mn<atual<mx):
        for d in dados:
            # otimização opcional
            # (d - atual)**2 < h**2/2
            if  atual - h/2 < d < atual + h/2:
                dados_discretizados.append(atual)
        atual += h
    return dados_discretizados

def momento_t(dados, t, centrado=0):
    return sum([(d-centrado)**t  for d in dados])/len(dados) 

def coeficiente_assimetria(dados):
    return momento_t(dados, 3, media(dados))/variancia(dados)**(3/2)

def coeficiente_assimetria(dados):
    return momento_t(dados, 4, media(dados))/variancia(dados)**(4/2)


