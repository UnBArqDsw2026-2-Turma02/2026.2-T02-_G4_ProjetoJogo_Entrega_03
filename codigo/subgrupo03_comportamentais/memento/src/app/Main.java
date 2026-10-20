package app;

import dominio.CategoriaXP;
import dominio.PetVirtual;
import memento.HistoricoPet;
import memento.MementoPet;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== EXECUÇÃO INDIVIDUAL: PADRÃO MEMENTO ===\n");

        PetVirtual pet = new PetVirtual("Tamagoshi");
        HistoricoPet caretaker = new HistoricoPet();

        System.out.println("--- 1. Estado Inicial ---");
        System.out.println(pet);
        
        System.out.println("\n--- 2. Progresso do Pet ---");
        pet.acumularExperiencia(CategoriaXP.SABEDORIA, 150.0f);
        pet.acumularExperiencia(CategoriaXP.INTELECTUAL, 50.0f);
        System.out.println(pet);

        System.out.println("\n--- 3. Salvando Snapshot de Segurança ---");
        // O Cliente orquestra: Pede ao Originator para criar o Memento e passa para o Caretaker guardar
        MementoPet snapshotSeguranca = pet.salvarEstado("Backup pré-quebra de ofensiva");
        caretaker.adicionarMemento(snapshotSeguranca);

        System.out.println("\n--- 4. Penalidade Sofrida ---");
        pet.sofrerPenalidadeXP(120.0f);
        System.out.println(pet);

        System.out.println("\n--- 5. Restaurando o Estado (Acionando o Memento) ---");
        // O Cliente orquestra: Pede o Memento ao Caretaker e repassa ao Originator
        MementoPet mementoRecuperado = caretaker.getUltimoMemento();
        if (mementoRecuperado != null) {
            pet.restaurarEstado(mementoRecuperado);
        }
        
        System.out.println("\n--- 6. Estado Final ---");
        System.out.println(pet);
    }
}