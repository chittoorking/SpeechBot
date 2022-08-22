import speech_recognition as sr
r = sr.Recognizer()
# obtain audio from the microphone
# the background thread stops soon after we call the stop function
def recordAudio():
    # recognize speech using Google Speech Recognition
    with sr.Microphone() as source:
        print("Please tell the requested info!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        x=r.recognize_google(audio)
        print("Giving results for  {} that I heard from you ".format(x))
        return  x
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
