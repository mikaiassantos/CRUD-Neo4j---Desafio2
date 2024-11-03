# operations/read.py
def read_user(session, nome):
    query = """
    MATCH (u:Usuario {nome: $nome})
    RETURN u.nome AS nome, u.idade AS idade, u.email AS email
    """
    result = session.run(query, nome=nome)
    for record in result:
        print(f"Nome: {record['nome']}, Idade: {record['idade']}, Email: {record['email']}")
