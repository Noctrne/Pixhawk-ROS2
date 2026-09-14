import rclpy
from rclpy.node import Node
from pix_msgs.msg import PixBaro

from pymavlink import mavutil
import numpy as np

class PixhawkBarometerNode(Node):
    def __init__(self):
        super().__init__('pixhawk_barometer_node')
        self.publisher_baro = self.create_publisher(PixBaro, 'pix/sensor/barometer', 10)
        
        self.pix_address = '127.0.0.1:14552'
        self.pix_baud = 57600
        
        self.get_logger().info('Mencoba connect mavrouter...')
        self.master = mavutil.mavlink_connection(self.pix_address, self.pix_baud)
        self.master.wait_heartbeat()
        self.get_logger().info('Node BAROMETER berhasil connect ke mavrouter - Pixhawk 6C')
        
    
        self.create_timer(0.1, self.baro_cb)
        
    def baro_cb(self):
        
        get_data = self.master.recv_match(type='SCALED_PRESSURE', blocking=1)
        
        if get_data is None:
            return
        
        data_baro = PixBaro()
        data_baro.abs_pressure = get_data.press_abs
        
        self.publisher_baro.publish(data_baro)
        
        self.get_logger().info(f'[Tekanan Udara] {get_data.press_abs:.2f}')
        
def main(args=None):
    rclpy.init(args=args)
    baro_node = PixhawkBarometerNode()
    rclpy.spin(baro_node)
    baro_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    
#test git credent