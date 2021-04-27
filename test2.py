

wikipedia.set_lang('vi')
def get_audio():
    print("Trợ Lý Ảo: Đang Nghe ... \t\t  0.0 ")
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        audio = ear_robot.listen(source , phrase_time_limit = 8)
        try:
            text = ear_robot.recognize_google(audio , language = "vi-VN")
            print("Tôi:  " , text)
            return text
        except:
            print("Lỗi rồi --__-- ")
            return 0

def stop():
    speak("Hẹn gặp lại bạn sau!")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi nghe không rõ. Bạn có thể nói lại được không nè ?")
    time.sleep(3)
    stop()
    return 0

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(2)

speak(strftime("%H hours %M minutes %S seconds"))
speak(strftime("%B %d, %Y"))