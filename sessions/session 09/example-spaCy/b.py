import spacy
nlp = spacy.load("es_core_news_sm")

texto = "El colegio de La Salle Gracia ofrece formación en IA y BigData y Cyberseguridad."

doc = nlp(texto)

print("Entidades reconocidas:")
for ent in doc.ents:
    print(ent.text, ent.label_)