#!/usr/bin/python
# cheng pei created by 20140127

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from time import gmtime, strftime


device = MonkeyRunner.waitForConnection()

# # Installs the Android package. Notice that this method returns a boolean, so you can test
# # to see if the installation worked.
# # device.installPackage('myproject/bin/MyApplication.apk')
# 
# # sets a variable with the package's internal name
# package = 'cn.cp.demo'
# 
# # sets a variable with the name of an Activity in the package
# activity = 'cn.cp.demo.MainActivity'
# 
# # sets the name of the component to start
# runComponent = package + '/' + activity
# 
# # Runs the component
# device.startActivity(component=runComponent)
# 
# # Presses the Menu button
# device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
result      = device.takeSnapshot()

datetime    = strftime("%Y-%m-%d %H:%M:%S", gmtime())
# Writes the screenshot to a file
result.writeToFile ( datetime + '.png','png')