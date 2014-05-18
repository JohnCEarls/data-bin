#!/usr/bin/env python
import boto
import boto.utils
import sys

site_name = 'aurea-nebula.adversary.us'
instance = boto.utils.get_instance_identity()['document']['instanceId']
def get_ip( site_name ):
    """
    Get the ip for this site from route 53 based on site name
    """
    r53 = boto.connect_route53()
    zone = r53.get_zone('.'.join(site_name.split('.')[1:]) + '.')
    record = zone.get_a(site_name).resource_records
    if record is None or len(record) != 1:
        print len(record)
        raise Exception(
                "Unable to find a unique route 53 record for [%s] [%r]" % (
            site_name, record) )
    return record 


def associate_ip( instance_id, site_name ):
    ec2 = boto.connect_ec2()
    success = False
    for address in ec2.get_all_addresses(get_ip(site_name)):
        try:
            res = address.associate(instance)
            if res:
                print "Associated with %s" % address
                break
        except Exception as e:
            print e
            print "Unable to associate with %s" % address 
print "Attempting to associate %s with %s" % ( site_name, instance )
associate_ip( instance, site_name)
