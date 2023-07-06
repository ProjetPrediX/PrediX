import base64
import pickle
# DB Management
import sqlite3
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
from streamlit import experimental_rerun
from streamlit.runtime.state import session_state
from streamlit_disqus import st_disqus
from streamlit_option_menu import option_menu

from Local import prediction, pretraitement_data

conn = sqlite3.connect ('data.db')
c = conn.cursor ( )


def create_usertable():
    c.execute ('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute ('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit ( )


def login_user(username, password):
    c.execute ('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall ( )
    return data


def view_all_users():
    c.execute ('SELECT * FROM userstable')
    data = c.fetchall ( )
    return data


def delete_user(username):
    c.execute ('DELETE FROM userstable WHERE username = ?', (username,))
    conn.commit ( )


def update_username(old_username, new_username):
    c.execute ('UPDATE userstable SET username = ? WHERE username = ?', (new_username, old_username))
    conn.commit ( )


def update_password(username, new_password):
    c.execute ('UPDATE userstable SET password = ? WHERE username = ?', (new_password, username))
    conn.commit ( )


def reset_password(username):
    new_password = "Achat1"  # Modifier le mot de passe par défaut ici
    c.execute ('UPDATE userstable SET password = ? WHERE username = ?', (new_password, username))
    conn.commit ( )


def logout():
    session_state.logged_in = False
    session_state.username = None


def main():
    """PrediX"""
    st.set_page_config (page_title="PrediX", page_icon="🤖")
    st.subheader ("L'intelligence artificielle à votre service")

    # Logo
    st.sidebar.title ("Bienvenue sur PrediX !")
    st.sidebar.image ("logo.png", width=60)

    with st.sidebar:
        selected = option_menu ("Main Menu", ["Home", "Login", "Signup", "Admin", "Chat"],
                                icons=['house', 'key', 'cloud', 'gear', "chat"],
                                menu_icon="cast", default_index=0)


        choice = selected

    # Définition de la mise en page de la barre de navigation avec les couleurs souhaitées
    navbar = """
        <style>
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 20px;
                background-color: #87CEEB; /* Bleu ciel clair */
                color: #FFFFFF;
                font-family: Arial, sans-serif;
            }
            .navbar-title {
                font-size: 24px;
                font-weight: bold;
            }
            .navbar-right {
                display: flex;
                align-items: center;

            .datetime {
                display: flex;
                align-items: center;
                margin-left: 20px;
                font-size: 18px;
            }
            .location-icon {
                width: 20px;
                height: 20px;
                fill: #FFFFFF;
                margin-right: 4px;
            }
            .location-text {
                margin-right: 140px;
            }
            .slogan-ribbon {
                background-color: #FFD700; /* Jaune */
                color: #000000; /* Couleur du texte du ruban */
                font-size: 14px;
                font-weight: bold;
                padding: 8px 20px;
                text-align: center;
                display: flex;
                align-items: center;
            }
            .slogan-icon {
                margin-right: 8px;
                font-size: 18px;
            }
        </style>
        <div class="navbar">
            <div class="navbar-title">
                <img "margin-right: 10px;">
            </div>
            <div class="navbar-right">
                <div class="datetime">
                    <svg class="location-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM10 2a6 6 0 100 12 6 6 0 000-12zm1 5a1 1 0 00-2 0v3.586L6.707 10.293a1 1 0 00-1.414 1.414l4 4a1 1 0 001.414 0l4-4a1 1 0 00-1.414-1.414L11 10.586V7z"/>
                    </svg>
                    <span class="location-text">Casablanca, MAROC</span>
                    <span id="datetime"></span>
                </div>
        <div class="slogan-ribbon">
            <span class="slogan-icon">📊</span>Anticipez Réussisez  Commandez !
        </div>
    """

    # Affichage de la barre de navigation
    st.markdown (navbar, unsafe_allow_html=True)

    # Affichage de l'heure et de la date actuelles sur la même ligne
    current_datetime = datetime.now ( )
    datetime_str = current_datetime.strftime ('%Y-%m-%d %H:%M:%S')
    st.write (f"Current Date and Time ⏱️ : {datetime_str}")

    if choice == "Home":
        st.markdown (

            "<h2 style='color: #00AEEF;'>Description de l'application</h2>"
            "<p style='color: #000000;'>PrediX est une application web créée par deux jeunes e-logisticiennes passionnées par le monde de l'intelligence artificielle. "
            "Nous aidons les entreprises à prendre des décisions éclairées en matière d'approvisionnement et d'achat pour minimiser les coûts et maximiser l'efficacité.</p>"
            "<h2 style='color: #00AEEF;'>Nos valeurs</h2>"
            "<ul>"
            "<li><strong style='color: #000000;'>Excellence :</strong> Nous nous efforçons d'atteindre l'excellence dans tout ce que nous faisons.</li>"
            "<li><strong style='color: #000000;'>Innovation :</strong> Nous sommes constamment à la recherche de nouvelles idées et de solutions innovantes.</li>"
            "<li><strong style='color: #000000;'>Collaboration :</strong> Nous croyons en la puissance de la collaboration et du travail d'équipe.</li>"
            "<li><strong style='color: #000000;'>Intégrité :</strong> Nous agissons avec intégrité et éthique dans toutes nos interactions.</li>"
            "</ul>",
            unsafe_allow_html=True)

        # Pied de page
        st.markdown (
            '<p style="font-size: small; text-align: right; color: #008000;"> [HABCHI Soumaya & BARKAL Hajar]</p>',
            unsafe_allow_html=True)

        create_usertable ( )

        # Liste des utilisateurs et mots de passe à intégrer
        usernames = ["OKhaled", "SBenlemoudden", "NSebbagh", "FHakkou", "ABahri", "MChakir", "MElmabrouki"]
        passwords = ["Achat1", "Achat2", "SCM1", "SI1", "Magasin1", "Magasin2", "Finance1"]

        # Ajouter les utilisateurs à la base de données s'ils n'existent pas déjà
        for i in range (len (usernames)):
            result = login_user (usernames[i], passwords[i])
            if not result:
                add_userdata (usernames[i], passwords[i])

    elif choice == "Login":
        st.subheader ("🤖")

        username = st.sidebar.text_input ("User Name")
        password = st.sidebar.text_input ("Password", type='password')

        if st.sidebar.checkbox ("Login / Logout "):
            create_usertable ( )
            result = login_user (username, password)
            if result:
                st.success ("Logged In as {}".format (username))
                task = st.sidebar.selectbox ("Task",
                                             ["Type achat", "local", "import"])
                if task == "Type achat":
                    st.subheader ("")

                if task == "local":
                    st.subheader ("Achat Local")

                    # Titre de l'application
                    st.subheader ("Comparaison entre les résultats réels et les prédictions du modèle XGBoost")
                    if st.button ("Afficher le graphique"):
                        # Chemin du graphique enregistré
                        graphique_path = 'graphique.png'

                        # Enregistrer le chemin du graphique dans un fichier pickle
                        with open ('graphique.pkl', 'wb') as file:
                            pickle.dump (graphique_path, file)

                        st.image (graphique_path)

                    # Formulaire de téléchargement du fichier Excel
                    st.subheader ("Télécharger le fichier Excel contenant les nouvelles données")

                    # Vérifier si un fichier a été téléchargé
                    file = st.file_uploader ("Importer un fichier Excel", type=["xlsx"], key="file_uploader")

                    # Vérifier si un fichier a été importé
                    if file is not None:
                        # Lire le fichier Excel en tant que DataFrame
                        df = pd.read_excel (file)

                        # Afficher le DataFrame importé
                        st.write ("Données importées :")
                        st.write (df)

                        # Bouton pour effectuer les prédictions
                        if st.button ("Effectuer les prédictions", key="predict_button"):
                            # Effectuer les prédictions
                            df_cleaned = pretraitement_data (df)
                            predictions = prediction (df_cleaned)
                            rounded_predictions = np.round (predictions).astype (int)

                            # Ajouter les prédictions au DataFrame
                            df['Prédiction Qté commandée'] = rounded_predictions

                            # Afficher les résultats
                            st.write ("Résultats des prédictions :")
                            st.write (df)
                            # Convert the DataFrame to Excel file
                            excel_path = "predictions.xlsx"
                            df.to_excel (excel_path, index=False)

                            # Encode the Excel file data to Base64
                            with open (excel_path, "rb") as file:
                                excel_data = file.read ( )
                            b64 = base64.b64encode (excel_data).decode ( )

                            # Generate the download link
                            href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="predictions.xlsx">Télécharger le fichier Excel</a>'
                            st.markdown (href, unsafe_allow_html=True)



                elif task == "import":
                    st.subheader ("              Achat Import            ")
                    st.subheader ("Comparaison entre les résultats réels et les prédictions du modèle XGBoost ")
                    if st.button ("Afficher le graphique"):
                        # Chemin du graphique enregistré
                        graphique_path = 'graphique_import.png'

                        # Enregistrer le chemin du graphique dans un fichier pickle
                        with open ('graphique_import.pkl', 'wb') as file:
                            pickle.dump (graphique_path, file)

                        st.image (graphique_path)

                    # Formulaire de téléchargement du fichier Excel
                    st.subheader ("Télécharger le fichier Excel contenant les nouvelles données")

                    # Vérifier si un fichier a été téléchargé
                    file = st.file_uploader ("Importer un fichier Excel", type=["xlsx"], key="file_uploader")

                    # columns_to_drop1 = ['Qté_Récep.', 'Unité_Récep.', 'Fournisseur', 'CC(O/N)', 'Jour', 'MT total', 'Nom_fournisseur',
                    # 'Désignation', 'N° BC', 'N° BL', 'Qté', 'Unité', 'Montant', 'Type', 'Coût_unitaire_moyen',
                    # 'Réglement', 'Année', 'Prix_unitaire', 'Unite_de_prix', 'Code_Nature',
                    # 'Trimestre', 'Qté_Commandé']

                    # Vérifier si un fichier a été importé
                    if file is not None:
                        # Lire le fichier Excel en tant que DataFrame
                        df = pd.read_excel (file)

                        # Afficher le DataFrame importé
                        st.write ("Données importées :")
                        st.write (df)

                        # Bouton pour effectuer les prédictions
                        if st.button ("Effectuer les prédictions", key="predict_button"):
                            # Effectuer les prédictions
                            df_cleaned = pretraitement_data (df)
                            predictions = prediction (df_cleaned)
                            rounded_predictions = np.round (predictions).astype (int)

                            # Ajouter les prédictions au DataFrame
                            df['Prédiction Qté commandée'] = rounded_predictions

                            # Afficher les résultats
                            st.write ("Résultats des prédictions :")
                            st.write (df)
                            # Convert the DataFrame to Excel file
                            excel_path = "predictions.xlsx"
                            df.to_excel (excel_path, index=False)

                            # Encode the Excel file data to Base64
                            with open (excel_path, "rb") as file:
                                excel_data = file.read ( )
                            b64 = base64.b64encode (excel_data).decode ( )

                            # Generate the download link
                            href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="predictions.xlsx">Télécharger le fichier Excel</a>'
                            st.markdown (href, unsafe_allow_html=True)
                        else:
                            st.warning ("Incorrect Username/Password")

    elif choice == "Signup":
        st.subheader ("create New Account")
        new_user = st.text_input ("Username")
        new_password = st.text_input ("password", type='password')
        if st.button ("Signup"):
            create_usertable ( )
            result = login_user (new_user, new_password)
            if not result:
                add_userdata (new_user, new_password)
                st.success ("You have successfully created a valid account")
                st.info ("Go to Login Menu")
            else:
                st.warning ("Username already exists")
    elif choice == "Admin":
        st.subheader ("Gestion de l'administrateur")
        st.markdown (
            "<p style='color: #000000;'>Bienvenue dans l'interface d'administration. Ici, vous pouvez afficher tous les "
            "utilisateurs enregistrés et les supprimer si nécessaire.</p>",
            unsafe_allow_html=True)
        admin_password = st.text_input ("Mot de passe administrateur", type="password")

        if admin_password == "BARKALHABCHI":
            # Display all users
            user_result = view_all_users ( )
            clean_db = pd.DataFrame (user_result, columns=["Username", "Password"])
            st.dataframe (clean_db)
            result = view_all_users ( )
            df = pd.DataFrame (result, columns=["Nom d'utilisateur", "Mot de passe"])
            st.dataframe (df)

            if st.button ("Rafraîchir"):
                experimental_rerun ( )

            # Add new user
            st.subheader ("Ajouter un nouvel utilisateur")
            new_username = st.text_input ("Nouvel utilisateur")
            new_password = st.text_input ("Mot de passe", type="password")
            if st.button ("Ajouter"):
                add_userdata (new_username, new_password)
                st.success ("Utilisateur ajouté avec succès")
                experimental_rerun ( )  # Redémarrage de l'application
                # Refresh the user list
                user_result = view_all_users ( )
                clean_db = pd.DataFrame (user_result, columns=["Username", "Password"])

            # Update username
            st.subheader ("Modifier le nom d'utilisateur")
            user_to_update_username = st.selectbox ("Utilisateur à modifier", clean_db["Username"],
                                                    key="update_username")
            new_username = st.text_input ("Nouveau nom d'utilisateur")
            if st.button ("Modify"):
                update_username (user_to_update_username, new_username)
                st.success ("Nom d'utilisateur modifié avec succès")
                experimental_rerun ( )  # Redémarrage de l'application
                # Refresh the user list
                user_result = view_all_users ( )
                clean_db = pd.DataFrame (user_result, columns=["Username", "Password"])

            # Update password
            st.subheader ("Modifier le mot de passe")
            user_to_update_password = st.selectbox ("Utilisateur à modifier", clean_db["Username"],
                                                    key="update_password")
            new_password = st.text_input ("Nouveau mot de passe", type="password")
            if st.button ("Modifier"):
                update_password (user_to_update_password, new_password)
                st.success ("Mot de passe modifié avec succès")
                experimental_rerun ( )  # Redémarrage de l'application
                # Refresh the user list
                user_result = view_all_users ( )
                clean_db = pd.DataFrame (user_result, columns=["Username", "Password"])

            # Delete user
            st.subheader ("Supprimer un utilisateur")
            user_to_delete = st.selectbox ("Utilisateur à supprimer", clean_db["Username"], key="delete_user")
            if st.button ("Supprimer"):
                delete_user (user_to_delete)
                st.success ("Utilisateur supprimé avec succès")
                experimental_rerun ( )  # Redémarrage de l'application
                # Refresh the user list
                user_result = view_all_users ( )
                clean_db = pd.DataFrame (user_result, columns=["Username", "Password"])

    elif choice == "Chat":
        st.subheader ("start the discussion")
        st_disqus ("streamlit-disqus-demo")


def login_admin(password):
    """Vérifie si le mot de passe administrateur est correct"""
    admin_password = "BARKALHABCHI"  # Mot de passe administrateur par défaut
    return password == admin_password


def logout_user():
    if st.sidebar.button ("Logout"):
        logout_user ( )


if __name__ == '__main__':
    main ( )
