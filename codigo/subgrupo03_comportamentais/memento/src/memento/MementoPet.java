package memento;

import state.EstadoPet;
import java.time.LocalDateTime;
import java.util.Arrays;

public class MementoPet {
    private final int nivel;
    private final int peso;
    private final float[] experienciasPorCategorias;
    private final float experienciaTotal;
    private final EstadoPet estadoAtual;
    private final LocalDateTime dataHoraSnapshot;
    private final String motivo;

    public MementoPet(int nivel, int peso, float[] experienciasPorCategorias, 
                      float experienciaTotal, EstadoPet estadoAtual, String motivo) {
        this.nivel = nivel;
        this.peso = peso;
        // Cópia profunda para blindar o estado salvo contra modificações externas
        this.experienciasPorCategorias = experienciasPorCategorias != null 
            ? Arrays.copyOf(experienciasPorCategorias, experienciasPorCategorias.length) 
            : new float[5];
        this.experienciaTotal = experienciaTotal;
        this.estadoAtual = estadoAtual;
        this.dataHoraSnapshot = LocalDateTime.now();
        this.motivo = motivo;
    }

    public int getNivel() { return nivel; }
    public int getPeso() { return peso; }
    public float[] getExperienciasPorCategorias() { 
        return Arrays.copyOf(experienciasPorCategorias, experienciasPorCategorias.length); 
    }
    public float getExperienciaTotal() { return experienciaTotal; }
    public EstadoPet getEstadoAtual() { return estadoAtual; }
    public LocalDateTime getDataHoraSnapshot() { return dataHoraSnapshot; }
    public String getMotivo() { return motivo; }
}