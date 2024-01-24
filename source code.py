import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translation to {target_language}: {translation.text}")
    return translation.text

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("translation.mp3")
    os.system("start translation.mp3")  # This command may vary based on your operating system

def choose_target_language():
    
    print("Select target language:")
    print("1. English")
    print("2. Spanish")
    print("3. Tamil")
    print("4. Bengali")
    print("5. Telugu")
    print("6. Marathi")
    print("7. Hindi")
    print("8. Urdu")
    print("9. Gujarati")
    print("10. Kannada")
    print("11. Odia")
    print("12. Punjabi")
    print("13. Malayalam")
    print("14. French")
    print("15. German")
    print("16. Italian")
    print("17. Portuguese")
    print("18. Chinese (Simplified)")
    print("19. Japanese")
    print("20. Korean")
    print("21. Arabic")
    print("22. Russian")
    print("23. Malay")
    print("24. Indonesian")
    print("25. Turkish")
    print("26. Vietnamese")
    print("27. Thai")
    print("28. Dutch")
    print("29. Greek")
    print("30. Hebrew")
    print("31. Swedish")
    print("32. Polish")
    print("33. Romanian")
    print("34. Czech")
    print("35. Hungarian")

    # Add more languages as needed
    
    choice = input("Enter the number corresponding to the language: ")
    
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'es'
    elif choice == '3':
        return 'ta'
    elif choice == '4':
        return 'bn'
    elif choice == '5':
        return 'te'
    elif choice == '6':
        return 'mr'
    elif choice == '7':
        return 'hi'
    elif choice == '8':
        return 'ur'
    elif choice == '9':
        return 'gu'
    elif choice == '10':
        return 'kn'
    elif choice == '11':
        return 'or'
    elif choice == '12':
        return 'pa'
    elif choice == '13':
        return 'ml'
    elif choice == '14':
        return 'fr'
    elif choice == '15':
        return 'de'
    elif choice == '16':
        return 'it'
    elif choice == '17':
        return 'pt'
    elif choice == '18':
        return 'zh-CN'
    elif choice == '19':
        return 'ja'
    elif choice == '20':
        return 'ko'
    elif choice == '21':
        return 'ar'
    elif choice == '22':
        return 'ru'
    elif choice == '23':
        return 'ms'
    elif choice == '24':
        return 'id'
    elif choice == '25':
        return 'tr'
    elif choice == '26':
        return 'vi'
    elif choice == '27':
        return 'th'
    elif choice == '28':
        return 'nl'
    elif choice == '29':
        return 'el'
    elif choice == '30':
        return 'he'
    elif choice == '31':
        return 'sv'
    elif choice == '32':
        return 'pl'
    elif choice == '33':
        return 'ro'
    elif choice == '34':
        return 'cs'
    elif choice == '35':
        return 'hu'

    
    print("Invalid choice. Defaulting to English.")
    return 'en'

while True:
    original_text = speech_to_text()
    
    if original_text:
        target_language = choose_target_language()
        translated_text = translate_text(original_text, target_language)
        text_to_speech(translated_text, target_language)
