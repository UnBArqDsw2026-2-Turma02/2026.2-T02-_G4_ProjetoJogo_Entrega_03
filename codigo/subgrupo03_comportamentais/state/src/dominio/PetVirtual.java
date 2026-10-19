package dominio;

import state.pet.EstadoPet;
import state.pet.EstadoBebe;

public class PetVirtual {

    private EstadoPet estadoAtual;

    private float experienciaTotal = 0.0f;

    public PetVirtual() {
        this.estadoAtual = new EstadoBebe();
    }

    public void setEstado(EstadoPet novoEstado) {
        if (novoEstado == null) {
            throw new IllegalArgumentException(
                    "O estado não pode ser nulo."
            );
        }

        this.estadoAtual = novoEstado;
    }

    public void acumularExperiencia(
            CategoriaXP categoria,
            float pontos) {

        if (categoria == null) {
            throw new IllegalArgumentException(
                    "A categoria não pode ser nula."
            );
        }

        if (pontos < 0) {
            throw new IllegalArgumentException(
                    "A experiência não pode ser negativa."
            );
        }
        
        this.experienciaTotal+= pontos;
        estadoAtual.processarExperiencia(this, categoria, pontos);
    }

    public float getExperienciaTotal() {
        return experienciaTotal;
    }
}