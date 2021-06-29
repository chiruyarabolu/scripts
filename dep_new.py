
###############################################
# Undeploy and Deploy applications
###############################################
import sys
import time as systime

username = sys.argv[1]
password = sys.argv[2]
URL = sys.argv[3]
dep_app = sys.argv[4]
dep_app_file = sys.argv[5] + "/" + dep_app + ".war"
deploymentTarget = sys.argv[6]

# Connect WLST to Adminserver
connect(""+username+"", ""+password+"", "t3://"+URL+":7001")

edit()
startEdit()

#Undeploy
undeploy(dep_app)

#Save & Activate
save()
activate()

edit()
startEdit()

#Deploy
deploy(""+dep_app+"",""+dep_app_file+"",targets=""+deploymentTarget+"")

#Save & Activate
save()
activate()

# Disconnect WLST
disconnect()

# Exit WLST
exit()
