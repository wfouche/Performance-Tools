# ===========================================================================

import xml.etree.ElementTree as XML
import time
import install_utils as U
import os

postilion_dir = os.getenv("PostilionDir")

# ===========================================================================

import getopt, glob, os, time, sys, find

def get_params(opt_list, trace=1):
    list = []
    for e in opt_list:
        if e[0] == "":
            pass
        else:
            if e[1] == None:
                list.append(e[0])
            else:
                list.append(e[0]+"=")   

    opts, args = getopt.getopt(sys.argv[1:], '', list)
    d = {}
    for o, a in opts:
        d[o] = a

    if trace: print ""    
    keys = d.keys()
    for k in keys:
        if trace: print "[%s]"%(k), "[%s]"%(d[k])
    if trace: print ""

    return d

# ------------------------------------------------------------------------------

opt_list = \
[
    ("debug",           None),
    ("test_run",        None),
    ("install",         None),
    ("create_iso",      None),
    ("media_path",      '=='),
    ("config_file",     '=='),
    ("svc_domain",      '=='),
    ("svc_account",     '=='),
    ("svc_password",    '=='), 
]

# ------------------------------------------------------------------------------

time_begin = time.time()

argv = get_params(opt_list)

test_run = 0
if argv.has_key('--test_run'):
    test_run = 1

option = None

if argv.has_key('--install'):
    option = 'install'

if argv.has_key('--create_iso'):
    option = 'create-iso'

if argv.has_key('--debug'):
    is_debug = 1
else:
    is_debug = 0

media_path  = argv['--media_path']
config_file = argv['--config_file']
py_code = "import %s as CONFIG_FILE"%(config_file[:-3])
exec (py_code)

if option == None:
    sys.exit(1)
    
# ---------------------------------------------------------------------------

def section(f=1,bold=0):
    if f: print ""
    if bold:
        print "# ========================================================================== #"
    else:
        print "# -------------------------------------------------------------------------- #"
    print ""

# ---------------------------------------------------------------------------

# INSTALL_SRC_PATH = 'x:\\MosaicReleases\\Global'
# INSTALL_SRC_PATH = 'd:'

INSTALL_SRC_PATH = media_path
LICENSE_FILE     = 'c:\\postilion.lic'

install_list = CONFIG_FILE.install_list

rc = 0
for b in install_list:
    if b.has_key('rsp_file'):
        s = b['rsp_file']
        if s:
            try:
                xml = XML.fromstring(s)
            except:
                rc = 1
                print "%s - response file is invalid."%(b['name'])
if rc:
    sys.exit(1)
    
# ---------------------------------------------------------------------------

error_list = []

# ---------------------------------------------------------------------------

def clean_temp():
    file_list = glob.glob('.\\temp\\*')
    for file in file_list:
        try:
            os.unlink(file)
        except:
            pass

# ---------------------------------------------------------------------------

def format_name(s):
    s = "-------- %s --------"%(s)
    while len(s) < 76:
        s = " %s "%(s)
    return s

# ---------------------------------------------------------------------------

def get_patch_nr(s):
    t = s.split("_")
    for e in t:
        if len(e) > len("patch"):
            if e[:len("patch")] == "patch":
                return int(e[-3:])
    return -1

# ---------------------------------------------------------------------------

def install(b, h_log, file_list):
    global test_run
    global error_list
    global is_debug
    computername = os.getenv("COMPUTERNAME")
    if not os.path.isfile(LICENSE_FILE):
        print ""
        print "Error - license file '%s' not found."%(LICENSE_FILE)
        print ""
        sys.exit(1)

    for file in file_list:
        clean_temp()
        
        #section(1,0)
        #
        #cmd = 'verify_hash.exe        ' + file
        #print '   ', cmd
        #os.system(cmd)
        #
        
        section(1,0)
        
        if file[-10:] == 'setupc.exe':
            s = file.replace('c.exe', '*.exe')
            cmd =  'xcopy.exe /Y "%s" .\\temp '%(s)
            print '   ', cmd
            os.system(cmd)
        else:
            if file[-4:] == '.zip':
                cmd = '7za.exe x -y -o.\\temp "' + file + '"'
            else:
                cmd = '7za.exe e -y -o.\\temp "' + file + '"'
            print '   ', cmd
            os.system(cmd)
     
        section(1,0)
    
        run_command = 1
        rc = 0
        if test_run:
            run_command = 0
        rsp_file = b['rsp_file']
        if b.has_key('cmd'):
            cmd = b['cmd']
            print '   ', cmd
            cwd = os.getcwd()
            if run_command:
                os.chdir('temp')
                rc = os.system(cmd)
                print "rc =", rc
                os.chdir(cwd)
        elif rsp_file:
            svc_account = argv['--svc_account']
            svc_password = argv['--svc_password']

            # If a domain account is not specified, use COMPUTERNAME\AccountName.
            # if svc_account.find('\\') < 0:
                # svc_account = computername + "\\" + svc_account
            
            rsp_file = rsp_file.replace('--svc-account--', svc_account)
            rsp_file = rsp_file.replace('--svc-password--', svc_password)
            rsp_file = rsp_file.replace('--postilion-dir--', postilion_dir)
            
            f = open('.\\temp\\rsp_file.xml', 'w+')
            f.write(rsp_file)
            f.close()
            
            cmd = '.\\temp\\setupc.exe -silent -responsefile ".\\temp\\rsp_file.xml" -logfile install.log'
            print '   ', cmd
            if run_command:
                rc = os.system(cmd)
                print "rc =", rc
        else:
            patch_nr = get_patch_nr(file)
            if b.has_key('patch_number_max'):
                max_patch_nr = b['patch_number_max']
            elif b.has_key('patch_number_list'):
                if patch_nr in b['patch_number_list']:
                    max_patch_nr = patch_nr
                else:
                    max_patch_nr = -1
            else:
                max_patch_nr = patch_nr
            if patch_nr <= max_patch_nr:
                print format_name(b['name'] + ", patch(%03d)"%(get_patch_nr(file)))
                print ""
                cmd = '.\\temp\\setupc.exe -silent'
                print '   ', cmd
                if run_command:
                    rc = os.system(cmd)
                    print "rc =", rc
            else:
                rc = -314159
        if rc == -314159:
            print ""
            #print "Skipped (%03d): The patch was not applied to the system."%(patch_nr)
            print "Skipped patch ...: The patch was not applied to the system."
            print ""
        elif rc <> 0:
            print ""
            print "Error: The install failed."
            print ""
            error_list.append(file)
            h_log.write("FAIL - %s\n"%(file))
            for fn in find.find('install.log'):
                h_log.write('>>>> - %s\n'%(fn))
                for line in open(fn, "r+").readlines():
                    h_log.write('>>>> -    ' + line)
                os.unlink(fn)
            h_log.flush()
            if is_debug:
                raw_input("Press enter to continue ...")
        else:
            print ""
            print "Success: The installation completed successfully."
            print ""
            h_log.write("DONE - %s\n"%(file))
            h_log.flush()
    
# ---------------------------------------------------------------------------

def create_iso(src_prefix, file_list):
    for file1 in file_list:
        if file1.find("setupc.exe") > -1:
            continue
        file2 = file1.replace(src_prefix, 'iso_image')
        if not os.path.isdir(os.path.dirname(file2)):
            cmd = 'xcopy.exe /I /T /E "%s" "%s"'%(os.path.dirname(file1) + '\\' + '*.*', os.path.dirname(file2))
            print cmd
            os.system(cmd)
        cmd = 'copy "%s" "%s"'%(file1, file2)
        print cmd
        os.system(cmd)
        
# ---------------------------------------------------------------------------

if option == "create-iso":
    if os.path.isdir('iso_image'):
        os.system("rd/q/s iso_image")
        os.system("md     iso_image")

# ---------------------------------------------------------------------------

h_log = open("postilion_install_log.txt", "w+")
for b in install_list:
    
    section(1,1)
    
    if b.has_key('install_src_path'):
        src_prefix = b['install_src_path']
    else:
        src_prefix = INSTALL_SRC_PATH

    t = src_prefix + '\\' + b['dir'] + '\\' + b['template']
    file_list = glob.glob(t)

    print format_name(b['name'])
    
    if option == "install":
        install(b, h_log, file_list)
        
    if option == "create-iso":
        print ""
        create_iso(src_prefix, file_list)
h_log.close()

section(1,1)

# ---------------------------------------------------------------------------

if option == "create-iso":
    x = time.localtime()
    cmd = 'g_mkisofs.exe -V PSTLN-%04d-%02d-%02d -R -iso-level 3 -joliet -o Postilion.iso iso_image'%(x.tm_year, x.tm_mon, x.tm_mday)
    print cmd
    os.system(cmd)
    os.system("rd/q/s iso_image")
    section(1,1)
    
# ---------------------------------------------------------------------------

if len(error_list) > 0:
    h = 1
    for file in error_list:
        if h:
            print ""
            print "The following files failed to install:"
            print ""
            h = 0
        print "   ", file
    section(1,1)

# ---------------------------------------------------------------------------

time_end = time.time()

print "Elapsed time =", U.get_elapsed_time(time_begin, time_end)

# ---------------------------------------------------------------------------

if len(error_list) > 0:
    sys.exit(1)
	
# ===========================================================================
