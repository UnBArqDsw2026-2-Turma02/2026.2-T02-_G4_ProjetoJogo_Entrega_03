package app;

import atividades.SessaoPomodoro;
import dominio.CategoriaXP;
import dominio.PetVirtual;
import observer.GerenciadorConquistas;

public class Main {

    public static void main(String[] args) {

        SessaoPomodoro sessao =
                new SessaoPomodoro(CategoriaXP.INTELECTUAL);

        PetVirtual pet = new PetVirtual();

        GerenciadorConquistas gerenciador =
                new GerenciadorConquistas();

        sessao.adicionarObservador(pet);
        sessao.adicionarObservador(gerenciador);

        System.out.println("Finalizando ciclo Pomodoro...");

        sessao.finalizarCicloComSucesso();

        sessao.removerObservador(gerenciador);
    }
}