from waitlist import Party

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
