rankvalues = dict((r,i) 
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

def rank_hand(handString):
	hand = handString.split(',')
		
	suits = [s[1] for r,s in enumerate(hand)]
	ranks = sorted([s[0] for r,s in enumerate(hand)], key=lambda i:rankvalues[i], reverse=True)

	max_rank = rankvalues[ranks[0]]
	min_rank = rankvalues[ranks[-1]]
	
	#a_to_five_straight = max_rank == 14 and min_rank == 2 and max_rank - min_rank == 12 and len(set(ranks)) == 5
	
	a_to_five_straight = ['A','5','4','3','2'] == ranks
	
	straight = (max_rank - min_rank) == 4 and len(set(ranks)) == 5 or a_to_five_straight
	flush = len(set(suits)) == 1


	def get_rank_values(cards):
		if a_to_five_straight:
			return [5,4,3,2,1]	
		
		return [rankvalues[s] for s in cards]
	
	def of_a_kind(numCards, butnot=None):	
		if butnot == None:
			return [r for r in ranks if ranks.count(r) == numCards][:numCards]
		
		return [r for r in ranks if ranks.count(r) == numCards and r not in butnot]
					
	if straight and flush: return CONST_STRAIGHT_FLUSH, get_rank_values(ranks)
	
	kind4 = of_a_kind(4)
	kind1 = of_a_kind(1)
		
	if kind4: return CONST_FOUR_OF_A_KIND, get_rank_values(kind4), get_rank_values(kind1)
	
	kind3 = of_a_kind(3)
	kind2 = of_a_kind(2)
		
	if kind3 and kind2: return CONST_FULL_HOUSE, get_rank_values(kind3), get_rank_values(kind2)
	if flush: return CONST_FLUSH, get_rank_values(ranks)
	if straight: return CONST_STRAIGHT, get_rank_values(ranks)
	if kind3: return CONST_THREE_OF_A_KIND, get_rank_values(kind3), get_rank_values([card for card in ranks if card not in kind3])
	
	secondKind2 = of_a_kind(2, kind2)
	
	if kind2 and secondKind2: return CONST_TWO_PAIR, get_rank_values(kind2), get_rank_values(secondKind2), get_rank_values(kind1)
	if kind2: return CONST_PAIR, get_rank_values(kind2), get_rank_values([card for card in ranks if card not in kind2]	)
	return CONST_HIGH_CARD, get_rank_values(ranks)
	
	
rank_hand('Tc,9d,8s,9s,Ac')