# a class for simulation commands for a robot
class RobotControllerSimulator:
    def init(self):
    # a list to store all the commands that were executed
        self.history = []

# method for execuuting robot commands in a simulation manner
    def execute_command(self, command):
        self.history.append(command)
        print(f"[ROS2 Simulation] Executing command: {command}")
        return f"[ROS2 Simulation] Arm moved as per: {command}"

# create a copy of simulator
ros_sim = RobotControllerSimulator()

# a function to assist in executing the robots command via the simulator
def move_robot_arm_ros(coordinates: str):
    return ros_sim.execute_command(coordinates)