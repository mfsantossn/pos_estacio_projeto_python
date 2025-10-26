# src/make_stats.py

import pandas as pd
import json
from src.core.metrics import analisar  # Importa a função de Programação Funcional

# --- Configurações ---
DATA_PATH = "dados.csv"
STATS_PATH = "stats.json"  # Será gerado na raiz do projeto

# Colunas para o cálculo da Receita e Desafio FP
FP_COLUNA = "qtd"
FP_LIMITE = 2


def gerar_estatisticas():
    """Lê o CSV, calcula estatísticas, aplica o desafio FP e salva em stats.json."""
    try:
        df = pd.read_csv(DATA_PATH, sep=';')

        # 1. Geração da coluna "receita"
        # O Pandas é robusto e lida com dados que podem ter sido lidos como str
        df['receita'] = df['preco'].astype(float) * df['qtd'].astype(int)

        # 2. Estatísticas Pandas
        qtd_total = df['qtd'].sum()
        receita_total = df['receita'].sum()
        preco_medio = df['preco'].mean() if len(df) > 0 else 0.0

        # 3. Desafio FP: Aplica a função 'analisar' à coluna 'qtd'
        # Usamos .astype(int) para garantir que os dados são inteiros
        fp_data = df[FP_COLUNA].astype(int).tolist()
        resultado_fp = analisar(fp_data, FP_LIMITE)

        # 4. Montar e salvar o resultado
        stats = {
            "pandas_stats": {
                "qtd_total": int(qtd_total),
                "receita_total": round(receita_total, 2),
                "preco_medio": round(preco_medio, 2)
            },
            "fp_desafio": {
                "coluna_aplicada": FP_COLUNA,
                "limite": FP_LIMITE,
                "resultado": resultado_fp
            }
        }

        with open(STATS_PATH, 'w') as f:
            json.dump(stats, f, indent=4)

        print(f"SUCESSO: Estatísticas salvas em {STATS_PATH}")

    except FileNotFoundError:
        print(f"ERRO CRÍTICO: Arquivo '{DATA_PATH}' não encontrado. Verifique se o CSV está em data/.")
    except Exception as e:
        print(f"Erro ao processar dados: {e}")


if __name__ == '__main__':
    gerar_estatisticas()