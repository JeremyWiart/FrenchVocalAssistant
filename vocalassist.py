import speech_recognition as speech
import sys
import os
import subprocess
import webbrowser
from halo import Halo
import pyttsx3
import datetime


pathGoogle = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pathDiscord = r"C:\Users\jerem\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord"
pathDiscTest = os.path.exists('C:\\Users\\jerem\\AppData\\Local\\Discord\\Update.exe')
pathRsiLauncher = r"C:\Program Files\Roberts Space Industries\RSI Launcher\RSI Launcher"
pathRsiTest = os.path.exists('C:\\Program Files\\Roberts Space Industries\\RSI Launcher\\RSI Launcher.exe')
reco = speech.Recognizer()
spin = Halo(spinner='line')
clear = lambda: os.system('cls')

def trigger_and_responses(var1,triggerMode,saveStateMode):
	print(var1,triggerMode,saveStateMode)	
	if 'triggerOff' in triggerMode:
#########################################################################################
		if "désactive toi" in var1 or "coupe-toi" in var1:
			responses_va("tout de suite")
			sys.exit()
#########################################################################################		 
		if "bonjour" in var1:
			responses_va("bonjour")
#########################################################################################
		if "Margot" in var1:
			responses_va("oui")
#########################################################################################
		if "quelle heure est-il" in var1:
			hours_minutes = datetime.datetime.now().strftime("%H:%M")
			responses_va(f"il est {hours_minutes}")
#########################################################################################
		if "quel jour sommes-nous" in var1 or "c'est quel jour aujourd'hui" in var1:
			day = datetime.datetime.now().strftime("%A ")
			if "Monday" in day:
				responses_va("nous sommes lundi")
			elif "Tuesday" in day:
				responses_va("nous sommes mardi")
			elif "Wednesday" in day:
				responses_va("nous sommes mercredi")
			elif "Thursday" in day:
				responses_va("nous sommes jeudi")
			elif "Friday" in day:
				responses_va("nous sommes vendredi")
			elif "Saturday" in day:
				responses_va("nous sommes samedi")
			elif "Sunday" in day:
				responses_va("nous sommes dimanche")
##########################################################################################
		if "nous sommes le combien" in var1 or "on est le combien" in var1:
			day = datetime.datetime.now().strftime("%d ")
			print(day)
			responses_va(f"nous sommes le {day}")
##########################################################################################
		if "ouvre discord" in var1 or "lance discord" in var1:
			if pathTest == True:
				responses_va("ouverture de discord en cours")
				os.startfile(pathDiscord)
			else:
				print(paths)
				responses_va("impossible d'ouvrir l'application discord, chemin incorrect ou application non installée")

		if "ferme discord" in var1 or "coupe discord" in var1:
			subprocess.call(["taskkill","/F","/IM","Discord.exe"])
			responses_va("fermeture de discord")
##########################################################################################
		if "ouvre le lanceur star citizen" in var1 or "lance le lanceur star citizen" in var1:
			if pathRsiTest == True:
				os.startfile(pathRsiLauncher)
				responses_va("ouverture du lanceur en cours")
			else:
				print(paths)
				responses_va("impossible d'ouvrir le lanceur star citizen, chemin incorrect ou application non installée")
				
		if "ferme le lanceur star citizen" in var1:
			subprocess.call(["taskkill","/F","/IM","RSI Launcher.exe"])
			responses_va("fermeture du lanceur")
##########################################################################################
		if "ouvre Google" in var1:
			responses_va("ouverture de google")
			os.startfile(pathGoogle)
		  
		if "ouvre YouTube" in var1:
			responses_va("ouverture de YouTube")
			webbrowser.open("youtube.com")
	return triggerMode
	
def change_mode(saveStateMode):
	if "triggerOff" in saveStateMode:
		responses_va("tout de suite")
		saveStateMode = ["triggerOn"]
	else:
		responses_va("tout de suite")
		saveStateMode = ["triggerOff"]
	return saveStateMode

def responses_va(var0):
	engine = pyttsx3.init()
	#voices = engine.getProperty('voices')
	#engine.setProperty('voice', voices[0].id)
	engine.setProperty('rate', 200)
	engine.say(var0)
	engine.runAndWait()
	
	
def request_va():
	with speech.Microphone() as mic:
		print("Debut de la capture...")
		spin.start()
		audio_data = reco.record(mic, duration=5)
		spin.stop()
		print("Fin de la capture.")
		print("Reconnaissance en cours...")
		request = reco.recognize_google(audio_data, language="fr-FR")
		return request

		
def main(triggerMode):
	try:
		saveStateMode = triggerMode
		while True:
			try:
				request = request_va()
				if triggerMode == ["triggerOff"] :
					triggerMode = trigger_and_responses(request,triggerMode,saveStateMode)
					if saveStateMode == ["triggerOn"] :
						triggerMode = ["triggerOn"]
					if request == "change de mode":
						saveStateMode = change_mode(saveStateMode)
						if saveStateMode == ["triggerOn"] :
							triggerMode = ["triggerOn"]
						else:
							triggerMode = ["triggerOff"]
					#clear()
				elif triggerMode == ["triggerOn"]:
					if request == "Margot":
						triggerMode = ["triggerOff"]
						triggerMode = trigger_and_responses(request,triggerMode,saveStateMode)	
					
			except speech.UnknownValueError:
				print("Erreur : parole non détecter ou trop longue (5s max)")
				print(saveStateMode)
				print(triggerMode)
			except speech.RequestError as e:
				print("Erreur : requête google speech non conforme".format(e))	
	except KeyboardInterrupt:
		pass



if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('Erreur argument manquant -> Usage:	python vocalassist.py triggerOn/triggerOff')
		sys.exit()
	if sys.argv[1:] != ["triggerOn"] and sys.argv[1:] != ["triggerOff"]:
		print('Erreur argument incorrect -> Usage:	 python vocalassist.py triggerOn/triggerOff')
		print("Erreur -> ",sys.argv[1:])
		sys.exit()

	main(sys.argv[1:])