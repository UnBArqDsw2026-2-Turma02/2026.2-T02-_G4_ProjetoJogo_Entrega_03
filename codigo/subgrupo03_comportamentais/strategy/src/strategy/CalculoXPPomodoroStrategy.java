package strategy;

import java.util.Map;

public class CalculoXPPomodoroStrategy implements CalculoXPStrategy {
    private float fatorXPPorMinuto = 2.0f;
    private float bonusCicloConcluido = 10.0f;

    @Override
    public float calcularXP(Map<String, Object> dadosContexto) {
        int minutosFocados = (int) dadosContexto.getOrDefault("minutosFocados", 0);
        boolean cicloConcluido = (boolean) dadosContexto.getOrDefault("foiConcluida", false);
        
        float xp = minutosFocados * fatorXPPorMinuto;
        if (cicloConcluido) {
            xp += bonusCicloConcluido;
        }
        return xp;
    }
}