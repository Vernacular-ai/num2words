# -*- encoding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

import re

from .base import Num2Word_Base


class Num2Word_GU(Num2Word_Base):
    def setup(self):
        self.low_numwords = [
            "સો",
            "નવ્વાણું",
            "અઠ્ઠાણું",
            "સત્તાણું",
            "છન્નું",
            "પંચાણું",
            "ચોરાણું",
            "ત્રાણું",
            "બાણું",
            "એકાણું",
            "નેવું",
            "નેવ્યાસી",
            "ઈઠ્યાસી",
            "સિત્યાસી",
            "છ્યાસી",
            "પંચાસી",
            "ચોર્યાસી",
            "ત્યાસી",
            "બ્યાસી",
            "એક્યાસી",
            "એંસી",
            "ઓગણાએંસી",
            "ઇઠ્યોતેર",
            "સિત્યોતેર",
            "છોતેર",
            "પંચોતેર",
            "ચુમોતેર",
            "તોતેર",
            "બોતેર",
            "એકોતેર",
            "સિત્તેર",
            "અગણોસિત્તેર",
            "અડસઠ",
            "સડસઠ",
            "છાસઠ",
            "પાંસઠ",
            "ચોસઠ",
            "ત્રેસઠ",
            "બાસઠ",
            "એકસઠ",
            "સાઈઠ",
            "ઓગણસાઠ",
            "અઠ્ઠાવન",
            "સત્તાવન",
            "છપ્પન",
            "પંચાવન",
            "ચોપન",
            "ત્રેપન",
            "બાવન",
            "એકાવન",
            "પચાસ",
            "ઓગણપચાસ",
            "અડતાલીસ",
            "સુડતાલીસ",
            "છેતાલીસ",
            "પિસ્તાલીસ",
            "ચુંમાલીસ",
            "ત્રેતાલીસ",
            "બેતાલીસ",
            "એકતાલીસ",
            "ચાલીસ",
            "ઓગણચાલીસ",
            "અડત્રીસ",
            "સડત્રીસ",
            "છત્રીસ",
            "પાંત્રીસ",
            "ચોત્રીસ",
            "તેત્રીસ",
            "બત્રીસ",
            "એકત્રીસ",
            "ત્રીસ",
            "ઓગણત્રીસ",
            "અઠ્ઠાવીસ",
            "સત્તાવીસ",
            "છવીસ",
            "પચ્ચીસ",
            "ચોવીસ",
            "તેવીસ",
            "બાવીસ",
            "એકવીસ",
            "વીસ",
            "ઓગણિસ",
            "અઢાર",
            "સત્તર",
            "સોળ",
            "પંદર",
            "ચૌદ",
            "તેર",
            "બાર",
            "અગિયાર",
            "દસ",
            "નવ",
            "આઠ",
            "સાત",
            "છ",
            "પાંચ",
            "ચાર",
            "ત્રણ",
            "બે",
            "એક",
            "શૂન્ય"
        ]
        self.mid_numwords = [(10000000, "કરોડ઼"), (100000, "લાખ"), (1000, "હજાર")]
        self.high_numwords = []

    def set_high_numwords(self, high_numwords):
        pass

    def to_cardinal(self, value: int) -> str:
        if value == 100:
            # This is to cover more common way of saying 100
            return self.cards[value]
        else:
            return super().to_cardinal(value)

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        else:
            if lnum >= 100 > rnum:
                return ("%s %s" % (ltext, rtext), lnum + rnum)
            elif rnum > lnum:
                return ("%s %s" % (ltext, rtext), lnum * rnum)
            else:
                return ("%s %s" % (ltext, rtext), lnum + rnum)
