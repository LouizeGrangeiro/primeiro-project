# src/02_gato.py

#  O gato aprova ou não a comida 🐾

# Comidas aprovadas
comidas_aprovadas = [
         "salmão",
         "atum",
         "sardinha",
         "frango cozido",
         "carne moída",         
 ]

# Pede a comida
comida = input("Digite a comida para o seu gato: ").strip().lower()

# Verifica se a comida está na lista de aprovadas
if comida in comidas_aprovadas:
     print(f"Seu gato aprova {comida} e acha uma delicinha! 😸")
else:
     print("Seu gato torce o nariz... tente outra coisa! 😾")
     print("Sugestão do CHEF: que tal experimentar um Salmão ou Sardinha?")
