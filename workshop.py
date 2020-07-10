from member import Instructor, Attendee
from datetime import datetime

class Workshop(object):
    """     
    Attributes: 
        date (str): Workshop happening date in the '%d-%m-%Y' format. 
        subject (str): Subject of the workshop. 
        no_of_instructors (int): Number of instructors. 
        no_of_attendees (int): Number of attendees. 
    """
    def __init__(self, date, subject, no_of_instructors, no_of_attendees):
        self._data = None
        self._no_of_instructors = None
        self._no_of_attendees = None
        self.subject = subject

        self.date = date
        self.no_of_instructors = no_of_instructors
        self.no_of_attendees = no_of_attendees

        self.instructors = set()
        self.attendees = set()

    @property
    def date(self):
        return self._date.strftime('%d-%m-%Y')

    @date.setter
    def date(self, date):
        try:
            self._date = datetime.strptime(date, '%d-%m-%Y')
        except:
            raise ValueError("Date should be in %d-%m-%Y format")

    @property
    def no_of_instructors(self):
        return self._no_of_instructors

    @no_of_instructors.setter
    def no_of_instructors(self, val):
        try:
            self._no_of_instructors = int(val)
        except:
            raise ValueError("Number of instructors should be integer")

    @property
    def no_of_attendees(self):
        return self._no_of_attendees

    @no_of_attendees.setter
    def no_of_attendees(self, val):
        try:
            self._no_of_attendees = int(val)
        except:
            raise ValueError("Number of attendees should be integer")

    def add_participant(self, member):
        if isinstance(member, Instructor):
            self._add_instructor(member)
        elif isinstance(member, Attendee):
            self._add_attendees(member)
        else:
            raise ValueError('Not a valid member')

    def _add_instructor(self, member):
        if len(self.instructors) < self.no_of_instructors:
            self.instructors.add(member)
        else:
            raise Exception('Space not available')

    def _add_attendees(self, member):
        if len(self.attendees) < self.no_of_attendees:
            self.attendees.add(member)
        else:
            raise Exception ("Space not available")

    def print_details(self):
        print('='*80)
        print('{:<20} {:<20}{:<20}{:<20}'.format('DATE', 'SUBJECT','INSTRUCTORS COUNT', 'ATTENDEES COUNT'))
        print('='*80)
        print('{:<20} {:<20}{:^20}{:^20}'.format(self.date, self.subject,len(self.instructors), len(self.attendees)))
        print('-'*80)

        print('{:<5}{:<40}{:<20}'.format('','INSTRUCTORS NAME', 'SKILLS'))
        print(' '*4,'-'*75)
        for i in self.instructors:
            print('{:<6}{:<40}{:<20}'.format(' ', i.name, ','.join(i.skills)))

        print(' '*4,'-'*75)
        print('{:<5}{:<40}{:<20}'.format(' ','ATTENDEES NAME', 'REASON'))
        print(' '*4,'-'*75)
        for i in self.attendees:
            print('{:<6}{:<40}{:<20}'.format(' ', i.name, i.reason))
        print('='*80)