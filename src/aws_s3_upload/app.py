#!/usr/bin/env python
import sys
import os
import boto3
import rospy
from boto3.s3.transfer import S3Transfer
from aws_s3_upload.msg import Uploader, UploaderStatus

AWS_ACCESS_KEY_ID = '<YOUR_ACCESS_KEY_ID>'
AWS_SECRET_ACCESS_KEY = '<YOUR_AWS_SECRET_ACCESS_KEY>'
AWS_BUCKET_NAME = '<YOUR_AWS_BUCKET_NAME>'
AWS_FOLDER_NAME = '<YOUR_AWS_FOLDER_NAME>'

TOPIC_FROM = 'file_uploader'
TOPIC_TO = 'file_uploader_status'

def create_uploader():
	return AwsS3Uploader(topic_from=TOPIC_FROM, topic_to=TOPIC_TO)

class AwsS3Uploader():
	def __init__(self, topic_from, topic_to):
		self._topic_from = topic_from
		self._aws_access_key_id = AWS_ACCESS_KEY_ID
		self._aws_secret_key = AWS_SECRET_ACCESS_KEY
		self._aws_bucket_name = AWS_BUCKET_NAME
		self._aws_folder_name = AWS_FOLDER_NAME
		self._subscriber = rospy.Subscriber(topic_from, Uploader, self._callback)
		self._publisher = rospy.Publisher(topic_to, UploaderStatus, queue_size=10)

		rospy.init_node('aws_s3_upload', anonymous = True)
		rospy.loginfo(" Create AWS S3 Uploader complete...")
		rospy.sleep(1)
		
	def _callback(self, msg):
		filepath = msg.filepath
		filename = msg.filename
		
		rospy.loginfo(rospy.get_caller_id() + " Upload file %s/%s to aws s3 server..." % (filepath, filename))
		full_file_name = os.path.join(filepath, filename)
		publish_msg = UploaderStatus()

		try:
			publish_msg.status = "uploading"
			self._publisher.publish(publish_msg)
			client = boto3.client('s3', aws_access_key_id=self._aws_access_key_id, aws_secret_access_key=self._aws_secret_key)
			transfer = S3Transfer(client)
			transfer.upload_file(full_file_name, self._aws_bucket_name, self._aws_folder_name+"/"+filename)
		except:
			rospy.loginfo(rospy.get_caller_id() + " Upload failed...")
			publish_msg.status = "failed"
			self._publisher.publish(publish_msg)
		else:
			rospy.loginfo(rospy.get_caller_id() + " Upload completed...")
			publish_msg.status = "success"
			self._publisher.publish(publish_msg)
		
	def on_shutdown(self):
		rospy.logdebug("shutdown AwsS3Uploader...")
		self._subscriber.unsubscribe(self._topic_from)

def aws_s3_upload_node():
	if len(sys.argv) < 2:
		print "USAGE: python upload.py <filename>"
		sys.exit(1)
	try:
		create_uploader()
	except rospy.ROSInterruptException:
		pass

	rospy.spin()
