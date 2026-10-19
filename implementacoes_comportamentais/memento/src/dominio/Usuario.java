package dominio;

public class Usuario {
    private String idUsuario;
    private String nomeExibicao;

    public Usuario(String idUsuario, String nomeExibicao) {
        this.idUsuario = idUsuario;
        this.nomeExibicao = nomeExibicao;
    }

    public String getIdUsuario() { return idUsuario; }
    public String getNomeExibicao() { return nomeExibicao; }
}