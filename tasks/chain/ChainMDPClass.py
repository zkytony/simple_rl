# Python libs.
import random
import sys
import os

# Local libs.
from mdp.MDPClass import MDP
from ChainStateClass import ChainState

class ChainMDP(MDP):
	''' Imeplementation for a standard Chain MDP '''

	actions = ["forward", "reset", "burn"]

	def __init__(self, numStates=5):
		'''
		Args:
			numStates (int) [optional]: Number of states in the chain.
		'''
		MDP.__init__(self, ChainMDP.actions, self._transitionFunction, self._rewardFunction, initState = ChainState(1))
		self.numStates = numStates

	def _rewardFunction(self, state, action, statePrime):
		'''
		Args:
			state (State)
			action (str)
			statePrime

		Returns
			(float)
		'''
		if action == "forward" and statePrime.num == self.numStates:
			return 1
		elif action == "reset":
			return 0.01
		elif action == "burn":
			return -2
		else:
			return 0
	
	def _transitionFunction(self, state, action):
		'''
		Args:
			state (State)
			action (str)

		Returns
			(State)
		'''
		if action == "forward":
			if self.curState < self.numStates:
				return self.curState + 1
			else:
				return self.curState
		elif action == "reset":
			return ChainState(1)
		elif action == "burn":
			return self.curState
		else:
			print "Error: Unrecognized action! (" + action + ")"
			quit()

	def __str__(self):
		return "chainmdp-" + str(self.numStates)
