from collections import Counter
import nltk



def main():
    """Calculate top term frequencies for a corpus (el quijote)."""

    # nltk.download('punkt_tab')

    n = 4
    corpus = load_data("el_quijote.txt")

    # Compute n-grams
    ngrams = Counter(nltk.ngrams(corpus, n))

    # Print most common n-grams
    for ngram, freq in ngrams.most_common(10):
        print(f"{freq}: {ngram}")


def load_data(filename):
  with open(filename, "r", encoding="utf-8") as f:
    text = f.read()
  contents = []
  contents.extend([
      word.lower() for word in
      nltk.word_tokenize(text, language="spanish")
      if any(c.isalpha() for c in word)
  ])
  return contents


if __name__ == "__main__":
    main()