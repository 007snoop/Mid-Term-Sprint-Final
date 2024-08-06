def A_B():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.55)
    chassis_ctrl.move_with_distance(0,0.3)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0,0.8)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0,0.38)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0,1.65)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0,0.45)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0,0.55)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0,1.5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0,0.54)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0,0.86)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0,0.41)
 
def B_C():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.56)
 
def C_D():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.25)
 
def D_E():
    chassis_ctrl.move_with_distance(0, 3.7)
 
def E_F():
    chassis_ctrl.move_with_distance(0, 4.9)
 
def F_G():
    chassis_ctrl.move_with_distance(0, 4.0)
 
def G_H():
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 1.2)
 
def H_D():
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    gimbal_ctrl.yaw_ctrl(-180)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 3.8)
 
def D_A():
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.47)
 
marker_found = False
 
def scan_for_marker():
    # Turn on detection and scan left and right until you hit a marker.rm_define.media_custom_audio_0
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    global marker_found
    marker_found = False
    gimbal_ctrl.yaw_ctrl(-90)
    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)
 
 
# Telling robot what to do once marker found
 
def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    media_ctrl.play_sound(rm_define.media_sound_recognize_success)
    time.sleep(3)
    led_ctrl.gun_led_on()
    gun_ctrl.set_fire_count(3)
    led_ctrl.gun_led_off()
    gimbal_ctrl.yaw_ctrl(0)
    time.sleep(5)
    marker_found = True
 
def vision_recognized_marker_letter_D(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    time.sleep(3)
    gimbal_ctrl.yaw_ctrl(0)
    time.sleep(5)
    marker_found = True
 
def vision_recognized_marker_number_one(msg):
    # if one chassis and gimbal
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.recenter()
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.yaw_ctrl(0)
    marker_found = True
 
 
 
def start():
 
    # Setting Robot Settings
 
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(60)
    chassis_ctrl.set_rotate_speed(30)
    chassis_ctrl.set_trans_speed(1)
    gimbal_ctrl.recenter()
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_marquee)
 
    # From A to B
    A_B()
 
    # From B to C
    B_C()
 
    H_D()
 
 