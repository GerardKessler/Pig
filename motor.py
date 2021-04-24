from colorama import Fore, init, Back
from random import randint
from random import sample
from time import sleep
from sound import Sonido

init()
print(Fore.BLUE+Back.WHITE)

dices = Sonido("sounds/dices.ogg")
register = Sonido("sounds/register.ogg")
nos = [Sonido("sounds/no1.ogg"),Sonido("sounds/no2.ogg"),Sonido("sounds/no3.ogg"),Sonido("sounds/no4.ogg"),Sonido("sounds/no5.ogg"),Sonido("sounds/no6.ogg")]

class Jugador():
	def __init__(self,nombre):
		self.nombre = nombre
		self.puntos = 0
		self.puntosRonda = 0

class LogIn():
	def __init__(self):
		self.jugadores = []

	def añadirJugador(self, nombre):
		jugador = Jugador(nombre)
		self.jugadores.append(jugador)

	# def desordenarLista(self):
		self.jugadores = sample(self.jugadores,k=len(self.jugadores))

class Juego():
	def __init__(self):
		self.juegoActivo = True
		self.rondaActiva = True
		self.meta = 100
		self.cantidadDeRondas = 0

	def ronda(self, jugadores):
		for jugador in jugadores:
			self.rondaActiva = True
			print("Es el turno de {}.".format(jugador.nombre))
			while self.rondaActiva:
				self.juego(jugador,jugadores)

	def rondas(self):
		self.cantidadDeRondas = self.cantidadDeRondas + 1
		print("ronda {}".format(self.cantidadDeRondas))

	def juego(self,jugador,jugadores):
		conmutador = input()
		if conmutador == "":
			dado = self.tirarLosDados()
			if dado > 1:
				jugador.puntosRonda = jugador.puntosRonda + dado
				print("{}. Total, {}".format(dado,jugador.puntosRonda))
			else:
				nos[randint(0,5)].reproducir()
				sleep(0.5)
				print("pig!")
				sleep(0.3)
				jugador.puntosRonda = 0
				self.rondaActiva = False
		elif conmutador == "p":
			self.puntaje(jugador,jugadores)
		elif conmutador == "s":
			print("Saliendo del juego...")
			sleep(0.5)
			print("¡Gracias por jugar!")
			sleep(1)
			exit()
		elif conmutador == " ":
			register.reproducir()
			jugador.puntos = jugador.puntos + jugador.puntosRonda
			sleep(0.7)
			print("puntaje general, {}.".format(jugador.puntos))
			jugador.puntosRonda = 0
			self.rondaActiva = False
			self.winnerVerify(jugador)

	def puntaje(self,jugador,jugadores):
		for jugador in jugadores:
			print("{}, {}".format(jugador.nombre,jugador.puntos))
			print("")
			sleep(0.5)
		print("La meta es {}!".format(self.meta))
		sleep(0.5)
		print("Es el turno de {}".format(jugador.nombre))
		sleep(0.5)

	def tirarLosDados(self):
		dices.reproducir()
		sleep(1)
		return randint(1,6)

	def verificarJuego(self):
		return self.juegoActivo

	def winnerVerify(self,jugador):
		if jugador.puntos >= self.meta:
			self.juegoActivo = False