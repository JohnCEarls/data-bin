#!/usr/bin/env python
import boto
import boto.utils

instance = boto.utils.get_instance_identity()['document']['instanceId']

ec2 = boto.connect_ec2()
eip = boto.ec2.address.Address( ec2, public_ip='184.73.161.43')
eip.associate(instance)
