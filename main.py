import pymysql




DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"
USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

users = [
    ("user1","password","user1@gmail.com"),
    ("user2","password","user2@gmail.com"),
    ("user3","password","user3@gmail.com"),
    ("user4","password","user4@gmail.com"),

]




if __name__ == "__main__":
    ## Conectamos con la base de datos
    try:
        connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root_local',
            passwd='',
            db='pythondb')
        
        ## Creamos un contexto para el cursor
        with connect.cursor() as cursor:
    
            cursor.execute(DROP_TABLE_USERS)

            cursor.execute(USER_TABLE)
            
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            
            # for user in users:
            #     cursor.execute(query, user)
            
            cursor.executemany(query, users)
            
            connect.commit()
            
            # query = "SELECT id, username, email FROM users "
            
            # row = cursor.execute(query)
            
            # # for user in cursor.fetchall():
            # #     print(user)
            
            # for user in cursor.fetchmany(2):
            #     print(user)
            
            # user = cursor.fetchone()
            # print("mi objeto user", user)
        
            query = 'UPDATE users SET username=%s WHERE id = %s'
            
            values = ('jose', 1 )
            
            cursor.execute(query, values)
            connect.commit()
            
            
            
            query = 'DELETE FROM users WHERE id = %s'
            
            values = ( 1 )
            
            cursor.execute(query, values)
            connect.commit()
            
            
            
        
    except pymysql.err.OperationalError as err:
        print(f'no fue posible realizar la conexión {err}')
        
    finally:
        
        
        ## Finalizamos 
        

        connect.close()
        
        print('Conexión finalizada de forma exitosa')