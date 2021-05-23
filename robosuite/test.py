import robosuite

from robosuite.controllers import load_controller_config

# load default controller parameters for Operational Space Control (OSC)
controller_config = load_controller_config(default_controller="OSC_POSE")

# create an environment to visualize on-screen
env = robosuite.make(
    "Lift",
    robots=["Sawyer"],             # load a Sawyer robot and a Panda robot
    gripper_types="PandaGripper",                # use default grippers per robot arm
    controller_configs=controller_config,   # each arm is controlled using OSC
    has_renderer=True,                      # on-screen rendering
    render_camera="frontview",              # visualize the "frontview" camera
    has_offscreen_renderer=False,           # no off-screen rendering
    control_freq=20,                        # 20 hz control for applied actions
    horizon=200,                            # each episode terminates after 200 steps
    use_object_obs=False,                   # no observations needed
    use_camera_obs=False,                   # no observations needed
    path=['/home/lthpc/Desktop/meta-role/robosuite/robosuite/my_xmls/sawyer/[1.1, 1.1, 1.1, 1.1, 1.1, 0.9, 0.9, 0.9, 0.9, 0.9].xml']
)
