from connect import connect_to_neo4j
from operations.create import create_user
from operations.read import read_user
from operations.update import update_user_email
from operations.delete import delete_user

# Conectar ao Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "desafio2"
session = connect_to_neo4j(uri, username, password)

if session:
    # Lista de 50 usuários (10 anteriores + 40 novos)
    users_data = [
        ("Alice", 25, "alice@example.com"),
        ("Bob", 30, "bob@example.com"),
        ("Carlos", 22, "carlos@example.com"),
        ("Diana", 28, "diana@example.com"),
        ("Evan", 35, "evan@example.com"),
        ("Fiona", 27, "fiona@example.com"),
        ("George", 29, "george@example.com"),
        ("Hannah", 24, "hannah@example.com"),
        ("Isaac", 32, "isaac@example.com"),
        ("Julia", 31, "julia@example.com"),
        ("Kevin", 23, "kevin@example.com"),
        ("Laura", 34, "laura@example.com"),
        ("Mia", 26, "mia@example.com"),
        ("Nathan", 29, "nathan@example.com"),
        ("Olivia", 33, "olivia@example.com"),
        ("Paul", 30, "paul@example.com"),
        ("Quinn", 24, "quinn@example.com"),
        ("Rita", 36, "rita@example.com"),
        ("Sam", 28, "sam@example.com"),
        ("Tina", 27, "tina@example.com"),
        ("Ursula", 29, "ursula@example.com"),
        ("Victor", 25, "victor@example.com"),
        ("Wendy", 32, "wendy@example.com"),
        ("Xander", 31, "xander@example.com"),
        ("Yara", 30, "yara@example.com"),
        ("Zoe", 22, "zoe@example.com"),
        ("Adam", 34, "adam@example.com"),
        ("Bella", 26, "bella@example.com"),
        ("Charlie", 29, "charlie@example.com"),
        ("David", 28, "david@example.com"),
        ("Eva", 27, "eva@example.com"),
        ("Frank", 25, "frank@example.com"),
        ("Grace", 31, "grace@example.com"),
        ("Henry", 30, "henry@example.com"),
        ("Isla", 22, "isla@example.com"),
        ("Jack", 35, "jack@example.com"),
        ("Kira", 33, "kira@example.com"),
        ("Leo", 26, "leo@example.com"),
        ("Maya", 29, "maya@example.com"),
        ("Noah", 24, "noah@example.com"),
        ("Opal", 28, "opal@example.com"),
        ("Piper", 27, "piper@example.com"),
        ("Quincy", 30, "quincy@example.com"),
        ("Riley", 22, "riley@example.com"),
        ("Sophie", 34, "sophie@example.com"),
        ("Travis", 32, "travis@example.com"),
        ("Uma", 31, "uma@example.com"),
        ("Vera", 29, "vera@example.com"),
        ("Will", 26, "will@example.com"),
        ("Xena", 30, "xena@example.com"),
        ("Yvonne", 28, "yvonne@example.com"),
        ("Zane", 35, "zane@example.com"),
    ]

    # Criar usuários
    for nome, idade, email in users_data:
        create_user(session, nome, idade, email)
        print(f"Usuário {nome} criado com sucesso!")

    # Ler todos os usuários criados
    for nome, _, _ in users_data:
        read_user(session, nome)
    
    # Atualizar email de um usuário
    update_user_email(session, "Alice", "alice_novo@example.com")

    # Ler o usuário atualizado
    read_user(session, "Alice")

    # Deletar um usuário
    delete_user(session, "Bob")

    # Ler todos os usuários restantes
    for nome, _, _ in users_data:
        read_user(session, nome)

    # Fechar a sessão ao final
    session.close()

