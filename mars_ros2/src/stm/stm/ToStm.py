import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import serial

#ser = serial.Serial('/dev/ttyUSB0', 115200)
#print(ser.name) 


class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(String, 'command', self.listener_callback, 10)
    
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        #ser.write(msg.data.encode('UTF-8'))
        print(msg.data.encode('UTF-8'))

def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
