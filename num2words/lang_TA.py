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

from .base import Num2Word_Base


class Num2Word_TA(Num2Word_Base):
    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10 ** n] = word

    def setup(self):
        self.low_numwords = [
            "பூஜ்ஜியம்",
            "ஒன்று",
            "இரண்டு",
            "மூன்று",
            "நான்கு",
            "ஐந்து",
            "ஆறு",
            "ஏழு",
            "எட்டு",
            "ஒன்பது",
            "பத்து",
            "பதினொன்று",
            "பன்னிரண்டு",
            "பதின்மூன்று",
            "பதினான்கு",
            "பதினைந்து",
            "பதினாறு",
            "பதினேழு",
            "பதினெட்டு",
            "பத்தொன்பது",
            "இருபது",
            "இருபத்தி ஒன்று",
            "இருபத்தி இரண்டு",
            "இருபத்தி மூன்று",
            "இருபத்தி நான்கு",
            "இருபத்தி ஐந்து",
            "இருபத்தி ஆறு",
            "இருபத்தி ஏழு",
            "இருபத்தி எட்டு",
            "இருபத்தி ஒன்பது",
            "முப்பது",
            "முப்பத்தி ஒன்று",
            "முப்பத்தி இரண்டு",
            "முப்பத்தி மூன்று",
            "முப்பத்தி நான்கு",
            "முப்பத்தி ஐந்து",
            "முப்பத்தி ஆறு",
            "முப்பத்தி ஏழு",
            "முப்பத்தி எட்டு",
            "முப்பத்தி ஒன்பது",
            "நாற்பது",
            "ஐம்பது",
            "அறுபது",
            "எழுபது",
            "எண்பது",
            "தொன்னூறு"
        ]

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)
