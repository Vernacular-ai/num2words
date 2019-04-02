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
    def setup(self):
        self.low_numwords = [
            "முப்பத்தி ஒன்பது",
            "முப்பத்தி எட்டு",
            "முப்பத்தி ஏழு",
            "முப்பத்தி ஆறு",
            "முப்பத்தி ஐந்து",
            "முப்பத்தி நான்கு",
            "முப்பத்தி மூன்று",
            "முப்பத்தி இரண்டு",
            "முப்பத்தி ஒன்று",
            "முப்பது",
            "இருபத்தி ஒன்பது",
            "இருபத்தி எட்டு",
            "இருபத்தி ஏழு",
            "இருபத்தி ஆறு",
            "இருபத்தி ஐந்து",
            "இருபத்தி நான்கு",
            "இருபத்தி மூன்று",
            "இருபத்தி இரண்டு",
            "இருபத்தி ஒன்று",
            "இருபது",
            "பத்தொன்பது",
            "பதினெட்டு",
            "பதினேழு",
            "பதினாறு",
            "பதினைந்து",
            "பதினான்கு",
            "பதின்மூன்று",
            "பன்னிரண்டு",
            "பதினொன்று",
            "பத்து",
            "ஒன்பது",
            "எட்டு",
            "ஏழு",
            "ஆறு",
            "ஐந்து",
            "நான்கு",
            "மூன்று",
            "இரண்டு",
            "ஒன்று",
            "பூஜ்ஜியம்"
        ]
        self.mid_numwords = [(1000, "ஆயிரம்"), (100, "நூறு"),
                             (90, "தொன்னூறு"), (80, "எண்பது"),
                             (70, "எழுபது"), (60, "அறுபது"),
                             (50, "ஐம்பது"), (40, "நாற்பது")]
        self.high_numwords = []

    def set_high_numwords(self, high_numwords):
        pass

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
