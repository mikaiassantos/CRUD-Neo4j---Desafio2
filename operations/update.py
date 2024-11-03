# operations/update.py
def update_user_email(session, nome, novo_email):
    query = """
    MATCH (u:Usuario {nome: $nome})
    SET u.email = $novo_email
    RETURN u
    """
    session.run(query, nome=nome, novo_email=novo_email)
    print("Email do usuário atualizado com sucesso!")
