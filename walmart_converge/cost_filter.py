from Text2Speech import Generate_text_to_speech
import RecordUserInput
def search_cost():
    Generate_text_to_speech("Tell me the maximum cost")
    cost=RecordUserInput.recordAudio()
    return cost