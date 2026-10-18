package state.pomodoro;

import atividades.SessaoPomodoro;

public class PomodoroFocoEmAndamento implements EstadoPomodoro {

    @Override
    public void pausarCiclo(SessaoPomodoro sessao) {
        System.out.println("[State FocoEmAndamento] Pausando o foco... Transicionando para 'Pausado'.");

        sessao.setEstado(new PomodoroPausado());
    }

    @Override
    public void finalizarCicloComSucesso(SessaoPomodoro sessao) {
        System.out.println("[State FocoEmAndamento] Ciclo concluído com êxito! Transicionando para 'Concluído'.");

        sessao.setEstado(new PomodoroConcluido());
    }
}