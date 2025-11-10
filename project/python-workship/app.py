from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>Welcome to my folio<h1>"

@app.route('/about')
def about():
   return "<h1>I'm byte<h1>"

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000) 
# 0.0.0.0 ทำให้สามารถเข้าถึงได้จากภาพนอก