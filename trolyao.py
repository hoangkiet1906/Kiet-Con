while True:
	robot_ear = speech_recognition.Recognizer()
	robot_nao=""
	with speech_recognition.Microphone() as mic:
		print("Robot dang nghe ")
		audio = robot_ear.listen(mic)
	print("Robot dang suy nghi")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)

	if you == "":
		robot_nao = "ko nghe được, try again"
	
	elif "understand" in you:
		robot_nao="Yes, I can understand what you say "
	elif "do you" in you:
		robot_nao="Ofcourse"
	elif "hello" in you:
		robot_nao="Xin chào Kiệt Senpai"
	elif "like" in you:
		robot_nao="I like you so much ! "
	elif "bye" in you:
		robot_nao="bye bye Kiet Senpai"
	elif "name" in you:
		robot_nao = "Kiet Senpai"
	elif "today" in you :
		today = date.today()
		robot_nao = today.strftime("%B %d, %Y")
	elif "time" in you :
		now = datetime.now();
		robot_nao = now.strftime("%H hours %M minutes %S seconds")
	elif "I am" in you: 
		robot_nao = "Kiet Senpai là lớp trưởng"
	elif "turn off" in you:
		robot_nao = "oke"
		break
	else:
		robot_nao = "not listen"
	print(robot_nao)

	import pyttsx3
	robot_noi = pyttsx3.init()
	robot_noi.say(robot_nao)
	robot_noi.runAndWait()