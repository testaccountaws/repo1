from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/application1")
def Application1():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Application 1</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f8ff;
            }
            .application {
                font-size: 24px;
                text-align: center;
                padding: 20px;
                border: 2px solid #0077b6;
                background-color: #d9f1ff;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>

        <div class="application">
            There's no such thing as a bad day when you're fishing.
        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
