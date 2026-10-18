package atividades;

import strategy.CalculoXPStrategy;
import java.util.HashMap;
import java.util.Map;

public class SessaoPomodoro {
    private CalculoXPStrategy estrategiaXP;

    public void setEstrategiaXP(CalculoXPStrategy estrategia) {
        this.estrategiaXP = estrategia;
    }

    public float calcularRecompensaExperiencia() {
        if (estrategiaXP == null) return 0.0f;
        
        Map<String, Object> contexto = new HashMap<>();
        contexto.put("minutosFocados", 25); // Dado simulado para o cálculo
        contexto.put("foiConcluida", true); // Dado simulado para o cálculo
        
        return estrategiaXP.calcularXP(contexto);
    }
}