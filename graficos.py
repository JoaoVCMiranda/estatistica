def circular_plot(L, title=""):
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax = plt.subplots(figsize=(6, 6))
    # Create the pie chart (outer part of the donut)
    wedges, texts, autotexts = ax.pie(L.keys(), labels=L.values(),
                                    autopct='%1.1f%%', startangle=90,
                                    pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Set title
    ax.set_title(title)

def barplot(L, title="",xlabel="", ylabel="",h=None):
    import matplotlib.pyplot as plt
    
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    if(h== None):
        plt.bar(L.keys(), L.values())
    else:
        plt.bar(L.keys(), L.values(),width=h)

def poligono_frequencias_acumuladas(L, title="", xlabel="", ylabel="", k=None):
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    x = []
    for i in range(int(min(L.keys())) , int(max(L.keys())) + 1):
        x.append(i) 
    
    y = [0]*(len(x))

    ultimo = 0
    for i in range(len(x)):
        #print(y, i, ultimo)
        try:
            y[i] = L[i+int(min(L.keys()))]
            ultimo = y[i]
        except KeyError:
            y[i] = ultimo 
    
    # Plota a linha do polígono
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    
    # Adiciona os pontos médios das classes reais para destaque
    plt.scatter(x, y, color='red', zorder=5)

    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.ylim(bottom=0)
    
    plt.tight_layout()
    plt.show()

def poligono_frequencias(L, title="", xlabel="", ylabel="", k=None):
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    x = range(int(min(L.keys())) , int(max(L.keys())) + 1)
    y = [0]*len(x)

    for i in range(len(x)):
        try:
            y[i] = L[i+int(min(L.keys()))]
        except KeyError:
            y[i] = 0 
    
    # Plota a linha do polígono
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    
    # Adiciona os pontos médios das classes reais para destaque
    plt.scatter(x, y, color='red', zorder=5)

    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.ylim(bottom=0)
    

    plt.tight_layout()
    plt.show()

