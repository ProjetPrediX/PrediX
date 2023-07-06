import time

def test_home_page_performance():
    start_time = time.time()

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

    end_time = time.time()
    response_time = end_time - start_time

    # Affichage du temps de réponse
    print("Temps de réponse de la page Home :", response_time, "secondes")
