from booking import ReservaHotel, ReservaVoo, ReservaTransporte
class ReservaFacade:
    def __init__(self):
        self.hotel = ReservaHotel()
        self.aereo = ReservaVoo()
        self.transporte = ReservaTransporte()

    def reserva_pacote(self, origem, destino, data_entrada, data_saida):
        self.aereo = ReservaVoo(origem, destino, data_entrada)
        self.hotel = ReservaHotel(destino, data_entrada, data_saida)
        self.transporte = ReservaTransporte(destino, data_entrada)

if __name__ == "__main__":
    fachada = ReservaFacade()
    fachada.reserva_pacote(
        origem = "São Paulo",
        destino = "Rio de Janeiro",
        data_entrada = "2024-12-24",
        data_saida = "2024-12-26"
    )