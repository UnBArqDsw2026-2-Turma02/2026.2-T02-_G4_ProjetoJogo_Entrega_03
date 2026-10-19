package state.pet;

import dominio.CategoriaXP;
import dominio.PetVirtual;

public class EstadoAdolescente implements EstadoPet {

    private static final float XP_PARA_EVOLUIR = 600.0f;

    @Override
    public void processarExperiencia(
            PetVirtual pet,
            CategoriaXP categoria,
            float pontos) {
        System.out.println("[Fase Adolescente] Processando " + pontos + " XP na categoria " + categoria + ".");

        avaliarEvolucao(pet);
    }

    @Override
    public void avaliarEvolucao(PetVirtual pet) {

        if (pet.getExperienciaTotal() >= XP_PARA_EVOLUIR) {
            System.out.println("[EVOLUÇÃO!] Pet acumulou " + pet.getExperienciaTotal() + " XP e evoluiu de ADOLESCENTE para ADULTO!");

            pet.setEstado(new EstadoAdulto());
        }
    }
}