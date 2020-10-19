#!/usr/bin/env python3

import connexion

from openapi_server import encoder

from neo4j import GraphDatabase
from flask import g

uri = "bolt://localhost:7687"

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Family Lock API'})
    app.run(port=8080)

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = GraphDatabase.driver(uri, auth=("neo4j", "1234"))
    return db

if __name__ == '__main__':
    main()
