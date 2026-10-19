package dominio;

import strategy.CalculoXPStrategy;
import java.util.HashMap;
import java.util.Map;

public class Habito {
    private CalculoXPStrategy estrategiaXP;

    public void setEstrategiaXP(CalculoXPStrategy estrategia) {
        this.estrategiaXP = estrategia;
    }

    public float calcularExperienciaGerada() {
        if (estrategiaXP == null) return 0.0f;
        
        Map<String, Object> contexto = new HashMap<>();
        contexto.put("streak", 3); 
        
        return estrategiaXP.calcularXP(contexto);
    }
}