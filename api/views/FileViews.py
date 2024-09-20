from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from collections import defaultdict

def parse_chat_text(chat_text):
    user_word_count = defaultdict(int)
    current_user = None

    lines = chat_text.splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith('<') and '>' in line:
            current_user = line.split('>')[0][1:]
            chat_message = line.split('>')[1].strip()
        elif current_user:
            chat_message = line

        if current_user:
            words = chat_message.split(" ")
            user_word_count[current_user] += len(words)

    sorted_users = sorted(user_word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_users

@csrf_exempt
def upload_text(request):
    if request.method == 'POST':
        chat_text = request.POST.get('chat_text', '')

        if chat_text:
            user_list = parse_chat_text(chat_text)
            return JsonResponse({'data': user_list})

        return JsonResponse({'msg': 'No Text Detect'})

