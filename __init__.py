from workshop import Workshop
from member import Instructor, Attendee

def create_samples():
    ins1 = Instructor('AAA', 'I have knowledge on GIL', skills=['python'] )
    ins2 = Instructor('BBB', 'I have knowledge on GIL', skills=['python', 'java'])
    ins3 = Instructor('BBB', 'I know somethink about memory', skills=['python', 'java'])

    att1 = Attendee('CCC', 'I want to know about GIL')
    att2 = Attendee('DDD', 'I want to know about GIL')
    att3 = Attendee('EEE', 'I want to know about python memory management')
    att4 = Attendee('FFF', 'I want to know about python memory management')
    att5 = Attendee('GGG', 'I want to know about GIL')

    workshop1 = Workshop('10-07-2020', 'python GIL', 2, 5)
    workshop1.add_participant(ins1)
    workshop1.add_participant(ins2)
    workshop1.add_participant(att1)
    workshop1.add_participant(att2)
    workshop1.add_participant(att3)
    workshop1.add_participant(att4)
    workshop1.print_details()

    print('\n')
    workshop2 = Workshop('11-07-2020', 'python Memory', 3, 10)
    workshop2.add_participant(ins1)
    workshop2.add_participant(ins2)
    workshop2.add_participant(ins3)
    workshop2.add_participant(att1)
    workshop2.add_participant(att2)
    workshop2.add_participant(att3)
    workshop2.add_participant(att4)
    workshop2.add_participant(att5)
    workshop2.print_details()

if __name__ == "__main__":
    create_samples()