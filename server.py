from waitress import serve
import os
    
from Eshop.wsgi import application
    
if __name__ == '__main__':
    serve(application, host='0.0.0.0', port=os.environ["PORT"])