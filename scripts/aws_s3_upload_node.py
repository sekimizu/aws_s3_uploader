#!/usr/bin/env python
import rospy
		
from aws_s3_upload.app import aws_s3_upload_node

if __name__ == '__main__':
	try:
		aws_s3_upload_node()
	except rospy.ROSInterruptException:
		pass
