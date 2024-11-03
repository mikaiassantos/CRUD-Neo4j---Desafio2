# connect.py
from neo4j import GraphDatabase

def connect_to_neo4j(uri, username, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        session = driver.session()
        print("Conexão estabelecida com sucesso!")
        return session
    except Exception as e:
        print("Erro ao conectar ao Neo4j:", e)
        return None
