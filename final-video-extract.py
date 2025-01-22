from googlesearch import search
import yt_dlp
import pandas as pd

# Defina o termo de busca no Google
search_query = 'site:youtube.com "adicione o seu termo aqui" site:youtube.com "adicione o seu termo aqui" site:youtube.com "adicione o seu termo aqui"'

# Lista de URLs de vídeos coletadas pela pesquisa
video_urls = []

# Use o googlesearch para buscar os links
for result in search(search_query, num=100):  # Aumentando o número de links retornados
    video_urls.append(result)

# Função para extrair informações do vídeo
def get_video_details(url):
    ydl_opts = {
        'quiet': True,  # Suprime a saída do terminal
        'extract_flat': True,  # Evita download do vídeo, apenas os metadados
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        
        if 'entries' in result:
            result = result['entries'][0]  # Se for uma playlist, pegamos o primeiro item
        
        video_info = {
            "url": url,  # Adicionando a URL como a primeira coluna
            "image": result.get("thumbnail", ""),
            "thumbnail_image_url": result.get("thumbnail", ""),
            "title": result.get("title", ""),
            "views_count": result.get("view_count", ""),
            "likes_count": result.get("like_count", ""),
            "comments_count": result.get("comment_count", ""),
            "published_date": result.get("upload_date", ""),
            "description_header": result.get("description", ""),
            "category": result.get("category", ""),
            "author": result.get("uploader", "")
        }
        return video_info

# Coletar os dados de cada vídeo
video_data = []
for url in video_urls:
    details = get_video_details(url)
    video_data.append(details)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(video_data)

# Reorganizar as colunas para que a URL seja a primeira
df = df[['url', 'image', 'thumbnail_image_url', 'title', 'views_count', 'likes_count', 'comments_count', 'published_date', 'description_header', 'category', 'author']]

# Exibir os resultados
print(df)

# Salvar em um arquivo CSV (se necessário)
df.to_csv("video_details_final.csv", index=False)

#Após gerar o arquivo, fazer a análise dele via Party Rock: https://partyrock.aws/u/cinthiaquadrado/Jd4BPk_55/Product-Insights-Analyzer
