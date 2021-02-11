def recherche(elt, tab):
    tab_elt = []
    for i in range(len(tab)):
        if tab[i] == elt:
            tab_elt.append(i)
    return tab_elt
