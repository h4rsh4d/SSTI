from flask import *

app = Flask(__name__)

@app.route("/")
def home():
        output = request.args.get('name')
        output = render_template_string(output)
        if output:
                pass
        else:
                output = "Test"
        return output

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=1337)
