from TTS.api import TTS


class SpeechSynthesis:
    def __init__(self, model_name=None, speaker=None):
        if model_name is None:
            model_name = TTS.list_models()[0]
        if speaker is None:
            speaker = TTS.list_models()[0]

        self.model_name = model_name
        self.speaker = speaker
        self.tts = TTS(model_name)

    def tts(self, text: str, language: str = "en"):
        return self.tts.tts(text, self.speaker, language)

    def tts_to_file(self, text: str, language: str, file_path: str):
        self.tts.tts_to_file(text, self.speaker, language, file_path)
