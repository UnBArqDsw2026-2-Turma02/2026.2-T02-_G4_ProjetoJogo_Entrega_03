package app;

import strategy.*;
import dominio.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== EXECUÇÃO INDIVIDUAL: PADRÃO STRATEGY ===\n");

        CalculoXPStrategy regraAgua = new CalculoXPAguaStrategy();
        CalculoXPStrategy regraHabito = new CalculoXPHabitoStrategy();
        CalculoXPStrategy regraPomodoro = new CalculoXPPomodoroStrategy();

        ContagemDeAgua agua = new ContagemDeAgua();
        agua.setEstrategiaXP(regraAgua);
        System.out.println("-> XP Água (100%): " + agua.calcularExperienciaGerada());

        Habito leitura = new Habito();
        leitura.setEstrategiaXP(regraHabito);
        System.out.println("-> XP Hábito (Streak 3): " + leitura.calcularExperienciaGerada());

        SessaoPomodoro estudo = new SessaoPomodoro();
        estudo.setEstrategiaXP(regraPomodoro);
        System.out.println("-> XP Pomodoro (25 min + Conclusão): " + estudo.calcularRecompensaExperiencia());
    }
}