import numpy as np

class State:
	def __init__(self, transitions=None, probabilities=None):
		self.transitions = transitions or {}
		nb_transitions = len(self.transitions)

		# Check if probabilities is a valid argument
		if probabilities is None or len(probabilities) != nb_transitions:
			self.probabilities = {key: 1/nb_transitions for key in self.transitions}
		else:
			self.probabilities = probabilities

		# Compute cumulative sums of probabilities
		self.cum_sums = []
		s = 0
		for i, (key, probability) in enumerate(self.probabilities.items()):
			s += probability
			# Force the final sum to be 1
			if i+1 == len(self.probabilities):
				s = 1
			self.cum_sums.append((s, key))

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
		s, key = self.cum_sums[i] 
		while v > s:
			i += 1
			s, key = self.cum_sums[i]
		return key

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
