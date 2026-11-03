import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from pix_msgs.msg import PixAtt, PixBaro

import numpy as np

class PixhawkDataCenterNode(Node):
    def __init__(self):
        super().__init__('pixhawk_collecting_data_node')
        self.subscriber_att = self.create_subscription(PixAtt, 'pix/sensor/attitude', self.att_cb, 10)
        self.subscriber_baro = self.create_subscription(PixBaro, 'pix/sensor/barometer',self.baro_cb ,10)
        
        #init data awal
        self.att_subsdata = None
        self.baro_subsdata = None
        
        self.create_timer(0.1, self.data_cb)
        
        
    def att_cb(self, msg):
        self.att_subsdata = msg
        
        
    def baro_cb(self, msg):
        self.baro_subsdata = msg
    
    
    
    def data_cb(self):
        
        if self.att_subsdata is None or self.baro_subsdata is None:
            return

        #ambil data dari msgs
        self.abs_pressure = self.baro_subsdata.abs_pressure
        self.roll = self.att_subsdata.roll
        self.pitch = self.att_subsdata.pitch
        self.yaw = self.att_subsdata.yaw
        
        self.get_logger().info(f'[Tekanan udara] {self.abs_pressure}')
        self.get_logger().info(f'[Sudut Roll] {self.roll}')
        self.get_logger().info(f'[Sudut Pitch] {self.pitch}')
        self.get_logger().info(f'[Sudut Yaw] {self.yaw}')
        
def main(args=None):
    rclpy.init(args=args)
    datacenter_node = PixhawkDataCenterNode()
    rclpy.spin(datacenter_node)
    datacenter_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()