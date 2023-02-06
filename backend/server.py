from flask import Flask
import datetime
# from flask_cors import CORS

# write a function to create the app so as to allow testing
def create_app():

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
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run( host='0.0.0.0', port=5001, debug=True)