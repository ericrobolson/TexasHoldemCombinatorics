import itertools

CONST_RANK_VALUES = dict((r,i) 
                   for i,r in enumerate('..23456789TJQKA'))

CONST_STRAIGHT_FLUSH = 9
CONST_FOUR_OF_A_KIND = 8
CONST_FULL_HOUSE = 7
CONST_FLUSH = 6
CONST_STRAIGHT = 5
CONST_THREE_OF_A_KIND = 4
CONST_TWO_PAIR = 3
CONST_PAIR = 2
CONST_HIGH_CARD = 1

# Rank a CSV separated hand of the format '9c,10d,5s,3h,2d'
def rank_hand(handString):
	hand = handString.split(',')
	return rank_hand_list(hand)
	
def rank_hand_list(hand):	
	suits = [s[1] for r,s in enumerate(hand)]
	ranks = sorted([s[0] for r,s in enumerate(hand)], key=lambda i:CONST_RANK_VALUES[i], reverse=True)
	
	max_rank = CONST_RANK_VALUES[ranks[0]]
	min_rank = CONST_RANK_VALUES[ranks[-1]]
	
	is_a_to_five_straight = ['A','5','4','3','2'] == ranks
	
	straight = (max_rank - min_rank) == 4 and len(set(ranks)) == 5 or is_a_to_five_straight
	flush = len(set(suits)) == 1

	def get_rank_values(cards):
		if is_a_to_five_straight:
			return [5,4,3,2,1]	
		
		return [CONST_RANK_VALUES[s] for s in cards]
	
	def of_a_kind(numCards, butnot=None):	
		if butnot == None:
			return [r for r in ranks if ranks.count(r) == numCards][:numCards]
		
		return [r for r in ranks if ranks.count(r) == numCards and r not in butnot]
				
	# Straight flush
	if straight and flush: 
		return CONST_STRAIGHT_FLUSH, [get_rank_values(ranks)]
	
	kind4 = of_a_kind(4)
	kind1 = of_a_kind(1)
		
	# 4 of a kind
	if kind4: 
		return CONST_FOUR_OF_A_KIND, [get_rank_values(kind4), get_rank_values(kind1)]
	
	kind3 = of_a_kind(3)
	kind2 = of_a_kind(2)
		
	# Full house
	if kind3 and kind2: 
		return CONST_FULL_HOUSE, [get_rank_values(kind3), get_rank_values(kind2)]
	if flush: 
		return CONST_FLUSH, [get_rank_values(ranks)]
	if straight: 
		return CONST_STRAIGHT, [get_rank_values(ranks)]
	# 3 of a kind
	if kind3: 
		return CONST_THREE_OF_A_KIND, [get_rank_values(kind3), get_rank_values([card for card in ranks if card not in kind3])]
	
	secondKind2 = of_a_kind(2, kind2)
	
	# 2 pair
	if kind2 and secondKind2: 
		return CONST_TWO_PAIR, [get_rank_values(kind2), get_rank_values(secondKind2), get_rank_values(kind1)]
	# Pair
	if kind2: 
		return CONST_PAIR, [get_rank_values(kind2), get_rank_values([card for card in ranks if card not in kind2])]
	# High card
	return CONST_HIGH_CARD, [get_rank_values(ranks)]
	

def get_best_hand(handString):
	hand = handString.split(',')
	
	hand_size = 5

	if len(hand) < hand_size:
		raise ValueError("Hand length must be at least 5 cards")
	
	permuations = list(itertools.combinations(hand, hand_size))
	best_hand = permuations[0]
	best_hand_value = rank_hand_list(best_hand)
		
	for current_hand in permuations:
		new_hand_value = rank_hand_list(current_hand)
		hand_type_power_index = 0
		
		new_hand_power = new_hand_value[hand_type_power_index]
		best_hand_power = best_hand_value[hand_type_power_index]
		
		if (new_hand_power > best_hand_power):
			best_hand_value = new_hand_value
			best_hand = current_hand
			continue
		elif new_hand_power == best_hand_power:
			# compare the hands and pick the one with the highest value
			hand_value_index = 1
			
			flattened_new_hand_values = [item for sublist in new_hand_value[hand_value_index] for item in sublist]
			flattened_best_hand_values = [item for sublist in best_hand_value[hand_value_index] for item in sublist]
			
			for i in range(0,5):
				if flattened_new_hand_values[i] > flattened_best_hand_values[i]:
					best_hand = current_hand
					best_hand_value = new_hand_value			
	
	return list(best_hand)
	