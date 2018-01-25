cmake_minimum_required(VERSION 2.8.3)
project(aws_s3_upload)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

 add_message_files(
   FILES
   Uploader.msg
   UploaderStatus.msg
 )

 generate_messages(
   DEPENDENCIES
   std_msgs
 )

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS message_runtime
#  INCLUDE_DIRS include
#  LIBRARIES aws_s3_upload
#  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

 install(PROGRAMS
   scripts/aws_s3_upload_node.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

 install(DIRECTORY launch
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
 )
