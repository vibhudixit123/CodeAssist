import requests
import json
import gradio as gr
import os 


url = "http://localhost:11434/api/generate"

headers  = {

    'Content-Type' : 'application/json'
}

#history = []

def generate_response(prompt):
    #history.append(prompt)
    #final_prompt = "\n".join(history)

    data = {
        "model": "CodeAssist",
        "prompt": prompt,
        "stream" : False
    }

    response = requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code == 200:
        response= response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("error:" ,response.text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))


    interface = gr.Interface(
      fn=generate_response,
      inputs=gr.Textbox(lines=5, placeholder="Enter your Query here"),
      outputs=gr.Textbox(placeholder="I am CodeAssist, an AI assistant that can assist with coding tasks and detect errors in code. I was created by Vibhu to help developers write cleaner and more efficient code. I can answer a wide range of questions related to coding and provide suggestions for improving existing code or identifying potential issues. In addition to my primary functionality, I am also capable of detecting errors in code and providing feedback on how to fix them.")
    )

    interface.launch()
