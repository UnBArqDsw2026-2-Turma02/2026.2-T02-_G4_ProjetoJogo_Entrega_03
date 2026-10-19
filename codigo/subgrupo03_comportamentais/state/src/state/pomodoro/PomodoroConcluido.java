package state.pomodoro;

import atividades.SessaoPomodoro;

public class PomodoroConcluido implements EstadoPomodoro {
    
  @Override 
    public void iniciarCiclo(SessaoPomodoro sessao) {
      System.out.println("[State Concluído] Reiniciando nova configuração de ciclo... Transicionando para 'Configurando'.");
      
      sessao.setEstado(new EstadoConfigurando());
  }
}