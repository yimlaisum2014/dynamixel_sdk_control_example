# dynamixel_sdk_control_example
ref : [DynamixelSDK](https://github.com/ROBOTIS-GIT/DynamixelSDK/tree/master)

## check the port name - dynamixel motor
```bash
$ ls /dev/tty #Check which port is being used on your controller (e.g /dev/ttyUSB0)
```

## give permission to the port
```bash
$ sudo chmod 777 /dev/ttyUSB0  
```

## clone the repo
```bash
git clone git@github.com:yimlaisum2014/dynamixel_sdk_control_example.git
```

## run script
```bash
$ cd ~/dynamixel_sdk_control_example/catkin_ws
$ catkin_make
$ source devel/setup.bash
$ rosrun dynamixel_sdk_examples read_write_node.py
```

you could see the current state of the motor by this command

`$ rosservice call /get_position "id: 1"`

you also could rostopic pub to control the motor

`$ rostopic pub /set_position dynamixel_sdk_examples/SetPosition "id: 1 position: 1000"`

>position:1000 -> TM-Gripper should be open

>position:2000 -> TM-Gripper should be close

#### Change below in the  read_write_node.py script if you have changed the setting the dynamixel motor setting
```bash
DXL_ID                      = 1                 # 9 for TM-Gripper
BAUDRATE                    = 57600             # 1000000 for TM-Gripper
DEVICENAME                  = '/dev/ttyUSB0'    # check the /dev in your computer
```