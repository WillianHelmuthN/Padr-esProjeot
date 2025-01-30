""" Módulo que contém as classes Factory """

class Npc:
    """ Classe que retorna NPC """

    def create_npc(self, npc_type, attack_power):
        """ Método que retorna NPC """
        return {"type": npc_type, "power": attack_power}

class Dragon(Npc):
    """ Classe que retorna Dragon """

    def create_dragon(self, type, power):
        """ Método que retorna Dragon """
        type = "dragon"
        power = 15
        return {"type": type, "power": power}

class Skeleton(Npc):
    """ Classe que retorna Skeleton """

    def create_skeleton(self, type_npc, power):
        """ Método que retorna Skeleton """
        type_npc = "skeleton"
        power = 10
        return {"type": type_npc, "power": power}


class Player:
    """ Classe que retorna Player """

    def create_player(self, type_player, hp, defense):
        """ Método que retorna Player """
        return {"type": type_player, "hp": hp, "defense": defense}

class Mario(Player):
    """ Classe que retorna Mario """

    def create_mario(self, type_player, hp, defense):
        """ Método que retorna Mario """
        type_player = "mario"
        hp = 100
        defense = 10
        return {"type": type_player, "hp": hp, "defense": defense}

class Joker(Player):
    """ Classe que retorna Joker """

    def create_joker(self, type_player, hp, defense):
        """ Método que retorna Joker """
        type_player = "joker"
        hp = 80
        defense = 5
        return {"type": type_player, "hp": hp, "defense": defense}
