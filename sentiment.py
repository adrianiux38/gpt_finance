import requests
from bs4 import BeautifulSoup
import os
import openai

url = "https://medium.com/digital-society/elon-musk-the-billion-dollar-tweeter-393a7a13297d"

# Obtener el contenido HTML de la página
response = requests.get(url)
html_content = response.text

# Analizar el contenido HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todos los párrafos de texto dentro de la etiqueta 'article'
article = soup.find('article')
paragraphs = article.find_all('p')

# Extraer el texto de cada párrafo y unirlo en un solo string
article_text = "\n".join([paragraph.text for paragraph in paragraphs])

#print(article_text)

# Configurar la clave API de OpenAI
openai.api_key = "YOUR_API_KEY"

def analyze_sentiment_and_summarize(text):
    prompt = (
        f"Please analyze the following text for its sentiment (positive, negative, or neutral) and provide a one-sentence summary:\n\n{text}\n\nSentiment: "
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5)
    print(response.choices[0].text.strip())

analyze_sentiment_and_summarize(article_text)