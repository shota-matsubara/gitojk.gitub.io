# ai_insight.py: Gemini API連携
import google.generativeai as genai
import os

def generate_insight(prompt):
    api_key = os.getenv("GOOGLE_API_KEY") 
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    # model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    response = model.generate_content(prompt)
    return response.text.strip()


# prompt = "ナンカオモロイコトイッテヤ"

# print(prompt)

# response = generate_insight(prompt)

# print(response)

def ask_about_kintore(userPromt,mode):
    context = "下記の質問に対して、マッスルな答えをしてください。500文字以内で。筋トレマニアにとって示唆のある回答を。"
    finalPromt = context + "対象は"+ mode +"向けに。" + userPromt
    response = generate_insight(finalPromt)
    return response
