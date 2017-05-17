# ------------------------------------------------------------------------------

import json
import pprint
import types

# ------------------------------------------------------------------------------

pp = pprint.pprint

# ------------------------------------------------------------------------------

print """= FIO Benchmark Report
:sectnums:
:toc: left
:toclevels: 3
:data-uri:

:toc!:
"""

# ------------------------------------------------------------------------------

json_data = open("report_json.txt").read()
data = json.loads(json_data)
#pp.pprint(data)

# ------------------------------------------------------------------------------

def print_iostats2(io_name, io_dict):
    print ""
    print "==== %s"%(io_name)
    print ""
    print '[cols="2,3a"]'
    print '|==='
    print '| Property | Value'
    
    x = io_dict
    for k in io_dict.keys():
        print ""
        print "|", k
        if not isinstance(x[k], types.DictionaryType):
            print "|", x[k]
        else:
            print "|"
            keys2 = x[k].keys()
            keys2.sort()
            for e in keys2:
                print "* %s: %d"%(e, x[k][e])
    print ""
    print "|==="
            
def print_iostats(io_name, io_dict):
    print ""
    print "=== %s"%(io_name)
    print ""
    print '[cols="2,3a"]'
    print '|==='
    print '| Property | Value'
    
    x = io_dict
    keys = io_dict.keys()
    keys.sort()
    L = []
    for k in keys:
        try:
            L.append(int(k))
        except:
            L.append(k)
    L.sort()
    for k0 in L:
        if isinstance(k0, types.IntType):
            k = "%d"%(k0)
        else:
            k = k0
        if not isinstance(x[k], types.DictionaryType):
            print ""
            print "|", k
            print "|", x[k]
    print ""
    print "|==="

    for k in keys:
        if isinstance(x[k], types.DictionaryType):
            print_iostats2(k, x[k])
    
# ------------------------------------------------------------------------------

print "== Report - Summary"
print ""
print "=== FIO Information"
print ""
k = "time"
print "%s::"%(k)
print "  * %s"%(data[k])

print ""
k = "fio version"
print "%s::"%(k)
print "  * %s"%(data[k])

print """
=== Global Options

[cols="2,3a"]
|===
| Property | Value"""

global_opts = data["global options"]
x = global_opts
keys = x.keys()
keys.sort()
for k in keys:
    print ""
    print "|", k
    print "|", x[k]
print ""
print "|==="

# ------------------------------------------------------------------------------

if "disk_util" in data.keys():
    print """
    === Disk Utilization

    [cols="2,3a"]
    |===
    | Property | Value"""

    disk_util = data["disk_util"]
    x = disk_util[0]
    keys = x.keys()
    keys.sort()
    for k in keys:
        print ""
        print "|", k
        print "|", x[k]
    print ""
    print "|==="

# ------------------------------------------------------------------------------

s = """
=== job options

[cols="2,3a"]
|===
| Property | Value"""

job_id = 0    
for job in data["jobs"]:
    print ""
    print "== Report - Job(%d) - %s"%(job_id, job["jobname"])
    print ""
    print '[cols="2,3a"]'
    print '|==='
    print '| Property | Value'

    x = job
    keys = job.keys()
    keys.sort()
    for k in keys:
        if not isinstance(x[k], types.DictionaryType):
            print ""
            print "|", k
            print "|", x[k]
    print ""
    print "|==="  

    for k in job.keys():
        if isinstance(x[k], types.DictionaryType):
            print_iostats(k, job[k])
    
    #print_iostats("read", job)    
    #print_iostats("write", job)
    
    job_id += 1
    
# ------------------------------------------------------------------------------
