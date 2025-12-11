def aproximacao_chi_quadrado(v):
    """
    v graus de liberdade
    essa aproximação só deve ser usada para v>30 
    """
    tmp = 2/(9*v)
    return v*(1-tmp+(tmp)**0.5)**3