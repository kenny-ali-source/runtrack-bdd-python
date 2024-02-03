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
        query = "SELECT SUM(capacite) AS total_capacite FROM salle;"
        cursor.execute(query)
        result = cursor.fetchone()

        total_capacite = result[0]
        print(f"La superficie de La Plateforme est de : {total_capacite}")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")

