/**
 * Padrão GoF Criacional: Builder (Construtor)
 * Projeto: G4_ProjetoJogo - Mascote Virtual & Pomodoro (Tamagotchi)
 * Disciplina: Arquitetura e Desenho de Software (FCTE/UnB)
 * Docente: Profa. Milene Serrano
 * 
 * Rastreabilidade:
 * - Entrega 01: BPMN (Task_S_InicializaPet, Task_J_DigitaNome, SubProcess_S_Tick)
 * - Entrega 02: Diagrama de Classes v2 (Danilo Barros) e Diagrama de Estados do Mascote (João Vitor Merlin)
 * - Entrega 03: FOCO_01 - GoF Criacional Builder
 * 
 * Responsável pela Implementação: Danilo Sarmento Barros (222008468)
 */

// ============================================================================
// 1. DOMÍNIO AUXILIAR: ITENS ESPECIALIZADOS (Diagrama de Classes v2 - Entrega 02)
// ============================================================================
class Item {
    constructor(nome, tipo, efeito) {
        this.nome = nome;
        this.tipo = tipo; // 'ALIMENTO', 'REMEDIO', 'LIMPEZA'
        this.efeito = efeito;
    }
}

class Alimento extends Item {
    constructor(nome, recuperaFome, bonusFelicidade = 5) {
        super(nome, 'ALIMENTO', { fome: recuperaFome, felicidade: bonusFelicidade });
    }
}

class Remedio extends Item {
    constructor(nome, curaSaude = 30) {
        super(nome, 'REMEDIO', { saude: curaSaude });
    }
}

class ItemLimpeza extends Item {
    constructor(nome, recuperaLimpeza = 40) {
        super(nome, 'LIMPEZA', { limpeza: recuperaLimpeza });
    }
}

// ============================================================================
// 2. PRODUCT (Produto Complexo: Mascote / Pet)
// ============================================================================
class Mascote {
    constructor() {
        this.nome = 'Mascote Sem Nome';
        this.estagioVida = 'FILHOTE'; // 'OVO', 'FILHOTE', 'JOVEM', 'ADULTO' (Entrega 02)
        this.estadoSaude = 'SAUDAVEL'; // 'SAUDAVEL', 'FAMINTA', 'SUJA', 'DOENTE' (Entrega 02)
        this.temperamento = 'EQUILIBRADO'; // 'EQUILIBRADO', 'COMILAO', 'BRINCALHAO', 'PREGUICOSO'
        this.xp = 0;
        
        // Atributos vitais (Regra clássica do BPMN da Entrega 01 e Diagrama de Classes da Entrega 02)
        this.atributos = {
            fome: 80,
            felicidade: 80,
            energia: 100,
            limpeza: 100,
            saude: 80
        };

        // Taxas de decaimento contínuo por segundo (tick)
        this.taxasDecaimento = {
            fome: 1.0,
            felicidade: 0.8,
            energia: 0.5,
            limpeza: 0.7
        };

        // Inventário inicial de itens especializados (Entrega 02)
        this.inventario = [];
        this.dataCriacao = new Date().toISOString();
        this.dormindo = false;
        this.desmaiado = false;
    }

    /**
     * Executa o ciclo contínuo do motor de jogo (SubProcess_S_Tick do BPMN)
     */
    tick() {
        if (this.desmaiado) {
            return `[ALERTA] ${this.nome} está desmaiado! Pressione A para reviver com 50 nos atributos.`;
        }

        // Aplica taxas de decaimento com precisão decimal
        this.atributos.fome = Math.max(0, +(this.atributos.fome - this.taxasDecaimento.fome).toFixed(1));
        this.atributos.felicidade = Math.max(0, +(this.atributos.felicidade - this.taxasDecaimento.felicidade).toFixed(1));
        this.atributos.limpeza = Math.max(0, +(this.atributos.limpeza - this.taxasDecaimento.limpeza).toFixed(1));

        if (this.dormindo) {
            this.atributos.energia = Math.min(100, +(this.atributos.energia + 2.0).toFixed(1));
            if (this.atributos.energia >= 80) this.dormindo = false;
        } else {
            this.atributos.energia = Math.max(0, +(this.atributos.energia - this.taxasDecaimento.energia).toFixed(1));
            if (this.atributos.energia === 0) this.dormindo = true;
        }

        // Atualização da máquina de estados de saúde (Diagrama de Estados da Entrega 02)
        if (this.atributos.fome < 20) this.estadoSaude = 'FAMINTA';
        else if (this.atributos.limpeza < 20) this.estadoSaude = 'SUJA';
        else if (this.atributos.saude < 30) this.estadoSaude = 'DOENTE';
        else this.estadoSaude = 'SAUDAVEL';

        // Fator de risco sobre a saúde
        const emRisco = this.atributos.fome < 20 || this.atributos.felicidade < 20 || this.atributos.limpeza < 20;
        if (emRisco) {
            this.atributos.saude = Math.max(0, +(this.atributos.saude - 2.0).toFixed(1));
            if (this.atributos.saude === 0) {
                this.desmaiado = true;
                this.estadoSaude = 'DOENTE';
            }
        }

        return `Tick: Fome=${this.atributos.fome}% | Felicidade=${this.atributos.felicidade}% | Energia=${this.atributos.energia}% | Limpeza=${this.atributos.limpeza}% | Saúde=${this.atributos.saude}% [Estado: ${this.estadoSaude}]`;
    }

    descrever() {
        return `
+------------------------------------------------------------------+
| CARTÃO DE STATUS DO MASCOTE (G4_PROJETOJOGO)                     |
+------------------------------------------------------------------+
| Nome: ${this.nome.padEnd(20)} Estágio: ${this.estagioVida.padEnd(12)} Saúde: ${this.estadoSaude.padEnd(10)} |
| Temperamento: ${this.temperamento.padEnd(12)} XP: ${String(this.xp).padEnd(10)} Criado em: ${this.dataCriacao.substring(0, 10)} |
+------------------------------------------------------------------+
| Atributos Vitais:                                                |
|   - Fome (HUN):       [${this._barra(this.atributos.fome)}] ${this.atributos.fome}%
|   - Felicidade (HAP): [${this._barra(this.atributos.felicidade)}] ${this.atributos.felicidade}%
|   - Energia (ENG):    [${this._barra(this.atributos.energia)}] ${this.atributos.energia}%
|   - Limpeza (CLN):    [${this._barra(this.atributos.limpeza)}] ${this.atributos.limpeza}%
|   - Saúde (HLT):      [${this._barra(this.atributos.saude)}] ${this.atributos.saude}%
+------------------------------------------------------------------+
| Taxas Decaimento/tick: HUN -${this.taxasDecaimento.fome} | HAP -${this.taxasDecaimento.felicidade} | ENG -${this.taxasDecaimento.energia} | CLN -${this.taxasDecaimento.limpeza}
| Inventário Inicial (${this.inventario.length} itens): [${this.inventario.map(i => i.nome).join(', ')}]
| Sprite LCD:
${this._sprite()}
+------------------------------------------------------------------+`;
    }

    _barra(valor) {
        const preenchido = Math.round((valor / 100) * 10);
        return '#'.repeat(preenchido) + '-'.repeat(10 - preenchido);
    }

    _sprite() {
        switch (this.estagioVida) {
            case 'OVO':     return '         ( O ) \n        (  o  )\n         (---) ';
            case 'FILHOTE': return '        (^-^)  \n       /( | )\\ \n         d b   ';
            case 'JOVEM':   return '       d(^_^)b \n       /( : )\\ \n         d b   ';
            case 'ADULTA':
            case 'ADULTO':
            default:        return '       \\(^o^)/ \n       <( : )> \n        /   \\  ';
        }
    }
}

// ============================================================================
// 3. BUILDER (Interface Abstrata)
// ============================================================================
class MascoteBuilder {
    reset() { throw new Error('reset() deve ser implementado'); }
    definirNome(nome) { throw new Error('definirNome() deve ser implementado'); }
    definirEstagioVida(estagio) { throw new Error('definirEstagioVida() deve ser implementado'); }
    definirTemperamento(temperamento) { throw new Error('definirTemperamento() deve ser implementado'); }
    definirAtributosVitais(atributos) { throw new Error('definirAtributosVitais() deve ser implementado'); }
    definirTaxasDecaimento(taxas) { throw new Error('definirTaxasDecaimento() deve ser implementado'); }
    adicionarItemInventario(item) { throw new Error('adicionarItemInventario() deve ser implementado'); }
    definirInventario(itens) { throw new Error('definirInventario() deve ser implementado'); }
    construir() { throw new Error('construir() deve ser implementado'); }
}

// ============================================================================
// 4. CONCRETE BUILDER (Construtor Concreto Fluente)
// ============================================================================
class MascoteConcretoBuilder extends MascoteBuilder {
    constructor() {
        super();
        this.reset();
    }

    reset() {
        this.mascote = new Mascote();
        return this;
    }

    definirNome(nome) {
        if (!nome || typeof nome !== 'string' || nome.trim() === '') {
            throw new Error('[Builder Erro] Nome do mascote não pode ser vazio.');
        }
        this.mascote.nome = nome.trim();
        return this;
    }

    definirEstagioVida(estagio) {
        const estagiosValidos = ['OVO', 'FILHOTE', 'JOVEM', 'ADULTO'];
        if (!estagiosValidos.includes(estagio)) {
            throw new Error(`[Builder Erro] Estágio de vida inválido: ${estagio}`);
        }
        this.mascote.estagioVida = estagio;
        return this;
    }

    definirTemperamento(temperamento) {
        const temperamentosValidos = ['EQUILIBRADO', 'COMILAO', 'BRINCALHAO', 'PREGUICOSO'];
        if (!temperamentosValidos.includes(temperamento)) {
            throw new Error(`[Builder Erro] Temperamento inválido: ${temperamento}`);
        }
        this.mascote.temperamento = temperamento;
        return this;
    }

    definirAtributosVitais(atributos) {
        const clamp = (val, padrao) => Math.max(0, Math.min(100, Number(val ?? padrao)));
        this.mascote.atributos = {
            fome: clamp(atributos.fome, 80),
            felicidade: clamp(atributos.felicidade, 80),
            energia: clamp(atributos.energia, 100),
            limpeza: clamp(atributos.limpeza, 100),
            saude: clamp(atributos.saude, 80)
        };
        return this;
    }

    definirTaxasDecaimento(taxas) {
        if (taxas) {
            this.mascote.taxasDecaimento = {
                fome: taxas.fome !== undefined ? Number(taxas.fome) : 1.0,
                felicidade: taxas.felicidade !== undefined ? Number(taxas.felicidade) : 0.8,
                energia: taxas.energia !== undefined ? Number(taxas.energia) : 0.5,
                limpeza: taxas.limpeza !== undefined ? Number(taxas.limpeza) : 0.7
            };
        } else {
            this._calcularDecaimentoPorTemperamento();
        }
        return this;
    }

    _calcularDecaimentoPorTemperamento() {
        switch (this.mascote.temperamento) {
            case 'COMILAO':
                this.mascote.taxasDecaimento = { fome: 1.8, felicidade: 0.8, energia: 0.5, limpeza: 0.8 };
                break;
            case 'BRINCALHAO':
                this.mascote.taxasDecaimento = { fome: 1.0, felicidade: 1.6, energia: 0.9, limpeza: 0.9 };
                break;
            case 'PREGUICOSO':
                this.mascote.taxasDecaimento = { fome: 0.8, felicidade: 0.7, energia: 1.3, limpeza: 0.5 };
                break;
            case 'EQUILIBRADO':
            default:
                this.mascote.taxasDecaimento = { fome: 1.0, felicidade: 0.8, energia: 0.5, limpeza: 0.7 };
                break;
        }
    }

    adicionarItemInventario(item) {
        if (!(item instanceof Item)) {
            throw new Error('[Builder Erro] Item deve ser uma instância da classe Item.');
        }
        this.mascote.inventario.push(item);
        return this;
    }

    definirInventario(itens) {
        if (!Array.isArray(itens)) {
            throw new Error('[Builder Erro] Inventário deve ser um Array de itens.');
        }
        this.mascote.inventario = [...itens];
        return this;
    }

    construir() {
        if (!this.mascote.nome) {
            throw new Error('[Builder Integridade] Não é possível construir mascote sem nome.');
        }
        if (!this.mascote.taxasDecaimento) {
            this._calcularDecaimentoPorTemperamento();
        }

        const produto = this.mascote;
        this.reset();
        return produto;
    }
}

// ============================================================================
// 5. DIRECTOR (Diretor com Receitas Oficiais do Projeto)
// ============================================================================
class MascoteDirector {
    constructor(builder) {
        this.builder = builder;
    }

    setBuilder(builder) {
        this.builder = builder;
    }

    /**
     * Constrói o Mascote Clássico da Entrega 01 (BPMN) e Entrega 02 (Diagrama de Classes v2)
     * Atributos: 80/80/100/100/80, Estágio: FILHOTE, Inventário com Alimento, Remédio e Limpeza.
     */
    construirMascotePadrao(nome) {
        return this.builder
            .reset()
            .definirNome(nome)
            .definirEstagioVida('FILHOTE')
            .definirTemperamento('EQUILIBRADO')
            .definirAtributosVitais({ fome: 80, felicidade: 80, energia: 100, limpeza: 100, saude: 80 })
            .definirTaxasDecaimento({ fome: 1.0, felicidade: 0.8, energia: 0.5, limpeza: 0.7 })
            .definirInventario([
                new Alimento('Maçã Pomodoro', 25, 10),
                new Remedio('Pílula de Foco', 30),
                new ItemLimpeza('Sabonete Anti-Distração', 40)
            ])
            .construir();
    }

    /**
     * Constrói o Mascote Desafiador / Hardcore (Taxas elevadas de decaimento)
     */
    construirMascoteHardcore(nome) {
        return this.builder
            .reset()
            .definirNome(nome)
            .definirEstagioVida('JOVEM')
            .definirTemperamento('BRINCALHAO')
            .definirAtributosVitais({ fome: 50, felicidade: 50, energia: 70, limpeza: 50, saude: 60 })
            .definirTaxasDecaimento({ fome: 2.2, felicidade: 2.0, energia: 1.5, limpeza: 1.8 })
            .definirInventario([
                new Alimento('Café Expresso', 15, 5)
            ])
            .construir();
    }

    /**
     * Constrói o Mascote Inicial (Ovo recém-iniciado)
     */
    construirMascoteOvo(nome) {
        return this.builder
            .reset()
            .definirNome(nome)
            .definirEstagioVida('OVO')
            .definirTemperamento('PREGUICOSO')
            .definirAtributosVitais({ fome: 100, felicidade: 100, energia: 100, limpeza: 100, saude: 100 })
            .definirTaxasDecaimento({ fome: 0.3, felicidade: 0.3, energia: 0.3, limpeza: 0.2 })
            .definirInventario([])
            .construir();
    }
}

// ============================================================================
// 6. CLIENT & DEMONSTRAÇÃO DO PADRÃO EM EXECUÇÃO
// ============================================================================
function demonstrarPadraoBuilder() {
    console.log('================================================================');
    console.log(' PADRÃO GOF CRIACIONAL: BUILDER - MASCOTE VIRTUAL & POMODORO    ');
    console.log(' Entrega 03 · Subgrupo 02 · G4_ProjetoJogo (UnB - 2026.2)       ');
    console.log(' Responsável: Danilo Sarmento Barros (222008468)                ');
    console.log('================================================================\n');

    const builder = new MascoteConcretoBuilder();
    const director = new MascoteDirector(builder);

    // 1. Construção via Director: Perfil Clássico (Rastreabilidade com Entrega 01 e 02)
    console.log('>>> [1] Construção via Director: Mascote Padrão (Entrega 01/02)...');
    const mascoteClassico = director.construirMascotePadrao('Tama-Danilo');
    console.log(mascoteClassico.descrever());

    // 2. Construção via Director: Perfil Hardcore
    console.log('>>> [2] Construção via Director: Mascote Hardcore (Desafio)...');
    const mascoteHard = director.construirMascoteHardcore('Spike-Desafio');
    console.log(mascoteHard.descrever());

    // 3. Construção Customizada Fluente (Direto pelo Builder)
    console.log('>>> [3] Construção customizada fluente via MascoteConcretoBuilder...');
    const mascoteCustom = builder
        .reset()
        .definirNome('Luna-Estudos')
        .definirEstagioVida('ADULTO')
        .definirTemperamento('COMILAO')
        .definirAtributosVitais({ fome: 90, felicidade: 95, energia: 85, limpeza: 90, saude: 100 })
        .definirTaxasDecaimento({ fome: 1.8, felicidade: 1.0, energia: 0.8, limpeza: 1.0 })
        .definirInventario([
            new Alimento('Banquete Pomodoro Especial', 50, 20),
            new Remedio('Elixir Restaurador Total', 100),
            new ItemLimpeza('Ducha Revigorante', 50)
        ])
        .construir();
    console.log(mascoteCustom.descrever());

    // 4. Ciclo em tempo real (Simulação de 3 Ticks da Engine de tempo contínuo)
    console.log('>>> [4] Execução em tempo real: Simulação de 3 ticks no Mascote Padrão:');
    for (let t = 1; t <= 3; t++) {
        console.log(`[Segundo ${t}] ${mascoteClassico.tick()}`);
    }

    console.log('\n================================================================');
    console.log(' EXECUÇÃO CONCLUÍDA COM SUCESSO! RASTREABILIDADE INTEGRAL.     ');
    console.log('================================================================');
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        Item,
        Alimento,
        Remedio,
        ItemLimpeza,
        Mascote,
        MascoteBuilder,
        MascoteConcretoBuilder,
        MascoteDirector,
        demonstrarPadraoBuilder
    };
}

if (typeof require !== 'undefined' && require.main === module) {
    demonstrarPadraoBuilder();
}
