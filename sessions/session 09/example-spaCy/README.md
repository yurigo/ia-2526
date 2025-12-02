# PNL con SpaCy

## Instalación

```bash
pip install spacy
python -m spacy download es_core_news_sm
```

```bash
python -m spacy download xx_ent_wiki_sm
```

FastText multilingue de Meta:

```bash
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.es.300.vec.gz
```

```python
import spacy
nlp = spacy.blank("es")
nlp.vocab.vectors.from_glove("cc.es.300.vec.gz")
```

```bash
python -m spacy init vectors es cc.es.300.vec.gz ./fasttext_es_vectors
```
