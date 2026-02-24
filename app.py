import streamlit as st
st.title("smart invest")
st.write("mon application fonctionne")

capital = st.number_input("Capital de départ", value=1000)
mois = st.number_input("nombre de mois", value=12)

resultat= capital* 1.05
st.write("le résultat est de ", resultat, "€")