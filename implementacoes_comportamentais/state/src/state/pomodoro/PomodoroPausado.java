package state.pomodoro;

import atividades.SessaoPomodoro;

public class PomodoroPausado implements EstadoPomodoro {

    @Override
    public void retomarCiclo(SessaoPomodoro sessao) {
        System.out.println("[State Pausado] Retomando ciclo de foco... Transicionando para 'Foco em Andamento'.");

        sessao.setEstado(new PomodoroFocoEmAndamento());
    }
}