package atividades;

import state.pomodoro.EstadoPomodoro;
import state.pomodoro.EstadoConfigurando;

public class SessaoPomodoro {

    private EstadoPomodoro estadoAtual;

    public SessaoPomodoro() {
        this.estadoAtual = new EstadoConfigurando();
    }

    public void setEstado(EstadoPomodoro novoEstado) {
        if (novoEstado == null) {
            throw new IllegalArgumentException(
                    "O estado não pode ser nulo."
            );
        }

        this.estadoAtual = novoEstado;
    }

    public void iniciarCiclo() {
        estadoAtual.iniciarCiclo(this);
    }

    public void pausarCiclo() {
        estadoAtual.pausarCiclo(this);
    }

    public void retomarCiclo() {
        estadoAtual.retomarCiclo(this);
    }

    public void finalizarCicloComSucesso() {
        estadoAtual.finalizarCicloComSucesso(this);
    }
}