import itertools
import PokerRules
import re

def split_hand(handString):
	return handString.split(',')

def order_hand(handString):
	hand = split_hand(handString)
	return order_hand_list(hand)
	
def order_hand_list(hand):
	return sorted([s for r,s in enumerate(hand)], key=lambda i:(PokerRules.CONST_RANK_VALUES[i[0]], i[1]), reverse=True)

def i_to_b(i, pad_to=0):
	binary_number = ''
	
	if i == 0 or i == None:
		return '0'
	else:
		binary_number = bin(i)[2:]
				
	if (pad_to > 0):
		return binary_number.rjust(pad_to, '0')
				
	return binary_number
	
CONST_HAND_SIZE = 5
CONST_CARD_BIT_LENGTH = 6 # 2 bits for suit, 4 bits for rank
CONST_CARD_BINARY_PAD_VALUE = '0'
CONST_SUIT_BINARY_VALUES = {'c':'00', 'd':'01', 'h':'10','s':'11'}
CONST_SUIT_BINARY_LENGTH = 2
CONST_RANK_VALUES = dict((r,i) 
                   for i,r in enumerate('..23456789TJQKA'))
	
def hash_handlist(hand):
	if (hand == None or len(hand) == 0):
		return 0
	
	binary_hand = ''
	
	CONST_RANK_INDEX = 0
	CONST_SUIT_INDEX = 1
	
	for card in order_hand_list(hand):
		rank = CONST_RANK_VALUES[card[CONST_RANK_INDEX]]	
		binary_rank = i_to_b(rank)
		
		binary_suit = CONST_SUIT_BINARY_VALUES[card[CONST_SUIT_INDEX]]	
						
		binary_hand += (binary_suit + binary_rank).rjust(CONST_CARD_BIT_LENGTH, CONST_CARD_BINARY_PAD_VALUE)
	
	
	base2 = 2
	
	return int(binary_hand, base2)

def hash_handstring(hand_str):	
	return hash_handlist(split_hand(handString))
	
def unhash_hand(i):
	binary_number = bin(i)[2:]
	binary_hand = binary_number.rjust(CONST_CARD_BIT_LENGTH * CONST_HAND_SIZE, CONST_CARD_BINARY_PAD_VALUE)
	split_hand = re.findall('......', binary_hand)
	empty_card = '000000'
		
	def get_card(binary_card):
		def get_key(dict, value):
			return (list(dict.keys())[list(dict.values()).index(value)])[0][0]
		
		suit = binary_card[0:CONST_SUIT_BINARY_LENGTH]
		rank = int(binary_card[CONST_SUIT_BINARY_LENGTH:], 2)
		
		suit = get_key(CONST_SUIT_BINARY_VALUES, suit)
		rank = get_key(CONST_RANK_VALUES, rank)
								
		return rank + suit
		
	binary_hand = list(card for card in split_hand if card != empty_card)
	
	cards_in_hand = list()
	for binary_card in binary_hand:
		cards_in_hand.append( get_card(binary_card))
	
	return cards_in_hand
	

def get_int_rank(handStr):
	handList = list(PokerRules.rank_hand_list(split_hand(handStr)))
	
	hand_power_len = 4
	rank_len = 5
	
	ranking = i_to_b(handList[0],hand_power_len)
		
	for set in handList[1]:
		for card in set:
			binary_card = i_to_b(card, rank_len)
			ranking += binary_card
	
	print(ranking)
	
	return int(ranking, 2)
	
