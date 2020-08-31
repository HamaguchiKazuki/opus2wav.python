# This requires PyOgg to be installed ( pip install pyogg )
from openal import *

import time

source = oalOpen("sample_opus_files/sample.opus")

source.play()

while source.get_state() == AL_PLAYING:
    time.sleep(1)
    print('hoge')
# remember, don't forget to quit
oalQuit()
