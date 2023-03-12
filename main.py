from _0audioequipment import *
from _1_1headphones import *
from _1_2hphone_types import *
from _1_3wireless_types import *
from _2_1speakers import *
from _2_2speakers_types import *
from _2_3indoors_types import *

audioequip = AudioEquipment("Союз")

headphone = Headphones("красный", producer="Союз")
wire = Wire(50, colour="красный", producer="Союз")
wireless = Wireless(300, colour="красный", producer="Союз")
tws = TWS("пластмасса", 20, battery_time=300, colour="красный", producer="Союз")
hoop = Hoop(battery_time=300, colour="красный", producer="Союз")

speaker = Speakers(95, producer="Союз")
outdoor = Outdoors(999, loudness=95, producer="Союз")
indoor = Indoors(2019, loudness=95, producer="Союз")
helper = VoiceHelper(year=2019, loudness=95, producer="Союз")

# print(audioequip.__dict__)
# print(headphone.__dict__)
# print(wire.__dict__)
# print(wireless.__dict__)
# print(tws.__dict__)
# print(hoop.__dict__)
#
# print(speaker.__dict__)
# print(outdoor.__dict__)
# print(indoor.__dict__)
# print(helper.__dict__)