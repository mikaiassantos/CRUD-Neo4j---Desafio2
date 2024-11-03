# operations/create.py
def create_user(session, nome, idade, email):
    query = """
    CREATE (u:Usuario {nome: $nome, idade: $idade, email: $email})
    RETURN u
    """
    session.run(query, nome=nome, idade=idade, email=email)
    print("Usuário criado com sucesso!")
