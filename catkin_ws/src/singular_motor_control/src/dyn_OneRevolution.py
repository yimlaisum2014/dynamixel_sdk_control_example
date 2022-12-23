#!/usr/bin/env python3

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from dynamixel_sdk_examples.msg import SetPosition

class Pub():
    def __init__(self):
        self.service = rospy.Service('/run_one_revolution', Trigger, self.trigger_response)

    def trigger_response(request,self):
        run_step = SetPosition()
        motor_id = 5
        pub_action = rospy.Publisher('/set_position',SetPosition, queue_size=1)

        while not rospy.is_shutdown():
            run_step.id = motor_id
            run_step.position = 0
            pub_action.publish(run_step)
            rospy.sleep(2)
            run_step.position = 4095
            pub_action.publish(run_step)
            rospy.sleep(2)

                        
if __name__=='__main__':

    rospy.init_node("one_revolution_loop", anonymous=False)
    shoot = Pub()

    rospy.spin()