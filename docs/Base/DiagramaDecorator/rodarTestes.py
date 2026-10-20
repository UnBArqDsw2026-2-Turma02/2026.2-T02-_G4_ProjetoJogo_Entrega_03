"""Executa os testes do Decorator e mostra cada um com uma descrição legível.

Executar a partir da raiz do repositório:
    python docs/exemplos/decorator/rodar_testes.py
"""
import sys
import unittest
from pathlib import Path

try:  # garante acentos corretos em terminais Windows
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

PASTA = Path(__file__).resolve().parent


def listar_testes(suite):
    """Percorre a suíte (que é aninhada) e devolve os testes um a um."""
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from listar_testes(item)
        else:
            yield item


def main() -> int:
    suite = unittest.defaultTestLoader.discover(str(PASTA), pattern="test_*.py")
    testes = list(listar_testes(suite))

    print("=" * 74)
    print(f"Testes do Decorator de bônus de XP ({len(testes)} testes)")
    print("=" * 74)

    falhas = 0
    for teste in testes:
        resultado = unittest.TestResult()
        teste.run(resultado)
        descricao = teste.shortDescription() or str(teste)
        if resultado.wasSuccessful():
            print(f"[OK]     {descricao}")
        else:
            falhas += 1
            print(f"[FALHOU] {descricao}")
            for _, detalhe in resultado.failures + resultado.errors:
                print("         " + detalhe.replace("\n", "\n         "))

    aprovados = len(testes) - falhas
    print("-" * 74)
    print(f"Resumo: {len(testes)} testes | {aprovados} aprovados | {falhas} com falha")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())