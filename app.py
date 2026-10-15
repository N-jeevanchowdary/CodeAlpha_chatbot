from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined chatbot responses based on intent/keywords
RESPONSES = {
    "hello": "Hello! Welcome to CodeAlpha Cloud Assistant. How can I help you today?",
    "hi": "Hi there! How can I assist you with cloud computing or our services?",
    "hey": "Hey! How can I help you today?",
    "what is cloud computing": "Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, and analytics—over the Internet.",
    "what is aws": "AWS (Amazon Web Services) is a comprehensive, evolving cloud computing platform provided by Amazon.",
    "what is azure": "Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications.",
    "what is flask": "Flask is a lightweight WSGI web application framework written in Python.",
    "who created you": "I am an AI-powered Web Chatbot developed for the CodeAlpha Cloud Computing Internship project!",
    "help": "You can ask me about Cloud Computing, AWS, Azure, Flask, or details about this CodeAlpha Internship Project!",
    "bye": "Goodbye! Have a great day ahead!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message", "").strip().lower()
    
    # Matching logic
    response_text = "I'm sorry, I didn't quite understand that. Type 'help' to see what you can ask me!"
    
    for pattern, resp in RESPONSES.items():
        if pattern in user_message:
            response_text = resp
            break

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
