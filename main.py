import os

import server
from waitress import serve

if __name__ == '__main__':
    PORT = os.environ.get('PORT', 80)

    print(f'Running on port {PORT}')
    serve(server.create_app(), host="localhost", port=PORT)
