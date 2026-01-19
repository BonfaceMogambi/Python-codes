import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gambigeeks@96',
    database='mydatabase'
)
cursor = conn.cursor()

try:
    # Step 1: Create a temporary table called 'students' with the same structure as 'users'
    cursor.execute("""
        CREATE TABLE students LIKE users;
    """)

    # Step 2: Insert data into 'students', letting MySQL auto-generate new IDs
    cursor.execute("""
        INSERT INTO students (name, age)
        SELECT name, age FROM users ORDER BY id;
    """)

    # Step 3: Drop the old 'users' table
    cursor.execute("DROP TABLE users;")

    # Step 4: Rename 'students' back to 'users'
    cursor.execute("RENAME TABLE students TO users;")

    # Step 5: Reset AUTO_INCREMENT to start from 1
    cursor.execute("ALTER TABLE users AUTO_INCREMENT = 1;")

    conn.commit()
    print("ID values successfully reset starting from 1.")
except mysql.connector.Error as err:
    print("Error:", err)
    conn.rollback()
finally:
    cursor.close()
    conn.close()