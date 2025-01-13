from flask import Flask, request, render_template_string

app = Flask(__name__)
server_counter=1
current_message = "Waiting for a message..."

@app.route("/", methods=["GET"])
def display_message():
    page_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Message Board</title>
    </head>
    <body>
        <h1>Received Message</h1>
        <p>{{ message }}</p>
    </body>
    </html>
    """
    return render_template_string(page_content, message=current_message)

@app.route("/submit", methods=["POST"])
def handle_message():
    global current_message
    payload = request.json
    if payload and "message" in payload:
        current_message = payload["message"]
        return {"status": "success", "message": "Your message has been saved."}, 200
    return {"status": "failure", "message": "Message not found in the request."}, 400
@app.route("/get_counter",methods=["GET"])
def get_counter():
    global server_counter
    return {"counter":server_counter},200
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
