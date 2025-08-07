# ⚖️ Classificador de contradições e/ou omissões em decisões judiciais

## 💡 Motivação

Quando um advogado inicia suas **atividades em escritório de advocacia na modalidade de associado**, frequentemente se deparam com a tarefa de analisar peças processuais que **não redigiram**. Essa falta de familiaridade com os pedidos já formulados e a dificuldade de compreender decisões complexas pode gerar insegurança — especialmente ao identificar **omissões**, **contradições** ou **pontos passíveis de embargos de declaração**.

Pensando nessa dor prática, desenvolvi um projeto que **auxilia na leitura e análise comparativa entre a petição/contestação e a sentença**, oferecendo como resultado:

- Um resumo claro dos pedidos  
- Uma **tabela comparativa completa**  
- Detecção de **omissões ou contradições**  
- Avaliação do **cabimento de embargos de declaração**

> ⚠️ **Atenção**: Este projeto **não substitui** a análise minuciosa e estratégica de um profissional jurídico. Ele serve como **ferramenta de apoio**, fornecendo agilidade e maior clareza na triagem de decisões, especialmente útil para advogados recém-chegados ao caso ou ao escritório.

---

## 📥 Prompt Desenvolvido

```text
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
<TEXTO DA PETIÇÃO>

📑 DECISÃO JUDICIAL:
-----------------------
<TEXTO DA DECISÃO>

Responda com clareza, sem criar informações inexistentes se o dado não estiver no texto.
```

---

### Exemplo de resposta via script

✅ Resultado da Análise:

🔹 Parte 1 – Resumo Textual da Análise

- **Lista completa dos pedidos da petição:**
  1. Tramitação do feito sob segredo de justiça.
  2. Concessão dos benefícios da justiça gratuita.
  3. Reconhecimento da rescisão indireta do contrato de trabalho, com projeção da data de saída para 09/03/2026.      
  4. Pagamento das verbas rescisórias devidas.
  5. Reconhecimento da estabilidade acidentária, com indenização do período estabilitário.
  6. Condenação ao pagamento de indenização por danos morais e materiais.
  7. Designação de perícia psiquiátrica judicial.
  8. Abertura da CAT pela empresa.
  9. Condenação ao pagamento de honorários sucumbenciais em 15%.
  10. Condenação ao pagamento de custas processuais.
  11. Protesto por todos os meios de prova em direito admitidos.

- **Síntese das decisões correspondentes:**
  1. Mantido o segredo de justiça.
  2. Justiça gratuita deferida.
  3. Rescisão indireta do contrato de trabalho declarada, com efeitos a partir do ajuizamento da ação.
  4. Pagamento das verbas rescisórias deferido, com algumas especificações.
  5. Estabilidade provisória reconhecida, com indenização substitutiva.
  6. Indenização por danos morais fixada em R$ 150.000,00; ressarcimento de despesas médicas condicionado à comprovação.
  7. Emissão da CAT determinada.
  8. Honorários advocatícios fixados em 10% para ambas as partes.
  9. Custas processuais a cargo da ré.
  10. Provas produzidas e consideradas.

- **Indicação de eventuais omissões, contradições ou obscuridades:**
  - Não há menção específica à projeção da data de saída para 09/03/2026.
  - A decisão não menciona a multa do art. 467 da CLT.

- **Fundamentação sobre o cabimento de embargos de declaração:**
  - Cabem embargos de declaração para esclarecer a ausência de menção à projeção da data de saída para 09/03/2026, bem como a omissão sobre a multa do art. 467 da CLT.

🔹 Parte 2 – Tabela Comparativa

| PEDIDO DA INICIAL | JULGAMENTO | FUNDAMENTAÇÃO | POSSIBILIDADE DE EMBARGOS |
|-------------------|------------|----------------|----------------------------|
| Segredo de justiça | Deferido | Mantido o segredo de justiça diante da natureza dos fatos tratados. | Não |
| Justiça gratuita | Deferido | Defiro a justiça gratuita à autora. | Não |
| Rescisão indireta | Deferido | Restando configurado o descumprimento contratual grave por parte do empregador, declaro a rescisão indireta do contrato de trabalho. | Sim, para esclarecer a projeção da data de saída. |
| Verbas rescisórias | Deferido | Condeno a ré ao pagamento de verbas rescisórias discriminadas. | Sim, para esclarecer a ausência de menção à multa do art. 467 da CLT. |
| Estabilidade acidentária | Deferido | Reconhecida a doença ocupacional, a reclamante faz jus à estabilidade provisória de 12 meses. | Não |
| Danos morais e materiais | Parcialmente deferido | Fixo a indenização por danos morais em R$ 150.000,00; ressarcimento de despesas médicas condicionado à comprovação. | Não |
| Abertura da CAT | Deferido | Emitir CAT no prazo de 10 dias, sob pena de multa diária de R$ 200,00. | Não |
| Honorários sucumbenciais | Parcialmente deferido | Fixo honorários advocatícios em 10% para ambas as partes. | Não |
| Custas processuais | Deferido | Custas processuais fixadas sobre condenação arbitrada em R$ 300.000,00. | Não |     
| Meios de prova | Deferido | Provas produzidas e consideradas. | Não |

Esta análise identifica pontos que podem ser objeto de embargos de declaração para esclarecer omissões na sentença.