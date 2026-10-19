package state;

import dominio.CategoriaXP;
import dominio.PetVirtual;

// Interface simplificada apenas para referenciar o estado no Memento
public interface EstadoPet {
    void processarExperiencia(PetVirtual pet, CategoriaXP categoria, float pontos);
    void avaliarEvolucao(PetVirtual pet);
}