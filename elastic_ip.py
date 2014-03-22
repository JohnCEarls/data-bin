#!/usr/bin/env python
import boto
import boto.utils

instance = boto.utils.get_instance_identity()['document']['instanceId']

ec2 = boto.connect_ec2()
success = False
for address in ec2.get_all_addresses():
    try:
        res = address.associate(instance)
        if res:
            print "Associated with %s" % address
            break
    except Exception as e:
        print e
        print "Unable to associate with %s" % address 

