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


class Num2Word_TE(Num2Word_Base):
    def __init__(self):
        super().__init__()
        # HACK: To be safe, we are clipping at 999, will be
        #       adding proper rules for higher numbers
        self.errmsg_notinrange = "abs(%s) must be less than %s or between %s and %s."

    def setup(self):
        self.corpus = [
            "సున్న",
            "ఒకటి",
            "రెండు",
            "మూడు",
            "నాలుగు",
            "ఐదు",
            "ఆరు",
            "ఏడు",
            "ఎనిమిది",
            "తొమ్మిది",
            "పది",
            "పదకొండు",
            "పన్నెండు",
            "పదమూడు",
            "పద్నాలుగు",
            "పదహైదు",
            "పదహారు",
            "పదిహేడు",
            "పద్దెనిమిది",
            "పందొమ్మిది",
            "ఇరవై",
            "ఇరవై ఒకటి",
            "ఇరవై రెండు",
            "ఇరవై మూడు",
            "ఇరవై నాలుగు",
            "ఇరవై అయిదు",
            "ఇరవై ఆరు",
            "ఇరవై ఏడు",
            "ఇరవై ఎనిమిది",
            "ఇరవై తొమ్మిది",
            "ముప్పై",
            "ముప్పై ఒకటి",
            "ముప్పై రెండు",
            "ముప్పై మూడు",
            "ముప్పై నాలుగు",
            "ముప్పై ఐదు",
            "ముప్పై ఆరు",
            "ముప్పై ఏడు",
            "ముప్పై ఎనిమిది",
            "ముప్పై తొమ్మిది",
            "నలభై",
            "నలభై ఒకటి",
            "నలభై రెండు",
            "నలభై మూడు",
            "నలభై నాలుగు",
            "నలభై ఐదు",
            "నలభై ఆరు",
            "నలభై ఏడు",
            "నలభై ఎనిమిది",
            "నలభై తొమ్మిది",
            "యాభై",
            "యాభై ఒకటి",
            "యాభై రెండు",
            "యాభై మూడు",
            "యాభై నాలుగు",
            "యాభై ఐదు",
            "యాభై ఆరు",
            "యాభై ఏడు",
            "యాభై ఎనిమిది",
            "యాభై తొమ్మిది",
            "అరవై",
            "అరవై ఒకటి",
            "అరవై రెండు",
            "అరవై మూడు",
            "అరవై నాలుగు",
            "అరవై ఐదు",
            "అరవై ఆరు",
            "అరవై ఏడు",
            "అరవై ఎనిమిది",
            "అరవై తొమ్మిది",
            "డెబ్బై",
            "డెబ్బై ఒకటి",
            "డెబ్బై రెండు",
            "డెబ్బై మూడు",
            "డెబ్బై నాలుగు",
            "డెబ్బై ఐదు",
            "డెబ్బై ఆరు",
            "డెబ్బై ఏడు",
            "డెబ్బై ఎనిమిది",
            "డెబ్బై తొమ్మిది",
            "ఎనభై",
            "ఎనభై ఒకటి",
            "ఎనభై రెండు",
            "ఎనభై మూడు",
            "ఎనభై నాలుగు",
            "ఎనభై ఐదు",
            "ఎనభై ఆరు",
            "ఎనభై ఏడు",
            "ఎనభై ఎనిమిది",
            "ఎనభై తొమ్మిది",
            "తొంభై",
            "తొంభై ఒకటి",
            "తొంభై రెండు",
            "తొంభై మూడు",
            "తొంభై నాలుగు",
            "తొంభై ఐదు",
            "తొంభై ఆరు",
            "తొంభై ఏడు",
            "తొంభై ఎనిమిది",
            "తొంభై తొమ్మిది",
            "వంద",
            "నూట ఒకటి",
            "నూట రెండు",
            "నూట మూడు",
            "నూట నాలుగు",
            "నూట ఐదు",
            "నూట ఆరు",
            "నూట ఏడు",
            "నూట ఎనిమిది",
            "నూట తొమ్మిది",
            "నూట పది",
            "నూట పదకొండు",
            "నూట పన్నెండు",
            "నూట పదమూడు",
            "నూట పద్నాలుగు",
            "నూట పదహైదు",
            "నూట పదహారు",
            "నూట పదిహేడు",
            "నూట పద్దెనిమిది",
            "నూట పందొమ్మిది",
            "నూట ఇరవై",
            "నూట ఇరవై ఒకటి",
            "నూట ఇరవై రెండు",
            "నూట ఇరవై మూడు",
            "నూట ఇరవై నాలుగు",
            "నూట ఇరవై అయిదు",
            "నూట ఇరవై ఆరు",
            "నూట ఇరవై ఏడు",
            "నూట ఇరవై ఎనిమిది",
            "నూట ఇరవై తొమ్మిది",
            "నూట ముప్పై",
            "నూట ముప్పై ఒకటి",
            "నూట ముప్పై రెండు",
            "నూట ముప్పై మూడు",
            "నూట ముప్పై నాలుగు",
            "నూట ముప్పై ఐదు",
            "నూట ముప్పై ఆరు",
            "నూట ముప్పై ఏడు",
            "నూట ముప్పై ఎనిమిది",
            "నూట ముప్పై తొమ్మిది",
            "నూట నలభై",
            "నూట నలభై ఒకటి",
            "నూట నలభై రెండు",
            "నూట నలభై మూడు",
            "నూట నలభై నాలుగు",
            "నూట నలభై ఐదు",
            "నూట నలభై ఆరు",
            "నూట నలభై ఏడు",
            "నూట నలభై ఎనిమిది",
            "నూట నలభై తొమ్మిది",
            "నూట యాభై",
            "నూట యాభై ఒకటి",
            "నూట యాభై రెండు",
            "నూట యాభై మూడు",
            "నూట యాభై నాలుగు",
            "నూట యాభై ఐదు",
            "నూట యాభై ఆరు",
            "నూట యాభై ఏడు",
            "నూట యాభై ఎనిమిది",
            "నూట యాభై తొమ్మిది",
            "నూట అరవై",
            "నూట అరవై ఒకటి",
            "నూట అరవై రెండు",
            "నూట అరవై మూడు",
            "నూట అరవై నాలుగు",
            "నూట అరవై ఐదు",
            "నూట అరవై ఆరు",
            "నూట అరవై ఏడు",
            "నూట అరవై ఎనిమిది",
            "నూట అరవై తొమ్మిది",
            "నూట డెబ్బై",
            "నూట డెబ్బై ఒకటి",
            "నూట డెబ్బై రెండు",
            "నూట డెబ్బై మూడు",
            "నూట డెబ్బై నాలుగు",
            "నూట డెబ్బై ఐదు",
            "నూట డెబ్బై ఆరు",
            "నూట డెబ్బై ఏడు",
            "నూట డెబ్బై ఎనిమిది",
            "నూట డెబ్బై తొమ్మిది",
            "నూట ఎనభై",
            "నూట ఎనభై ఒకటి",
            "నూట ఎనభై రెండు",
            "నూట ఎనభై మూడు",
            "నూట ఎనభై నాలుగు",
            "నూట ఎనభై ఐదు",
            "నూట ఎనభై ఆరు",
            "నూట ఎనభై ఏడు",
            "నూట ఎనభై ఎనిమిది",
            "నూట ఎనభై తొమ్మిది",
            "నూట తొంభై",
            "నూట తొంభై ఒకటి",
            "నూట తొంభై రెండు",
            "నూట తొంభై మూడు",
            "నూట తొంభై నాలుగు",
            "నూట తొంభై ఐదు",
            "నూట తొంభై ఆరు",
            "నూట తొంభై ఏడు",
            "నూట తొంభై ఎనిమిది",
            "నూట తొంభై తొమ్మిది",
            "రెండు వందలు",
            "రెండు వందల ఒకటి",
            "రెండు వందల రెండు",
            "రెండు వందల మూడు",
            "రెండు వందల నాలుగు",
            "రెండు వందల ఐదు",
            "రెండు వందల ఆరు",
            "రెండు వందల ఏడు",
            "రెండు వందల ఎనిమిది",
            "రెండు వందల తొమ్మిది",
            "రెండు వందల పది",
            "రెండు వందల పదకొండు",
            "రెండు వందల పన్నెండు",
            "రెండు వందల పదమూడు",
            "రెండు వందల పద్నాలుగు",
            "రెండు వందల పదహైదు",
            "రెండు వందల పదహారు",
            "రెండు వందల పదిహేడు",
            "రెండు వందల పద్దెనిమిది",
            "రెండు వందల పందొమ్మిది",
            "రెండు వందల ఇరవై",
            "రెండు వందల ఇరవై ఒకటి",
            "రెండు వందల ఇరవై రెండు",
            "రెండు వందల ఇరవై మూడు",
            "రెండు వందల ఇరవై నాలుగు",
            "రెండు వందల ఇరవై అయిదు",
            "రెండు వందల ఇరవై ఆరు",
            "రెండు వందల ఇరవై ఏడు",
            "రెండు వందల ఇరవై ఎనిమిది",
            "రెండు వందల ఇరవై తొమ్మిది",
            "రెండు వందల ముప్పై",
            "రెండు వందల ముప్పై ఒకటి",
            "రెండు వందల ముప్పై రెండు",
            "రెండు వందల ముప్పై మూడు",
            "రెండు వందల ముప్పై నాలుగు",
            "రెండు వందల ముప్పై ఐదు",
            "రెండు వందల ముప్పై ఆరు",
            "రెండు వందల ముప్పై ఏడు",
            "రెండు వందల ముప్పై ఎనిమిది",
            "రెండు వందల ముప్పై తొమ్మిది",
            "రెండు వందల నలభై",
            "రెండు వందల నలభై ఒకటి",
            "రెండు వందల నలభై రెండు",
            "రెండు వందల నలభై మూడు",
            "రెండు వందల నలభై నాలుగు",
            "రెండు వందల నలభై ఐదు",
            "రెండు వందల నలభై ఆరు",
            "రెండు వందల నలభై ఏడు",
            "రెండు వందల నలభై ఎనిమిది",
            "రెండు వందల నలభై తొమ్మిది",
            "రెండు వందల యాభై",
            "రెండు వందల యాభై ఒకటి",
            "రెండు వందల యాభై రెండు",
            "రెండు వందల యాభై మూడు",
            "రెండు వందల యాభై నాలుగు",
            "రెండు వందల యాభై ఐదు",
            "రెండు వందల యాభై ఆరు",
            "రెండు వందల యాభై ఏడు",
            "రెండు వందల యాభై ఎనిమిది",
            "రెండు వందల యాభై తొమ్మిది",
            "రెండు వందల అరవై",
            "రెండు వందల అరవై ఒకటి",
            "రెండు వందల అరవై రెండు",
            "రెండు వందల అరవై మూడు",
            "రెండు వందల అరవై నాలుగు",
            "రెండు వందల అరవై ఐదు",
            "రెండు వందల అరవై ఆరు",
            "రెండు వందల అరవై ఏడు",
            "రెండు వందల అరవై ఎనిమిది",
            "రెండు వందల అరవై తొమ్మిది",
            "రెండు వందల డెబ్బై",
            "రెండు వందల డెబ్బై ఒకటి",
            "రెండు వందల డెబ్బై రెండు",
            "రెండు వందల డెబ్బై మూడు",
            "రెండు వందల డెబ్బై నాలుగు",
            "రెండు వందల డెబ్బై ఐదు",
            "రెండు వందల డెబ్బై ఆరు",
            "రెండు వందల డెబ్బై ఏడు",
            "రెండు వందల డెబ్బై ఎనిమిది",
            "రెండు వందల డెబ్బై తొమ్మిది",
            "రెండు వందల ఎనభై",
            "రెండు వందల ఎనభై ఒకటి",
            "రెండు వందల ఎనభై రెండు",
            "రెండు వందల ఎనభై మూడు",
            "రెండు వందల ఎనభై నాలుగు",
            "రెండు వందల ఎనభై ఐదు",
            "రెండు వందల ఎనభై ఆరు",
            "రెండు వందల ఎనభై ఏడు",
            "రెండు వందల ఎనభై ఎనిమిది",
            "రెండు వందల ఎనభై తొమ్మిది",
            "రెండు వందల తొంభై",
            "రెండు వందల తొంభై ఒకటి",
            "రెండు వందల తొంభై రెండు",
            "రెండు వందల తొంభై మూడు",
            "రెండు వందల తొంభై నాలుగు",
            "రెండు వందల తొంభై ఐదు",
            "రెండు వందల తొంభై ఆరు",
            "రెండు వందల తొంభై ఏడు",
            "రెండు వందల తొంభై ఎనిమిది",
            "రెండు వందల తొంభై తొమ్మిది",
            "మూడు వందలు",
            "మూడు వందల ఒకటి",
            "మూడు వందల రెండు",
            "మూడు వందల మూడు",
            "మూడు వందల నాలుగు",
            "మూడు వందల ఐదు",
            "మూడు వందల ఆరు",
            "మూడు వందల ఏడు",
            "మూడు వందల ఎనిమిది",
            "మూడు వందల తొమ్మిది",
            "మూడు వందల పది",
            "మూడు వందల పదకొండు",
            "మూడు వందల పన్నెండు",
            "మూడు వందల పదమూడు",
            "మూడు వందల పద్నాలుగు",
            "మూడు వందల పదహైదు",
            "మూడు వందల పదహారు",
            "మూడు వందల పదిహేడు",
            "మూడు వందల పద్దెనిమిది",
            "మూడు వందల పందొమ్మిది",
            "మూడు వందల ఇరవై",
            "మూడు వందల ఇరవై ఒకటి",
            "మూడు వందల ఇరవై రెండు",
            "మూడు వందల ఇరవై మూడు",
            "మూడు వందల ఇరవై నాలుగు",
            "మూడు వందల ఇరవై అయిదు",
            "మూడు వందల ఇరవై ఆరు",
            "మూడు వందల ఇరవై ఏడు",
            "మూడు వందల ఇరవై ఎనిమిది",
            "మూడు వందల ఇరవై తొమ్మిది",
            "మూడు వందల ముప్పై",
            "మూడు వందల ముప్పై ఒకటి",
            "మూడు వందల ముప్పై రెండు",
            "మూడు వందల ముప్పై మూడు",
            "మూడు వందల ముప్పై నాలుగు",
            "మూడు వందల ముప్పై ఐదు",
            "మూడు వందల ముప్పై ఆరు",
            "మూడు వందల ముప్పై ఏడు",
            "మూడు వందల ముప్పై ఎనిమిది",
            "మూడు వందల ముప్పై తొమ్మిది",
            "మూడు వందల నలభై",
            "మూడు వందల నలభై ఒకటి",
            "మూడు వందల నలభై రెండు",
            "మూడు వందల నలభై మూడు",
            "మూడు వందల నలభై నాలుగు",
            "మూడు వందల నలభై ఐదు",
            "మూడు వందల నలభై ఆరు",
            "మూడు వందల నలభై ఏడు",
            "మూడు వందల నలభై ఎనిమిది",
            "మూడు వందల నలభై తొమ్మిది",
            "మూడు వందల యాభై",
            "మూడు వందల యాభై ఒకటి",
            "మూడు వందల యాభై రెండు",
            "మూడు వందల యాభై మూడు",
            "మూడు వందల యాభై నాలుగు",
            "మూడు వందల యాభై ఐదు",
            "మూడు వందల యాభై ఆరు",
            "మూడు వందల యాభై ఏడు",
            "మూడు వందల యాభై ఎనిమిది",
            "మూడు వందల యాభై తొమ్మిది",
            "మూడు వందల అరవై",
            "మూడు వందల అరవై ఒకటి",
            "మూడు వందల అరవై రెండు",
            "మూడు వందల అరవై మూడు",
            "మూడు వందల అరవై నాలుగు",
            "మూడు వందల అరవై ఐదు",
            "మూడు వందల అరవై ఆరు",
            "మూడు వందల అరవై ఏడు",
            "మూడు వందల అరవై ఎనిమిది",
            "మూడు వందల అరవై తొమ్మిది",
            "మూడు వందల డెబ్బై",
            "మూడు వందల డెబ్బై ఒకటి",
            "మూడు వందల డెబ్బై రెండు",
            "మూడు వందల డెబ్బై మూడు",
            "మూడు వందల డెబ్బై నాలుగు",
            "మూడు వందల డెబ్బై ఐదు",
            "మూడు వందల డెబ్బై ఆరు",
            "మూడు వందల డెబ్బై ఏడు",
            "మూడు వందల డెబ్బై ఎనిమిది",
            "మూడు వందల డెబ్బై తొమ్మిది",
            "మూడు వందల ఎనభై",
            "మూడు వందల ఎనభై ఒకటి",
            "మూడు వందల ఎనభై రెండు",
            "మూడు వందల ఎనభై మూడు",
            "మూడు వందల ఎనభై నాలుగు",
            "మూడు వందల ఎనభై ఐదు",
            "మూడు వందల ఎనభై ఆరు",
            "మూడు వందల ఎనభై ఏడు",
            "మూడు వందల ఎనభై ఎనిమిది",
            "మూడు వందల ఎనభై తొమ్మిది",
            "మూడు వందల తొంభై",
            "మూడు వందల తొంభై ఒకటి",
            "మూడు వందల తొంభై రెండు",
            "మూడు వందల తొంభై మూడు",
            "మూడు వందల తొంభై నాలుగు",
            "మూడు వందల తొంభై ఐదు",
            "మూడు వందల తొంభై ఆరు",
            "మూడు వందల తొంభై ఏడు",
            "మూడు వందల తొంభై ఎనిమిది",
            "మూడు వందల తొంభై తొమ్మిది",
            "నాలుగు వందలు",
            "నాలుగు వందల ఒకటి",
            "నాలుగు వందల రెండు",
            "నాలుగు వందల మూడు",
            "నాలుగు వందల నాలుగు",
            "నాలుగు వందల ఐదు",
            "నాలుగు వందల ఆరు",
            "నాలుగు వందల ఏడు",
            "నాలుగు వందల ఎనిమిది",
            "నాలుగు వందల తొమ్మిది",
            "నాలుగు వందల పది",
            "నాలుగు వందల పదకొండు",
            "నాలుగు వందల పన్నెండు",
            "నాలుగు వందల పదమూడు",
            "నాలుగు వందల పద్నాలుగు",
            "నాలుగు వందల పదహైదు",
            "నాలుగు వందల పదహారు",
            "నాలుగు వందల పదిహేడు",
            "నాలుగు వందల పద్దెనిమిది",
            "నాలుగు వందల పందొమ్మిది",
            "నాలుగు వందల ఇరవై",
            "నాలుగు వందల ఇరవై ఒకటి",
            "నాలుగు వందల ఇరవై రెండు",
            "నాలుగు వందల ఇరవై మూడు",
            "నాలుగు వందల ఇరవై నాలుగు",
            "నాలుగు వందల ఇరవై అయిదు",
            "నాలుగు వందల ఇరవై ఆరు",
            "నాలుగు వందల ఇరవై ఏడు",
            "నాలుగు వందల ఇరవై ఎనిమిది",
            "నాలుగు వందల ఇరవై తొమ్మిది",
            "నాలుగు వందల ముప్పై",
            "నాలుగు వందల ముప్పై ఒకటి",
            "నాలుగు వందల ముప్పై రెండు",
            "నాలుగు వందల ముప్పై మూడు",
            "నాలుగు వందల ముప్పై నాలుగు",
            "నాలుగు వందల ముప్పై ఐదు",
            "నాలుగు వందల ముప్పై ఆరు",
            "నాలుగు వందల ముప్పై ఏడు",
            "నాలుగు వందల ముప్పై ఎనిమిది",
            "నాలుగు వందల ముప్పై తొమ్మిది",
            "నాలుగు వందల నలభై",
            "నాలుగు వందల నలభై ఒకటి",
            "నాలుగు వందల నలభై రెండు",
            "నాలుగు వందల నలభై మూడు",
            "నాలుగు వందల నలభై నాలుగు",
            "నాలుగు వందల నలభై ఐదు",
            "నాలుగు వందల నలభై ఆరు",
            "నాలుగు వందల నలభై ఏడు",
            "నాలుగు వందల నలభై ఎనిమిది",
            "నాలుగు వందల నలభై తొమ్మిది",
            "నాలుగు వందల యాభై",
            "నాలుగు వందల యాభై ఒకటి",
            "నాలుగు వందల యాభై రెండు",
            "నాలుగు వందల యాభై మూడు",
            "నాలుగు వందల యాభై నాలుగు",
            "నాలుగు వందల యాభై ఐదు",
            "నాలుగు వందల యాభై ఆరు",
            "నాలుగు వందల యాభై ఏడు",
            "నాలుగు వందల యాభై ఎనిమిది",
            "నాలుగు వందల యాభై తొమ్మిది",
            "నాలుగు వందల అరవై",
            "నాలుగు వందల అరవై ఒకటి",
            "నాలుగు వందల అరవై రెండు",
            "నాలుగు వందల అరవై మూడు",
            "నాలుగు వందల అరవై నాలుగు",
            "నాలుగు వందల అరవై ఐదు",
            "నాలుగు వందల అరవై ఆరు",
            "నాలుగు వందల అరవై ఏడు",
            "నాలుగు వందల అరవై ఎనిమిది",
            "నాలుగు వందల అరవై తొమ్మిది",
            "నాలుగు వందల డెబ్బై",
            "నాలుగు వందల డెబ్బై ఒకటి",
            "నాలుగు వందల డెబ్బై రెండు",
            "నాలుగు వందల డెబ్బై మూడు",
            "నాలుగు వందల డెబ్బై నాలుగు",
            "నాలుగు వందల డెబ్బై ఐదు",
            "నాలుగు వందల డెబ్బై ఆరు",
            "నాలుగు వందల డెబ్బై ఏడు",
            "నాలుగు వందల డెబ్బై ఎనిమిది",
            "నాలుగు వందల డెబ్బై తొమ్మిది",
            "నాలుగు వందల ఎనభై",
            "నాలుగు వందల ఎనభై ఒకటి",
            "నాలుగు వందల ఎనభై రెండు",
            "నాలుగు వందల ఎనభై మూడు",
            "నాలుగు వందల ఎనభై నాలుగు",
            "నాలుగు వందల ఎనభై ఐదు",
            "నాలుగు వందల ఎనభై ఆరు",
            "నాలుగు వందల ఎనభై ఏడు",
            "నాలుగు వందల ఎనభై ఎనిమిది",
            "నాలుగు వందల ఎనభై తొమ్మిది",
            "నాలుగు వందల తొంభై",
            "నాలుగు వందల తొంభై ఒకటి",
            "నాలుగు వందల తొంభై రెండు",
            "నాలుగు వందల తొంభై మూడు",
            "నాలుగు వందల తొంభై నాలుగు",
            "నాలుగు వందల తొంభై ఐదు",
            "నాలుగు వందల తొంభై ఆరు",
            "నాలుగు వందల తొంభై ఏడు",
            "నాలుగు వందల తొంభై ఎనిమిది",
            "నాలుగు వందల తొంభై తొమ్మిది",
            "ఐదు వందలు",
            "ఐదు వందల ఒకటి",
            "ఐదు వందల రెండు",
            "ఐదు వందల మూడు",
            "ఐదు వందల నాలుగు",
            "ఐదు వందల ఐదు",
            "ఐదు వందల ఆరు",
            "ఐదు వందల ఏడు",
            "ఐదు వందల ఎనిమిది",
            "ఐదు వందల తొమ్మిది",
            "ఐదు వందల పది",
            "ఐదు వందల పదకొండు",
            "ఐదు వందల పన్నెండు",
            "ఐదు వందల పదమూడు",
            "ఐదు వందల పద్నాలుగు",
            "ఐదు వందల పదహైదు",
            "ఐదు వందల పదహారు",
            "ఐదు వందల పదిహేడు",
            "ఐదు వందల పద్దెనిమిది",
            "ఐదు వందల పందొమ్మిది",
            "ఐదు వందల ఇరవై",
            "ఐదు వందల ఇరవై ఒకటి",
            "ఐదు వందల ఇరవై రెండు",
            "ఐదు వందల ఇరవై మూడు",
            "ఐదు వందల ఇరవై నాలుగు",
            "ఐదు వందల ఇరవై అయిదు",
            "ఐదు వందల ఇరవై ఆరు",
            "ఐదు వందల ఇరవై ఏడు",
            "ఐదు వందల ఇరవై ఎనిమిది",
            "ఐదు వందల ఇరవై తొమ్మిది",
            "ఐదు వందల ముప్పై",
            "ఐదు వందల ముప్పై ఒకటి",
            "ఐదు వందల ముప్పై రెండు",
            "ఐదు వందల ముప్పై మూడు",
            "ఐదు వందల ముప్పై నాలుగు",
            "ఐదు వందల ముప్పై ఐదు",
            "ఐదు వందల ముప్పై ఆరు",
            "ఐదు వందల ముప్పై ఏడు",
            "ఐదు వందల ముప్పై ఎనిమిది",
            "ఐదు వందల ముప్పై తొమ్మిది",
            "ఐదు వందల నలభై",
            "ఐదు వందల నలభై ఒకటి",
            "ఐదు వందల నలభై రెండు",
            "ఐదు వందల నలభై మూడు",
            "ఐదు వందల నలభై నాలుగు",
            "ఐదు వందల నలభై ఐదు",
            "ఐదు వందల నలభై ఆరు",
            "ఐదు వందల నలభై ఏడు",
            "ఐదు వందల నలభై ఎనిమిది",
            "ఐదు వందల నలభై తొమ్మిది",
            "ఐదు వందల యాభై",
            "ఐదు వందల యాభై ఒకటి",
            "ఐదు వందల యాభై రెండు",
            "ఐదు వందల యాభై మూడు",
            "ఐదు వందల యాభై నాలుగు",
            "ఐదు వందల యాభై ఐదు",
            "ఐదు వందల యాభై ఆరు",
            "ఐదు వందల యాభై ఏడు",
            "ఐదు వందల యాభై ఎనిమిది",
            "ఐదు వందల యాభై తొమ్మిది",
            "ఐదు వందల అరవై",
            "ఐదు వందల అరవై ఒకటి",
            "ఐదు వందల అరవై రెండు",
            "ఐదు వందల అరవై మూడు",
            "ఐదు వందల అరవై నాలుగు",
            "ఐదు వందల అరవై ఐదు",
            "ఐదు వందల అరవై ఆరు",
            "ఐదు వందల అరవై ఏడు",
            "ఐదు వందల అరవై ఎనిమిది",
            "ఐదు వందల అరవై తొమ్మిది",
            "ఐదు వందల డెబ్బై",
            "ఐదు వందల డెబ్బై ఒకటి",
            "ఐదు వందల డెబ్బై రెండు",
            "ఐదు వందల డెబ్బై మూడు",
            "ఐదు వందల డెబ్బై నాలుగు",
            "ఐదు వందల డెబ్బై ఐదు",
            "ఐదు వందల డెబ్బై ఆరు",
            "ఐదు వందల డెబ్బై ఏడు",
            "ఐదు వందల డెబ్బై ఎనిమిది",
            "ఐదు వందల డెబ్బై తొమ్మిది",
            "ఐదు వందల ఎనభై",
            "ఐదు వందల ఎనభై ఒకటి",
            "ఐదు వందల ఎనభై రెండు",
            "ఐదు వందల ఎనభై మూడు",
            "ఐదు వందల ఎనభై నాలుగు",
            "ఐదు వందల ఎనభై ఐదు",
            "ఐదు వందల ఎనభై ఆరు",
            "ఐదు వందల ఎనభై ఏడు",
            "ఐదు వందల ఎనభై ఎనిమిది",
            "ఐదు వందల ఎనభై తొమ్మిది",
            "ఐదు వందల తొంభై",
            "ఐదు వందల తొంభై ఒకటి",
            "ఐదు వందల తొంభై రెండు",
            "ఐదు వందల తొంభై మూడు",
            "ఐదు వందల తొంభై నాలుగు",
            "ఐదు వందల తొంభై ఐదు",
            "ఐదు వందల తొంభై ఆరు",
            "ఐదు వందల తొంభై ఏడు",
            "ఐదు వందల తొంభై ఎనిమిది",
            "ఐదు వందల తొంభై తొమ్మిది",
            "ఆరు వందలు",
            "ఆరు వందల ఒకటి",
            "ఆరు వందల రెండు",
            "ఆరు వందల మూడు",
            "ఆరు వందల నాలుగు",
            "ఆరు వందల ఐదు",
            "ఆరు వందల ఆరు",
            "ఆరు వందల ఏడు",
            "ఆరు వందల ఎనిమిది",
            "ఆరు వందల తొమ్మిది",
            "ఆరు వందల పది",
            "ఆరు వందల పదకొండు",
            "ఆరు వందల పన్నెండు",
            "ఆరు వందల పదమూడు",
            "ఆరు వందల పద్నాలుగు",
            "ఆరు వందల పదహైదు",
            "ఆరు వందల పదహారు",
            "ఆరు వందల పదిహేడు",
            "ఆరు వందల పద్దెనిమిది",
            "ఆరు వందల పందొమ్మిది",
            "ఆరు వందల ఇరవై",
            "ఆరు వందల ఇరవై ఒకటి",
            "ఆరు వందల ఇరవై రెండు",
            "ఆరు వందల ఇరవై మూడు",
            "ఆరు వందల ఇరవై నాలుగు",
            "ఆరు వందల ఇరవై అయిదు",
            "ఆరు వందల ఇరవై ఆరు",
            "ఆరు వందల ఇరవై ఏడు",
            "ఆరు వందల ఇరవై ఎనిమిది",
            "ఆరు వందల ఇరవై తొమ్మిది",
            "ఆరు వందల ముప్పై",
            "ఆరు వందల ముప్పై ఒకటి",
            "ఆరు వందల ముప్పై రెండు",
            "ఆరు వందల ముప్పై మూడు",
            "ఆరు వందల ముప్పై నాలుగు",
            "ఆరు వందల ముప్పై ఐదు",
            "ఆరు వందల ముప్పై ఆరు",
            "ఆరు వందల ముప్పై ఏడు",
            "ఆరు వందల ముప్పై ఎనిమిది",
            "ఆరు వందల ముప్పై తొమ్మిది",
            "ఆరు వందల నలభై",
            "ఆరు వందల నలభై ఒకటి",
            "ఆరు వందల నలభై రెండు",
            "ఆరు వందల నలభై మూడు",
            "ఆరు వందల నలభై నాలుగు",
            "ఆరు వందల నలభై ఐదు",
            "ఆరు వందల నలభై ఆరు",
            "ఆరు వందల నలభై ఏడు",
            "ఆరు వందల నలభై ఎనిమిది",
            "ఆరు వందల నలభై తొమ్మిది",
            "ఆరు వందల యాభై",
            "ఆరు వందల యాభై ఒకటి",
            "ఆరు వందల యాభై రెండు",
            "ఆరు వందల యాభై మూడు",
            "ఆరు వందల యాభై నాలుగు",
            "ఆరు వందల యాభై ఐదు",
            "ఆరు వందల యాభై ఆరు",
            "ఆరు వందల యాభై ఏడు",
            "ఆరు వందల యాభై ఎనిమిది",
            "ఆరు వందల యాభై తొమ్మిది",
            "ఆరు వందల అరవై",
            "ఆరు వందల అరవై ఒకటి",
            "ఆరు వందల అరవై రెండు",
            "ఆరు వందల అరవై మూడు",
            "ఆరు వందల అరవై నాలుగు",
            "ఆరు వందల అరవై ఐదు",
            "ఆరు వందల అరవై ఆరు",
            "ఆరు వందల అరవై ఏడు",
            "ఆరు వందల అరవై ఎనిమిది",
            "ఆరు వందల అరవై తొమ్మిది",
            "ఆరు వందల డెబ్బై",
            "ఆరు వందల డెబ్బై ఒకటి",
            "ఆరు వందల డెబ్బై రెండు",
            "ఆరు వందల డెబ్బై మూడు",
            "ఆరు వందల డెబ్బై నాలుగు",
            "ఆరు వందల డెబ్బై ఐదు",
            "ఆరు వందల డెబ్బై ఆరు",
            "ఆరు వందల డెబ్బై ఏడు",
            "ఆరు వందల డెబ్బై ఎనిమిది",
            "ఆరు వందల డెబ్బై తొమ్మిది",
            "ఆరు వందల ఎనభై",
            "ఆరు వందల ఎనభై ఒకటి",
            "ఆరు వందల ఎనభై రెండు",
            "ఆరు వందల ఎనభై మూడు",
            "ఆరు వందల ఎనభై నాలుగు",
            "ఆరు వందల ఎనభై ఐదు",
            "ఆరు వందల ఎనభై ఆరు",
            "ఆరు వందల ఎనభై ఏడు",
            "ఆరు వందల ఎనభై ఎనిమిది",
            "ఆరు వందల ఎనభై తొమ్మిది",
            "ఆరు వందల తొంభై",
            "ఆరు వందల తొంభై ఒకటి",
            "ఆరు వందల తొంభై రెండు",
            "ఆరు వందల తొంభై మూడు",
            "ఆరు వందల తొంభై నాలుగు",
            "ఆరు వందల తొంభై ఐదు",
            "ఆరు వందల తొంభై ఆరు",
            "ఆరు వందల తొంభై ఏడు",
            "ఆరు వందల తొంభై ఎనిమిది",
            "ఆరు వందల తొంభై తొమ్మిది",
            "ఏడు వందలు",
            "ఏడు వందల ఒకటి",
            "ఏడు వందల రెండు",
            "ఏడు వందల మూడు",
            "ఏడు వందల నాలుగు",
            "ఏడు వందల ఐదు",
            "ఏడు వందల ఆరు",
            "ఏడు వందల ఏడు",
            "ఏడు వందల ఎనిమిది",
            "ఏడు వందల తొమ్మిది",
            "ఏడు వందల పది",
            "ఏడు వందల పదకొండు",
            "ఏడు వందల పన్నెండు",
            "ఏడు వందల పదమూడు",
            "ఏడు వందల పద్నాలుగు",
            "ఏడు వందల పదహైదు",
            "ఏడు వందల పదహారు",
            "ఏడు వందల పదిహేడు",
            "ఏడు వందల పద్దెనిమిది",
            "ఏడు వందల పందొమ్మిది",
            "ఏడు వందల ఇరవై",
            "ఏడు వందల ఇరవై ఒకటి",
            "ఏడు వందల ఇరవై రెండు",
            "ఏడు వందల ఇరవై మూడు",
            "ఏడు వందల ఇరవై నాలుగు",
            "ఏడు వందల ఇరవై అయిదు",
            "ఏడు వందల ఇరవై ఆరు",
            "ఏడు వందల ఇరవై ఏడు",
            "ఏడు వందల ఇరవై ఎనిమిది",
            "ఏడు వందల ఇరవై తొమ్మిది",
            "ఏడు వందల ముప్పై",
            "ఏడు వందల ముప్పై ఒకటి",
            "ఏడు వందల ముప్పై రెండు",
            "ఏడు వందల ముప్పై మూడు",
            "ఏడు వందల ముప్పై నాలుగు",
            "ఏడు వందల ముప్పై ఐదు",
            "ఏడు వందల ముప్పై ఆరు",
            "ఏడు వందల ముప్పై ఏడు",
            "ఏడు వందల ముప్పై ఎనిమిది",
            "ఏడు వందల ముప్పై తొమ్మిది",
            "ఏడు వందల నలభై",
            "ఏడు వందల నలభై ఒకటి",
            "ఏడు వందల నలభై రెండు",
            "ఏడు వందల నలభై మూడు",
            "ఏడు వందల నలభై నాలుగు",
            "ఏడు వందల నలభై ఐదు",
            "ఏడు వందల నలభై ఆరు",
            "ఏడు వందల నలభై ఏడు",
            "ఏడు వందల నలభై ఎనిమిది",
            "ఏడు వందల నలభై తొమ్మిది",
            "ఏడు వందల యాభై",
            "ఏడు వందల యాభై ఒకటి",
            "ఏడు వందల యాభై రెండు",
            "ఏడు వందల యాభై మూడు",
            "ఏడు వందల యాభై నాలుగు",
            "ఏడు వందల యాభై ఐదు",
            "ఏడు వందల యాభై ఆరు",
            "ఏడు వందల యాభై ఏడు",
            "ఏడు వందల యాభై ఎనిమిది",
            "ఏడు వందల యాభై తొమ్మిది",
            "ఏడు వందల అరవై",
            "ఏడు వందల అరవై ఒకటి",
            "ఏడు వందల అరవై రెండు",
            "ఏడు వందల అరవై మూడు",
            "ఏడు వందల అరవై నాలుగు",
            "ఏడు వందల అరవై ఐదు",
            "ఏడు వందల అరవై ఆరు",
            "ఏడు వందల అరవై ఏడు",
            "ఏడు వందల అరవై ఎనిమిది",
            "ఏడు వందల అరవై తొమ్మిది",
            "ఏడు వందల డెబ్బై",
            "ఏడు వందల డెబ్బై ఒకటి",
            "ఏడు వందల డెబ్బై రెండు",
            "ఏడు వందల డెబ్బై మూడు",
            "ఏడు వందల డెబ్బై నాలుగు",
            "ఏడు వందల డెబ్బై ఐదు",
            "ఏడు వందల డెబ్బై ఆరు",
            "ఏడు వందల డెబ్బై ఏడు",
            "ఏడు వందల డెబ్బై ఎనిమిది",
            "ఏడు వందల డెబ్బై తొమ్మిది",
            "ఏడు వందల ఎనభై",
            "ఏడు వందల ఎనభై ఒకటి",
            "ఏడు వందల ఎనభై రెండు",
            "ఏడు వందల ఎనభై మూడు",
            "ఏడు వందల ఎనభై నాలుగు",
            "ఏడు వందల ఎనభై ఐదు",
            "ఏడు వందల ఎనభై ఆరు",
            "ఏడు వందల ఎనభై ఏడు",
            "ఏడు వందల ఎనభై ఎనిమిది",
            "ఏడు వందల ఎనభై తొమ్మిది",
            "ఏడు వందల తొంభై",
            "ఏడు వందల తొంభై ఒకటి",
            "ఏడు వందల తొంభై రెండు",
            "ఏడు వందల తొంభై మూడు",
            "ఏడు వందల తొంభై నాలుగు",
            "ఏడు వందల తొంభై ఐదు",
            "ఏడు వందల తొంభై ఆరు",
            "ఏడు వందల తొంభై ఏడు",
            "ఏడు వందల తొంభై ఎనిమిది",
            "ఏడు వందల తొంభై తొమ్మిది",
            "ఎనిమిది వందలు",
            "ఎనిమిది వందల ఒకటి",
            "ఎనిమిది వందల రెండు",
            "ఎనిమిది వందల మూడు",
            "ఎనిమిది వందల నాలుగు",
            "ఎనిమిది వందల ఐదు",
            "ఎనిమిది వందల ఆరు",
            "ఎనిమిది వందల ఏడు",
            "ఎనిమిది వందల ఎనిమిది",
            "ఎనిమిది వందల తొమ్మిది",
            "ఎనిమిది వందల పది",
            "ఎనిమిది వందల పదకొండు",
            "ఎనిమిది వందల పన్నెండు",
            "ఎనిమిది వందల పదమూడు",
            "ఎనిమిది వందల పద్నాలుగు",
            "ఎనిమిది వందల పదహైదు",
            "ఎనిమిది వందల పదహారు",
            "ఎనిమిది వందల పదిహేడు",
            "ఎనిమిది వందల పద్దెనిమిది",
            "ఎనిమిది వందల పందొమ్మిది",
            "ఎనిమిది వందల ఇరవై",
            "ఎనిమిది వందల ఇరవై ఒకటి",
            "ఎనిమిది వందల ఇరవై రెండు",
            "ఎనిమిది వందల ఇరవై మూడు",
            "ఎనిమిది వందల ఇరవై నాలుగు",
            "ఎనిమిది వందల ఇరవై అయిదు",
            "ఎనిమిది వందల ఇరవై ఆరు",
            "ఎనిమిది వందల ఇరవై ఏడు",
            "ఎనిమిది వందల ఇరవై ఎనిమిది",
            "ఎనిమిది వందల ఇరవై తొమ్మిది",
            "ఎనిమిది వందల ముప్పై",
            "ఎనిమిది వందల ముప్పై ఒకటి",
            "ఎనిమిది వందల ముప్పై రెండు",
            "ఎనిమిది వందల ముప్పై మూడు",
            "ఎనిమిది వందల ముప్పై నాలుగు",
            "ఎనిమిది వందల ముప్పై ఐదు",
            "ఎనిమిది వందల ముప్పై ఆరు",
            "ఎనిమిది వందల ముప్పై ఏడు",
            "ఎనిమిది వందల ముప్పై ఎనిమిది",
            "ఎనిమిది వందల ముప్పై తొమ్మిది",
            "ఎనిమిది వందల నలభై",
            "ఎనిమిది వందల నలభై ఒకటి",
            "ఎనిమిది వందల నలభై రెండు",
            "ఎనిమిది వందల నలభై మూడు",
            "ఎనిమిది వందల నలభై నాలుగు",
            "ఎనిమిది వందల నలభై ఐదు",
            "ఎనిమిది వందల నలభై ఆరు",
            "ఎనిమిది వందల నలభై ఏడు",
            "ఎనిమిది వందల నలభై ఎనిమిది",
            "ఎనిమిది వందల నలభై తొమ్మిది",
            "ఎనిమిది వందల యాభై",
            "ఎనిమిది వందల యాభై ఒకటి",
            "ఎనిమిది వందల యాభై రెండు",
            "ఎనిమిది వందల యాభై మూడు",
            "ఎనిమిది వందల యాభై నాలుగు",
            "ఎనిమిది వందల యాభై ఐదు",
            "ఎనిమిది వందల యాభై ఆరు",
            "ఎనిమిది వందల యాభై ఏడు",
            "ఎనిమిది వందల యాభై ఎనిమిది",
            "ఎనిమిది వందల యాభై తొమ్మిది",
            "ఎనిమిది వందల అరవై",
            "ఎనిమిది వందల అరవై ఒకటి",
            "ఎనిమిది వందల అరవై రెండు",
            "ఎనిమిది వందల అరవై మూడు",
            "ఎనిమిది వందల అరవై నాలుగు",
            "ఎనిమిది వందల అరవై ఐదు",
            "ఎనిమిది వందల అరవై ఆరు",
            "ఎనిమిది వందల అరవై ఏడు",
            "ఎనిమిది వందల అరవై ఎనిమిది",
            "ఎనిమిది వందల అరవై తొమ్మిది",
            "ఎనిమిది వందల డెబ్బై",
            "ఎనిమిది వందల డెబ్బై ఒకటి",
            "ఎనిమిది వందల డెబ్బై రెండు",
            "ఎనిమిది వందల డెబ్బై మూడు",
            "ఎనిమిది వందల డెబ్బై నాలుగు",
            "ఎనిమిది వందల డెబ్బై ఐదు",
            "ఎనిమిది వందల డెబ్బై ఆరు",
            "ఎనిమిది వందల డెబ్బై ఏడు",
            "ఎనిమిది వందల డెబ్బై ఎనిమిది",
            "ఎనిమిది వందల డెబ్బై తొమ్మిది",
            "ఎనిమిది వందల ఎనభై",
            "ఎనిమిది వందల ఎనభై ఒకటి",
            "ఎనిమిది వందల ఎనభై రెండు",
            "ఎనిమిది వందల ఎనభై మూడు",
            "ఎనిమిది వందల ఎనభై నాలుగు",
            "ఎనిమిది వందల ఎనభై ఐదు",
            "ఎనిమిది వందల ఎనభై ఆరు",
            "ఎనిమిది వందల ఎనభై ఏడు",
            "ఎనిమిది వందల ఎనభై ఎనిమిది",
            "ఎనిమిది వందల ఎనభై తొమ్మిది",
            "ఎనిమిది వందల తొంభై",
            "ఎనిమిది వందల తొంభై ఒకటి",
            "ఎనిమిది వందల తొంభై రెండు",
            "ఎనిమిది వందల తొంభై మూడు",
            "ఎనిమిది వందల తొంభై నాలుగు",
            "ఎనిమిది వందల తొంభై ఐదు",
            "ఎనిమిది వందల తొంభై ఆరు",
            "ఎనిమిది వందల తొంభై ఏడు",
            "ఎనిమిది వందల తొంభై ఎనిమిది",
            "ఎనిమిది వందల తొంభై తొమ్మిది",
            "తొమ్మిది వందలు",
            "తొమ్మిది వందల ఒకటి",
            "తొమ్మిది వందల రెండు",
            "తొమ్మిది వందల మూడు",
            "తొమ్మిది వందల నాలుగు",
            "తొమ్మిది వందల ఐదు",
            "తొమ్మిది వందల ఆరు",
            "తొమ్మిది వందల ఏడు",
            "తొమ్మిది వందల ఎనిమిది",
            "తొమ్మిది వందల తొమ్మిది",
            "తొమ్మిది వందల పది",
            "తొమ్మిది వందల పదకొండు",
            "తొమ్మిది వందల పన్నెండు",
            "తొమ్మిది వందల పదమూడు",
            "తొమ్మిది వందల పద్నాలుగు",
            "తొమ్మిది వందల పదహైదు",
            "తొమ్మిది వందల పదహారు",
            "తొమ్మిది వందల పదిహేడు",
            "తొమ్మిది వందల పద్దెనిమిది",
            "తొమ్మిది వందల పందొమ్మిది",
            "తొమ్మిది వందల ఇరవై",
            "తొమ్మిది వందల ఇరవై ఒకటి",
            "తొమ్మిది వందల ఇరవై రెండు",
            "తొమ్మిది వందల ఇరవై మూడు",
            "తొమ్మిది వందల ఇరవై నాలుగు",
            "తొమ్మిది వందల ఇరవై అయిదు",
            "తొమ్మిది వందల ఇరవై ఆరు",
            "తొమ్మిది వందల ఇరవై ఏడు",
            "తొమ్మిది వందల ఇరవై ఎనిమిది",
            "తొమ్మిది వందల ఇరవై తొమ్మిది",
            "తొమ్మిది వందల ముప్పై",
            "తొమ్మిది వందల ముప్పై ఒకటి",
            "తొమ్మిది వందల ముప్పై రెండు",
            "తొమ్మిది వందల ముప్పై మూడు",
            "తొమ్మిది వందల ముప్పై నాలుగు",
            "తొమ్మిది వందల ముప్పై ఐదు",
            "తొమ్మిది వందల ముప్పై ఆరు",
            "తొమ్మిది వందల ముప్పై ఏడు",
            "తొమ్మిది వందల ముప్పై ఎనిమిది",
            "తొమ్మిది వందల ముప్పై తొమ్మిది",
            "తొమ్మిది వందల నలభై",
            "తొమ్మిది వందల నలభై ఒకటి",
            "తొమ్మిది వందల నలభై రెండు",
            "తొమ్మిది వందల నలభై మూడు",
            "తొమ్మిది వందల నలభై నాలుగు",
            "తొమ్మిది వందల నలభై ఐదు",
            "తొమ్మిది వందల నలభై ఆరు",
            "తొమ్మిది వందల నలభై ఏడు",
            "తొమ్మిది వందల నలభై ఎనిమిది",
            "తొమ్మిది వందల నలభై తొమ్మిది",
            "తొమ్మిది వందల యాభై",
            "తొమ్మిది వందల యాభై ఒకటి",
            "తొమ్మిది వందల యాభై రెండు",
            "తొమ్మిది వందల యాభై మూడు",
            "తొమ్మిది వందల యాభై నాలుగు",
            "తొమ్మిది వందల యాభై ఐదు",
            "తొమ్మిది వందల యాభై ఆరు",
            "తొమ్మిది వందల యాభై ఏడు",
            "తొమ్మిది వందల యాభై ఎనిమిది",
            "తొమ్మిది వందల యాభై తొమ్మిది",
            "తొమ్మిది వందల అరవై",
            "తొమ్మిది వందల అరవై ఒకటి",
            "తొమ్మిది వందల అరవై రెండు",
            "తొమ్మిది వందల అరవై మూడు",
            "తొమ్మిది వందల అరవై నాలుగు",
            "తొమ్మిది వందల అరవై ఐదు",
            "తొమ్మిది వందల అరవై ఆరు",
            "తొమ్మిది వందల అరవై ఏడు",
            "తొమ్మిది వందల అరవై ఎనిమిది",
            "తొమ్మిది వందల అరవై తొమ్మిది",
            "తొమ్మిది వందల డెబ్బై",
            "తొమ్మిది వందల డెబ్బై ఒకటి",
            "తొమ్మిది వందల డెబ్బై రెండు",
            "తొమ్మిది వందల డెబ్బై మూడు",
            "తొమ్మిది వందల డెబ్బై నాలుగు",
            "తొమ్మిది వందల డెబ్బై ఐదు",
            "తొమ్మిది వందల డెబ్బై ఆరు",
            "తొమ్మిది వందల డెబ్బై ఏడు",
            "తొమ్మిది వందల డెబ్బై ఎనిమిది",
            "తొమ్మిది వందల డెబ్బై తొమ్మిది",
            "తొమ్మిది వందల ఎనభై",
            "తొమ్మిది వందల ఎనభై ఒకటి",
            "తొమ్మిది వందల ఎనభై రెండు",
            "తొమ్మిది వందల ఎనభై మూడు",
            "తొమ్మిది వందల ఎనభై నాలుగు",
            "తొమ్మిది వందల ఎనభై ఐదు",
            "తొమ్మిది వందల ఎనభై ఆరు",
            "తొమ్మిది వందల ఎనభై ఏడు",
            "తొమ్మిది వందల ఎనభై ఎనిమిది",
            "తొమ్మిది వందల ఎనభై తొమ్మిది",
            "తొమ్మిది వందల తొంభై",
            "తొమ్మిది వందల తొంభై ఒకటి",
            "తొమ్మిది వందల తొంభై రెండు",
            "తొమ్మిది వందల తొంభై మూడు",
            "తొమ్మిది వందల తొంభై నాలుగు",
            "తొమ్మిది వందల తొంభై ఐదు",
            "తొమ్మిది వందల తొంభై ఆరు",
            "తొమ్మిది వందల తొంభై ఏడు",
            "తొమ్మిది వందల తొంభై ఎనిమిది",
            "తొమ్మిది వందల తొంభై తొమ్మిది"
        ]

        self.years = {
            1950: "ఒక వెయ్యి తొమ్మిది వందల యాభై",
            1951: "ఒక వెయ్యి తొమ్మిది వందల యాభై ఒకటి",
            1952: "ఒక వెయ్యి తొమ్మిది వందల యాభై రెండు",
            1953: "ఒక వెయ్యి తొమ్మిది వందల యాభై మూడు",
            1954: "ఒక వెయ్యి తొమ్మిది వందల యాభై నాలుగు",
            1955: "ఒక వెయ్యి తొమ్మిది వందల యాభై ఐదు",
            1956: "ఒక వెయ్యి తొమ్మిది వందల యాభై ఆరు",
            1957: "ఒక వెయ్యి తొమ్మిది వందల యాభై ఏడు",
            1958: "ఒక వెయ్యి తొమ్మిది వందల యాభై ఎనిమిది",
            1959: "ఒక వెయ్యి తొమ్మిది వందల యాభై తొమ్మిది",
            1960: "ఒక వెయ్యి తొమ్మిది వందల అరవై",
            1961: "ఒక వెయ్యి తొమ్మిది వందల అరవై ఒకటి",
            1962: "ఒక వెయ్యి తొమ్మిది వందల అరవై రెండు",
            1963: "ఒక వెయ్యి తొమ్మిది వందల అరవై మూడు",
            1964: "ఒక వెయ్యి తొమ్మిది వందల అరవై నాలుగు",
            1965: "ఒక వెయ్యి తొమ్మిది వందల అరవై ఐదు",
            1966: "ఒక వెయ్యి తొమ్మిది వందల అరవై ఆరు",
            1967: "ఒక వెయ్యి తొమ్మిది వందల అరవై ఏడు",
            1968: "ఒక వెయ్యి తొమ్మిది వందల అరవై ఎనిమిది",
            1969: "ఒక వెయ్యి తొమ్మిది వందల అరవై తొమ్మిది",
            1970: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై",
            1971: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై ఒకటి",
            1972: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై రెండు",
            1973: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై మూడు",
            1974: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై నాలుగు",
            1975: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై ఐదు",
            1976: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై ఆరు",
            1977: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై ఏడు",
            1978: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై ఎనిమిది",
            1979: "ఒక వెయ్యి తొమ్మిది వందల డెబ్బై తొమ్మిది",
            1980: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై",
            1981: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై ఒకటి",
            1982: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై రెండు",
            1983: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై మూడు",
            1984: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై నాలుగు",
            1985: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై ఐదు",
            1986: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై ఆరు",
            1987: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై ఏడు",
            1988: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై ఎనిమిది",
            1989: "ఒక వెయ్యి తొమ్మిది వందల ఎనభై తొమ్మిది",
            1990: "ఒక వెయ్యి తొమ్మిది వందల తొంభై",
            1991: "ఒక వెయ్యి తొమ్మిది వందల తొంభై ఒకటి",
            1992: "ఒక వెయ్యి తొమ్మిది వందల తొంభై రెండు",
            1993: "ఒక వెయ్యి తొమ్మిది వందల తొంభై మూడు",
            1994: "ఒక వెయ్యి తొమ్మిది వందల తొంభై నాలుగు",
            1995: "ఒక వెయ్యి తొమ్మిది వందల తొంభై ఐదు",
            1996: "ఒక వెయ్యి తొమ్మిది వందల తొంభై ఆరు",
            1997: "ఒక వెయ్యి తొమ్మిది వందల తొంభై ఏడు",
            1998: "ఒక వెయ్యి తొమ్మిది వందల తొంభై ఎనిమిది",
            1999: "ఒక వెయ్యి తొమ్మిది వందల తొంభై తొమ్మిది",
            2000: "రెండు వేలు",
            2001: "రెండు వేల ఒకటి",
            2002: "రెండు వేల రెండు",
            2003: "రెండు వేల మూడు",
            2004: "రెండు వేల నాలుగు",
            2005: "రెండు వేల ఐదు",
            2006: "రెండు వేల ఆరు",
            2007: "రెండు వేల ఏడు",
            2008: "రెండు వేల ఎనిమిది",
            2009: "రెండు వేల తొమ్మిది",
            2010: "రెండు వేల పది",
            2011: "రెండు వేల పదకొండు",
            2012: "రెండు వేల పన్నెండు",
            2013: "రెండు వేల పదమూడు",
            2014: "రెండు వేల పద్నాలుగు",
            2015: "రెండు వేల పదహైదు",
            2016: "రెండు వేల పదహారు",
            2017: "రెండు వేల పదిహేడు",
            2018: "రెండు వేల పద్దెనిమిది",
            2019: "రెండు వేల పందొమ్మిది",
            2020: "రెండు వేల ఇరవై",
            2021: "రెండు వేల ఇరవై ఒకటి",
            2022: "రెండు వేల ఇరవై రెండు"
        }

    def to_cardinal(self, value):
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        if 0 <= value < len(self.corpus):
            return self.corpus[value]

        elif value in self.years.keys():
            return self.years[value]

        else:
            # TODO computing min and max is compute heavy. We probably dont need to do this every time since Python3 has order in keys.
            raise OverflowError(self.errmsg_notinrange % (value, len(self.corpus), min(self.years.keys()), max(self.years.keys())))
