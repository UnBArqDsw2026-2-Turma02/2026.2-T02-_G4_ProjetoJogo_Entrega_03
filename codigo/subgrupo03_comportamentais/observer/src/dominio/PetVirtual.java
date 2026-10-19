package dominio;

import observer.EventoConclusaoAtividade;
import observer.ObservadorAtividade;

public class PetVirtual implements ObservadorAtividade {

    private float experienciaTotal = 0.0f;

    @Override
    public void emAtividadeConcluida(
            EventoConclusaoAtividade evento) {
        System.out.println("[PetVirtual] Reagindo à notificação da atividade...");
        acumularExperiencia(
                evento.getCategoria(),
                evento.getXPGerado()
        );
    }

    public void acumularExperiencia(
            CategoriaXP categoria,
            float pontos) {

        this.experienciaTotal += pontos;

        System.out.println(" -> + " + pontos + " XP acumulados na categoria " + categoria + "."); 
        
        System.out.println(" -> Experiência Total do Pet: " + experienciaTotal + " XP.");
    }
}