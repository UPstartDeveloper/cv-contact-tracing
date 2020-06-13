#!/usr/bin/env python3
import unittest

from touchtrail.scene import Object


class ObjectTestCase(unittest.TestCase):

    def test_init(self):
        obj = Object(0, 0, 0, 0)
        assert obj.left == 0
        assert obj.top == 0
        assert obj.height == 0
        assert obj.width == 0

        obj = Object(98, 5644356, 0, 347834)
        assert obj.left == 0
        assert obj.top == 347834
        assert obj.height == 5644356
        assert obj.width == 98

        obj = Object(.5644356, .347834, 0, .513)
        assert obj.left == 0
        assert obj.top == .513
        assert obj.height == .347834
        assert obj.width == .5644356

    def test_collision(self):
        #                                              __________________
        #                        ___________          |                  |
        #  _________            |           |         |    _____   G     |
        # |         |           |     C     |         |   |     |        |
        # |    A    |___________|__         |         |   |  F  |        |
        # |_________|              |________|         |   |_____|        |
        #         |                |                  |__________________|
        #         |       B        |
        #     ____|            ____|____       ___________
        #    |    |___________|         |     |          _|________
        #    |     |          |    D    |     |    H    |    I     |
        #    |  E  |          |_________|     |         |__________|
        #    |_____|                          |___________|
        ## Test perfectly overlapping object F – G
        F = Object(width=10, height=10, left=0, top=0)
        G = Object(width=10, height=10, left=0, top=0)
        assert F.is_touching(G)
        assert G.is_touching(F)

        ## Test top left corner overlap A – B
        A = Object(width=10, height=10, left=0, top=0)
        B = Object(width=10, height=10, left=9, top=8)
        assert A.is_touching(B)
        assert B.is_touching(A)

        ## Test top left corner overlap A – B
        A = Object(width=10, height=10, left=0, top=0)
        B = Object(width=10, height=10, left=9, top=8)
        assert A.is_touching(B)
        assert B.is_touching(A)

        ## Test top right corner overlap B – C
        C = Object(width=10, height=10, left=0, top=0)
        assert C.is_touching(B)
        assert B.is_touching(C)

        ## Test bottom left corner overlap E – B
        E = Object(width=10, height=10, left=0, top=17)
        assert E.is_touching(B)
        assert B.is_touching(E)

        ## Test bottom left corner E – B touch
        E = Object(width=10, height=10, left=0, top=18)
        assert E.is_touching(B)
        assert B.is_touching(E)

        ## Test bottom right corner overlap B – D
        D = Object(width=10, height=10, left=18, top=15)
        assert D.is_touching(B)
        assert B.is_touching(D)

        ## Test bottom right corner touch B – D
        D = Object(width=10, height=10, left=18, top=18)
        assert D.is_touching(B)
        assert B.is_touching(D)

        ## Test overlap on one side H – I
        H = Object(width=10, height=10, left=0, top=0)
        I = Object(width=10, height=7, left=9, top=1)
        assert H.is_touching(I)
        assert I.is_touching(H)
