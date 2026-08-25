from rest_framework.response import Response
from rest_framework.views import APIView

from .services.gemini import GeminiService


class GenerateTextView(APIView):
    """Minimal teaching endpoint for the first Gemini lesson."""

    def post(self, request):
        prompt = request.data.get("prompt", "").strip()
        if not prompt:
            return Response({"message": "prompt is required"}, status=400)

        try:
            text = GeminiService().generate(prompt)
        except RuntimeError as exc:
            return Response({"message": str(exc)}, status=503)
        except Exception as exc:
            return Response({"message": "Gemini request failed", "error": str(exc)}, status=502)

        return Response({"text": text})
