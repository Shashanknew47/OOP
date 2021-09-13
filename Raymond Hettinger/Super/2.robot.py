import unittest
 
class Robot(object):

    def fetch(self,tool):
        print('Physical movement! fetching.')
    
    def move_forward(self,tool):
        print('Physical movement! moving forward.')

    def move_backward(self,tool):
        print('Physical movement! moveing backward.')

    def replace(self,tool):
        print('Physical Movement! Replacing.')


class CleaningRobot(Robot):
    
    def clean(self,tool,times=10):
        super().fetch(tool)
        for _ in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)

# if __name__=='__main__':
    # t = CleaningRobot()
    # t.clean('broom')
    
class MockBot(Robot):

    def __init__(self):
        self.tasks = []
    
    def fetch(self,tool):
        self.tasks.append(f'fetching {tool}')

    def move_forward(self,tool):
        self.tasks.append(f'forward {tool}')

    def move_backward(self,tool):
        self.tasks.append(f'backward {tool}')

    def replace(self,tool):
        self.tasks.append(f'replace {tool}')

class MockedCleaningRobot(CleaningRobot,MockBot):
    pass


class TestCleaningRobot(unittest.TestCase):
    
    def test_clean(self):

        t = MockedCleaningRobot()
        t.clean('mop')
        expected =  (['fetching mop'] + ['forward mop','backward mop']*10 + ['replace mop'])

        self.assertEqual(t.tasks,expected)

unittest.main()
