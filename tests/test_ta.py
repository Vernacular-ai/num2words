# -*- coding: utf-8 -*-
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

from unittest import TestCase

from num2words import num2words

class Num2WordsTATest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(2, lang="ta"), "இரண்டு")
        self.assertEqual(num2words(7, lang="ta"), "ஏழு")
        self.assertEqual(num2words(8, lang="ta"), "எட்டு")
        self.assertEqual(num2words(20, lang="ta"), "இருபத்து")
        self.assertEqual(num2words(22, lang="ta"), "இருபத்திரண்டு")
        self.assertEqual(num2words(24, lang="ta"), "இருபத்தினாங்கு")
        self.assertEqual(num2words(50, lang="ta"), "அம்பது")
        self.assertEqual(num2words(60, lang="ta"), "அறுபது")
        self.assertEqual(num2words(70, lang="ta"), "எழுபத்து")
        self.assertEqual(num2words(80, lang="ta"), "எண்பது")
        self.assertEqual(num2words(82, lang="ta"), "எண்பத்திதரண்டு")
        self.assertEqual(num2words(200, lang="ta"), "இருநூறு")
        self.assertEqual(num2words(600, lang="ta"), "அறுநூறு")
        self.assertEqual(num2words(700, lang="ta"), "எழுநூறு")
        self.assertEqual(num2words(1000, lang="ta"), "ஆயிரம்")
        self.assertEqual(num2words(2000, lang="ta"), "இரண்டாயிரம்")
        self.assertEqual(num2words(6000, lang="ta"), "ஆறாயிரம்")
        self.assertEqual(num2words(7000, lang="ta"), "ஏழாயிரம்")
        self.assertEqual(num2words(8000, lang="ta"), "எட்டாயிரம்")
        self.assertEqual(num2words(100000, lang="ta"), "இலட்சம்")
