import server
from waitress import serve

if __name__ == '__main__':
    print('Running on port 8080')
    serve(server.create_app(), host="localhost", port=8080)
