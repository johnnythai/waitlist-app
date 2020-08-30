from datetime import datetime
import mysql.connector
from getpass import getpass

"""
We are using MySQL to manage our 'waitlist' database.
We will have two tables: waiting and seated.
Limited number of guests can be seated. When a seated guest leaves, 
a waiting guest will be removed from waiting table and  moved to the seated table

connector() is a method that instantiates an object using the definition found in class
"""

# username = input('Enter username: ')
# password = getpass('Logging into \'{user}\'...\nEnter password: ').format(user=username)

# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user=username,
#     password=password,
#     database="waitlist"
# )

# mycursor = conn.cursor()

class Party:
    """
    Created Party object whenever guests check in.
    """

    def __init__(self, date, party_num, name, size, phone, wait_time):
        self.date = date
        self.party_num = party_num
        self.name = name
        self.size = size
        self.phone = phone
        self.wait_time = wait_time

        def __str__(self):
            return self.name

    def show_party(self):
        """
        Function to print table info.
        """

        print(
            '\nParty Number ', self.party_num,
            '\n     Name: ', self.name,
            '\n     Size: ', self.size,
            '\n     Phone: ', self.phone,
            '\n     Wait Time: ', self.wait_time, ' minutes'
        )

    def time_seated(self):
        """
        Time (minutes) table will be occupied after being seated. A function of party size.
        Returns eat_time.
        """

        if datetime.datetime.now().hour <= 16:
            '''
            Lunch time is before 4pm.
            '''

            if self.size <= 4:
                eat_time = 60
                return eat_time

            elif self.size < 8:
                eat_time = 75
                return eat_time
            
            else:
                eat_time = 90
                return eat_time

        if datetime.datetime.now().hour > 16:
            '''
            Dinner time is after 4pm.
            '''

            if self.size <= 4:
                eat_time = 90
                return eat_time

            elif self.size < 8:
                eat_time = 105
                return eat_time
            
            else:
                eat_time = 120
                return eat_time

def commit():
    """
    Committing changes to the database.
    """

    conn.commit()
    print('Changes have been saved!')

def create_tables():
    """
    Creating waiting and seated tables for our db.
    """
    
    mycursor.execute("""
        CREATE TABLE waiting
        (date date, party_num int, name text, size int, phone int, wait_time int)
        """)

    mycursor.execute("""
        CREATE TABLE seated
        (date date, table_num int, name text, size int, time_seated int)
        """)

def check_tables():
    """
    Checking if the waiting and seated tables exist. If so, delete table data. If none exist, create new.
    """

    mycursor.execute('''
        SELECT count(*) FROM information_schema.tables WHERE table_name="waiting" OR table_name="seated"
        ''')

    # If waiting and seated tables exist, we check if it is a new day. If so, we run del_tables() to clear the data.
    if mycursor.fetchone()[0] == 2:
        print('A table already exists. Checking if we should clear the table...')
        del_tables(mycursor)

    else:
        print('Tables do not exist. Creating tables...')
        create_tables(mycursor)
        print('\nTables for \'waiting\' and \'seated\' have now been created.')

def del_tables():
    """
    Clearing our table data. This function should run if it is a new day.
    """
    
    today = datetime.now()
    waiting_date = mycursor.execute("SELECT date FROM waiting")
    seated_date = mycursor.execute("SELECT date FROM seated")

    if waiting_date == None and seated_date == None:
        pass

    elif waiting_date == today or seated_date == today:
        pass

    else:
        mycursor.execute("DELETE TABLE waiting")
        mycursor.execute("DELETE TABLE seated")
        commit()

def insert(new_party):
    """
    Inserting a party into a table.
    """

    commit()

def home():
    """
    From here, we can see who is on the waitlist, manipulate waitlist, show waitlisted party info, show seated list,
    add to waitlist, move waitlisted party to seated list
    
    1. Always show waitlist (names and size)
    2. Show waitlist party info (able to edit)
    3. show seated list
    4. Insert into waiting table
    5. Insert into seated table
    """

    print('we did it!')

    new_party = Party(datetime.now(), 1, Johnny, 3, 9492000892, 0)

    insert(mycursor, new_party)

if __name__ == '__main__':
    check_tables()