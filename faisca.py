import speech_recognition as sr
import pyttsx3
import os

# Inicializar reconhecimento de voz e sintetizador de fala
recon = sr.Recognizer()
sintetizador = pyttsx3.init()

def falar(texto):
    sintetizador.say(texto)
    sintetizador.runAndWait()

def ouvindo_comando():
    with sr.Microphone() as fonte:
        print("ouvindo!!")
        recon.adjust_for_ambient_noise(fonte)
        try:
            audio = recon.listen(fonte, timeout=5)
            comando = recon.recognize_google(audio, language='pt-BR')
            print(comando)
            return comando.lower()
        except sr.UnknownValueError:
            falar("Desculpa, não entendi o que disse.")
            return ""
        except sr.RequestError as e:
            falar(f"Erro no serviço de reconhecimento da fala; {e}")
            return ""
        except sr.WaitTimeoutError:
            return ""

def abrir_programa(nome_programa):
    pasta_atalhos = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs" # Caminho para a pasta de atalhos

    try:
        caminho_atalho = os.path.join(pasta_atalhos, f"{nome_programa}.lnk")
        os.startfile(caminho_atalho)
        falar(f"Abrindo {nome_programa}")
    except FileNotFoundError:
        falar("Desculpa, não conheço esse programa.")

def main():
    while True:
        comando = ouvindo_comando()
        if comando:
            if "faísca" in comando: # comando de ativação
                print("assistente ativado")
                falar("diga mano!")
                comando = ouvindo_comando()
                if "abrir" in comando:
                    nome_programa = comando.replace("abrir ", "").strip()
                    abrir_programa(nome_programa)
            elif "sair" in comando:
                falar("to saindo menor")
                break

if __name__ == "__main__":
    main()
