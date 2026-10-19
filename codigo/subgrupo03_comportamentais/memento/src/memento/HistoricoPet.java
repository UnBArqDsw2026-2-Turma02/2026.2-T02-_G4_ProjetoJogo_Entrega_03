package memento;

import java.util.ArrayList;
import java.util.List;

public class HistoricoPet {
    private final List<MementoPet> mementos = new ArrayList<>();
    private final int limiteSnapshots = 10;

    public void adicionarMemento(MementoPet memento) {
        if (mementos.size() >= limiteSnapshots) {
            mementos.remove(0); 
        }
        mementos.add(memento);
        System.out.println("Caretaker: Snapshot armazenado com segurança.");
    }

    public MementoPet getUltimoMemento() {
        if (!mementos.isEmpty()) {
            return mementos.remove(mementos.size() - 1);
        }
        System.out.println("Caretaker: Nenhum histórico disponível.");
        return null;
    }
    
    public MementoPet getMemento(int index) {
        if (index >= 0 && index < mementos.size()) {
            return mementos.get(index);
        }
        return null;
    }
}