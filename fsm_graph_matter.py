#!/usr/bin/env python
"""Example of FSM graph"""

import os, sys, inspect, io

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from transitions import *
from transitions.extensions import GraphMachine
#from IPython.display import Image, display, display_png

class Matter(object):
    def is_valid(self):
        return True

    def is_not_valid(self):
        return False

    def is_also_valid(self):
        return True

#    # graph object is created by the machine
#    def show_graph(self, **kwargs):
#        stream = io.BytesIO()
#        self.get_graph(**kwargs).draw(stream, prog='dot', format='png')
#        display(Image(stream.getvalue()))


transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'conditions':'is_valid' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas', 'unless':'is_not_valid' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma',
      'conditions':['is_valid','is_also_valid'] }
]
states=['solid', 'liquid', 'gas', 'plasma']

model = Matter()
machine = GraphMachine(model=model,
                       states=states,
                       transitions=transitions,
                       initial='solid',
                       show_auto_transitions=True, # default value is False
                       title="Matter is Fun!",
                       show_conditions=True)
#model.show_graph()
model.get_graph().draw('fsm_example_matter.png', prog='dot')

print("Done!")