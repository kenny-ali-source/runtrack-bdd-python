import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "LaPlateforme"

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
       
        cursor = connection.cursor()

       
        query = "SELECT nom, capacite FROM salle;"
        cursor.execute(query)

   
        results = cursor.fetchall()

        cursor.close()
        connection.close()

       
        formatted_results = '[' + ', '.join([f'("{nom}", {capacite})' for nom, capacite in results]) + ']'

        print(formatted_results)

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
