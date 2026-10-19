package state.pomodoro;

import atividades.SessaoPomodoro;

public class EstadoConfigurando implements EstadoPomodoro {

    @Override
    public void iniciarCiclo(SessaoPomodoro sessao) {
        System.out.println("[State Configurando] Iniciando ciclo de foco... Transicionando para 'Foco em Andamento'.");

        sessao.setEstado(new PomodoroFocoEmAndamento());
    }
}