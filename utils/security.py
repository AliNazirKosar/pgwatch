# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/73532164/proper-data-encryption-with-a-user-set-password-in-python3

from pwdlib import PasswordHash

# recommended() significa que elige automaticamente el algoritmo mas seguro disponible,
# tambien hay otra opcion que es sin recommended() en la cual tenemos que especificar
# el algoritmo
# sin recommended — configuras tu pwd = PasswordHash([HasherArgon2()])
pwd = PasswordHash.recommended()

# convierto la pass en un hash
def hash_password(password: str) -> str:
    return pwd.hash(password)

# verifico que la pass coincide con el hash guardado en BD
# se usa cuando el usuario quiere conectarse, es decir, para comprobar si la pass que manda coincide
# con el hash guardado
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)