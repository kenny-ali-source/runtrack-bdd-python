import mysql.connector

class employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employe (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                prenom VARCHAR(255),
                salaire DECIMAL(10, 2),
                id_service INT
            )
        ''')
        self.conn.commit()

    def insert_employe(self, nom, prenom, salaire, id_service):
        self.cursor.execute('''
            INSERT INTO employe (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        ''', (nom, prenom, salaire, id_service))
        self.conn.commit()

    def get_employes_above_salary(self, salary):
        self.cursor.execute('SELECT * FROM employe WHERE salaire > %s', (salary,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


employe_manager = employe(
    host='localhost',
    user='root',
    password='root',
    database='LaPlateforme'
)

employe_manager.create_table()
employe_manager.insert_employe('Nom4', 'Prenom4', 3200.00, 2)

result = employe_manager.get_employes_above_salary(3000)
print(result)

employe_manager.close_connection()
