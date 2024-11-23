#! /usr/bin/env python
#
# main.py - Main entry point for the ROS-to-OpenCog converter
# Copyright (C) 2015  Hanson Robotics
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License v3 as
# published by the Free Software Foundation and including the exceptions
# at http://opencog.org/wiki/Licenses
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License
# along with this program; if not, write to:
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# XXX To be removed when https://github.com/hansonrobotics/HEAD/issues/618
# is resolved nicely
import sys
sys.path.append("/opt/hansonrobotics/ros/lib/python2.7/dist-packages/")

import logging
import rospy
from affect import Affect
from audio_power import AudioPower
from chat_track import ChatTrack
from control import Control
from control_psi import ControlPsi
from face_recog import FaceRecog
from face_track import FaceTrack
from sound_track import SoundTrack
from room_brightness import RoomBrightness
from saliency_track import SaliencyTrack
from tts_feedback import TTSFeedback

rospy.init_node("OpenCog_ROS_bridge")
logging.info("Starting the OpenCog ROS Bridge")
print "Starting the OpenCog ROS Bridge"

co = Control()
cp = ControlPsi()
af = Affect()
ap = AudioPower()
ct = ChatTrack()
fc = FaceRecog()
ft = FaceTrack()
st = SoundTrack()
br = RoomBrightness()
sl = SaliencyTrack()
tf = TTSFeedback

try:
	rospy.spin()
except rospy.ROSInterruptException as e:
	print(e)

print "Exit OpenCog ROS bridge"
