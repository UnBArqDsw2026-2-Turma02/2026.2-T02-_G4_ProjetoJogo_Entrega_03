package observer;

public class GerenciadorConquistas
        implements ObservadorAtividade {

    @Override
    public void emAtividadeConcluida(
            EventoConclusaoAtividade evento) {

        System.out.println(
                "[Gerenciador de conquistas] evento capturado."
        );

        System.out.println(" -> Categoria: " + evento.getCategoria() + " | XP Gerado: " + evento.getXPGerado()); 
        
        System.out.println(" -> Verificando requisitos para concessão de conquistas...");
    }
}