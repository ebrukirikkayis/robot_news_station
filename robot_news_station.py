#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): 
    def __init__(self): 
        self.robot_name = "VEX Robot"
        super().__init__("robot_news_station") 
        self.get_logger().info("the robot news station has been started")


        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        
    def publish_news (self):
        msg = String()
        msg.data = "Hello, this is a " + str(self.robot_name) + " sending data from robot news station"
        self.publisher_.publish(msg)

    
	
def main(args=None):
    rclpy.init(args=args) # init communication
    node = RobotNewsStationNode() # MODIFY NAME, create the node object from the node class
    rclpy.spin(node)      # spin the node, so the callback is alive
    rclpy.shutdown()      # stop the communication


if __name__ == "__main__": # call the main function
    main()
