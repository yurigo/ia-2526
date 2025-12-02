# Cargar el archivo
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    texto = f.read()

print(texto[:500])  # ver primeros 500 caracteres



import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt") #download punkt tokenizer
"""
punkt es un modelo preentrenado para tokenizar texto en varios idiomas, incluyendo español.
Se utiliza para dividir el texto en oraciones o palabras de manera efectiva.
"""
nltk.download("stopwords") # download stopwords
"""
stopwords es un conjunto de palabras comunes (como "y", "el", "de") que a menudo se filtran en el procesamiento de lenguaje natural.
Estas palabras no aportan mucho significado y se eliminan para centrarse en términos más relevantes.
"""

# Tokenizar en palabras
tokens = word_tokenize(texto, language="spanish")

# Stopwords en español
stopwords_es = set(stopwords.words("spanish"))

# Filtrar solo palabras alfabéticas y sin stopwords
tokens_filtrados = [
    t.lower() for t in tokens
    if t.isalpha() and t.lower() not in stopwords_es
]

print(tokens_filtrados[:30])
