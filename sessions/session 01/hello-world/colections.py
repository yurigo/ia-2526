# list

list =  [1,2,3,4,5,6]
list[1] = 10000
print(list[1], list[-1])
print(list[1:4])


list.append(3)
print(list)
list.insert(1,7)
print(list)
list.extend([100,200])
print(list)
list.remove(3)
print(list)
el_ultimo = list.pop()
# del list[0]
print(list, el_ultimo)

ordenada = sorted(list)

# list.sort()


print(list)
print(ordenada)

# punto

punto = (1,2)
# punto[0] = 1000
print(punto)


# conjunto

a = {1,2,3}
b = {3,4,5}

# a, b =  {1,2,3}, {3,4,5}

print(a | b) # union
print(a & b) # intersection
print(a - b) # diferencia
print(a ^ b) # diferencia simetrica


# dictionary

d = {
    "clave": 3,
    "json": "derulo",
    "otra_clave": [
        1,2,3,4
    ] 
}

print(d)

print(d["clave"])
print(d["otra_clave"][-2])
print(d.get("json"))

for k , v in d.items():
    print("key: " , k , " value: ", v)

print(d.keys())
print(d.values())



