# ComputerVision-ROS-LaptopCamera

This repository contains a ROS package that captures images from the laptop camera using OpenCV and publishes them on a ROS topic.

## Prerequisites

* Ubuntu 18.04 or later
* ROS Melodic or later
* OpenCV
* cv_bridge
* sensor_msgs

## Installation

1. Clone the repository:

* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/abelxmendoza/ComputerVision-ROS-LaptopCamera.git
  </code></div></div></pre>
* Build the package:

1. <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">cd ComputerVision-ROS-LaptopCamera/catkin_ws
   catkin_make
   </code></div></div></pre>

## Usage

1. Run the camera_publisher_node.py file to start capturing images from the laptop camera and publishing them on the "camera_image" topic:

* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">rosrun camera_publisher camera_publisher_node.py
  </code></div></div></pre>
* View the published images using an image viewer such as rviz or image_view:
  span

1. <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">rosrun image_view image_view image:=/camera_image
   </code></div></div></pre>

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.

## Acknowledgments

This project was inspired by the [ROS OpenCV Camera](https://github.com/ros-drivers/usb_cam) package.
