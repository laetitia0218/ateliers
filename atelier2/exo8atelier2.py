# Version simple pour débutants

points_map = ["0", "15", "30", "40"]

class TennisMatch:
    def __init__(self):
        self.points = [0, 0]  # points dans le jeu actuel
        self.jeux = [0, 0]    # jeux dans le set
        self.logs = []

    def ajouter_point(self, joueur):
        adv = 1 - joueur
        self.logs.append(f"Joueur {joueur+1} marque un point.")

        # Points normaux
        if self.points[joueur] < 3:
            self.points[joueur] += 1
        else:
            # Joueur gagne le jeu
            self.jeux[joueur] += 1
            self.points = [0, 0]
            self.logs.append(f"Joueur {joueur+1} gagne le jeu ! Score des jeux : {self.jeux[0]}-{self.jeux[1]}")

    def afficher_points(self):
        return f"{points_map[self.points[0]]}-{points_map[self.points[1]]}"

    def afficher_logs(self):
        for log in self.logs:
            print(log)


# Exemple simple
match = TennisMatch()
match.ajouter_point(0)  # Joueur 1 marque
match.ajouter_point(1)  # Joueur 2 marque
match.ajouter_point(0)  # Joueur 1 marque
match.ajouter_point(0)  # Joueur 1 marque
match.ajouter_point(0)  # Joueur 1 gagne le jeu

print("Points actuels :", match.afficher_points())
match.afficher_logs()
