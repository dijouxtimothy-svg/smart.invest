import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="smart invest", layout="centered")

st.title("📈smart invest")
st.subheader("simulateur d'investissement mensuel")

# ---inputs---
capital_initial = st.number_input("Capital de départ (€, une seule fois)", value=1000.0)
ajout_mensuel = st.number_input("Ajout mensuel (€, chaque mois)", value=100.0)
taux_annuel = st.slider("Rendement annuel (%)", 0, 15, 5)
mois = st.slider("Durée (en mois)", 1, 240, 60)

# ---calculs---
# convertir en taux mensuel
taux_mensuel = taux_annuel / 100 / 12
capital = capital_initial
historique = [capital]
contributions = [capital_initial]  # somme des apports cumulés

for i in range(1, mois + 1):
    # appliquer le rendement sur le capital existant
    capital = capital * (1 + taux_mensuel)
    # ajouter la nouvelle contribution
    capital += ajout_mensuel
    historique.append(capital)
    contributions.append(capital_initial + ajout_mensuel * i)

# ---résultats---
st.markdown("## 💰  Résultat final")

total_apports = capital_initial + ajout_mensuel * mois
total_gain = capital - total_apports

st.success(f"Capital estimé après {mois} mois : {round(capital,2)} €")
st.info(f"Total des apports : {round(total_apports,2)} €")
st.info(f"Gain généré (intérêts) : {round(total_gain,2)} €")

#---graphique---

st.markdown("## 📊  Évolution du capital")

fig, ax = plt.subplots()
ax.plot(historique, label="Capital total")
ax.plot(contributions, label="Apports cumulés", linestyle="--")
ax.set_xlabel("Mois")
ax.set_ylabel("Montant (€)")
ax.set_title("Croissance de l'investissement par rapport aux apports")
ax.legend()
ax.grid(True)

st.pyplot(fig)
