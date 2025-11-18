from logicCNF import *
# from logic import *

#  1. p ∧ q → r ∨ s
#  2. p → q
#  3. p ∧ ( r → ( t ∧ u ) )
#  4. s → t ∧ w
#  Query: t ∨ u 

# pista1 = ("IMP", ("AND" , "P" , "Q") , ("OR" , "R" , "S"))
# knowledge =  pista1

# pista2 = ("IMP", "P", "Q")
# knowledge = ("AND", knowledge, pista2)

# pista3 = ("AND" , "P" , ("IMP", "R", ("AND" , "T" , "U")))
# knowledge = ("AND", knowledge, pista3)

# pista4 = ("IMP", "S", ("AND" , "T" , "W"))
# knowledge = ("AND", knowledge, pista4)

# show(knowledge)

# query = ("IMP" , "S" , ("OR" , "T", "U"))
# print("hi:" , entails(knowledge, query))

# ==================================================================================

# pista1 = ("IMP", "P" , ("AND" , ("NOT", "Q") , "R"))
# knowledge =  pista1

# pista2 = ("IMP", "R" , "Q")
# knowledge = ("AND", knowledge, pista2)

# show(knowledge)

# query = ("NOT" , "P")
# print("hi:" , entails(knowledge, query))

# ==================================================================================

# pista1 = ("IMP", (("AND", ("IMP", "A", "B") , ("IMP", "B" , "C") )) , ("IMP", "A", "C"))
# knowledge =  pista1

# pista2 = ("A")
# knowledge = ("AND", knowledge, pista2)

# pista3 = ("IMP", "C" , ("AND" , ("IMP" , "D", "X") , ("IMP", "E", "X")))
# knowledge = ("AND", knowledge, pista3)

# pista4 = ("IMP", ("OR", "D", "E") , ("AND" , "F" , "G"))
# knowledge = ("AND", knowledge, pista4)

# pista5 = ("IMP", ("AND", "F", "G") , ("OR" , "X" , "Y"))
# knowledge = ("AND", knowledge, pista5)

# show(knowledge)

# query = ("OR" , "X" , "Y")
# print("hi:" , entails(knowledge, query))

# ==================================================================================

# 
#  1. p ∨ s → ¬(q ∧ r)
#  2. r → w ∨ m
#  Experimento para forzar implicaciones y literales:
#  3. w → e0
#  i. ei → ei+1 
#  4. en → s
#  5. ¬(q ∧ r) → ¬t
#  Query: ¬t
import time

# Record the start time before the code block
start_time = time.time()


variable = 100

pista1 = ("IMP", ("OR", "P", "S") , ("NOT" , ("AND", "Q", "R")))
knowledge =  pista1

pista2 = ("IMP" , "R" , ("OR" , "W" , "M"))
knowledge = ("AND", knowledge, pista2)

pista3 = ("IMP", "W" , "E0")
knowledge = ("AND", knowledge, pista3)

pista3 = ("IMP", "E" + str(variable)  , "P")
knowledge = ("AND", knowledge, pista3)

pista4 = ("IMP", "M", "S")
knowledge = ("AND", knowledge, pista4)

pista5 = ("IMP", ("NOT", ("AND", "Q", "R")) , ("NOT" , "T"))
knowledge = ("AND", knowledge, pista5)

for i in range(0, variable):
    pistaExtra = ("IMP", "E" + str(i) , "E" + str(i + 1))
    knowledge = ("AND", knowledge, pistaExtra)

show(knowledge)

query = ("NOT", "T" )
print("hi:" , entails(knowledge, query))


# Record the end time
end_time = time.time()

# Calculate and print the elapsed time to the console
elapsed_time = end_time - start_time
print(f"--- {elapsed_time} seconds ---") 