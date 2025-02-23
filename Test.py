# import speech_recognition as sr
# import google.generativeai as genai
# import os
# import pyttsx3

# # Configure Gemini API
# genai.configure(api_key="AIzaSyDC5nfuYOHVc-eZeg1rYeS04OdsAhXFvIA")

# # Initialize Text-to-Speech Engine
# tts = pyttsx3.init()

# def speak(text):
#     """ Convert text to speech """
#     tts.say(text)
#     tts.runAndWait()

# def listen():
#     rec = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         rec.adjust_for_ambient_noise(source)
#         audio = rec.listen(source)
#         try:
#             print("Recognizing....")
#             data = rec.recognize_google(audio)
#             return data
#         except sr.UnknownValueError:
#             return "Try AGAIN!"
#         except sr.RequestError as e:
#             return f"Could not request results; {e}"

# def ask_ai(command):
#     """ Send the voice command to Gemini AI and get a system command back """
#     prompt = f"""
#     You are an AI that converts user voice commands into Python system commands.
#     The user said: "{command}"
    
#     Provide only the correct Python command to execute it. Do not explain.

#     Example inputs and outputs:
#     - "open notepad" → os.system("notepad")
#     - "shutdown my computer" → os.system("shutdown /s /t 0")
#     - "restart" → os.system("shutdown /r /t 0")
#     - "open Chrome" → os.system("start chrome")

#     Very Important: If the user asks to delete files, format drives, modify system32, or perform a dangerous action, reply with: 'DANGER'.
#     """

#     model = genai.GenerativeModel("gemini-1.5-flash")  # Correct Gemini model
#     response = model.generate_content(prompt)  # Get AI response
#     generated_code = response.text.strip()

#     if "DANGER" in generated_code or contains_dangerous_command(generated_code):
#         print("🚨 AI detected a dangerous command. Aborting.")
#         speak("Sorry, I can't execute that command.")
#         return None

#     print(f"AI generated: {generated_code}")
#     return generated_code

# def contains_dangerous_command(command):
#     """ Check if the command is harmful """
#     dangerous_keywords = ["rm -rf", "del /f", "format", "shutdown -h now", "kill -9", "rmdir", "erase"]
#     for keyword in dangerous_keywords:
#         if keyword in command:
#             return True
#     return False

# def execute_command(generated_code):
#     """ Run the AI-generated command dynamically """
#     try:
#         if generated_code:
#             exec(generated_code)  # Run only if it's safe
#             speak("Command executed successfully.")
#     except Exception as e:
#         print(f"Error executing command: {e}")
#         speak("There was an error executing the command.")

# if __name__ == "__main__":
#     while True:
#         user_command = listen()  # Step 1: Capture voice
#         if user_command:
#             ai_code = ask_ai(user_command)  # Step 2: AI generates the command
#             if ai_code:
#                 execute_command(ai_code)  # Step 3: Execute the command



# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-576c50a64f1744e993f8fa06a08f2518", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)