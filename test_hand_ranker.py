import PokerRules

def test_rank_hand_Ad2c3h6d8s_returns_1_A8632():
	expected = PokerRules.CONST_HIGH_CARD, ['A','8','6','3','2']
	actual = PokerRules.rank_hand("Ad,2c,3h,6d,8s")
	assert actual == expected
	
	
def test_rank_hand_AsKsQsJsTs_returns_9_AKQJT():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, ['A','K','Q','J','T']
	actual = PokerRules.rank_hand("As,Ks,Qs,Js,Ts")
	assert actual == expected
	
def test_rank_hand_9c8c7c6c5c_returns_9_98765():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, ['9','8','7','6','5']
	actual = PokerRules.rank_hand("9c,8c,7c,6c,5c")
	assert actual == expected
		
def test_rank_hand_4c4d4h4sAc_returns_8_4444A():
	expected = PokerRules.CONST_FOUR_OF_A_KIND, ['4','4','4','4'], ['A']
	actual = PokerRules.rank_hand("4c,4d,4h,4s,Ac")
	assert actual == expected
		
def test_rank_hand_4c4d4hAdAc_returns_7_444AA():
	expected = PokerRules.CONST_FULL_HOUSE, ['4','4','4'], ['A','A']
	actual = PokerRules.rank_hand("4c,4d,4h,Ad,Ac")
	assert actual == expected
	
def test_rank_hand_9c2cKcAc6c_returns_6_AK962():
	expected = PokerRules.CONST_FLUSH, ['A','K','9','6','2']
	actual = PokerRules.rank_hand("9c,2c,Kc,Ac,6c")
	assert actual == expected
	
def test_rank_hand_9c8c7c6c5d_returns_5_98765():
	expected = PokerRules.CONST_STRAIGHT, ['9','8','7','6','5']
	actual = PokerRules.rank_hand("9c,8c,7c,6c,5d")
	assert actual == expected
			
def test_rank_hand_4c4d4hAd2c_returns_4_444A2():
	expected = PokerRules.CONST_THREE_OF_A_KIND, ['4','4','4'], ['A','2']
	actual = PokerRules.rank_hand("4c,4d,4h,Ad,2c")
	assert actual == expected

def test_rank_hand_4c4dAhAd2c_returns_3_44AA2():
	expected = PokerRules.CONST_TWO_PAIR, ['A','A'],['4','4'],['2']
	actual = PokerRules.rank_hand("4c,4d,Ah,Ad,2c")
	assert actual == expected

	
def test_rank_hand_3c5dAhAd2c_returns_2_AA532():
	expected = PokerRules.CONST_PAIR, ['A','A'],['5','3','2']
	actual = PokerRules.rank_hand("3c,5d,Ah,Ad,2c")
	assert actual == expected
