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
        # NOTE: There is a definite pattern that can be exploited here but
        #       we are going with hardcoded words til 100 for now.
        self.low_numwords = [
            "நூறு",
            "தொண்ணூற்றிஒன்பது",
            "தொண்ணூற்றியெட்டு",
            "தொண்ணூற்றியேழு",
            "தொண்ணூற்றியாறு",
            "தொண்ணூற்றிஐந்து",
            "தொண்ணூற்றிநான்கு",
            "தொண்ணூற்றிமூன்று",
            "தொண்ணூற்றிரண்டு",
            "தொண்ணூற்றியொன்று",
            "தொன்னூறு",
            "எண்பத்தியொன்பது",
            "எண்பத்தியெட்டு",
            "எண்பத்திஏழு",
            "எண்பத்திஆறு",
            "என்பதினைந்து",
            "என்பதினான்கு",
            "எண்பத்திமூன்று",
            "எண்பத்திரண்டு",
            "எண்பத்தியொன்று",
            "எண்பது",
            "எழுபத்தி ஒன்பது",
            "எழுபத்தி எட்டு",
            "எழுபத்தி ஏழு",
            "எழுபத்தி ஆறு",
            "எழுபத்தி ஐந்து",
            "எழுபத்தி நான்கு",
            "எழுபத்தி முச்சக்கர",
            "எழுபத்தி இரண்டு",
            "எழுபத்தி ஒன்று",
            "எழுபது",
            "அறுபத்து ஒன்பது",
            "அறுபத்து எட்டு",
            "அறுபத்து ஏழு",
            "அறுபத்து ஆறு",
            "அறுபத்து ஐந்து",
            "அறுபத்து நான்கு",
            "அறுபத்து மூன்று",
            "அறுபத்து இரண்டு",
            "அறுபத்து ஒன்று",
            "அறுபது",
            "ஐம்பத்து ஒன்பது",
            "ஐம்பத்து எட்டு",
            "ஐம்பத்து ஏழு",
            "ஐம்பத்து ஆறு",
            "ஐம்பத்து ஐந்து",
            "ஐம்பத்து நான்கு",
            "ஐம்பத்து மூன்று",
            "ஐம்பத்து இரண்டு",
            "ஐம்பத்து ஒன்று",
            "ஐம்பது",
            "நாற்பத்து ஒன்பது",
            "நாற்பத்து எட்டு",
            "நாற்பத்து ஏழு",
            "நாற்பத்து ஆறு",
            "நாற்பத்து ஐந்து",
            "நாற்பத்து நான்கு",
            "நாற்பத்து மூன்று",
            "நாற்பத்து இரண்டு",
            "நாற்பத்து ஒன்று",
            "நாற்பது",
            "முப்பத்து ஒன்பது",
            "முப்பத்து எட்டு",
            "முப்பத்து ஏழு",
            "முப்பத்து ஆறு",
            "முப்பத்து ஐந்து",
            "முப்பத்து நான்கு",
            "முப்பத்து மூன்று",
            "முப்பத்து இரண்டு",
            "முப்பத்து ஒன்று",
            "முப்பது",
            "இருபத்து ஒன்பது",
            "இருபத்து எட்டு",
            "இருபத்து ஏழு",
            "இருபத்து ஆறு",
            "இருபத்து ஐந்து",
            "இருபத்து நான்கு",
            "இருபத்து மூன்று",
            "இருபத்து இரண்டு",
            "இருபத்து ஒன்று",
            "இருபது",
            "பத்தொன்பது",
            "பதினெட்டு",
            "பதினேழு",
            "பதினாறு",
            "பதினைந்து",
            "பதினான்கு",
            "பதிமூன்று",
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
        self.mid_numwords = [(1000, "ஆயிரம்")]
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
