""" Testando """

from factory import Npc, Player

def main():
    """ Instâncias das factories """
    npc_factory = Npc()
    player_factory = Player()

    dragon = npc_factory.create_npc("dragon")
    skeleton = npc_factory.create_npc("skeleton")

    mario = player_factory.create_player("mario")

    print("NPCs Criados:")
    print(f"- {dragon['type']} com poder de ataque: {dragon['attack_power']}")
    print(f"- {skeleton['type']} com poder de ataque: {skeleton['attack_power']}")

    print("\nPlayer Criado:")
    print(f"- {mario['name']} com HP: {mario['hp']} e defesa: {mario['defense']}")

if __name__ == "__main__":
    main()
