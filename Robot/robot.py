#description: RoboMaster S1 commands
#author: Colin Yetman
#date(s): 2024-08-02
marker_found = False
import robomaster
import time
def ledFlash()
    led_ctrl.set_flash(rm_define.armor_all,2)


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    a_b()

def markerScanNum():
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)

def markerScanLetter():
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P) # person
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D) # danger
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F) # fire


def vision_ctrl_recognized_marker_number_one(msg):
    # if one chassis and gimbal
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_ctrl_detection_marker)
    gimbal_ctrl.recenter()
    gimbal_ctrl.yaw_ctrl(90)
    gimbal_ctrl.recenter()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    
    marker_found = True
    pass

def vision_ctrl_recognized_marker_number_two(msg):
    # if two do something with LED
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_ctrl_detection_marker)
    media_ctrl.play_sound(rm_define.media_sound_scanning)
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()


    marker_found = True
    pass


def vision_ctrl_recognized_marker_number_three(msg):
    # if three do something with LED and gimbal and chassis
    global marker_found

    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.disable_detection(rm_define.vision_ctrl_detection_marker)
    time.sleep(2)

    media_ctrl.play_sound(rm_define.media_sound_count_down)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 200, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 200, 0, rm_define.effect_flash)
    time.sleep(2)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 200, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 200, rm_define.effect_flash)

    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

    gimbal_ctrl.set_rotate_speed(90)
    gimbal_ctrl.yaw_ctrl(75)
    gimbal_ctrl.pitch_ctrl(30)
    gimbal_ctrl.recenter()

    marker_found = True
    pass


def last_move():
    time.sleep(3)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.set_follow_chassis_offset(35)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.pitch_ctrl(20)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    gimbal_ctrl.pitch_ctrl(0)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    gimbal_ctrl.pitch_ctrl(20)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    gimbal_ctrl.pitch_ctrl(0)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1G)
    gimbal_ctrl.pitch_ctrl(20)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1DSharp)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    gimbal_ctrl.pitch_ctrl(0)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1C)
    gimbal_ctrl.pitch_ctrl(20)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
    gimbal_ctrl.pitch_ctrl(0)


 