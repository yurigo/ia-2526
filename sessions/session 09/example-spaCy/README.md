# PNL con SpaCy

## Instalación

```bash
pip install spacy
```

```bash
## descargar el modelo
python -m spacy download es_core_news_sm
```

```bash
## descargar el modelo
python -m spacy download xx_ent_wiki_sm
```

FastText multilingue de Meta:

Descargar el modelo

```bash
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.es.300.vec.gz
```

convertirlo a vectores para spacy (tarda de 4 a 5 minutos)

```bash
python -m spacy init vectors es cc.es.300.vec.gz ./fasttext_es_vectors
```
