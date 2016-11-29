# ---------------------------------------------------------------------------

import os

PostilionDir = os.getenv("PostilionDir")

# ---------------------------------------------------------------------------

install_list = []

# ---------------------------------------------------------------------------

bundle_rtfw = { \
    'name'     : 'Realtime Framework v5.5',
    'dir'      : 'Global\\Postilion\\Realtime\\Framework\\v5.5',
    'template' : 'RealtimeFramework_se_*.exe',
    'rsp_file' : """
        <project>
                <property name="database.server.type" value="Local" />
                <property name="postilion.dir" value="--postilion-dir--" if="${is.clean}" />
                <property name="server.hostname" environment = "COMPUTERNAME" />               
                <property name="tranmgr.currency" value="840" />
                <property name="install.type" value="Principal Server" />
                <property name="license.file" value="C:\\postilion.lic" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
                <datasource
                        id="datasource.realtime"
                        type="sqlserver"
                        name="realtime"
                        server="${server.hostname}"
                        port="1433"
                        schema="dbo"
                        database="realtime"
                        description="Realtime Framework" />
                <database
                        id="database.realtime"
                        datadevicename="realtime_data"
                        datadevicefilename="C:\\realtime_data.mdf"
                        datadevicesize="1000"
                        datadevicefilegrowth="1000"
                        logdevicename="realtime_log"
                        logdevicefilename="C:\\realtime_log.ldf"
                        logdevicesize="1000"
                        logdevicefilegrowth="1000" />
        </project>    
"""  
}

# ---------------------------------------------------------------------------

bundle_rtfw_patches = { \
    'name'     :  'Realtime Framework v5.5 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Framework\\v5.5\\Patches',
    'template' :  'RealtimeFramework_v5.5_patch*.exe',
    'rsp_file' : None,
    #'patch_number_list': [1,2,3,4,5,6],
	#'patch_number_max':  64,
}

# ---------------------------------------------------------------------------

bundle_hsm_load_balancer = { \
    'name'     :  'HSM Load Balancer',
    'dir'      :  'realtime\\resources\\hsmservices',
    'template' :  'setupc.exe',
    'install_src_path' : PostilionDir,
    'rsp_file' : """
        <project>
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
                <property name="hsm.service.type" value="Thales RG7000 Load Balancer" />
                <property name="hsm.type" value="${hsm.lb.type}" />
                <property name="hsm.name" value="HSM Load Balancer" />
                <property name="hsm.address" value="${server.hostname}" />
                <property name="hsm.port" value="9990" />
                
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_ssf = { \
    
    'name'     :  'SSF_v5.2',
    'dir'      :  'Global\\Postilion\\Realtime\\Terminal Drivers\\SSF\\v5.2',
    'template' :  'SSF_v5.2_*.exe',
    'rsp_file' : """
        <project>
                <property name="install.type" value="Principal Server" />
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_ssf_patches = { \
    'name'     :  'SSF_v5.2 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Terminal Drivers\\SSF\\v5.2\\patches',
    'template' :  'SSF_v5.2_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_atmapp = { \
    
    'name'     :  'AtmApp_v5.5',
    'dir'      :  'Global\\Postilion\\Realtime\\Terminal Drivers\\AtmApp\\v5.5',
    'template' :  'AtmApp_v5.5_*.exe',
    'rsp_file' : """
        <project>
                <property name="install.type" value="Principal Server" />
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_atmapp_patches = { \
    'name'     :  'AtmApp_v5.5 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Terminal Drivers\\AtmApp\\v5.5\\patches',
    'template' :  'AtmApp_v5.5_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_posconnect = { \
    
    'name'     :  'PosConnect_v5.2',
    'dir'      :  'Global\\eSocket\\PosConnect\\v5.2',
    'template' :  'PosConnect_v5.2*.exe',
    'rsp_file' : """
        <project>
                <property name="install.type" value="Principal Server" />
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_posconnect_patches = { \
    'name'     :  'PosConnect_v5.2 (Patches)',
    'dir'      :  'Global\\eSocket\\PosConnect\\v5.2\\Patches',
    'template' :  'PosConnect_v5.2_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_nixbridge = { \
    
    'name'     :  'Nixbridge_v5.2',
    'dir'      :  'Global\\Postilion\\Realtime\\Host and Network Interfaces\\Nixbridge\\v5.2',
    'template' :  'Nixbridge_v5.2_*.exe',
    'rsp_file' : """
        <project>
                <property name="install.type" value="Principal Server" />
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_nixbridge_patches = { \
    'name'     :  'Nixbridge_v5.2 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Host and Network Interfaces\\Nixbridge\\v5.2\\Patches',
    'template' :  'Nixbridge_v5.2_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_postcard = { \
    'name'     : 'Postcard v5.5',
    'dir'      : 'Global\\Postilion\\Realtime\\Postcard\\v5.5',
    'template' : 'Postcard_se_*.exe',
    'rsp_file' : """
        <project>
                <property name="postilion.dir" value="--postilion-dir--" if="${is.clean}" />
                <property name="server.hostname" environment = "COMPUTERNAME" />               
                <property name="tranmgr.currency" value="840" />
                <property name="install.type" value="Principal Server" />
                <property name="license.file" value="C:\\postilion.lic" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
                <datasource
                        id="datasource.postcard"
                        type="sqlserver"
                        name="postcard"
                        server="${server.hostname}"
                        port="1433"
                        schema="dbo"
                        database="postcard"
                        description="Postcard" />
                <database
                        id="database.postcard"
                        datadevicename="postcard_data"
                        datadevicefilename="C:\\postcard_data.mdf"
                        datadevicesize="1000"
                        datadevicefilegrowth="1000"
                        logdevicename="postcard_log"
                        logdevicefilename="C:\\postcard_log.ldf"
                        logdevicesize="1000"
                        logdevicefilegrowth="1000" />
        </project>    
"""
   
}

# ---------------------------------------------------------------------------

bundle_postcard_patches = { \
    'name'     :  'Postcard_v5.5 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Postcard\\v5.5\\Patches',
    'template' :  'Postcard_v5.5_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_postbridge = { \
    
    'name'     :  'Postbridge_v8.2',
    'dir'      :  'Global\\Postilion\\Realtime\\Host and Network Interfaces\\Postbridge\\v8.2',
    'template' :  'Postbridge_v8.2_*.exe',
    'rsp_file' : """
        <project>
                <property name="install.type" value="Principal Server" />
                <property name="server.hostname" environment = "COMPUTERNAME" />
                <serviceaccount
                        id="service.account"
                        username="--svc-account--"
                        password="--svc-password--" />
        </project>
"""    
}

# ---------------------------------------------------------------------------

bundle_postbridge_patches = { \
    'name'     :  'Postbridge_v8.2 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Host and Network Interfaces\\Postbridge\\v8.2\\Patches',
    'template' :  'Postbridge_v8.2_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_portal = { \
    'name'     : 'PortalFramework_1.4',
    'dir'      : 'Global\\Postilion\\Realtime\\Portal\\Framework\\v1.4',
    'template' : 'PortalFramework_v1.4_*.exe',
    'rsp_file' : """
        <project>
                <property name="destination.dir" value="${postilion.dir}\portalframework" />
				<property name="server.hostname" value="COMPUTERNAME" />
				<property name="install.type" value="Principal Server" />
				<property name="license.file" value="C:\\postilion.lic" />
				<property name="application.server.type" value="Tomcat" />
				<property name="tomcat.location" value="c:\\apache-tomcat" />

				<serviceaccount
					id="service.account"
					username="--svc-account--"
					password="--svc-password--" />
				</project>    
"""   
}

# ---------------------------------------------------------------------------

bundle_portal_patches = { \
    'name'     :  'PortalFramework_1.4 (Patches)',
    'dir'      :  'Global\\Postilion\\Realtime\\Portal\\Framework\\v1.4\\Patches',
    'template' :  'PortalFramework_v1.4_patch*.exe',
    'rsp_file' : None
}

# ---------------------------------------------------------------------------

bundle_java = { \
    
    'name'     :  'Postilion JRE Installer v1.8.112',
    'dir'      :  'Global\\Postilion\\Realtime\\Other\\JRE Installer\\v1.8.112',
    'template' :  'jre_installer_*.zip',
    'rsp_file' :   None,
    'cmd'      :  'jre_installer_silent.cmd'
}

# ---------------------------------------------------------------------------

install_list.append(bundle_rtfw)
install_list.append(bundle_rtfw_patches)
install_list.append(bundle_hsm_load_balancer)
#install_list.append(bundle_postcard)
#install_list.append(bundle_postcard_patches)
install_list.append(bundle_ssf)
install_list.append(bundle_ssf_patches)
install_list.append(bundle_atmapp)
install_list.append(bundle_atmapp_patches)
#install_list.append(bundle_posconnect)
#install_list.append(bundle_posconnect_patches)
#install_list.append(bundle_nixbridge)
#install_list.append(bundle_nixbridge_patches)
#install_list.append(bundle_postbridge)
#install_list.append(bundle_postbridge_patches)
#install_list.append(bundle_portal)
#install_list.append(bundle_portal_patches)
install_list.append(bundle_java)

# ---------------------------------------------------------------------------