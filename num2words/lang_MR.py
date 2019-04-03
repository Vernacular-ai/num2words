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


class Num2Word_MR(Num2Word_Base):
    def setup(self):
        self.low_numwords = [
            "शंभर",
            "नव्व्याण्णव",
            "अठ्ठ्याण्णव",
            "सत्त्याण्णव",
            "शहाण्णव",
            "पंच्याण्णव",
            "चौऱ्याण्णव",
            "त्र्याण्णव",
            "ब्याण्णव",
            "एक्क्याण्णव",
            "नव्वद",
            "एकोणनव्वद",
            "अठ्ठ्याऐंशी",
            "सत्त्याऐंशी",
            "शहाऐंशी",
            "पंच्याऐंशी",
            "चौऱ्याऐंशी",
            "त्र्याऐंशी",
            "ब्याऐंशी",
            "एक्क्याऐंशी",
            "ऐंशी",
            "एकोण ऐंशी",
            "अठ्ठ्याहत्तर",
            "सत्याहत्तर",
            "शहात्तर",
            "पंच्याहत्तर",
            "चौर्‍याहत्तर",
            "त्र्याहत्तर",
            "बाहत्तर",
            "एक्काहत्तर",
            "सत्तर",
            "एकोणसत्तर",
            "अडुसष्ठ",
            "सदुसष्ठ",
            "सहासष्ठ",
            "पासष्ठ",
            "चौसष्ठ",
            "त्रेसष्ठ",
            "बासष्ठ",
            "एकसष्ठ",
            "साठ",
            "एकोणसाठ",
            "अठ्ठावन्न",
            "सत्तावन्न",
            "छप्पन्न",
            "पंचावन्न",
            "चोपन्न",
            "त्रेपन्न",
            "बावन्न",
            "एक्कावन्न",
            "पन्नास",
            "एकोणपन्नास",
            "अठ्ठेचाळीस",
            "सत्तेचाळीस",
            "सेहेचाळीस",
            "पंचेचाळीस",
            "चव्वेचाळीस",
            "त्रेचाळीस",
            "बेचाळीस",
            "एक्केचाळीस",
            "चाळीस",
            "एकोणचाळीस",
            "अडतीस",
            "सदतीस",
            "छत्तीस",
            "पस्तीस",
            "चौतीस",
            "तेहेतीस",
            "बत्तीस",
            "एकतीस",
            "तीस",
            "एकोणतीस",
            "अठ्ठावीस",
            "सत्तावीस",
            "सव्वीस",
            "पंचवीस",
            "चोवीस",
            "तेवीस",
            "बावीस",
            "एकवीस",
            "वीस",
            "एकोणीस",
            "अठरा",
            "सतरा",
            "सोळा",
            "पंधरा",
            "चौदा",
            "तेरा",
            "बारा",
            "अकरा",
            "दहा",
            "नऊ",
            "आठ",
            "सात",
            "सहा",
            "पाच",
            "चार",
            "तीन",
            "दोन",
            "एक",
            "शून्य"
        ]
        self.mid_numwords = [(10000000, "कोटी"), (100000, "लाख"), (1000, "हजार")]
        self.high_numwords = []

    def set_high_numwords(self, high_numwords):
        pass

    def to_cardinal(self, value: int) -> str:
        basic_cardinal = super().to_cardinal(value)
        # We are doing this again instead of being smart in merge fn because we
        # don't want to spoil the cards
        return re.sub("^शे", "शंभर", basic_cardinal, flags=re.U)

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        else:
            # Non ending 100 is different
            ltext = re.sub("शंभर$", "शे", ltext, flags=re.U)
            if lnum >= 100 > rnum:
                return ("%s %s" % (ltext, rtext), lnum + rnum)
            elif rnum > lnum:
                return ("%s %s" % (ltext, rtext), lnum * rnum)
            else:
                return ("%s %s" % (ltext, rtext), lnum + rnum)
