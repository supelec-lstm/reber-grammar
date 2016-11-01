from automaton import *

start = State()
state0 = State()
state1 = State()
state2 = State()
state3 = State()
state4 = State()
state5 = State()
end = State()

start.set_transitions({'B': state0})
state0.set_transitions({'T': state1, 'P': state2})
state1.set_transitions({'S': state1, 'X': state3})
state2.set_transitions({'T': state2, 'V': state4})
state3.set_transitions({'X': state2, 'S': state5})
state4.set_transitions({'P': state3, 'V': state5})
state5.set_transitions({'E': end})
automaton = Automaton(start, end)

print(automaton.generate())

s = 0
N = 10000
for _ in range(N):
	s += len(automaton.generate())
print(s / N)