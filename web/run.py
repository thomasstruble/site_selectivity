"""
Runs the web browser interface for the site selectivity app
"""

from argparse import ArgumentParser
import os

from app import app

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host IP address')
    parser.add_argument('--port', type=int, default=5000, help='Define the port to use')
    parser.add_argument('--debug', action='store_true', default=False, help='Run in debug mode')
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
