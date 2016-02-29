"""
Toggles the Dynamic Evaluation stage for Maya Parallel evaluation.

Useful if dynmaics are causing the scene to run slowly.
"""

import maya.cmds as mc

state = mc.evaluator(q=True, name='dynamics')
mc.evaluator(en=not state, name='dynamics')
if state:
    print('Dynamics Evaluation Turned OFF'),
else:
    print('Dynamics Evaluation Turned ON'),
