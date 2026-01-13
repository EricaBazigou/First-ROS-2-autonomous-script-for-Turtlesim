import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleDriver(Node):
    def __init__(self):
        super().__init__('circle_driver')
        # Δημιουργούμε έναν "εκδότη" που στέλνει εντολές ταχύτητας
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # Κάθε 0.5 δευτερόλεπτα θα τρέχει η συνάρτηση drive
        self.timer = self.create_timer(0.5, self.drive)

    def drive(self):
        msg = Twist()
        msg.linear.x = 2.0  # Ταχύτητα μπροστά
        msg.angular.z = 1.0 # Πόσο πολύ θα στρίβει
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = CircleDriver()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()