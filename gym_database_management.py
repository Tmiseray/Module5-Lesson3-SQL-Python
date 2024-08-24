from connect_mysql import connect_database

# Task 1: Add a New Member
def add_member(conn, cursor, id, name, age):
    # First, check if ID already exists in the database
    check_query = "SELECT id FROM Members WHERE id = %s"
    cursor.execute(check_query, (id,))
    member = cursor.fetchone()

    if member:
        # If member ID already exists, raise error
        raise ValueError(f"Member ID: {id} already exists.")
    else:
        # If Member ID does not exist
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        conn.commit()
        print("New member added successfully!")

# Task 2: Add a Workout Session
def add_workout_session(conn, cursor, member_id, date, duration_minutes, calories_burned):
    # First, check if member ID is valid/exists
    check_query = "SELECT id FROM Members WHERE id = %s"
    cursor.execute(check_query, (member_id,))
    member = cursor.fetchone()

    if member:
        # If Member ID valid/exists
        query = "INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print(f"Susccessfully added workout session for Member ID: {member_id}")
    else:
        # If member ID invalid/doesn't exist raise error
        raise ValueError(f"Member ID: {member_id} is invalid or does not exist in database.")
    
# Task 3: Updating Member Information
def update_member_age(conn, cursor, member_id, new_age):
    # First check if Member ID exists
    check_query = "SELECT id FROM Members WHERE id = %s"
    cursor.execute(check_query, (member_id,))
    member = cursor.fetchone()

    if member:
        # If Member ID valid/exists
        query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(query, (new_age, member_id))
        conn.commit()
        print(f"Successfully updated Age to {new_age} for Member ID: {member_id}")
    else:
        # If member ID invalid/doesn't exist raise error
        raise ValueError(f"Member ID: {member_id} is invalid or does not exist in database.")

# Task 4: Delete a Workout Session
def delete_workout_session(conn, cursor, session_id):
    # First, check if Session ID exists
    check_query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
    cursor.execute(check_query, (session_id,))
    session = cursor.fetchone()

    if session:
        # If session ID valid/exists
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, (session_id,))
        conn.commit()
        print(f"Successfully deleted Session ID: {session_id}")
    else:
        # If Session ID invalid/doesn't exist raise error
        raise ValueError(f"Session ID: {session_id} is invalid or does not exist in database.")
    
# 2. Task 1: SQL BETWEEN
def get_members_in_age_range(cursor, min_age, max_age):
    query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (min_age, max_age))
    print(f"Members with ages between {min_age} and {max_age}:")
    for member in cursor.fetchall():
        print(member)

def gym_database_management():
    # Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            print("\nGym Database Management")
            print("1: Add a Member")
            print("2: Add a Workout Session")
            print("3: Update Member's Age")
            print("4: Delete a Workout Session")
            print("5: Find Members in Age Range")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                id = input("Enter Member ID: ")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                add_member(conn, cursor, id, name, age)
            elif choice == '2':
                member_id = input("Enter Member ID: ")
                date = input("Enter Date (YYYY-MM-DD): ")
                duration_minutes = input("Enter Duration in Minutes: ")
                calories_burned = input("Enter Calories Burned: ")
                add_workout_session(conn, cursor, member_id, date, duration_minutes, calories_burned)
            elif choice == '3':
                member_id = input("Enter Member ID: ")
                new_age = input("Enter Member's New Age: ")
                update_member_age(conn, cursor, member_id, new_age)
            elif choice == '4':
                session_id = input("Enter Session ID to Delete: ")
                delete_workout_session(conn, cursor, session_id)
            elif choice == '5':
                min_age = input("Enter Minimum Age: ")
                max_age = input("Enter Maximum Age: ")
                get_members_in_age_range(cursor, min_age, max_age)
            else:
                print("Invalid choice.")

        except ValueError as v:
            print(v)
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    gym_database_management()