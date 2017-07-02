# Anveshak
The purpose of Anveshak is to decrease the complexity of exploration in space. The rover is
designed to mimic the features of SPIRIT rover. A major difference between the two rovers
is that anveshak tends to perform task on its own. Unlike SPIRIT, Anveshak can be
programmed to perform tasks on daily basis. It can differentiate between an interesting rock
and others.  Following figure shows a schematic of its software architecture:
![alt text](https://github.com/Asheeshkrsharma/Anveshak/blob/master/images/figure.png "Logo Title Text 1")

## Layer 1: Sensor Interface
A laser-based sensor is used to calculate wheel velocity. Arduino with ATMega328, which
has two photo-resistors, connected (with a 10k pull down resistor). Laser is aimed on a
photo-resistor (which is enclosed within a dark box). The Arduino monitors the values
returned from the light sensor, and watches for any changes that indicate that the laser beam
has been broken. Arduino then calculates the amount of time between when each sensor was
tripped. It then sends that value to the Adobe AIR based client, which is connected to the
Arduino via USB. Figure 12 shows the schematic of the circuit. As a webcam can yield the
required result for real-time performance, we use a ‘minoru-3d camera’, which is a stereo
camera (30hz@ 20fps), yielding required time stamping.

## Layer 2: Perception
Vision mapper: It is software, which actually calculates the 3d-Reconstruction data (Extrinsic
matrix, Intrinsic matrix, camera parameter prediction matrix) and maps the environment in a
point cloud. Based on Unscented Kalman filter (UKF), it uses camera pose estimation for
measurement of car position (to be used for planning using the map obtained from vision
mapper.

## Layer 3: Planning and control
Steering and Break: It comprises direct interface with the steering and breaking actuators on
the car. Once the path is obtained using path planner, it uses ‘PID’ algorithm to control
break/steering.
Manual Override: it is a counter switch for manual (user) control, which can be engaged
using the graphic user interface from computer.
Path planning: It uses A* search algorithm to plan routes using the map obtained.

# Chassis
A chassis consists of an internal framework that supports a man-made object in its
construction and use. It is analogous to an animal's skeleton. An example of a chassis is the
under part of a motor vehicle, consisting of the frame (on which the body is mounted) with the
wheels and machinery. For Anveshak, it is made up of Aluminum 6051. Gas welding was
used to join beams. Any good chassis must do several things:

1. Be structurally sound in every way over the expected life of the vehicle and
beyond. This means nothing will ever break under normal conditions.
2. Maintain the suspension mounting locations so that handling is safe and consistent
under high cornering and bump loads.
3. Support the body panels and other passenger components so that everything feels
solid and has a long, reliable life.
4. Protect the occupants from external intrusion.

Even though an individual rectangular tube is about 2% less stiff in torsion than the equivalent
round tube, we must consider the chassis design as a whole. For each transverse tie-in we
create a system that becomes more like a single large tube spanning the whole width of the
chassis- the ultimate in efficiency. We have integrated 7 transverse members along our main
rails in such a way that the chassis has much more torsional stiffness than the tubes taken
individually. We even put extra braces on our central "X" member to make it even stronger.
The stiffness of an ideal unitized structure is proportional to the square of the distance of the
components from the centerline. Double the distance and you have four times the overall
stiffness. While practical automotive considerations eliminate an ideal connection between the
rails, widely spaced tubes that are tied together well work more efficiently than the same tubes
on a narrower base. The original 427 Cobras' rails were only 20 inches apart. Ours are spaced
at 27 inches on center through the middle of the chassis, one of the widest spacing in the
industry. And we still are one of the few in the industry that have left room for an under car
exhaust outside the rails.

# Source code for Anveshak space exploration rover
The software follows the 4-layer architecture as discussed above.

## Parameter setup window
Interface is written on Linux native GUI design tool Glade interface designer. Following
code results the parameter setup window of the software. Parameter setup window renders
ability to tweak pinouts of Arduino on the fly. This ability requires parallel programming.
Following figure shows the Parameter setup window.

![alt text](https://github.com/Asheeshkrsharma/Anveshak/blob/master/images/Screenshot%20from%202012-10-28%2020_22_23.png "Logo Title Text 1")

### Steps to run the code.
 1. Connections: Pins of Arduino are connected according to following table.

| Pin Configuration Table       | pin|
|-------------------------------|----|
| Right Head lamp               | 9  |
| Left Head lamp                | 10 |
| Fan                           | 8  |
| Steering Motor (relay enable) | 12 |
| Engine Motor (relay enable)   | 11 |
| Steering Motor (Direction)    | 3  |
| Engine Motor (Direction)      | 2  |

2. Connect the Arduino cable to Computer.

3. In a terminal
   ```cd Anveshak/```
   ```python main.py```
4. When the Parameter Shows up, Type the Arduino device address and hit configure
button.

When the configure button is pressed, it opens a terminal window automatically, wakes up
ROSCORE process and ROSPY child process. ROSCORE process is shown in figure 8.3.
Rospy child process is show in figure 8.4.
![alt text](https://github.com/Asheeshkrsharma/Anveshak/blob/master/images/Screenshot%20from%202012-10-28%2020_25_01.png "Logo Title Text 1")
![alt text](https://github.com/Asheeshkrsharma/Anveshak/blob/master/images/Screenshot%20from%202012-10-28%2020_25_19.png "Logo Title Text 1")


5. Go back to Parameter setup window, and type pin numbers as per table 1. This will
start Headlights, motors and fan one by one.
