#! /usr/bin/env python

import rospy 
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random

def my_publisher():
    # control part

    rospy.init_node('rrr_control_python_node')
    control_publisher = rospy.Publisher('/arm_controller_bis/command', JointTrajectory, queue_size=10)

    while not rospy.is_shutdown():
        
        msg = JointTrajectory()

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']

        point = JointTrajectoryPoint()
        j1 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j2 = 2 * (random.random() - 0.5)
        j3 = 2 * (random.random() - 0.5)
        j4 = 2 * (random.random() - 0.5)
        j5 = 2 * (random.random() - 0.5)
        j6 = 2 * (random.random() - 0.5)
        j7 = 2 * (random.random() - 0.5)

        point.positions = [j1, j2, j3, j4, j5, j6, j7]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append( point )

        control_publisher.publish( msg )
        rospy.loginfo( msg ) 


if __name__ == '__main__':

    my_publisher()


