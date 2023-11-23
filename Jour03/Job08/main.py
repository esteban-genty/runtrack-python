def saison_fruit (type, saison):
    if type=="fruits":
        if saison=="hiver":
            print ("orange, mandarine et kiwi")
        elif saison=="ete":
            print ("Poire, fraise, cassis")
    elif type=="legume":
        if saison=="hiver":
            print ("carotte, topinambour, endive")
        elif saison=="ete":
            print ("artichaut, aubergine,navet")

saison_fruit ("fruits", "hiver")
saison_fruit ("fruits", "ete")
saison_fruit ("legume", "hiver")
saison_fruit ("legume", "ete")