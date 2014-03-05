#!/usr/bin/python

#pylint: disable-msg: C0111

class Command:
    def __init__(self, name, args):
        self.name = name
        self.args = []
        for a in args:
            self.args.append(a, None)

    def marshal(self):
        raise NotImplementedException()
  
    def unmarshal(self):
        raise NotImplementedException()

    def execute(self):
        raise NotImplementedException()

    def syntax(self):
        return "%s" + ' '.join([a[0] for a in args])

class SetState(Command):
    def __init__(self):
        super(SetState, self).__init__('SetState', ['speaker', 'state'])

class GetState(Command):
    def __init__(self):
        super(SetState, self).__init__('GetState')
        

print SetState().syntax()
print GetState().syntax()

