#description: RoboMaster S1 commands
#author: Colin Yetman
#date(s): 2024-08-02
import robomaster as rb

import time








def start():
    rb.armor_ctrl().set_hit_sensitivity(10)
    rb.led.turn_off(rb.rm_define.armor_ctrl_all())
    time.sleep(3)