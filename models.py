from datetime import datetime, date
import json
from types import NoneType
from random import shuffle


class Tournament():

    def __init__(self, name, address, start: datetime, end: datetime,
                 nb_rounds=4, description="", round_list=None, players=None, index_current_round=-1, is_open=True):
        if round_list is None:
            round_list = []

        self.round_list = round_list

        if players is None:
            players = []

        self.players = players

        self.name = name
        self.address = address
        self.start = start
        self.end = end
        self.nb_rounds = nb_rounds
        self.description = description
        self.index_current_round = index_current_round
        self.is_open = is_open

    def create_next_round(self, start=datetime.now()):
        if len(self.round_list) >= self.nb_rounds:
            raise Exception(" Limite de round atteinte ")

        if len(self.players) <= 1:
            raise Exception("Il n'y a pas assez  de joueur ")

        if not self.is_open:
            raise Exception('Le tournois est termine ')

        if self.index_current_round != -1 and self.round_list[-1].end is None:
            raise Exception("Le precdent round n'est pas terminer ")
#         ==> Ici on secur que nos  listes (voir si elle existe, )
        round_number = self.index_current_round + 2
        round = Round("Round " + str(round_number), start=start)
        players_by_score = self.get_players_by_score()
        self.create_matchs(players_by_score, round)
        self.round_list.append(round)
        self.index_current_round += 1

    def get_players_by_score(self):
        players_by_score = []
        for player in self.players:
            while len(players_by_score) <= player[1]:
                players_by_score.append([])
            players_by_score[player[1]].append(player[0])
        players_by_score.reverse()
#       Pour commecner la liste des joueur par le plus
#       fort et pour eviter que le joueur le plus fort soit avantager
        return players_by_score

    def create_matchs(self, players_by_score, round):
        selected_players = []
        for player_list in players_by_score:
            shuffle(player_list)
            for player in player_list:
                selected_players.append(player)
                # Des qu'on est a deux on cree le match
                if len(selected_players) == 2:
                    round.add_match(selected_players[0], selected_players[1])
                    selected_players = []

        if len(selected_players) == 1:
            round.add_match(selected_players[0], None)
            match_ = round.matchs[-1]
            match_[0][1] = 2
            match_[1][1] = 0
            self.add_score_to_player(2, selected_players[0])

    def to_dict(self):

        dico = {"name": self.name, "address": self.address, "start": self.start.isoformat(),
                "end": self.end.isoformat(), "nb_rounds": self.nb_rounds, "description": self.description,
                "round_list": [round.to_dict()for round in self.round_list],
                "players": [(player[0].to_dict(), player[1])for player in self.players],
                "index_current_round": self.index_current_round, "is_open": self.is_open}
        return dico

    @classmethod
    def from_dict(self, dict):

        if "id" in dict:
            return Player.from_dict(dict)

        if "matchs" in dict:
            return Round.from_dict(dict)
        return Tournament(dict["name"],
                          dict["address"],
                          datetime.fromisoformat(dict["start"]),
                          datetime.fromisoformat(dict["end"]), dict["nb_rounds"],
                          dict["description"], dict["round_list"], dict["players"],
                          dict["index_current_round"], dict["is_open"])

    def register_player(self, player):
        for pl in self.players:
            if pl[0].id == player.id:
                raise Exception("le joueur avec l'id " + player.id + " est deja inscrit ")
        self.players.append([player, 0])

    def __str__(self):
        return f"{self.name},{self.start},{self.end}{self.address}{self.description}"

    def close_tournament(self):
        self.is_open = False

    def add_score_to_player(self, score: int, player):
        for pl in self.players:
            if pl[0].id == player.id:
                pl[1] = pl[1] + score
                break
        else:
            raise Exception("Impossible d'ajouter  le score au joueur , joueur inexistant ")

    def get_last_round(self):

        if self.index_current_round <= -1:

            raise Exception("Il n'y a pas de round ")

        if len(self.round_list) <= self.index_current_round:
            raise Exception("Le nombre de round est inferieur à l'index")
        return self.round_list[self.index_current_round]


class TournamentManager():
    def __init__(self, save_file_name="tournaments.json"):

        self.save_file_name = save_file_name
        self.list_tournaments = []
        self.load()

    def add_tournament(self, tournament: Tournament):
        self.list_tournaments.append(tournament)

    def close_tournament(self, name: str):
        for tournament in self.list_tournaments:
            if tournament.name == name:
                tournament.close_tournament()
                break

        else:
            raise Exception(f"Le tournois : {name} est inconnu")

    def save(self):
        try:
            save_file = open(self.save_file_name, "w+")
            json.dump([tournament.to_dict()for tournament in self.list_tournaments], save_file)
            save_file.close()

        except Exception as error:
            raise Exception("Error saving tournament info : ", error)

    def trier(self):
        self.list_tournaments.sort(key=lambda tournament: tournament.start)

    def load(self):
        try:
            save_file = open(self.save_file_name, "r")
            self.list_tournaments = json.load(save_file, object_hook=lambda dict: Tournament.from_dict(dict))
            save_file.close()

        except Exception as error:
            print("Error loading tournament info : ", error)

    def get_open_tournaments(self):
        open_tournaments = []
        for tournament in self.list_tournaments:
            if tournament.is_open:
                open_tournaments.append(tournament)
        return open_tournaments


class Player():

    def __init__(self, name, first_name, born: date, id):
        self.name = name
        self.first_name = first_name
        self.id = id
        self.born = born

    def __str__(self):
        return f"{self.name},{self.first_name},{self.id}{self.born}"

    def __repr__(self):
        return f"< Player name:{self.name} first_name:{self.first_name} id:{self.id} born:{self.born} >"

    def to_dict(self):
        dico = {"name": self.name, "first_name": self.first_name, "id": self.id, "born": self.born.isoformat()}
        return dico

    @classmethod
    def from_dict(self, dict):
        return Player(dict["name"], dict["first_name"], date.fromisoformat(dict["born"]), dict["id"])


class PlayerManager():

    def __init__(self, save_file_name="players.json"):
        self.save_file_name = save_file_name
        self.list_player = []
        self.load()

    def save(self):

        try:
            save_file = open(self.save_file_name, "w+")
            json.dump([player.to_dict() for player in self.list_player], save_file)
            save_file.close()

        except Exception as error:
            raise Exception(f"Error saving players info : {error}")

    def add_player(self, player: Player):
        for pl in self.list_player:
            if pl.id == player.id:
                raise Exception(f"Le joueur avec {pl.id} existe deja ")

        self.list_player.append(player)

    def trier(self):
        self.list_player.sort(key=lambda player: player.id)

    def load(self):
        try:
            save_file = open(self.save_file_name, "r")
            self.list_player = json.load(save_file, object_hook=lambda dict: Player.from_dict(dict))
            save_file.close()
        except Exception as error:
            print("Error loading players info : ", error)


class Round(object):
    def __init__(self, name, matchs = None, start: datetime | NoneType = None, end: datetime | NoneType = None):
        if matchs is None:
            self.matchs = []
        else:
            self.matchs = matchs
        self.start = start
        self.end = end
        self.name = name

    def start_round(self):
        self.start = datetime.now()

    def end_round(self):
        self.end = datetime.now()

    def add_match(self, player1, player2):
        playerA = [player1, None]
        playerB = [player2, None]
        _match = (playerA, playerB)
        self.matchs.append(_match)

    def to_dict(self):
        matchs = []
        for match in self.matchs:
            m = []
#           matchs.append(match)
            for player in match:
                pl = None
                if player[0] is not None:
                    pl = player[0].to_dict()
                m.append([pl, player[1]])
            matchs.append((m[0], m[1]))
        dico = {"name": self.name, "matchs": matchs, "start": self.start, "end": self.end}
        if self.start is not None:
            dico["start"] = self.start.isoformat()
        if self.end is not None:
            dico["end"] = self.end.isoformat()
        return dico

    @classmethod
    def from_dict(self, dict):
        if dict["start"] is not None:
            dict["start"]=datetime.fromisoformat(dict["start"])
        if dict["end"] is not None:
            dict["end"]=datetime.fromisoformat(dict["end"])
        return Round(dict["name"],dict["matchs"],dict["start"],dict["end"])
