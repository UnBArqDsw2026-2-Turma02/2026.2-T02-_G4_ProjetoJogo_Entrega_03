package observer;

import dominio.CategoriaXP;

public class EventoConclusaoAtividade {

    private final CategoriaXP categoria;
    private final float xpGerado;

    public EventoConclusaoAtividade(
            CategoriaXP categoria,
            float xpGerado) {

        this.categoria = categoria;
        this.xpGerado = xpGerado;
    }

    public CategoriaXP getCategoria() {
        return categoria;
    }

    public float getXPGerado() {
        return xpGerado;
    }
}