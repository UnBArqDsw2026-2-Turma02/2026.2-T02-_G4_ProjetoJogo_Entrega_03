package state.pet;

import dominio.CategoriaXP;
import dominio.PetVirtual;

public class EstadoCrianca implements EstadoPet {

    @Override
    public void processarExperiencia(
            PetVirtual pet,
            CategoriaXP categoria,
            float pontos) {

        System.out.println("[Fase Criança] Processando " + pontos + " XP na categoria " + categoria + ".");

        avaliarEvolucao(pet);
    }

    @Override
    public void avaliarEvolucao(PetVirtual pet) {

        if (pet.getExperienciaTotal() >= 300.0f) {
            System.out.println("[EVOLUÇÃO!] Pet acumulou " + pet.getExperienciaTotal() + " XP e evoluiu de CRIANÇA para ADOLESCENTE!");

            pet.setEstado(new EstadoAdolescente());
        }
    }
}