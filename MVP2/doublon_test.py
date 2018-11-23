from doublon import *


def test_suppression_espace_string():
    assert suppression_espace_string("   bonjour   ")=="bonjour   "

def test_doublon():
    assert doublon("test_mvp2.txt")==[["\n",5],["assert\n",2],["test\n",3]]


