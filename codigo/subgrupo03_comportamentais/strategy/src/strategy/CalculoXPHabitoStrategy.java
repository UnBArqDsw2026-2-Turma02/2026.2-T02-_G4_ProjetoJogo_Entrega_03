package strategy;

import java.util.Map;

public class CalculoXPHabitoStrategy implements CalculoXPStrategy {
    private float xpBaseCheckIn = 15.0f;
    private float multiplicadorMaximo = 3.0f;

    @Override
    public float calcularXP(Map<String, Object> dadosContexto) {
        int streak = (int) dadosContexto.getOrDefault("streak", 1);
        float multiplicador = Math.min(1.0f + (streak * 0.1f), multiplicadorMaximo);
        return xpBaseCheckIn * multiplicador;
    }
}