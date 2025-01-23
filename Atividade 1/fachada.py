from computador import pc

class fachada:
    def __init__(self):
        self.pc = pc()

    def Ligar_pc(self, cpu, memoria, hd, vga):
        self.pc.peca(cpu, memoria, hd, vga)

if __name__ == "__main__":
    fachada = fachada()
    fachada.Ligar_pc(
        cpu = "OK",
        memoria = "OK",
        hd = "OK",
        vga = "OK"
    )