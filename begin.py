


#pour les litres
negative_number_litre = True
litre_float = False
capacite_impossible = True

while negative_number_litre == True or litre_float == False or capacite_impossible == True:
    negative_number_litre = True
    litre_float = False
    capacite_impossible = True
    litre_dans_le_reservoir_total = input("La nombre de litres total de ton réservoir est ")
    litre_dans_le_reservoir_avant = input("et il en contient actuellement ")
    if litre_dans_le_reservoir_total.replace(".", "", 1).isnumeric() and litre_dans_le_reservoir_avant.replace(".", "", 1).isnumeric():
        litre_float = True
        litre_dans_le_reservoir_total = float(litre_dans_le_reservoir_total)
        litre_dans_le_reservoir_avant = float(litre_dans_le_reservoir_avant)
        if (litre_dans_le_reservoir_total < 0) or (litre_dans_le_reservoir_avant < 0):
            print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")
        else:
            negative_number_litre = False
            while capacite_impossible == True:
                if litre_dans_le_reservoir_total <= litre_dans_le_reservoir_avant:
                    print("votre capacité d'essence est déjà au maximum! Veuillez essayer encore S.V.P!")
                    negative_number_litre = True
                    litre_float = False
                    capacite_impossible = False
                else:
                        capacite_impossible = False
    else:
        print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")


#pour le montant fixe

negative_fixe = True
fixe_float = False

while negative_fixe == True or fixe_float == False:
    total_prix_desirer = input("Veuillez inscrire le montant souhaité : ")
    if total_prix_desirer.replace(".", "", 1).isdigit():
        fixe_float = True
        total_prix_desirer = float(total_prix_desirer)
        if (total_prix_desirer < 0):
            print("Cela est un choix invalide! Veuillez essayer encore S.V.P.!")
        else:
            negative_fixe = False
    else:
        print("Cela est un choix invalide! Veuillez essayer encore S.V.P.!")




print("out")