# smart.invest 
import matplotlib.pyplot as plt

def simuler_investissement(capital_depart, mois , ajout_mensuel, volatilite , frais_annuel, inflation_annuelle  ):
    capital = capital_depart

    frais_mensuel = frais_annuel / 12
    inflation_mensuelle = inflation_annuelle / 12

    for _ in range ( mois ) :

      # Variation marché
      if random.random () < 0.10 : # Corrected from ⍃
        variation = random.uniform ( -15 * volatilite , -5 * volatilite)
      else :
        variation = random.uniform ( -3 * volatilite , 5 * volatilite)

      # Application variation
      capital = capital + ( capital * variation / 100 )

      # ajout investissement
      capital += ajout_mensuel


      #  Retrait frais
      capital -= capital * ( frais_mensuel / 100)

      # Ajustement inflation
      capital -= capital * ( inflation_mensuelle / 100)

    return capital


 # ---- Paramètres ----

capital = float(input("capital de départ (€) : "))
mois = int(input("nombre de mois d'investissement : ")) # Added missing parenthesis

frais_annuel = 1.10      # 1% de frais annuel (Corrected comma to dot for float)
inflation_annuelle = 2.0  # 2% inflation annuelle
simulations = 100 # Corrected variable name from 'simulation' to 'simulations' for consistency


strategie_strategique = { # Corrected to dictionary syntax with curly braces
    "100€ / mois prudent " : (100 , 0.7),
    "200€ / mois prudent " : (200 , 0.7),
    "200€ / mois agressif " : (200 , 1.5) # Renamed to differentiate, corrected comma to dot

}

resultats_strategiques = {} # Initialized as a dictionary

for nom ,( ajout , volatilite) in strategie_strategique.items() :
    resultats = []
    for _ in range ( simulations ) :
        final = simuler_investissement (
            capital , mois , ajout , volatilite , frais_annuel , inflation_annuelle # Corrected 'capita' to 'capital'
        )
        resultats .append ( final )

    moyenne = sum ( resultats ) / simulations
    resultats_strategiques[nom] = moyenne # Corrected dictionary assignment

    print ("\nStrategie : " , nom )
    print ("capital moyen :", round ( moyenne , 2 ) , "€")


plt.bar(resultats_strategiques.keys(), resultats_strategiques.values()) # Added parentheses
plt.title("Comparaison avec frais et inflation")
plt.xlabel("Stratégie") # Added x-label for clarity
plt.ylabel("capital moyen réel (€)")
plt.xticks(rotation = 45) # Corrected ptl.xtickis to plt.xticks and added parentheses
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()
# Removed duplicate plt.ylabel and plt.show as they were redundant after the bar plotimport random