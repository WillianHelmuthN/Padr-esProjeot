""" Módulo que contém as classes Factory """

class Npc:
    """ Classe que retorna NPC """

    def create_npc(self, npc_type):
        """ Método que retorna NPC """
        if npc_type == "dragon":
            return {"type": "Dragon", "attack_power": 15}
        elif npc_type == "skeleton":
            return {"type": "Skeleton", "attack_power": 10}
        else:
            raise ValueError(f"Não tem: {npc_type}")


class Player:
    """ Classe que retorna Player """

    def create_player(self, player_type):
        """ Método que retorna Player """
        if player_type == "mario":
            return {"name": "Mario", "hp": 100, "defense": 8}
        elif player_type == "joker":
            return {"name": "Joker", "hp": 120, "defense": 5}
        else:
            raise ValueError(f"Não tem: {player_type}")
