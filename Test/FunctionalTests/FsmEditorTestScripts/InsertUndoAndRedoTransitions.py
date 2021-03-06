﻿#Copyright (c) 2014 Sony Computer Entertainment America LLC. See License.txt.

import sys
sys.path.append("./CommonTestScripts")

import Test
import FsmUtil

atfDocService.OpenNewDocument(editor)

Test.Equal(0, fsm.Transitions.Count, "Verify new document has no transitions")

statesLeft = []
statesRight = []
transitions = []
transitionsCnt = 10

print "First create a bunch of states"
for i in range(transitionsCnt):
    statesLeft.append(editingContext.InsertState(100, 100 + 50*i, "Left#" + str(i), 64))
for i in range(transitionsCnt):
    statesRight.append(editingContext.InsertState(300, 100 + 50*i, "Right#" + str(i), 64))

print "Now add the transitions"
for i in range(transitionsCnt):
    transitions.append(FsmUtil.AddNewTransitionAndVerify(editingContext, statesLeft[i], statesRight[i]))
    transitions[i].Label = "Transition#" + str(i)

print "Start undo testing"
for i in range(transitionsCnt, 0, -1):
    Test.Equal(i, fsm.Transitions.Count, "Verify transitions count before undo")
    hist.Undo()
    Test.Equal(i - 1, fsm.Transitions.Count, "Verify transitions count after undo");

print "Start redo testing"
for i in range(transitionsCnt):
    Test.Equal(i, fsm.Transitions.Count, "Verify transitions count before redo")
    hist.Redo()
    Test.Equal(i + 1, fsm.Transitions.Count, "Verify transitions count after redo");

cnt = 0
for transition in fsm.Transitions:
    Test.Equal("Transition#" + str(cnt), transition.Label, "Verify label of transition is consistent after redo")
    cnt = cnt + 1

print Test.SUCCESS
