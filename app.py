from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render your main workshop HTML page located in the templates folder
    return render_template('index.html')

@app.route('/online')
def home2():
    # Render your main workshop HTML page located in the templates folder
    return render_template('online.html') 

@app.route('/www.talentmap.in')
def website():
    # Render your main workshop HTML page located in the templates folder
    return render_template('www.talentmap.in')    

if __name__ == '__main__':
    app.run(debug=False)



