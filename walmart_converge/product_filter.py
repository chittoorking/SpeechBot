from Text2Speech import Generate_text_to_speech
import RecordUserInput
def search_product():
    Generate_text_to_speech("Tell me the product name as long as you remember")
    product=RecordUserInput.recordAudio()
    return product