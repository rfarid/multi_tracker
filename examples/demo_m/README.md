# Using multiple camera simultaneously

## Exemplar cameras
| Camera#       | serial        | 
| ------------- |:-------------:|
|	1			|	11381191	|
|	2			| 	11381192	|
|	3			| 	11462467	|
|	4			| 	11381149	|

# How to run 
1. **Copy** demo_m to the **home** directory
2. Follow these steps (shown for camera1) for each camera to run the multi-tracking
* terminal 1
	```
	roslaunch pointgrey_camera_driver camera.launch camera_serial:=11381191 camera_name:=camera1
	```
* terminal 2
	```
	cd ~/demo_m/cam1/src

	// check if camera is ready and publishes properly

	rosrun image_view image_view image:=/camera1/image_raw

	// stop and run tracker

	roslaunch tracking_launcher.launch
	```
* terminal 3: (optional) record specific topic as a bag file
	```
	rosbag record subset list multi_tracker/1/contours
	```
* terminal 4: (optional)
	```
 	// add multi_tracker/1/contours topic to delta_video_config.py (look at cam2)
 	```
* moving inside the experiment environment for a while
* ctrl+c all terminals at the end of performance

# How to display the recorded data
1. **Copy** stored data (png, bag and hdf5 files) to cam1/test_data folder
2. **Rename** the config file using hdf5 timestamp
3. **Replace** bag file name in launch_delta_video.launch
4. 
```
	roslaunch launch_delta_video.launch
```
5. optional
```
	roslaunch launch_delta_video_with_contours.launch (look at cam2)
```
6. optional
```
	// check recorded bag file
	// rosbag info -y <bag_file>
 	// roscore and rosbag play <bag_file>
	// rqt_bag 
```
more options: (http://wiki.ros.org/rqt_bag)

