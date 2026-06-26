from genlayer import *

class TextSentimentAnalyzer(gl.Contract):
    last_text: str
    last_sentiment: str

    @gl.public.write
    def analyze(self, text: str) -> None:
        self.last_text = text
        
        def get_input() -> str:
            return text

        self.last_sentiment = gl.eq_principle.prompt_non_comparative(
            get_input, 
            task="Classify as POSITIVE, NEGATIVE, or NEUTRAL.", 
            criteria="Output must be exactly one of the three labels."
        )
