from rest_framework.response import Response
from rest_framework.views import APIView

from .services.gemini import GeminiService


class GenerateTextView(APIView):
    """Minimal teaching endpoint for the first Gemini lesson."""

    def post(self, request):
        name = request.data.get("name", "").strip()
        category = request.data.get("category", "").strip()
        if not name or not category:
            return Response({"message": "name and category are required"}, status=400)

        prompt = (
            f"Write a concise product description for '{name}' in the "
            f"'{category}' category. Return only the description."
        )

        try:
            text = GeminiService().generate(prompt)
        except RuntimeError as exc:
            return Response({"message": str(exc)}, status=503)
        except Exception as exc:
            return Response({"message": "Gemini request failed", "error": str(exc)}, status=502)

        return Response({"description": text})
