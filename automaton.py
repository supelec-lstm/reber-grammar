import numpy as np

class State:
	def __init__(self):
		self.transitions = {}
		self.probabilities = {}
		self.cum_sums = []

	def set_transitions(self, transitions, probabilities=None):
		self.transitions = transitions
		# Check if the probabilities are valid
		if probabilities is None or len(probabilities) != len(self.transitions):
			self.probabilities = {signal: 1/len(self.transitions) for signal in self.transitions}
		else:
			self.probabilities = probabilities
		self.update_cum_sums()		

	def update_cum_sums(self):
		# Compute cumulative sums of probabilities
		s = 0
		for i, (signal, probability) in enumerate(self.probabilities.items()):
			s += probability
			# Force the final sum to be 1
			if i+1 == len(self.probabilities):
				s = 1
			self.cum_sums.append((s, signal))

	def next(self, signal):
		if signal in self.transitions:
			return self.transitions[signal]
		else:
			# We should define a new exception ...
			raise ValueError("'{}' is not a valid transition.".format(signal))

	def sample(self):
		v = np.random.rand()
		# For more efficiency, binary search should be used
		i = 0
		s, signal = self.cum_sums[i] 
		while v > s:
			i += 1
			s, signal = self.cum_sums[i]
		return signal

class Automaton:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def check(self, string):
		cur_state = self.start
		try:
			for c in string:
				cur_state = cur_state.next(c)
		except:
			return False
		return cur_state is self.end

	def generate(self):
		string = ''
		cur_state = self.start
		while cur_state is not self.end:
			signal = cur_state.sample()
			string += signal
			cur_state = cur_state.next(signal)
		return string
