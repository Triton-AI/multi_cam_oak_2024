import cv2 #open cv import
import depthai as dai #depthai import
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node



class OakCamNode(Node):
    #todo define params for camera settnigs


    #todo define params for camera pipline configuration
    
    def __init__(self):
        super().__init__("oak_cam_node")
        device_info = dai.Device.getAllAvailableDevices()
        num_devices = len(device_info)
        print("number of oak devices: ",num_devices)
        for dev in device_info:
            print("==== Oak device =====")
            print("\t>>> Connceted to:", dev.getMxId())
            print("\t>>> Name:",dev.name)
            print("---------------")
    #todo add pipeline setup



def main():
    rclpy.init()
    cam_node = OakCamNode()

if __name__ == "main":
    main()