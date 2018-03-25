import PokerRules

def test_rank_hand_Ad2c3h6d8s_returns_1_A8632():
	expected = PokerRules.CONST_HIGH_CARD, ['A','8','6','3','2']
	actual = PokerRules.rank_hand("Ad,2c,3h,6d,8s")
	assert actual == expected
	
	
def test_rank_hand_AsKsQsJsTs_returns_9_AKQJT():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, ['A','K','Q','J','T']
	actual = PokerRules.rank_hand("As,Ks,Qs,Js,Ts")
	assert actual == expected
	