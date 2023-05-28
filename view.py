from datetime import datetime
import sys
from collections.abc import Callable
from controler import Controler
from prettytable import PrettyTable
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class View(object):
    def __init__(self):
        self.controler = Controler()

#   __________________________________________MENU___________________________________
    def menu(self, welcome=False):

        if welcome:
            print("Salut, tu es dans le menu :")
        print("Tu as le choix entre :")
        print("1: Joueur")
        print("2: Tournois")
        print("3: Sauvegarde")

        choose = None
        if choose is None:
            choose = self.ask_string("Fait ton choix (met un chiffre)")
        if choose == "1":
            self.player_menu()
        elif choose == "2":
            self.tournament_menu()

        elif choose == "3":
            try:
                self.controler.save()
                print("\nCa a bien ete sauvegarde \n")
            except Exception as error:
                print(f"Impossible de sauvegarder : {error}")
        else:
            self.exit_back(choose, sys.exit)

#   _______________________________PLAYER_____________________________________

    def player_menu(self):
        print("Menu Player : \n")
        print("\n1 : Consulter\n")
        print("\n2 : Creation \n")
        print(" \n3 : Recherche par identifiant\n")
        print("")
        choose = None
        while choose is None:
            choose = self.ask_string("Ta le choix entre consulter \n""ou creer (pas les deux en meme temps)")

        if choose == "1":
            print("")
            self.consulter_player()

        elif choose == "2":
            print("Te voila dans le menu creation  , ta cru on etait dans un jeux video ")
            self.player_creation()

        elif choose == "3":
            self.player_data()
        else:
            # self.exit_back(choose, self.menu)
            pass

    def consulter_player(self):
        list_player = self.controler.get_list_players()
        for index, player in enumerate(list_player):
            print(f"{index + 1}. first name ='{player.first_name}'; name ='{player.name}; \
                born ='{player.born}'; id = '{player.id}'")
        print(f"Il y a {len(list_player)}  joueur(s) enregistré(s) ")
        self.player_menu()

    def player_creation(self):

        name = first_name = id = born = None
        while name is None:
            name = self.ask_string("Name : ")
        while first_name is None:
            first_name = self.ask_string("first_name :")
        while id is None:
            id = self.ask_string('ID : ')
        while born is None:
            born = self.ask_date("Born : ", False)

        try:
            self.controler.add_player(name, first_name, born, id)
            print(f"Ton joueur : {name} avec l'id :{id} a ete crée  ")
        except Exception as error:
            print("Impossible de creer le joueur : ", error)
        self.player_menu()

    def player_data(self,):
        print("Tu souhaites connaitres toutes les info sur un joueur ?")
        id = None
        while id is None:
            id = self.ask_string("Rentre son id juste en bas ")
        try:
            player = self.controler.get_player_by_id(id)
            print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'\
                ")
        except Exception as error:
            print("Impossible d'afficher les données du joueur : ", error)
        self.player_menu()

#   __________________________ TOURNAMENT ____________________________________

    def tournament_menu(self):

        print("\nOk Super te voila dans le menu des tournois tu as le choix entre : \n")
        print("\n1 :Creer un tournois  \n")
        print("\n2: Consulter un tournois   \n ")
        print("\n3: Inscrire un joueur au tournois   \n ")
        print("\n4: Commencer un round  \n ")
        print("\n5: Gerer les match\n ")
        print("\n6: Cloturer \n ")
        choose = None
        while choose is None:
            choose = self.ask_string("Indique ton choix")
        if choose == "1":
            self.debut_tournois()
        elif choose == "2":
            self.consulter_tournois()
        elif choose == "3":
            self.inscription()
        elif choose == "4":
            self.start_round()
        elif choose == "5":
            self.end_match()
        elif choose == '6':
            tournament = None
            while tournament is None:
                tournament = self.ask_tournament()
            self.controler.close_tournament(tournament)
            print(f"Cloture effectué :  {tournament}")
            players = tournament.get_players_by_score()
            my_table = PrettyTable()
            my_table.field_names = ["Nom", "Prenom", "Score", "Classement"]
            classment = 1
            for i in range(len(players)):
                if len(players[i]) == 0:
                    continue
                for player in players[i]:
                    my_table.add_row([player.name, player.first_name, len(players)-i-1, classment])
                classment += 1
            print(my_table)
        else:
            self.exit_back(choose, self.menu)

    def debut_tournois(self):
        print("\nEntre les info pour la creation d'un tournois   \n")
        my_table = PrettyTable()
        my_table.field_names = ["Nom", "Date de debut", "Date de fin", "Adresse"]

        name, start, end, address = None, None, None, None
        while name is None:
            name = self.ask_string("Nom du tournois svp ? ")
        while end is None or start >= end:
            if end is not None:
                start, end = None, None
                print("La date de début est supérieure à la date de fin")

            while start is None:
                start = self.ask_date("Quelle est la date de début du tournois ? : ", True)
                now = datetime.now()
                if start is not None and now > start:
                    print("Pas de date du passé  ")
                    start = None

            while end is None:
                end = self.ask_date("Quelle est la date de fin du tournois ? : ", True)

                now = datetime.now()
                if end is not None and now > end:
                    print("Pas de date du passé  ")
                    end = None

        while address is None:
            address = self.ask_string("Quelle est votre adress")
        my_table.add_row([name, start, end, address])
        print(my_table)
        self.controler.create_tournament(name, start, end, address)

    def consulter_tournois(self):
        my_table = PrettyTable()
        my_table.field_names = ["Nom", "Date de debut", "Date de fin", "Adresse"]

        list_tournois = self.controler.get_list_tournement()
        if (list_tournois is not None) and len(list_tournois) != 0:
            for list in list_tournois:
                my_table.add_row([list.name, list.start, list.end, list.address])
            print(my_table)
        else:
            print("\nIl n'y a pas de tournois \n ")

    def inscription(self):
        print("\n Bonjour vous voici dans l'etape de l'inscription")
        try:
            name, id_player = None, None
            while name is None:
                name = self.ask_string("Rentrer le nom  du tournois  ")
            tournament = self.controler.get_tournement_by_name(name)
            while id_player is None:
                id_player = self.ask_string("Rentrer l'id  du joueur ")
            player = self.controler.get_player_by_id(id_player)
            self.controler.register_player_to_tournament(player, tournament)
            print("le joueur a bien ete inscrit ")
        except Exception as error:
            print(f"Inscription du joueur impossible dans le tournois {name}:", error)
            self.tournament_menu()

    def start_round(self):

        tournament = None
        while tournament is None:
            tournament = self.ask_tournament()
        try:
            self.controler.start_round(tournament)

        except Exception as error:
            print(f"Impossible de faire le round : {error}")

    def end_match(self):
        selected_tournament = self.ask_tournament()
        print(selected_tournament.name)
        try:
            last_round = self.controler.get_last_round(selected_tournament)

        except Exception as error:
            print(f"Impossible d'obtenir le dernier round  :{error}")
            self.tournament_menu()
            return
        select_match = self.ask_match(last_round)
        tableau_score = [1, 2, 0]
        score = None
        while score is None:
            score = self.ask_int("\nQui a gagne ?\n 1 : Joueur 1\n 2 : Joueur 2 \n 0 : Egalité ")
            if score is not None and score not in tableau_score:
                print("Tu t'es tromper selectionne un chiffre (1,2 ou 0)")
        self.controler.end_match(select_match, selected_tournament, score)
        print("le match est Terminer  ")

#    ___________________________TOOLS________________________________
    def ask_string(self, question: str):

        name = input(question)
        if name == "":
            print("Reponse vide")
            return None
        if len(name) >= 100:
            print("Reponse trop longue   (limité a 99 caracteres)")
            return None
        return name

    def ask_date(self, question, time: bool = False):

        format = "%d/%m/%Y"
        date = input(question)
        if time:
            format = format + " %H:%M"
        try:
            date = datetime.strptime(date, format)
            if not time:
                date = date.date()
        except ValueError:
            error = "La date doit etre au format jj/mm/aaaa "
            if time:
                error = error + "heure:minute"
            print(error)
            return None
        return date

    def ask_int(self, question: str):
        try:
            return int(input(question))

        except Exception as error:
            print("Pas un nombre : ", error)
            return None

    def ask_tournament(self):
        index = 1
        open_tournaments = self.controler.get_open_tournaments()
        if len(open_tournaments) == 0:
            print("Aucun tournois en cours ")
            self.tournament_menu()
            return
        for tournement in open_tournaments:
            print(f"{index} : {tournement.name}")
            index += 1

        index_choose = None
        while index_choose is None:
            index_choose = self.ask_int("Quel est le tournois concerné ?")
            if index_choose is not None and (index_choose > len(open_tournaments) or index_choose < 1):
                index_choose = None
                print("Mauvais choix  ")
        return open_tournaments[index_choose - 1]

    def ask_match(self, last_round):
        index = 1
        if len(last_round.matchs) == 0:
            print('Aucun match en cours')
            self.tournament_menu()
            return

        for matchou in last_round.matchs:
            if matchou[1][0] is None:
                continue
            print(f"{index}:{matchou[0][0].name} vs {matchou[1][0].name}")
            index += 1

        indexou_choose = None
        while indexou_choose is None:
            indexou_choose = self.ask_int("Quel est le match concerne")
            if indexou_choose is not None and (indexou_choose > len(last_round.matchs) or indexou_choose < 1):
                indexou_choose = None
                print("Mauvais choix de match   ")
        return last_round.matchs[indexou_choose - 1]

    def exit_back(self, choose: str, back: Callable):
        if choose == "exit":
            sys.exit()
        elif choose == "back":
            back()

        else:
            print("\nCe choix n'est pas dispo ou n'existe pas \n")
