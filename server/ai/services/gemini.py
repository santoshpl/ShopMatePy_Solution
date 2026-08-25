from django.conf import settings


class GeminiService:
    """Small wrapper around the Gemini SDK.

    Students can extend this class as the course moves from basic generation
    to structured output, tool calling, and RAG.
    """

    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.client = None

        if self.api_key:
            from google import genai

            self.client = genai.Client(api_key=self.api_key)

    def generate(self, prompt: str, model: str = "gemini-3.7-flash") -> str:
        if not self.client:
            raise RuntimeError("GEMINI_API_KEY is not configured.")

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
        )
        return response.text or ""
