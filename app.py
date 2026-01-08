import psycopg2
import pandas as pd
import streamlit as st
from db import get_connection

conn = get_connection()

st.title("Plateforme d’optimisation des examens")

df_exam = pd.read_sql("SELECT * FROM examens", conn)
df_prof = pd.read_sql("SELECT p.nom, COUNT(e.id) nb_exam FROM professeurs p JOIN examens e ON e.prof_id = p.id GROUP BY p.nom", conn)

st.subheader("Examens")
st.dataframe(df_exam)

st.subheader("Charge par professeur")
st.bar_chart(df_prof.set_index("nom"))

conn.close()
