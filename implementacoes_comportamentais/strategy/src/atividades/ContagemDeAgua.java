package atividades;

import strategy.CalculoXPStrategy;
import java.util.HashMap;
import java.util.Map;

public class ContagemDeAgua {
    private CalculoXPStrategy estrategiaXP;

    public void setEstrategiaXP(CalculoXPStrategy estrategia) {
        this.estrategiaXP = estrategia;
    }

    public float calcularExperienciaGerada() {
        if (estrategiaXP == null) return 0.0f;
        
        Map<String, Object> contexto = new HashMap<>();
        contexto.put("percentual", 1.0f); // Dado simulado para o cálculo
        
        return estrategiaXP.calcularXP(contexto);
    }
}