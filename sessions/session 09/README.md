| Herramienta  | ¿Qué es?                            | ¿Para qué se usa?                                                     | Ventajas                                               | Limitaciones                                     |
| ------------ | ----------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------ |
| **spaCy**    | Framework moderno de NLP            | Tokenizar, lematizar, POS tagging, dependencias, entidades, similitud | Muy rápido, profesional, fácil de usar, buenos modelos | Los modelos pequeños no tienen embeddings reales |
| **NLTK**     | Librería clásica de NLP             | Stemming, stopwords, tokenización básica, gramáticas                  | Muy didáctica, ideal para aprender fundamentos         | No es rápida ni apta para producción             |
| **FastText** | Modelo de _embeddings_ (Meta)       | Obtener vectores de palabras y frases, medir similitud                | Maneja palabras nuevas, vectores de alta calidad       | Los modelos ocupan mucho (1–2 GB)                |
| **Gensim**   | Librería para trabajar con vectores | Cargar Word2Vec, GloVe, FastText; similitud y analogías               | Perfecta para explorar embeddings y semántica          | No hace análisis lingüístico (solo vectores)     |

| Tarea                                    | Herramienta recomendada   |
| ---------------------------------------- | ------------------------- |
| Tokenizar, lematizar, POS, NER           | **spaCy**                 |
| Eliminar stopwords o aplicar stemming    | **NLTK**                  |
| Medir similitud entre palabras           | **FastText** o **Gensim** |
| Obtener palabras más parecidas (vecinos) | **Gensim**                |
| Pipeline NLP completo y rápido           | **spaCy**                 |
| Explorar matemáticas de vectores         | **Gensim**                |
