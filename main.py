import server
from waitress import serve

if __name__ == '__main__':
    print('Running on port 80')
    serve(server.create_app(), host="localhost", port=80)
