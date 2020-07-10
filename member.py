from abc import ABC, abstractmethod

class Member(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def introduce_yourself(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Instructor(Member):

    def __init__(self, name, bio, skills=None):
        super(Instructor, self).__init__(name)
        self.bio = bio
        self._skills = set()
        if type(skills) is list:
            for skil in skills:
                self.add_skill(skil) 

    def __str__(self):
        return f'Instructor - {self.name}'

    @property
    def skills(self):
        return self._skills

    def add_skill(self, skill):
        self._skills.add(str(skill).lower())


    def introduce_yourself(self):
        return '''
            Hi, my name is {}.
            I am here because {}.
            '''.format(self.name, self.bio)

class Attendee(Member):

    def __init__(self, name, reason):
        super(Attendee, self).__init__(name)
        self.reason = reason

    def __str__(self):
        return f'Attendee - {self.name}'

    def introduce_yourself(self):
        return '''
            Hi, my name is {}.
            I am here because {}.
            '''.format(self.name, self.reason)