cmake_minimum_required(VERSION 3.5)

project(delta_lidar)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

set(SDK_PATH "./sdk/")

FILE(GLOB SDK_SRC 
  "${SDK_PATH}/src/*.cpp"
)

include_directories(
  ${PROJECT_SOURCE_DIR}/src
  ${PROJECT_SOURCE_DIR}/sdk/include
  ${PROJECT_SOURCE_DIR}/sdk/src
)

add_executable(delta_lidar_node src/node.cpp  ${SDK_SRC})
ament_target_dependencies(delta_lidar_node
  "rclcpp"
  "sensor_msgs"
)

add_executable(delta_lidar_node_client src/client.cpp)
ament_target_dependencies(delta_lidar_node_client
  "rclcpp"
  "sensor_msgs"
)


install(TARGETS
  delta_lidar_node delta_lidar_node_client
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch rviz sdk
  DESTINATION share/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()