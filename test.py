import unittest
from member import Member, Instructor, Attendee
from workshop import Workshop

class TestMember(unittest.TestCase):

    def test_instructor(self):
        name = 'Sachin'
        bio = "I want to share my experience!"
        instructor = Instructor(name, bio, skills=['Python'])

        self.assertEqual(instructor.name, name)
        self.assertEqual(instructor.bio, bio)
        self.assertEqual(instructor.skills, {'python'})
        instructor.add_skill('java')
        self.assertEqual(instructor.skills, {'python', 'java'})

    def test_attendee(self):
        name = 'Sachin'
        reason  = "I want to make websites"
        attendee = Attendee(name, reason)

        self.assertEqual(attendee.name, name)
        self.assertEqual(attendee.reason, reason)


class TestWorkshop(unittest.TestCase):

    def test_workshop(self):
        date = '10-07-2020'
        sub = 'python memory management'
        no_of_instructors = 2
        no_of_attendees = 10
        workshop = Workshop(date, sub, no_of_instructors, no_of_attendees)
        self.assertEqual(workshop.date, date)
        self.assertEqual(workshop.subject, sub)
        self.assertEqual(workshop.no_of_instructors, no_of_instructors)
        self.assertEqual(workshop.no_of_attendees, no_of_attendees)

    def test_workshop_params(self):
        date = '2020-01-20'
        sub = 'python memory management'
        no_of_instructors = 'a'
        no_of_attendees = 'b'

        with self.assertRaises(ValueError) as e:
            Workshop(date, sub, no_of_instructors, no_of_attendees)

        date = '10-07-2020' 
        with self.assertRaises(ValueError) as e:
            Workshop(date, sub, no_of_instructors, no_of_attendees)

        no_of_instructors = 2
        with self.assertRaises(ValueError) as e:
            Workshop(date, sub, no_of_instructors, no_of_attendees)

        no_of_attendees = 10
        workshop = Workshop(date, sub, no_of_instructors, no_of_attendees)            
        self.assertEqual(workshop.date, date)
        self.assertEqual(workshop.subject, sub)
        self.assertEqual(workshop.no_of_instructors, no_of_instructors)
        self.assertEqual(workshop.no_of_attendees, no_of_attendees)

    def test_add_participant(self):
        instructor1 = Instructor('Instructor1', 'some bio')
        attendee1 = Attendee('Attendee1', 'some reason')

        date = '10-07-2020'
        sub = 'python memory management'
        no_of_instructors = 2
        no_of_attendees = 10
        workshop = Workshop(date, sub, no_of_instructors, no_of_attendees)
        workshop.add_participant(instructor1)     
        workshop.add_participant(attendee1)
        self.assertEqual(workshop.instructors, {instructor1})
        self.assertEqual(workshop.attendees, {attendee1})

        #trying to add same members multiple times
        workshop.add_participant(instructor1)     
        workshop.add_participant(instructor1)     
        workshop.add_participant(attendee1)
        workshop.add_participant(attendee1)
        self.assertEqual(workshop.instructors, {instructor1})
        self.assertEqual(workshop.attendees, {attendee1})        


        instructor2 = Instructor('Instructor2', 'bio', skills=['python','c++'])
        attendee2 = Attendee('Attendee2', 'reason')
        workshop.add_participant(instructor2) 
        workshop.add_participant(attendee2) 
        self.assertEqual(workshop.instructors, {instructor1, instructor2})
        self.assertEqual(workshop.attendees, {attendee1, attendee2})

        # adding more instructor (or attendee) raises exception
        instructor3 = Instructor('Instructor3', 'bio')
        with self.assertRaises(Exception) as e:
            workshop.add_participant(instructor2)

        workshop.print_details()

if __name__ == '__main__':
    unittest.main()