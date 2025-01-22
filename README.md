# Coleta e Análise de Vídeos do YouTube

Este projeto visa coletar informações sobre vídeos do YouTube com base em um termo de pesquisa fornecido. Usando a biblioteca `googlesearch` para buscar links relevantes e `yt-dlp` para extrair metadados dos vídeos, o código gera um DataFrame com informações detalhadas sobre os vídeos, que pode ser salvo em um arquivo CSV para análise posterior.

## Objetivo

O objetivo deste script é automatizar a coleta de metadados de vídeos do YouTube, como título, visualizações, curtidas, comentários e muito mais, com base em um termo de pesquisa específico. Esses dados podem ser usados para análise de tendências, comparação entre vídeos ou para insights sobre o conteúdo mais popular em determinado tópico.

## Funcionalidade

1. **Busca de Links**: Utiliza o `googlesearch` para buscar links de vídeos no YouTube com base em um termo de pesquisa.
2. **Extração de Metadados**: Usa a biblioteca `yt-dlp` para extrair metadados de cada vídeo, incluindo título, visualizações, curtidas, comentários, descrição, etc.
3. **Criação de DataFrame**: Organiza as informações extraídas em um DataFrame utilizando a biblioteca `pandas`.
4. **Geração de CSV**: Salva os dados extraídos em um arquivo CSV para análise posterior.

### Estrutura do DataFrame

O DataFrame resultante terá as seguintes colunas:

- **url**: Link para o vídeo no YouTube.
- **image**: URL da imagem de miniatura do vídeo.
- **thumbnail_image_url**: URL da miniatura do vídeo.
- **title**: Título do vídeo.
- **views_count**: Número de visualizações.
- **likes_count**: Número de curtidas.
- **comments_count**: Número de comentários.
- **published_date**: Data de publicação.
- **description_header**: Descrição do vídeo.
- **category**: Categoria do vídeo.
- **author**: Nome do autor do vídeo.

## Análise Posterior

Após gerar o arquivo CSV, você pode realizar a análise dos dados utilizando a ferramenta Party Rock. Para isso, carregue o arquivo CSV gerado em [Party Rock: Product-Insights-Analyzer](https://partyrock.aws/u/cinthiaquadrado/Jd4BPk_55/Product-Insights-Analyzer).

## Exemplos de Insights

Com os dados extraídos e organizados, você pode obter insights como:

- **Tendências**: Identificar quais vídeos estão recebendo mais visualizações, curtidas e comentários sobre um determinado tema.
- **Análise de Desempenho**: Comparar o desempenho de vídeos com base nas métricas coletadas.
- **Análise de Sentimento**: Estudar os comentários para entender o sentimento do público em relação aos vídeos.
- **Categorias Populares**: Descobrir quais categorias de vídeos estão em alta.

## Personalização

- **Ajuste do Termo de Pesquisa**: Você pode modificar o `search_query` para refletir diferentes tópicos de interesse, garantindo que o código busque vídeos com base em qualquer área ou assunto específico.
- **Ajuste de Quantidade de Links**: A variável `num` no comando `search` define o número de links retornados pela pesquisa. Você pode aumentar ou diminuir esse valor conforme necessário.
