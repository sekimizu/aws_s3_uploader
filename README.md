# ***** NOTICE *****
This is a ROS package to support upload file to AWS S3 server.

------

## REQUIREMENTS
- Ubuntu 16.04
- ROS Kinetic Kame
- [python boto3](https://boto3.readthedocs.io/en/latest/)

## DESCRIPTIONS
Use the following topics to launch file upload process and report status

> Receive file upload command:
> > * topic: file_uploader
> > * type: Uploader
> > * data: "filepath: '/xxxx/xxxx/xxxx', filename: 'xxx.mp3'"
>
> Report status:
> > * topic: file_uploader_status
> > * data: "uploading" / "success" / "failed"
> 
> AWS S3 server information:
> > * account: aqua@Pega
> > * bucket name: aqua-pega-camera-capture
> > * folder name: camera_capture
> > * region: S3 server didn't required region specification
> > * access url: https://s3.console.aws.amazon.com/s3/buckets/aqua-pega-camera-capture/?region=us-east-2&tab=overview
>

## INSTALLATIONS
-   boto3

     ```
     $ pip install boto3
     ```

-   aws s3 uploader

     ```
     $ cp aws_s3_upload ~/catkin_ws/src
     $ cd ~/catkin_ws
     $ catkin_make
     ```

## USAGES

Start aws_s3_upload node
```
$ roslaunch aws_s3_upload aws_s3_upload.launch
```
Fill-in AWS related infroamtion into 'app.py'

AWS_ACCESS_KEY_ID = '<YOUR_ACCESS_KEY_ID>'
AWS_SECRET_ACCESS_KEY = '<YOUR_AWS_SECRET_ACCESS_KEY>'
AWS_BUCKET_NAME = '<YOUR_AWS_BUCKET_NAME>'
AWS_FOLDER_NAME = '<YOUR_AWS_FOLDER_NAME>'


## TESTING
- Test uploader status report.
```
$ rostopic echo /file_uploader_status
```

- Test upload file.

Try to upload local file "/shared/audio_files/morning_jp.mp3" to AWS S3 server.

```
$ rostopic pub -1 /file_uploader aws_s3_upload/Uploader "filepath: '/shared/audio_files'
filename: 'morning_jp.mp3'"
```
