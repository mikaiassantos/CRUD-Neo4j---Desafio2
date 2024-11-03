# operations/delete.py
def delete_user(session, nome):
    query = """
    MATCH (u:Usuario {nome: $nome})
    DELETE u
    """
    session.run(query, nome=nome)
    print("Usuário deletado com sucesso!")
