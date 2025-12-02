# markovify

import markovify
# import sys

# Read text from file
# if len(sys.argv) != 2:
#     sys.exit("Usage: python generator.py sample.txt")
# with open(sys.argv[1]) as f:
#     text = f.read()

# Cargar el archivo
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text[:500] + "...") 

print("\nGenerating sentences...\n")

# Train model
text_model = markovify.Text(text)

# Generate sentences
print()
for i in range(5):
    print(text_model.make_sentence())
    print()