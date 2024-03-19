from flask import Flask

# Flask-App erstellen
app = Flask(__name__)

# Routen definieren
@app.route('/')
def index():
    return 'Hallo, Welt! Dies ist meine erste Flask-Anwendung.'

@app.route('/about')
def about():
    return 'Über diese Anwendung: Eine kleine Backend-Anwendung mit Flask.'

# Starte die Flask-App
if __name__ == '__main__':
    app.run(debug=True)
