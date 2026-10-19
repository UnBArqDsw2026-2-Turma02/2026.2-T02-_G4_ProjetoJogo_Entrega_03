package app;

import atividades.SessaoPomodoro;
import dominio.CategoriaXP;
import dominio.PetVirtual;

public class Main {

    public static void main(String[] args) {

        // Teste do State - Pomodoro
        SessaoPomodoro sessao = new SessaoPomodoro();

        sessao.iniciarCiclo();
        sessao.pausarCiclo();
        sessao.retomarCiclo();
        sessao.finalizarCicloComSucesso();

        System.out.println();

        // Teste do State - Pet Virtual
        PetVirtual pet = new PetVirtual();

        pet.acumularExperiencia(CategoriaXP.INTELECTUAL, 50.0f);
        pet.acumularExperiencia(CategoriaXP.ZEN, 60.0f);
        pet.acumularExperiencia(CategoriaXP.ATLETICO, 200.0f);
        pet.acumularExperiencia(CategoriaXP.SABEDORIA, 300.0f);
    }
}