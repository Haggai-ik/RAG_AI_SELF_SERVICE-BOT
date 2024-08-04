import requests
import json 

def api_call_question(question):
    url = "http://127.0.0.1:8000/chat" 

    payload = {
        "question": question
    }

    headers = {
        "Content-Type": "application/json"
    }

    response =requests.post(url ,data=json.dumps(payload),headers=headers)
    if response.status_code == 200:
            response_json = response.json()
            answer = response_json.get('answer')
           
    
    # Extract the "answer" value
            # for key in answer:
            #      result =key['answer'

    return answer


def get_chat_history():
    url_get = "http://127.0.0.1:8000/chat_history"
    response = requests.get(url_get)
    if response.status_code == 200:
        response_json = response.json()
        history = response_json.get('history')
        return history
    else:
        return None
    

# api_call_question('helo')
# print(get_chat_history())








        