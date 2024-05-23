import speech_recognition as sr
import os

while True:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('# ouvindo.')
        audio = recognizer.listen(source, timeout=None)

    try:
        output = recognizer.recognize_google(audio)
        print(output)
        
        if 'break' in output:
            break
        elif 'open' in output:
            app = output.replace('open ', '').strip()
            print(app)
            os.startfile(f"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\{app}.lnk")
            
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {e}")
