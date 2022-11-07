from sound import Sonido
from colorama import Back,init, Fore 
from motor import sleep
from motor import Juego
from motor import LogIn

login = LogIn()
juego = Juego()
init()

backGround = Sonido("sounds/backGround.ogg")
start = Sonido("sounds/start.ogg")
bell = Sonido("sounds/bell.ogg")
winner = Sonido("sounds/winner.ogg")

start.reproducir()
sleep(2)
print(Fore.BLUE+Back.WHITE+"¡pig!")
sleep(0.5)

try:
	participantes = int(input("¿Cuántos jugadores van a participar?"))
except ValueError:
	print("Debes ingresar un número. Cerrando el juego...")
	sleep(2)
	exit()

try:
	meta = int(input("¿A cuántos puntos será la partida?"))
except ValueError:
	print("Debes ingresar un número. Cerrando el juego...")
	sleep(2)
	exit()

juego.meta = meta

for x in range(participantes):
	nombre = input("ingresa el nombre del jugador {}".format(x+1))
	login.añadirJugador(nombre)
	bell.reproducir()

# login.desordenarLista()
print("hay {} jugadores para esta partida".format(str(len(login.jugadores))))

sleep(0.5)
print("pulsa énter para comenzar el juego")
input()

backGround.reproducir(continuo=True)

while juego.verificarJuego():
	juego.rondas()
	sleep(0.3)
	juego.ronda(login.jugadores)

sleep(1)
backGround.detener()
winner.reproducir()
sleep(1.5)
jugadores = [jugador.puntos for jugador in login.jugadores]
max = max(jugadores)
for jugador in login.jugadores:
	if jugador.puntos == max:
		print("¡Felicitaciones {}!".format(jugador.nombre))
		break
sleep(0.7)
print("¡Has ganado la partida.")
sleep(2)