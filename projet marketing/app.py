# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Prédiction de clic pub", page_icon="📣", layout="centered")

# --- Charger le pipeline
cache = joblib.load("modele_rl_pipeline.joblib")
pipe = cache["pipeline"]
cat_cols = cache["cat_cols"]
num_cols = cache["num_cols"]

st.title("📣 Prédiction de clic publicitaire")
st.markdown("Entrez les informations d’un client et obtenez sa probabilité de cliquer.")

# --- Formulaire utilisateur
with st.form("form_pred"):
    col1, col2 = st.columns(2)

    with col1:
        sexe = st.selectbox("Sexe", ["Homme","Femme"])
        canal_marketing = st.selectbox("Canal", ["email","sms","reseaux_sociaux"])
        appareil = st.selectbox("Appareil", ["mobile","ordinateur","tablette"])
        categorie_client = st.selectbox("Catégorie client", ["bronze","silver","gold","platinum"])
        age = st.number_input("Âge", min_value=18, max_value=100, value=30)

        anciennete_mois = st.number_input("Ancienneté (mois)", min_value=0, max_value=240, value=12)
        nb_campagnes_recues = st.number_input("Nb campagnes (3 mois)", min_value=0, max_value=50, value=3)
        nb_achats_3mois = st.number_input("Nb achats (3 mois)", min_value=0, max_value=50, value=2)

    with col2:
        revenu_mensuel = st.number_input("Revenu mensuel (€)", min_value=0, max_value=20000, value=2500)
        jour_envoi = st.number_input("Jour envoi (0=Lun..6=Dim)", min_value=0, max_value=6, value=2)
        heure_envoi = st.number_input("Heure envoi (0..23)", min_value=0, max_value=23, value=14)
        taux_remise = st.slider("Taux de remise", 0.0, 0.5, 0.10, step=0.01)
        temps_site_moyen = st.number_input("Temps site moyen (sec)", min_value=0, max_value=10000, value=120)
        taux_ouverture_email = st.slider("Taux ouverture email", 0.0, 1.0, 0.3, step=0.01)
        fidelite_score = st.slider("Score fidélité", 0, 100, 40, 1)

    submitted = st.form_submit_button("🔮 Prédire")

# --- Prédiction 1 par 1
if submitted:
    row = {  # respecter les colonnes du training
        "sexe": sexe,
        "canal_marketing": canal_marketing,
        "appareil": appareil,
        "categorie_client": categorie_client,
        "age": age,
        "revenu_mensuel": revenu_mensuel,
        "anciennete_mois": anciennete_mois,
        "jour_envoi": jour_envoi,
        "heure_envoi": heure_envoi,
        "taux_remise": taux_remise,
        "nb_campagnes_recues": nb_campagnes_recues,
        "nb_achats_3mois": nb_achats_3mois,
        "temps_site_moyen": temps_site_moyen,
        "taux_ouverture_email": taux_ouverture_email,
        "fidelite_score": fidelite_score,
    }
    X_new = pd.DataFrame([row])
    proba = float(pipe.predict_proba(X_new)[:,1])
    pred = int(proba >= 0.5)

    st.subheader("Résultat")
    st.metric("Probabilité de clic", f"{proba*100:.1f}%")
    st.write("Décision (seuil 0.5) :", "✅ Clique" if pred==1 else "❌ Ne clique pas")

st.divider()

# --- Prédiction par lot (CSV)
st.subheader("Prédiction par CSV")
st.caption("Le CSV doit contenir exactement les colonnes du modèle (catégorielles + numériques).")
file = st.file_uploader("Uploader un fichier CSV", type=["csv"])
if file is not None:
    df_up = pd.read_csv(file)
    proba_batch = pipe.predict_proba(df_up)[:,1]
    pred_batch = (proba_batch >= 0.5).astype(int)
    df_out = df_up.copy()
    df_out["proba_clic"] = proba_batch
    df_out["prediction"] = pred_batch
    st.dataframe(df_out.head(20))
    st.download_button("💾 Télécharger les prédictions", df_out.to_csv(index=False).encode("utf-8"), file_name="predictions_clic.csv")
