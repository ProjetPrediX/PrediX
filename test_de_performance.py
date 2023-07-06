import time
import pytest

@pytest.mark.performance
def test_login_admin_performance():
    def login_admin(password):
        """Vérifie si le mot de passe administrateur est correct"""
        admin_password = "BARKALHABCHI"  # Mot de passe administrateur par défaut
        return password == admin_password

    # Mesure du temps de réponse
    start_time = time.time()

    # Appel de la fonction login_admin() avec le mot de passe requis
    login_admin("BARKALHABCHI")

    # Calcul du temps de réponse
    end_time = time.time()
    response_time = end_time - start_time

    # Affichage du temps de réponse
    print("Temps de réponse :", response_time, "secondes")
