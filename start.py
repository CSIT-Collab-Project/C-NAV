from Backend import main
from waitress import serve

if __name__ == '__main__':
    print('Running on port 8080')
    serve(main.create_app(), host="localhost", port=8080)
