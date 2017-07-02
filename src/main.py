#!/usr/bin/env python
from gi.repository import Gtk, GdkPixbuf, Gdk
import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import String
import os, sys
import time
class GUI:
	def __init__(self):
		self.gladefile = "tutorial-5c.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		window = self.builder.get_object('window1')
		window.show()
	def  on_button1_clicked(self, widget):
		pub = rospy.Publisher('servo', UInt16)
		rospy.init_node('nh')
		if not rospy.is_shutdown():
			righth = self.builder.get_object('entry1')
			lefth = self.builder.get_object('entry2')
			fan = self.builder.get_object('entry7')
			steerM = self.builder.get_object('entry3')
			engineM = self.builder.get_object('entry4')
			pub.publish(int(righth.get_text()))
			rospy.sleep(2)
			pub.publish(int(lefth.get_text()))
			rospy.sleep(2)
			pub.publish(int(fan.get_text()))
			rospy.sleep(2)
			pub.publish(int(steerM.get_text()))
			rospy.sleep(2)
			pub.publish(int(engineM.get_text()))
	def on_Conf_clicked(self, widget):
		#Simple button cliked event
		port = self.builder.get_object('entry9')
		print port.get_text()
		os.system("sh Internal.sh " + port.get_text()) 
	def destroy(window, self):
		Gtk.main_quit()

def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())
