package strategy;

import java.util.Map;

public class CalculoXPAguaStrategy implements CalculoXPStrategy {
    private float xpMetaCompleta = 50.0f;

    @Override
    public float calcularXP(Map<String, Object> dadosContexto) {
        float percentual = (float) dadosContexto.getOrDefault("percentual", 1.0f);
        return xpMetaCompleta * percentual;
    }
}