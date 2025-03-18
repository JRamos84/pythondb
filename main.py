import pymysql
from decouple import config



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
            values = ('Jose', '123', 'jose@email.com')
            
            cursor.execute(query, values)
            
            connect.commit()
                       
            
        
    
        
    except pymysql.err.OperationalError as err:
        print(f'no fue posible realizar la conexión {err}')
        
    finally:
        
        
        ## Finalizamos 
        

        connect.close()
        
        print('Conexión finalizada de forma exitosa')