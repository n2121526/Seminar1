#задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.#

def statement(x, y, z):
  print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
  return (not (x or y or z)) == (not x and not y and not z)
if(statement(0, 0, 0) and statement(0, 0, 1) and statement(0, 1, 0) and 
     statement(0, 1, 1) and statement(1, 0, 0) and statement(1, 0, 1) and
     statement(1, 1, 0) and statement(1, 1, 1)):
        print("Истина")
else:
        print("Ложь")