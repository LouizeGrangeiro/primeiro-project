# src/03_despertador.py

# Desperta 5 vezes com 1 segundo de intervalo
import time

def despertador():
    for i in range(5):
        print(f"🚨 Alarme {i+1}: Acorda, Lou!!! 🚨")
        time.sleep(1)
despertador()