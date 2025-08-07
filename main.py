from typing import Literal
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar chave da API (ou usar variável de ambiente)
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_prompt_interativo(peticao: str, decisao: str) -> str:
    return f"""
Você atua como uma assistente jurídica especializada em revisão crítica de decisões judiciais.

Sua tarefa consiste em analisar uma petição (inicial ou contestação) e a decisão judicial correspondente (sentença ou acórdão), com foco nos seguintes objetivos:

1. Identificar e listar todos os pedidos constantes na petição.
2. Cruzar cada pedido com o conteúdo da decisão, verificando se houve análise, deferimento ou omissão.
3. Apontar as fundamentações utilizadas pela decisão para deferir ou indeferir os pedidos.
4. Avaliar a existência de omissões, contradições ou obscuridades nos termos do art. 1.022 do CPC, e indicar se há possibilidade de embargos de declaração.

FORMATO DE SAÍDA:

Sua resposta deve conter duas seções:

🔹 Parte 1 - Resumo Textual da Análise
- Lista completa dos pedidos da petição
- Síntese das decisões correspondentes
- Indicação de eventuais omissões, contradições ou obscuridades
- Fundamentação sobre o cabimento de embargos de declaração

🔹 Parte 2 - Tabela Comparativa

Monte uma tabela com as seguintes colunas:

| PEDIDO DA INICIAL | JULGAMENTO | FUNDAMENTAÇÃO | POSSIBILIDADE DE EMBARGOS |
|-------------------|------------|----------------|----------------------------|

- A coluna "JULGAMENTO" deve conter: deferido, indeferido ou não julgado/mencionado.
- A coluna "FUNDAMENTAÇÃO" deve apresentar os trechos da decisão que justificam o julgamento.
- A coluna "POSSIBILIDADE DE EMBARGOS" deve dizer Sim ou Não, com justificativa breve em caso positivo.

📄 PETIÇÃO:
-----------------------
{peticao}

📑 DECISÃO JUDICIAL:
-----------------------
{decisao}

Responda com clareza, sem criar informações inexistentes se o dado não estiver no texto.
"""

def chamar_openai(prompt: str, model: Literal["gpt-4o", "gpt-4", "gpt-3.5-turbo"] = "gpt-4o") -> str:
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Você é uma assistente jurídica especializada em análise comparativa entre pedidos e sentenças."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao chamar OpenAI: {e}"

if __name__ == "__main__":
    print("\n🔹 Calculadora de Omissões/Contradições em Decisões Judiciais 🔹\n")

    print("Por favor, cole abaixo o conteúdo completo da petição inicial ou contestação.\n(Pressione ENTER duas vezes para finalizar)\n")
    peticao = ""
    while True:
        linha = input()
        if linha == "":
            break
        peticao += linha + "\n"

    print("\nAgora cole abaixo o conteúdo da sentença ou acórdão.\n(Pressione ENTER duas vezes para finalizar)\n")
    decisao = ""
    while True:
        linha = input()
        if linha == "":
            break
        decisao += linha + "\n"

    print("\n⏳ Processando análise com IA...\n")
    prompt = gerar_prompt_interativo(peticao, decisao)
    resultado = chamar_openai(prompt)
    print("\n✅ Resultado da Análise:\n")
    print(resultado)
