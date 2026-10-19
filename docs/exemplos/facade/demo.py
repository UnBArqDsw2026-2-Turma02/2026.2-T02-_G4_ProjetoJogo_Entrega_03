"""Cliente da demonstração independente do Facade. Execute a partir da raiz."""
from jogo_facade import CategoriaXP, Conquista, JogoFacade, Usuario


class ClienteDemo:
    def __init__(self):
        self.usuario = Usuario("usuario-demo", conquistas=[
            Conquista("Primeira atividade", 1),
            Conquista("Duas atividades", 2),
        ], totalAtividadesPrevistas=3)
        self.jogo = JogoFacade(self.usuario)

    def mostrarEstado(self):
        pet = self.usuario.pet
        xp = ", ".join(f"{categoria.value}: {pontos}" for categoria, pontos
                       in zip(CategoriaXP, pet.vetorXP))
        print(f"  XP: {xp}")
        print(f"  Forma do pet: {pet.evolucao.value}")
        print(f"  Histórico: {len(self.usuario.historico.registros)} conclusão(ões)")
        for conquista in self.usuario.conquistas:
            estado = "DESBLOQUEADA" if conquista.foiDesbloqueada else "BLOQUEADA"
            print(f"  Conquista '{conquista.nome}': {estado}")

    def executar(self):
        print("FACADE — DEMONSTRAÇÃO INDEPENDENTE")
        print("Dados em memória; valores e critérios ilustrativos.\n")
        print("ESTADO INICIAL")
        self.mostrarEstado()
        cenarios = [
            ("1. Pomodoro concluído", "pomodoro-001", CategoriaXP.INTELECTUAL, 50),
            ("2. Reenvio da mesma conclusão", "pomodoro-001", CategoriaXP.INTELECTUAL, 50),
            ("3. Meta de água concluída", "agua-dia-01", CategoriaXP.HIDRATACAO, 20),
            ("4. Outra ocorrência de hidratação", "agua-dia-02", CategoriaXP.HIDRATACAO, 40),
        ]
        for titulo, identificador, categoria, pontos in cenarios:
            print(f"\n{titulo}")
            print(f"  → concluirAtividade('{identificador}', {categoria.value}, {pontos})")
            resultado = self.jogo.concluirAtividade(identificador, categoria, pontos)
            print(f"  Resultado: {resultado.situacao.value}")
            print("  Novas conquistas:", ", ".join(resultado.novasConquistas) or "nenhuma")
            self.mostrarEstado()


if __name__ == "__main__":
    ClienteDemo().executar()
