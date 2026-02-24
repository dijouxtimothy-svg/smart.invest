import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="smart invest"), layout="centered")

st.title("📈smart invest")
st.subheader("simulateur d'investissement mensuel")

# ---inputs---
capital_initial = st.number_input("Capital de départ(€)",  value=1000.0))
ajout_mensuel = st.number_input("Ajout mensuel(€)", value=100.0))
taux_annuel = st.slider(" rendement annuel(%)", 0 ,15 , 5)
mois = st.slider("Durée (en mois)", 1 , 240 , 60)

# ---calculs---
taux_mensuel = taux_annuel / 100 / 12
capital = capital_initial
historique = [capital]

for i in range(mois):
    capital = capital * (1 + taux_mensuel) 
    capital += ajout_mensuel
    historique.append(capital)

# ---résultrats---
st.markdown("## 💰  résultat final")
st.success ( f" capital estimé aprés {mois} mois : { round(capital,2)} €")

#---graphique---

st.markdown("## 📊  évolution du capital")

fig, ax = plt.subplots()
ax.plot(historique)
ax.set_xlabel("Mois")
ax.set_ylabel("Capital (€)")
ax.set_title("Croissance de l'investissement")

st.pyplot(fig)
