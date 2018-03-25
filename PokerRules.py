rankvalues = dict((r,i) 
                   for i,r in enumerate('..23456789TJQKA'))

# def poker(hand):
#     hand = hand.split()
# 
#     suits = [s for r,s in hand]
#     ranks = sorted([rankvalues[[i][/i]r] for r,s in hand])
#     ranks.reverse()
#     flush = len(set(suits)) == 1
#     straight = (max(ranks)-min(ranks))==4 
#                 and len(set(ranks))==5
# 
#     def kind(n, butnot=None):
#         return some(r for r in ranks
#                     if ranks.count(r) == n and r != butnot)
# 
# 
#     if straight and flush: return 9, ranks
#     if kind(4): return 8, kind(4), kind(1)
#     if kind(3) and kind(2): return 7, kind(3), kind(2)
#     if flush: return 6, ranks
#     if straight: return 5, ranks
#     if kind(3): return 4, kind(3), ranks
#     if kind(2) and kind(2, kind(2)): 
#         return 3, kind(2), kind(2, kind(2)), ranks
#     if kind(2): return 2, kind(2), ranks
#     return 1, ranks
# 
# print sum(poker(line[0:14]) > poker(line[15:29])
#                  for line in file("poker.txt"))
# 
# define poker hands like: 

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
	
	straight = (max_rank - min_rank) == 4 and len(set(ranks)) == 5
	flush = len(set(suits)) == 1
	
	def of_a_kind(numCards, butnot=None):	
		if butnot == None:
			return [r for r in ranks if ranks.count(r) == numCards][:numCards]
		
		return [r for r in ranks if ranks.count(r) == numCards and r not in butnot]
		
		
	if straight and flush: return CONST_STRAIGHT_FLUSH, ranks
	if of_a_kind(4): return CONST_FOUR_OF_A_KIND, of_a_kind(4), of_a_kind(1)
	if of_a_kind(3) and of_a_kind(2): return CONST_FULL_HOUSE, of_a_kind(3), of_a_kind(2)
	if flush: return CONST_FLUSH, ranks
	if straight: return CONST_STRAIGHT, ranks
	if of_a_kind(3): return CONST_THREE_OF_A_KIND, of_a_kind(3), [card for card in ranks if card not in of_a_kind(3)]
	if of_a_kind(2) and of_a_kind(2, of_a_kind(2)): return CONST_TWO_PAIR, of_a_kind(2), of_a_kind(2, of_a_kind(2)), of_a_kind(1)
	if of_a_kind(2): return CONST_PAIR, of_a_kind(2), [card for card in ranks if card not in of_a_kind(2)]	
	return CONST_HIGH_CARD, ranks

