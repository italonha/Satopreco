from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')  # Garante que o Flask encontre os templates

IMAGES = [
    "https://lh3.googleusercontent.com/d/11AECCL0pQYqsaVaUVS5nGlVVV9AJh-ZZ=w1000",
    "https://lh3.googleusercontent.com/d/1IKDoEKsES6mwFY0BZJ9r_T5abmMy8nvt=w1000",
    "https://lh3.googleusercontent.com/d/1WWZa6Rsf3GSqjVjg88chxiwFv7zGCZG7=w1000"
]

@app.route('/')
def index():
    print("🔹 Imagens carregadas no Flask:", IMAGES)  # Isso deve aparecer no terminal
    return render_template('index.html', images=IMAGES)

if __name__ == '__main__':
    app.run(debug=True)