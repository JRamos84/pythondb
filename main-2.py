import psycopg2

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"
USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

users = [
    ("user1", "password", "user1@gmail.com"),
    ("user2", "password", "user2@gmail.com"),
    ("user3", "password", "user3@gmail.com"),
    ("user4", "password", "user4@gmail.com"),
]

if __name__ == "__main__":
    ## Conectamos con la base de datos
    try:
        connect = psycopg2.connect(
            dbname="pythondb",
            user="jose",
            password="tu_contraseña",  # Reemplaza con la contraseña real
            host="localhost",
            port="5432"  # Asegúrate de que el puerto es correcto
        )
        
        ## Creamos un contexto para el cursor
        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USER_TABLE)
            
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            cursor.executemany(query, users)
            connect.commit()
            
            # Actualizar usuario
            query = "UPDATE users SET username=%s WHERE id = %s"
            values = ("jose", 1)
            cursor.execute(query, values)
            connect.commit()
            
            # Eliminar usuario
            query = "DELETE FROM users WHERE id = %s"
            values = (1,)  # Debe ser una tupla con una coma al final
            cursor.execute(query, values)
            connect.commit()
    
    except psycopg2.OperationalError as err:
        print(f"⚠️ No fue posible realizar la conexión: {err}")

    finally:
        if 'connect' in locals() and connect:
            connect.close()
            print("✅ Conexión finalizada de forma exitosa")
