# 👋 Oi, Python! Vamos brincar com nome e idade!

# Criamos uma caixinha chamada 'nome' e colocamos o valor "Lou" dentro
nome = "Lou"

# Mostrando a mensagem com uma vírgula (forma clássica)
print("Olá,", nome)

'''
print("Olá," nome)  # ❌ Vai dar erro!
🚨 O Python entra em pânico aqui!

Ele grita: "Ei! Você colocou duas coisas grudadas sem dizer que quer juntá-las!
Cadê a vírgula, o '+', ou o carinho pra unir esse texto e a variável?"
'''

# Duas formas corretas de mostrar texto + variável:

# Forma 1: Usando vírgula para separar texto da variável
print("Olá,", nome)

# Forma 2: Usando f-string (a forma mais chique e moderna 🧋)
print(f"Olá, {nome}")

'''
💡 f-strings: Permitem misturar texto e variáveis dentro de aspas com {chaves}.
Fica mais bonito e fácil de ler. Muito útil para mensagens personalizadas!
'''

# Agora vamos deixar o código mais interativo com idade!

# ✨ Solicita a idade do usuário
idade = int(input("Qual sua idade? "))

'''
🔍 EXPLICANDO TUDO:

input() → Abre uma caixinha perguntando algo pra pessoa digitar
int() → Transforma o que ela digitou (que é texto) em número
'''

# 🤔 Vamos decidir se a pessoa pode entrar no evento
if idade >= 18:
    print(f"{nome}, você pode entrar no evento 🥳")
else:
    print(f"Desculpa, {nome}, entrada não permitida 😢")

'''
if → É uma pergunta: "A idade é maior ou igual a 18?"
else → É o plano B: "Se não for, então faz isso aqui"
>= → Comparador: "maior ou igual a"
print() → Mostra o resultado na tela
'''
