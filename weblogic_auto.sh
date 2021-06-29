#export ORACLE_HOME=/scratch/oipa/Oracle/Middleware/Oracle_Home
cd /scratch/oipa/Oracle/Middleware/Oracle_Home/wlserver/common/bin/ 
./scratch/oipa/Oracle/Middleware/Oracle_Home/wlserver/server/bin/setWLSEnv.sh
echo "Deployment is starting..."
./wlst.sh /scratch/oipa/Scripts/dep_new.py $serverUserName $adminPassword $HostName $DeploymentApp $WARFileLoc $Target
echo "Deployment is done..."
