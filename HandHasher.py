import itertools
import PokerRules

def split_hand(handString):
	return handString.split(',')

def order_hand(handString):
	hand = split_hand(handString)
	return order_hand_list(hand)
	
def order_hand_list(hand):
	return sorted([s for r,s in enumerate(hand)], key=lambda i:(PokerRules.CONST_RANK_VALUES[i[0]], i[1]), reverse=True)

def hash_handlist(hand):
	return -1

def hash_handstring(hand_str):
		
	return hash_handlist(split_hand(handString))
	
	