import spacy
nlp = spacy.load("es_core_news_sm")

texto = "El colegio de La Salle Gracia ofrece formación en IA y BigData y Cyberseguridad."

doc = nlp(texto)

print("Tokens:")
for token in doc:
    print(token.text, token.pos_, token.lemma_)
