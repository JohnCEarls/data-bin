#!/usr/bin/env python
import boto
import boto.utils

instance = boto.utils.get_instance_identity()['document']['instanceId']

ec2 = boto.connect_ec2()
success = False
for address in ec.get_all_addresses():
    try:
        eip = boto.ec2.address.Address( ec2, public_ip=address)
        res = eip.associate(instance)
        if res:
            print "Associated with %s" % address
            break
    except:
        print "Unable to associate with %s" % address 

