# ComputerVision-ROS-LaptopCamera

This repository contains a ROS package for capturing video from the laptop camera and performing basic computer vision operations on the captured frames.

## Installation

1. Clone this repository to your local machine:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/abelxmendoza/ComputerVision-ROS-LaptopCamera.git
  </code></div></div></pre>
* Install the necessary dependencies:
  <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>arduino</span></div></div></pre>

1. <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">sudo apt-get install ros-<distro>-cv-camera
   </code></div></div></pre>

   Replace `<distro>` with your ROS distribution (e.g. melodic, noetic, etc.).

## Usage

1. Launch the `cv_camera_node` node:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"></div></div></pre>

* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">roslaunch cv_camera cv_camera_node.launch
  </code></div></div></pre>
* Launch the `image_processing` node:
  <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"></div></div></pre>
* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">roslaunch cv_camera image_processing.launch
  </code></div></div></pre>
* View the processed images using an image viewer such as `rqt_image_view`:
  <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"></div></div></pre>

1. <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">rosrun rqt_image_view rqt_image_view
   </code></div></div></pre>

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

## License

This software is released under the MIT License. See the LICENSE file for details.
