import rclpy
from rclpy.node import Node
from pix_msgs.msg import PixAtt
from numpy import rad2deg

from pymavlink import mavutil
import numpy as np

class PixhawkAttitudeNode(Node):
    def __init__(self):
        super().__init__('pixhawk_attitude_node')
        self.publisher_att = self.create_publisher(PixAtt, 'pix/sensor/attitude', 10)
        
        
        self.pix_address = '127.0.0.1:14553'
        self.pix_baud = 57600
        
        self.get_logger().info('Mencoba connect mavrouter...')
        self.master = mavutil.mavlink_connection(self.pix_address, self.pix_baud)
        self.master.wait_heartbeat()
        self.get_logger().info('Node ATTITUDE berhasil connect ke mavrouter - Pixhawk 6C')
        
        self.create_timer(0.1, self.att_cb)
        
    def att_cb(self):
        
        get_data = self.master.recv_match(type='ATTITUDE', blocking=1)
        
        if get_data is None:
            return
        
        data_att = PixAtt()
        data_att.roll = rad2deg(get_data.roll) 
        data_att.pitch = rad2deg(get_data.pitch)
        data_att.yaw = rad2deg(get_data.yaw)
        
        self.publisher_att.publish(data_att)
        
        self.get_logger().info(f'[Roll] {data_att.roll:.2f} | [Pitch] {data_att.pitch:.2f} | [Yaw] {data_att.yaw:.2f}')


def main(args=None):
    rclpy.init(args=args)
    att_node = PixhawkAttitudeNode()
    rclpy.spin(att_node)
    att_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()