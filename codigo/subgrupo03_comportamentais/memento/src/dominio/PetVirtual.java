package dominio;

import memento.MementoPet;
import state.EstadoPet;

public class PetVirtual {
    private String nomePet;
    private int nivel;
    private int peso;
    private float[] experienciasPorCategorias = new float[5];
    private float experienciaTotal;
    private EstadoPet estadoAtual;

    public PetVirtual(String nomePet) {
        this.nomePet = nomePet;
        this.nivel = 1;
        this.peso = 5;
        this.experienciaTotal = 0.0f;
    }

    public void acumularExperiencia(CategoriaXP categoria, float pontosXp) {
        this.experienciaTotal += pontosXp;
        System.out.println("[" + nomePet + "] Acumulou " + pontosXp + " XP na categoria " + categoria);
    }

    // =========== MEMENTO (Originator) ===========

    public MementoPet salvarEstado(String motivo) {
        System.out.println("Originator: Salvando estado no Memento. Motivo: " + motivo);
        return new MementoPet(nivel, peso, experienciasPorCategorias, 
                              experienciaTotal, estadoAtual, motivo);
    }

    public void restaurarEstado(MementoPet memento) {
        this.nivel = memento.getNivel();
        this.peso = memento.getPeso();
        this.experienciasPorCategorias = memento.getExperienciasPorCategorias();
        this.experienciaTotal = memento.getExperienciaTotal();
        this.estadoAtual = memento.getEstadoAtual();
        
        System.out.println("Originator: Estado restaurado após usar Memento. Retornado ao ponto: " + memento.getMotivo());
    }

    // Modificador extra para simular perda de progresso
    public void sofrerPenalidadeXP(float pontosPerdidos) {
        this.experienciaTotal -= pontosPerdidos;
        System.out.println("[" + nomePet + "] Sofreu penalidade de " + pontosPerdidos + " XP.");
    }
    
    @Override
    public String toString() {
        return "PetVirtual {nome='" + nomePet + "', nivel=" + nivel + ", expTotal=" + experienciaTotal + "}";
    }
}