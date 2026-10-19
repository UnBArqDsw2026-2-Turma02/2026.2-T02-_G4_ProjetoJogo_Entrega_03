package observer;

import java.util.ArrayList;
import java.util.List;

public abstract class AssuntoAtividade {

    private final List<ObservadorAtividade> observadores =
            new ArrayList<>();

    public void adicionarObservador(ObservadorAtividade obs) {
        if (obs != null && !observadores.contains(obs)) {
            observadores.add(obs);
        }
    }

    public void removerObservador(ObservadorAtividade obs) {
        observadores.remove(obs);
    }

    protected void notificarObservadores(
            EventoConclusaoAtividade evento) {

        List<ObservadorAtividade> copia =
                new ArrayList<>(observadores);

        for (ObservadorAtividade observador : copia) {
            observador.emAtividadeConcluida(evento);
        }
    }
}