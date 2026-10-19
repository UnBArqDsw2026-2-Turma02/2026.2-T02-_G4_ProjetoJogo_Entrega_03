package state.pet;

import dominio.CategoriaXP;
import dominio.PetVirtual;

public class EstadoBebe implements EstadoPet {

    @Override
    public void processarExperiencia(
            PetVirtual pet,
            CategoriaXP categoria,
            float pontos) {
        System.out.println("[Fase Bebê] Processando " + pontos + " XP na categoria " + categoria + ".");

        avaliarEvolucao(pet);
    }

    @Override
    public void avaliarEvolucao(PetVirtual pet) {

        if (pet.getExperienciaTotal() >= 100.0f) {
            System.out.println("[EVOLUÇÃO!] Pet acumulou " + pet.getExperienciaTotal() + " XP e evoluiu de BEBÊ para CRIANÇA!");

            pet.setEstado(new EstadoCrianca());
        }
    }
}