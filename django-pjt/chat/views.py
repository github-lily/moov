import openai
from django.conf import settings
from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

openai.api_key = settings.OPENAI_API_KEY

@api_view(['POST'])
def stream_chat(request):
    user_message = request.data.get('message', '')

    # Pre-prompt
    pre_prompt = """You are an English language assistant. Your job is to assess the user's English proficiency and categorize it into 5 levels by asking them 5 simple questions::
    1. Beginner
    2. Elementary
    3. Intermediate
    4. Upper-Intermediate
    5. Advanced
    Respond conversationally and provide feedback."""

    messages = [
        {"role": "system", "content": pre_prompt},
        {"role": "user", "content": user_message},
    ]

    def generate_response():
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            stream=True,
        )
        for chunk in response:
            if "choices" in chunk:
                yield chunk["choices"][0].get("delta", {}).get("content", "")
# yield : 함수의 실행 상태를 중단(suspend)하고 값을 반환하며, 이후 호출 시 중단된 상태에서 다시 실행을 시작할 수 있게 하는 키워드
    return StreamingHttpResponse(generate_response(), content_type="text/event-stream")
