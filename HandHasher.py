import itertools
import PokerRules

def split_hand(handString):
	return handString.split(',')

def order_hand(handString):
	hand = split_hand(handString)
	return order_hand_list(hand)
	
def order_hand_list(hand):
	return sorted([s for r,s in enumerate(hand)], key=lambda i:(PokerRules.CONST_RANK_VALUES[i[0]], i[1]), reverse=True)

def i_to_b(i):
	binary_number = ''
	
	if i == 0 or i == None:
		return '0'
	else:
		binary_number = bin(i)[2:]
				
	return binary_number
	
CONST_CARD_BIT_LENGTH = 6 # 2 bits for suit, 4 bits for rank
CONST_CARD_BINARY_PAD_VALUE = '0'
CONST_SUIT_VALUES = {'c':0, 'd':1, 'h':2,'s':3}
CONST_RANK_VALUES = dict((r,i) 
                   for i,r in enumerate('..23456789TJQKA'))
	
def hash_handlist(hand):
	if (hand == None or len(hand) == 0):
		return i_to_b(0)
	
	binary_hand = ''
	
	CONST_RANK_INDEX = 0
	CONST_SUIT_INDEX = 1
	
	for card in order_hand_list(hand):
		suit = CONST_SUIT_VALUES[card[CONST_SUIT_INDEX]]
		rank = CONST_RANK_VALUES[card[CONST_RANK_INDEX]]	
	
		binary_suit = i_to_b(suit)
		binary_rank = i_to_b(rank)
						
		binary_hand += (binary_suit + binary_rank).rjust(CONST_CARD_BIT_LENGTH, CONST_CARD_BINARY_PAD_VALUE)
	
	
	return binary_hand

def hash_handstring(hand_str):	
		
	return hash_handlist(split_hand(handString))
	
	