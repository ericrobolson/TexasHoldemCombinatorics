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
	expected = '0'
	
	assert actual == expected
	
def test_hash_handlist_EmptyList_returns_0():
	actual = HandHasher.hash_handlist([])
	expected = '0'
	
	assert actual == expected
	
def test_hash_handlist_As_returns_111110():
	actual = HandHasher.hash_handlist(['As'])
	expected = '111110'
	
	assert actual == expected
	
def test_hash_handlist_Ac_returns_001110():
	actual = HandHasher.hash_handlist(['Ac'])
	expected = '001110'
	
	assert actual == expected
	
def test_hash_handlist_As2d_returns_1001110():
	actual = HandHasher.hash_handlist(['As', 'Ac'])
	expected = '111110001110'
	
	assert actual == expected	

	
def test_order_hand_Ad4sAcAs9s_returns_x():
	hand = HandHasher.split_hand("Ad,4s,Ac,As,9s")

	actual = HandHasher.hash_handlist(hand)
	expected = '111110011110001110111001011100'
	
	assert actual == expected