import PokerRules

def test_rank_hand_Ad2c3h6d8s_returns_1_A8632():
	expected = PokerRules.CONST_HIGH_CARD, [[14,8,6,3,2]]
	actual = PokerRules.rank_hand("Ad,2c,3h,6d,8s")

	assert actual == expected
	
	
def test_rank_hand_AsKsQsJsTs_returns_9_AKQJT():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, [[14,13,12,11,10]]
	actual = PokerRules.rank_hand("As,Ks,Qs,Js,Ts")

	assert actual == expected
	
def test_rank_hand_9c8c7c6c5c_returns_9_98765():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, [[9,8,7,6,5]]
	actual = PokerRules.rank_hand("9c,8c,7c,6c,5c")

	assert actual == expected
		
def test_rank_hand_4c4d4h4sAc_returns_8_4444A():
	expected = PokerRules.CONST_FOUR_OF_A_KIND, [[4,4,4,4], [14]]
	actual = PokerRules.rank_hand("4c,4d,4h,4s,Ac")

	assert actual == expected
		
def test_rank_hand_4c4d4hAdAc_returns_7_444AA():
	expected = PokerRules.CONST_FULL_HOUSE, [[4,4,4], [14,14]]
	actual = PokerRules.rank_hand("4c,4d,4h,Ad,Ac")

	assert actual == expected
	
def test_rank_hand_9c2cKcAc6c_returns_6_AK962():
	expected = PokerRules.CONST_FLUSH, [[14,13,9,6,2]]
	actual = PokerRules.rank_hand("9c,2c,Kc,Ac,6c")

	assert actual == expected
	
def test_rank_hand_9c8c7c6c5d_returns_5_98765():
	expected = PokerRules.CONST_STRAIGHT, [[9,8,7,6,5]]
	actual = PokerRules.rank_hand("9c,8c,7c,6c,5d")

	assert actual == expected
			
def test_rank_hand_4c4d4hAd2c_returns_4_444A2():
	expected = PokerRules.CONST_THREE_OF_A_KIND, [[4,4,4], [14,2]]
	actual = PokerRules.rank_hand("4c,4d,4h,Ad,2c")

	assert actual == expected

def test_rank_hand_4c4dAhAd2c_returns_3_44AA2():
	expected = PokerRules.CONST_TWO_PAIR, [[14,14],[4,4],[2]]
	actual = PokerRules.rank_hand("4c,4d,Ah,Ad,2c")

	assert actual == expected

def test_rank_hand_3c5dAhAd2c_returns_2_AA532():
	expected = PokerRules.CONST_PAIR, [[14,14],[5,3,2]]
	actual = PokerRules.rank_hand("3c,5d,Ah,Ad,2c")
	
	assert actual == expected

def test_rank_hand_Ac2c3c4c5c_returns_9_54321():
	expected = PokerRules.CONST_STRAIGHT_FLUSH, [[5,4,3,2,1]]
	actual = PokerRules.rank_hand("Ac,2c,3c,4c,5c")
	
	assert actual == expected
	
def test_get_best_hand_4c5d3h7sJcKdKc_returns_KdKcJc7s5d():
	actual = PokerRules.get_best_hand("4c,5d,3h,7s,Jc,Kd,Kc")
	expected = ['5d','7s','Jc','Kd','Kc']
	
	assert actual == expected

def test_get_best_hand_Ad2sAsJc8sJdTc5d_returns_AdAsJcJdTc():
	actual = PokerRules.get_best_hand("Ad,2s,As,Jc,8s,Jd,Tc,5d")
	expected = ['Ad','As','Jc','Jd','Tc']
	
	assert actual == expected
	
def test_get_best_hand_Ad2s3s4s5d8s9s_returns_2s3s4s8s9s():
	actual = PokerRules.get_best_hand("Ad,2s,3s,4s,5d,8s,9s")
	expected = ['2s','3s','4s','8s','9s']
	
	assert actual == expected