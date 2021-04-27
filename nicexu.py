

def stop():
    speak("OK tạm biệt !")

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Nói nhỏ quá không nghe được ")
    time.sleep(3)
    stop()
    return 0

def hello(name):
    day_time = int(strftime('%H'))

    if 0 <= day_time < 11:
        speak(f'Chào buổi sáng bạn {name}. Chúc bạn một ngày tốt lành. Bạn đã học bài chưa!')
    elif 11 <= day_time < 13:
        speak(f'Chào buổi trưa bạn {name}. Bạn đã được nghỉ trưa chưa vậy ?')
    elif 13 <= day_time < 18:
        speak(f'Chào buổi chiều bạn {name}. Bạn đã có dự định gì cho chiều nay chưa nè ? ')
    elif 18 <= day_time <= 23:
        speak(f'Chào buổi tối bạn {name}. Bạn ăn tối chưa ?')

def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f'Bây giờ là {now.hour}:{now.minute}:{now.second}')
    elif "ngày" in text:
        speak(f'hôm nay là ngày {now.day} tháng {now.month} năm {now.year}')
    else:
        speak(f'Kiệt Con chưa hiểu ý của mi. mi có thể nói lại không ạ ?')

def help_me():
    speak("""
    Kiệt Con có các chức năng sau:
    1. Chào hỏi
    2. Ngày & giờ
    3. Tạm biệt
    4. Mở ứng dụng
    5. Phát nhạc
    6. Mở trang webs
    """)
def open_application(text):
    if "cốc cốc" in text:
        speak("Đang Mở Cốc Cốc")
        time.sleep(5)
        os.startfile('"C:\\Users\\ADMIN\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"')
    elif "word" in text:
        speak("Đang Mở Microsoft Word")
        time.sleep(5)
        os.startfile('"C:\\Users\\ADMIN\\Desktop\\office\\Word 2016.lnk"')
    elif "code" in text:
        speak("Đang Mở Visual Studio Code")
        time.sleep(5)
        os.startfile('"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
    elif "excel" in text:
        speak("Đang Mở Microsoft Excel")
        time.sleep(5)
        os.startfile('"C:\\Users\\ADMIN\\Desktop\\office\\Excel 2016.lnk"')
    else:
        speak("Ứng dụng chưa được cài đặt đâu !")
        time.sleep(3)

def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(5)

def open_websites():
        url = 'file:///C:/Users/ADMIN/Documents/gacon/gaconhamhoc.html' 
        webbrowser.open(url)
        speak("Đây là trang web đầu tiên của thằng Kiệt hắn làm trong 2 tuần")
        time.sleep(9)

def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        time.sleep(7)
        return True
    else:
        return False

def main_brain():
    speak("Xin chào bạn. Bạn tên là gì ?")
    name = get_text()
    if name:
        speak(f'Chào bạn {name}')
        speak(f'Bạn cần Kiệt Con giúp gì không ạ ?')
        while True:
            text = get_text()
            if not text:
                break
            elif ('tạm biệt' in text) or ('cút' in text):
                stop()
                break
            elif ('chào trợ lý ảo' in text) or ('chào' in text):
                hello(name)
            elif ('chưa' in text):
                speak('vậy thì học bài đi nhé !')
            elif ('rồi' in text):
                speak('vậy thì tốt rồi !')
            elif 'có thể làm gì' in text:
                help_me()
            elif "hiện tại" in text:
                get_time(text)
            elif 'thank you' in text:
                speak('ahihi không có gì !')
            elif 'nhạc' in text:
                play_song()
            elif 'ứng dụng' in text:
                open_application(text)
            elif 'mở' in text:
                open_website(text)
            elif 'đầu tiên' in text:
                open_websites()
            else:
                speak('Thằng Kiệt hằn chưa làm chức năng đó cho tôi ')

main_brain()






