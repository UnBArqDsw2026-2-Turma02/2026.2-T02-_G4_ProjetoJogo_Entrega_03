package atividades;

import dominio.CategoriaXP;
import observer.AssuntoAtividade;
import observer.EventoConclusaoAtividade;

public class SessaoPomodoro extends AssuntoAtividade {

    private final CategoriaXP tagCategoria;

    public SessaoPomodoro(CategoriaXP tagCategoria) {
        this.tagCategoria = tagCategoria;
    }

    public void finalizarCicloComSucesso() {
        System.out.println("\n[SessaoPomodoro] Ciclo de foco concluído com êxito!"); 
        float xpGerado = 50.0f;

        EventoConclusaoAtividade evento =
                new EventoConclusaoAtividade(
                        this.tagCategoria,
                        xpGerado
                );

        notificarObservadores(evento);
    }
}