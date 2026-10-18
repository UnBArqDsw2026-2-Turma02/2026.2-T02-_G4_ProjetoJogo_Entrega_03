package app;

import strategy.*;
import atividades.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== TESTE DO NOVO DIAGRAMA STRATEGY ===");

        // 1. Inicializar Estratégias
        CalculoXPStrategy regraAgua = new CalculoXPAguaStrategy();
        CalculoXPStrategy regraHabito = new CalculoXPHabitoStrategy();
        CalculoXPStrategy regraPomodoro = new CalculoXPPomodoroStrategy();

        // 2. Testar Contagem de Água
        ContagemDeAgua agua = new ContagemDeAgua();
        agua.setEstrategiaXP(regraAgua);
        System.out.println("XP Água: " + agua.calcularExperienciaGerada());

        // 3. Testar Hábito
        Habito leitura = new Habito();
        leitura.setEstrategiaXP(regraHabito);
        System.out.println("XP Hábito: " + leitura.calcularExperienciaGerada());

        // 4. Testar Sessão Pomodoro
        SessaoPomodoro estudo = new SessaoPomodoro();
        estudo.setEstrategiaXP(regraPomodoro);
        System.out.println("XP Pomodoro: " + estudo.calcularRecompensaExperiencia());
    }
}