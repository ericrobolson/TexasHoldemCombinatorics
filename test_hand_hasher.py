import sys
import HandHasher

def test_order_hand_Ad4s5d8s9s_returns_Ad9s8s5d4s():
	actual = HandHasher.order_hand("Ad,4s,5d,8s,9s")
	expected = ['Ad','9s','8s','5d','4s']
	
	assert actual == expected
	
def test_order_hand_Ad4sAcAs9s_returns_AsAdAc9s4s():
	actual = HandHasher.order_hand("Ad,4s,Ac,As,9s")
	expected = ['As','Ad','Ac','9s','4s']
	
	assert actual == expected
	
def test_i_to_b_0_returns_0():
	actual = HandHasher.i_to_b(0)
	expected = '0'
	
	assert actual == expected
	
def test_i_to_b_none_returns_0():
	actual = HandHasher.i_to_b(None)
	expected = '0'
	
	assert actual == expected

def test_i_to_b_1_returns_1():
	actual = HandHasher.i_to_b(1)
	expected = '1'
	
	assert actual == expected
	
def test_i_to_b_4_returns_100():
	actual = HandHasher.i_to_b(4)
	expected = '100'
	
	assert actual == expected

def test_i_to_b_8_returns_1000():
	actual = HandHasher.i_to_b(8)
	expected = '1000'
	
	assert actual == expected	
	
def test_i_to_b_9_returns_1001():
	actual = HandHasher.i_to_b(9)
	expected = '1001'
	
	assert actual == expected	
	
def test_hash_handlist_None_returns_0():
	actual = HandHasher.hash_handlist(None)
	expected = 0
	
	assert actual == expected
	
def test_hash_handlist_EmptyList_returns_0():
	actual = HandHasher.hash_handlist([])
	expected = 0
	
	assert actual == expected
	
def test_hash_handlist_As_returns_62():
	actual = HandHasher.hash_handlist(['As'])
	expected = 62
	
	assert actual == expected
	
def test_hash_handlist_Ac_returns_14():
	actual = HandHasher.hash_handlist(['Ac'])
	expected = 14
	
	assert actual == expected
	
def test_hash_handlist_As2d_returns_3982():
	actual = HandHasher.hash_handlist(['As', 'Ac'])
	expected = 3982
	
	assert actual == expected	

	
def test_order_hand_Ad4sAcAs9s_returns_1048112732():
	hand = HandHasher.split_hand("Ad,4s,Ac,As,9s")

	actual = HandHasher.hash_handlist(hand)
	expected = 1048112732
	
	assert actual == expected
	
def test_order_hand_As9sAcAd4s_returns_1048112732():
	hand = HandHasher.split_hand("As,9s,Ac,Ad,4s")

	actual = HandHasher.hash_handlist(hand)
	expected = 1048112732
	
	assert actual == expected
	
	
def test_unhash_14_returns_Ac():
	input = 14
	expected = ['Ac']
	actual = HandHasher.unhash(input)
	
	assert actual == expected
	

def test_unhash_1048112732_returns_AsAdAc9s4s():
	input = 1048112732

	actual = HandHasher.unhash(input)
	expected = ['As', 'Ad', 'Ac', '9s', 'Qd']
	
	assert actual == expected
