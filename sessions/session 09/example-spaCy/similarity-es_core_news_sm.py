import spacy
nlp = spacy.load("es_core_news_sm")

doc1 = nlp("El alumno entregó la práctica sobre programación orientada a objetos.")
doc2 = nlp("La estudiante completó el proyecto de software.")

print(doc1.similarity(doc2))
print("\n-----\n")

doc1 = nlp("programación")
doc2 = nlp("software")

print(doc1.similarity(doc2))