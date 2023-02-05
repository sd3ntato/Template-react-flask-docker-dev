from flask import Flask
import datetime
# from flask_cors import CORS
  
x = datetime.datetime.now()
  
app = Flask(__name__)
# CORS(app)
  

@app.route('/data')
def get_time():
  
    return {
        'Name':"gek", 
        "Age":"27",
        "Date":x, 
        "programming":"python"
        }
  

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5001, debug=True)