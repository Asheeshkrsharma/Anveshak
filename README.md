# Anveshak
Source code for Anveshak space exploration rover
Connections: Pins of Arduino are connected according to:

| Pin Configuration Table       |    |
|-------------------------------|----|
| Right Head lamp               | 9  |
| Left Head lamp                | 10 |
| Fan                           | 8  |
| Steering Motor (relay enable) | 12 |
| Engine Motor (relay enable)   | 11 |
| Steering Motor (Direction)    | 3  |
| Engine Motor (Direction)      | 2  |

## Run

1. ```cd Anveshak/```
2. ```python main.py```
3. When the Parameter Shows up, Type the Arduino device address & Pin configurations and hit ```configure```.

When the configure button is pressed, it opens a terminal window automatically, wakes up ROSCORE process and ROSPY child process.
