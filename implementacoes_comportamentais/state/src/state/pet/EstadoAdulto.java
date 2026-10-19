package state.pet;

import dominio.CategoriaXP;
import dominio.PetVirtual;

public class EstadoAdulto implements EstadoPet {

    @Override
    public void processarExperiencia(
            PetVirtual pet,
            CategoriaXP categoria,
            float pontos) {
        System.out.println("[Fase Adulto] Processando " + pontos + " XP na categoria " + categoria + " (Nível Máximo Atingido).");

        avaliarEvolucao(pet);
    }

    @Override
    public void avaliarEvolucao(PetVirtual pet) {
        System.out.println(" -> Pet já se encontra em sua fase adulta máxima.");
    }
}