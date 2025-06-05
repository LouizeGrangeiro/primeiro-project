# src/01_logica_basica.py

# Verificar se a pessoa pode entrar e dar uma mensagem personalizada


# Regras da Festa:
# Idade mínima para entrar: 18 anos
# Se a pessoa tiver 60 anos ou mais, ela é VIP
# Se tiver menos de 18, não entra

nome = input("Qual seu nome?")
idade = int(input("Quantos anos você tem?"))
# 3. Verificar a idade com if / elif / else
if idade >= 60:
    print(f"{nome}, entrada liberada com tapete vermelho! 👑 ")
elif idade >= 18:
    print(f"{nome}, você pode entrar no evento 🥳")
else:
    print(f"Desculpa, {nome}, você ainda não pode entrar  😢 ")



    


