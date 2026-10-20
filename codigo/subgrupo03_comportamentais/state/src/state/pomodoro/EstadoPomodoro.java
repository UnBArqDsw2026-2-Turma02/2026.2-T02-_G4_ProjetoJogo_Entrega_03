package state.pomodoro;

import atividades.SessaoPomodoro;

public interface EstadoPomodoro {

    default void iniciarCiclo(SessaoPomodoro sessao) {
        throw new IllegalStateException(
                "Não é possível iniciar o ciclo neste estado."
        );
    }

    default void pausarCiclo(SessaoPomodoro sessao) {
        throw new IllegalStateException(
                "Não é possível pausar o ciclo neste estado."
        );
    }

    default void retomarCiclo(SessaoPomodoro sessao) {
        throw new IllegalStateException(
                "Não é possível retomar o ciclo neste estado."
        );
    }

    default void finalizarCicloComSucesso(SessaoPomodoro sessao) {
        throw new IllegalStateException(
                "Não é possível finalizar o ciclo neste estado."
        );
    }
}