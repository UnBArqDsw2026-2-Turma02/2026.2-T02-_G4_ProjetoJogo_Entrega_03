/**
 * Entrega 03 · Subgrupo 02 · GoF Criacional — Factory Method (Método Fábrica)
 * Projeto G4 — Mascote Virtual & Pomodoro
 *
 * Participantes do padrão (GAMMA et al., 1994):
 *   Product          → Atividade (abstrata)
 *   ConcreteProduct  → SessaoPomodoro, CheckinHabito, RegistroHidratacao
 *   Creator          → CriadorDeAtividade (declara o factory method criarAtividade)
 *   ConcreteCreator  → CriadorSessaoPomodoro, CriadorCheckinHabito, CriadorRegistroHidratacao
 *
 * Rastreabilidade com a Entrega 02: RF01, RF02, RF03, RF05, RF06 e RF11; regras RN01 e RN02;
 * Diagrama de Sequência "Sessão Pomodoro concluída → XP → Evolução do Mascote".
 *
 * Autor: João Vitor Mendonça Merlin (@jvopBR)
 * Execução: node factory_method_atividades.js
 */

'use strict';

/**
 * RN02: o valor de cada categoria é o índice dela no vetor de XP de 5 posições do mascote.
 */
const CategoriaXP = Object.freeze({
  INTELECTUAL: 0,
  SABEDORIA: 1,
  ZEN: 2,
  ATLETICO: 3,
  HIDRATACAO: 4
});

const NOME_CATEGORIA = Object.freeze(Object.keys(CategoriaXP));

/* ------------------------------------------------------------------ *
 * PRODUCT — contrato comum de tudo o que o usuário conclui e vira XP
 * ------------------------------------------------------------------ */
class Atividade {
  constructor(categoria, data = new Date()) {
    if (new.target === Atividade) {
      throw new Error('Atividade é abstrata: instancie uma atividade concreta.');
    }
    if (!Object.values(CategoriaXP).includes(categoria)) {
      throw new Error('Categoria de XP inválida (RN02).');
    }
    this.categoria = categoria;
    this.data = data;
  }

  calcularXP() { throw new Error('calcularXP() deve ser implementado pela atividade concreta.'); }
  validar() { throw new Error('validar() deve ser implementado pela atividade concreta.'); }
  descrever() { throw new Error('descrever() deve ser implementado pela atividade concreta.'); }

  getCategoria() { return this.categoria; }
  getNomeCategoria() { return NOME_CATEGORIA[this.categoria]; }
}

/* ------------------------------------------------------------------ *
 * CONCRETE PRODUCTS
 * ------------------------------------------------------------------ */

/** RF01 e RF03 — sessão de foco concluída. RN01: 25 min concluídos = +50 XP. */
class SessaoPomodoro extends Atividade {
  static DURACAO_CICLO_MIN = 25;
  static XP_POR_CICLO = 50;

  constructor({ tempoFocadoMin, tarefa, categoria, duracaoCicloMin = SessaoPomodoro.DURACAO_CICLO_MIN }) {
    super(categoria);
    this.tempoFocadoMin = Number(tempoFocadoMin);
    this.tarefa = String(tarefa ?? '').trim();
    this.duracaoCicloMin = duracaoCicloMin;
  }

  validar() {
    if (!Number.isFinite(this.tempoFocadoMin) || this.tempoFocadoMin < this.duracaoCicloMin) {
      throw new Error(
        `Sessão não concluída: são necessários ao menos ${this.duracaoCicloMin} min de foco (RN01).`
      );
    }
    if (!this.tarefa) {
      throw new Error('Sessão inválida: informe a tarefa associada (RF03).');
    }
  }

  calcularXP() {
    const ciclos = Math.floor(this.tempoFocadoMin / this.duracaoCicloMin);
    return ciclos * SessaoPomodoro.XP_POR_CICLO;
  }

  descrever() {
    return `Pomodoro de ${this.tempoFocadoMin} min em "${this.tarefa}"`;
  }
}

/** RF05, RF07 e RF09 — check-in diário de hábito. RN03: só conta em dia ativo. */
class CheckinHabito extends Atividade {
  // RN01 credita XP pelo check-in, mas não fixa o valor: parâmetro acordado pela equipe.
  static XP_POR_CHECKIN = 20;

  constructor({ habito, categoria, diasAtivosSemana = [1, 2, 3, 4, 5, 6, 7], diaDaSemana }) {
    super(categoria);
    this.habito = String(habito ?? '').trim();
    this.diasAtivosSemana = diasAtivosSemana;
    this.diaDaSemana = diaDaSemana ?? ((this.data.getDay() + 6) % 7) + 1; // 1 = segunda
  }

  validar() {
    if (!this.habito) {
      throw new Error('Check-in inválido: informe o hábito (RF07).');
    }
    if (!this.diasAtivosSemana.includes(this.diaDaSemana)) {
      throw new Error(`Check-in fora dos dias ativos do hábito "${this.habito}" (RN03).`);
    }
  }

  calcularXP() { return CheckinHabito.XP_POR_CHECKIN; }

  descrever() { return `Check-in do hábito "${this.habito}"`; }
}

/** RF06 — ingestão de água. RN01: cada 250 ml creditam XP em HIDRATACAO. */
class RegistroHidratacao extends Atividade {
  static COPO_ML = 250;
  static META_DIARIA_ML = 2000;
  // Também é parâmetro da equipe: RN01 não fixa o XP por copo.
  static XP_POR_COPO = 10;

  constructor({ mililitros }) {
    super(CategoriaXP.HIDRATACAO);
    this.mililitros = Number(mililitros);
  }

  validar() {
    if (!Number.isFinite(this.mililitros) || this.mililitros < RegistroHidratacao.COPO_ML) {
      throw new Error(`Registro inválido: mínimo de ${RegistroHidratacao.COPO_ML} ml por registro (RN01).`);
    }
  }

  calcularXP() {
    const copos = Math.floor(this.mililitros / RegistroHidratacao.COPO_ML);
    return copos * RegistroHidratacao.XP_POR_COPO;
  }

  descrever() { return `Hidratação de ${this.mililitros} ml`; }
}

/* ------------------------------------------------------------------ *
 * CREATOR — o fluxo comum fica aqui; só a criação do produto varia
 * ------------------------------------------------------------------ */
class CriadorDeAtividade {
  /** Factory Method: cada criador concreto decide qual Atividade instanciar. */
  criarAtividade(dados) { // eslint-disable-line no-unused-vars
    throw new Error('criarAtividade() deve ser implementado pelo criador concreto.');
  }

  /**
   * Fluxo idêntico para qualquer atividade concluída, sem conhecer a classe concreta:
   * criar → validar → calcular XP → registrar no histórico → creditar no mascote.
   */
  registrarAtividade(dados, { historico, mascote }) {
    const atividade = this.criarAtividade(dados); // ← único ponto de variação
    atividade.validar();

    const xp = atividade.calcularXP();
    historico.registrarSessao(atividade);
    mascote.receberXP(xp, atividade.getCategoria());

    return {
      atividade: atividade.descrever(),
      categoria: atividade.getNomeCategoria(),
      xp,
      ofensivaDiaria: historico.calcularOfensivaDiaria()
    };
  }
}

/* ------------------------------------------------------------------ *
 * CONCRETE CREATORS
 * ------------------------------------------------------------------ */
class CriadorSessaoPomodoro extends CriadorDeAtividade {
  constructor(duracaoCicloMin = SessaoPomodoro.DURACAO_CICLO_MIN) {
    super();
    this.duracaoCicloMin = duracaoCicloMin;
  }

  criarAtividade({ tempoFocadoMin, tarefa, categoria }) {
    return new SessaoPomodoro({ tempoFocadoMin, tarefa, categoria, duracaoCicloMin: this.duracaoCicloMin });
  }
}

class CriadorCheckinHabito extends CriadorDeAtividade {
  criarAtividade({ habito, categoria, diasAtivosSemana, diaDaSemana }) {
    return new CheckinHabito({ habito, categoria, diasAtivosSemana, diaDaSemana });
  }
}

class CriadorRegistroHidratacao extends CriadorDeAtividade {
  constructor(metaDiariaMl = RegistroHidratacao.META_DIARIA_ML) {
    super();
    this.metaDiariaMl = metaDiariaMl;
  }

  criarAtividade({ mililitros }) {
    return new RegistroHidratacao({ mililitros });
  }
}

/* ------------------------------------------------------------------ *
 * COLABORADORES — versões mínimas para a demonstração.
 * Na aplicação integrada, `mascote` é o objeto montado pelo Builder
 * (tamagotchi_builder.js) e `historico` é a classe HistoricoTarefa do
 * Diagrama de Classes da Entrega 02.
 * ------------------------------------------------------------------ */
class HistoricoTarefa {
  constructor() { this.registros = []; }

  registrarSessao(atividade) {
    this.registros.push({ data: atividade.data, descricao: atividade.descrever() });
  }

  /** Simplificação: conta os dias distintos com registro (RF08). */
  calcularOfensivaDiaria() {
    return new Set(this.registros.map(r => r.data.toISOString().slice(0, 10))).size;
  }
}

class Mascote {
  // Limiares da sub-máquina de evolução (Diagrama de Estados da Entrega 02).
  static LIMIAR_JOVEM = 150;
  static LIMIAR_ADULTO = 400;

  constructor(nome) {
    this.nome = nome;
    this.estagioVida = 'FILHOTE';
    this.vetorXP = [0, 0, 0, 0, 0]; // RN02
    this.xpTotal = 0;
  }

  receberXP(pontos, categoria) {
    this.vetorXP[categoria] += pontos;
    this.xpTotal += pontos;
    this.ganharXP(pontos);
  }

  ganharXP() {
    const anterior = this.estagioVida;
    if (this.xpTotal >= Mascote.LIMIAR_ADULTO) this.estagioVida = 'ADULTO';
    else if (this.xpTotal >= Mascote.LIMIAR_JOVEM) this.estagioVida = 'JOVEM';
    if (anterior !== this.estagioVida) {
      console.log(`   [EVOLUCAO] ${this.nome}: ${anterior} -> ${this.estagioVida} (XP total ${this.xpTotal})`);
    }
  }

  afinidade() {
    const maior = Math.max(...this.vetorXP);
    return NOME_CATEGORIA[this.vetorXP.indexOf(maior)];
  }
}

/* ------------------------------------------------------------------ *
 * DEMONSTRAÇÃO
 * ------------------------------------------------------------------ */
function demonstrar() {
  const historico = new HistoricoTarefa();
  const mascote = new Mascote('Tama');

  // A aplicação escolhe o criador conforme a tela/ação do usuário.
  const criadorPomodoro = new CriadorSessaoPomodoro();
  const criadorHabito = new CriadorCheckinHabito();
  const criadorAgua = new CriadorRegistroHidratacao();

  console.log('=== Factory Method: atividades que geram XP ===\n');

  console.log('[1] Sessao Pomodoro (RF01/RN01)');
  console.log('   ', criadorPomodoro.registrarAtividade(
    { tempoFocadoMin: 50, tarefa: 'Arquitetura e Desenho de Software', categoria: CategoriaXP.INTELECTUAL },
    { historico, mascote }
  ));

  console.log('\n[2] Check-in de habito (RF05/RN03)');
  console.log('   ', criadorHabito.registrarAtividade(
    { habito: 'Meditar 10 min', categoria: CategoriaXP.ZEN, diasAtivosSemana: [1, 2, 3, 4, 5], diaDaSemana: 3 },
    { historico, mascote }
  ));

  console.log('\n[3] Registro de hidratacao (RF06/RN01)');
  console.log('   ', criadorAgua.registrarAtividade(
    { mililitros: 750 },
    { historico, mascote }
  ));

  console.log('\n[4] Validacao: sessao interrompida antes dos 25 min');
  try {
    criadorPomodoro.registrarAtividade(
      { tempoFocadoMin: 10, tarefa: 'Leitura', categoria: CategoriaXP.SABEDORIA },
      { historico, mascote }
    );
  } catch (erro) {
    console.log('    [REJEITADO]', erro.message);
  }

  console.log('\n[5] Validacao: check-in em dia nao ativo do habito');
  try {
    criadorHabito.registrarAtividade(
      { habito: 'Correr', categoria: CategoriaXP.ATLETICO, diasAtivosSemana: [6, 7], diaDaSemana: 2 },
      { historico, mascote }
    );
  } catch (erro) {
    console.log('    [REJEITADO]', erro.message);
  }

  console.log('\n=== Estado final do mascote ===');
  console.log('    Vetor de XP por categoria:', NOME_CATEGORIA.map((n, i) => `${n}=${mascote.vetorXP[i]}`).join(' | '));
  console.log('    XP total:', mascote.xpTotal, '| Estagio de vida:', mascote.estagioVida, '| Afinidade:', mascote.afinidade());
  console.log('    Atividades no historico:', historico.registros.length, '| Ofensiva diaria:', historico.calcularOfensivaDiaria());
}

if (typeof module !== 'undefined' && require.main === module) {
  demonstrar();
}

if (typeof module !== 'undefined') {
  module.exports = {
    CategoriaXP,
    Atividade,
    SessaoPomodoro,
    CheckinHabito,
    RegistroHidratacao,
    CriadorDeAtividade,
    CriadorSessaoPomodoro,
    CriadorCheckinHabito,
    CriadorRegistroHidratacao,
    HistoricoTarefa,
    Mascote,
    demonstrar
  };
}
