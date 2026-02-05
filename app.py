from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>AWS Cloud Project</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 80px;
          }
        </style>
      </head>
      <body>
        <h1>Cloud Project Deployed Successfully on AWS 🚀</h1>
        <p>Flask + Gunicorn + Nginx</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
