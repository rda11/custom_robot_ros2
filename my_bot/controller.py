import rclpy
from rclpy.node import Node 
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class Trajectory_publisher(Node):

    def __init__(self):
        super().__init__('trajectory_publisher_node')
        publish_topic = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publisher = self.create_publisher(JointTrajectory, publish_topic, 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joints = ['first_joint', 'fourth_joint', 'sixth_joint']
        self.goal_positions = [1.57, 0.50, 1.20]

    def timer_callback(self):
        my_bot_trajectory_msg = JointTrajectory()
        my_bot_trajectory_msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = self.goal_positions
        point.time_from_start = Duration(sec=2)
        my_bot_trajectory_msg.points.append(point)
        self.trajectory_publisher.publish(my_bot_trajectory_msg)

def main(args=None):
    rclpy.init(args=args)
    joint_trajectory_object = Trajectory_publisher()

    rclpy.spin(joint_trajectory_object)
    joint_trajectory_object.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
