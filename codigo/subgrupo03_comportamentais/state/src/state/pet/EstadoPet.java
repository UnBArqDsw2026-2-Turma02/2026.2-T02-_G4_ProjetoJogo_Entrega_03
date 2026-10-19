package state.pet;

import dominio.CategoriaXP;
import dominio.PetVirtual;

public interface EstadoPet {

    void processarExperiencia(
            PetVirtual pet,
            CategoriaXP categoria,
            float pontos
    );

    void avaliarEvolucao(PetVirtual pet);
}