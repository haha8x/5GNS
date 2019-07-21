# openstack-network-slicing

## Labs, Workshops, and Documentation

* [lab0](/lab0/README.md) - Deploy DevStack and a Juniper router and setup a BGP session between them forked from idx-labs/openstack-network-slicing

## Links

* [Next Generation Mobile Networks Technical Documents](https://www.ngmn.org/publications/technical-deliverables.html)
* [NGMN - Network Slicing](https://www.ngmn.org/fileadmin/user_upload/160113_Network_Slicing_v1_0.pdf)

# Requirement
- Openstack AIO or Cluster installed with OpenVSwitch

# setup Openstack and Open Day Light using devstack
# System requirements
- Virtual machine on a real ESXi/KVM/Xen/etc. hypervisor, or a bare metal server with virtualization support
- 8 GB of RAM (minimum)
- 4 cores of CPU (minimum)
- 100 GB of hard disk space (minimum)
- An updated Ubuntu 16.04 LTS Desktop
- Static IP

# Update and install dependencies
First, you must update Ubuntu
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```
Once those commands have completed, you'll need to install git.

```
sudo apt-get install git
```
## Installing Oracle JDK
```
sudo apt-get install openjdk-8-jdk
```
<!-- In this section, you will need sudo privileges
```
sudo su
```
The /opt directory is reserved for all the software and add-on packages that are not part of the default installation. Create a directory for your JDK installation:
```
mkdir /opt/jdk
apt-get install libc6-i386
```
Download and and extract java into the /opt/jdk directory:
```
cd /opt/jdk
wget http://ftp.osuosl.org/pub/funtoo/distfiles/oracle-java/jdk-7u80-linux-i586.tar.gz
tar -zxf jdk-7u80-linux-i586.tar.gz -C /opt/jdk
```
Verify that the file has been extracted into the /opt/jdk directory.
```
ls /opt/jdk
```
## Setting Oracle JDK as the default JVM
In our case, the java executable is located under /opt/jdk/jdk1.8.0_05/bin/java . To set it as the default JVM in your machine run:
```
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.7.0_80/bin/java 100
update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.7.0_80/bin/javac 100
```
## Verify your installation
Verify that java has been successfully configured by running:
```
update-alternatives --display java
update-alternatives --display javac
```
The output should look like this:
```
java - auto mode
link currently points to /opt/jdk/jdk1.7.0_80/bin/java
/opt/jdk/jdk1.7.0_80/bin/java - priority 100
Current 'best' version is '/opt/jdk/jdk1.7.0_80/bin/java'.

javac - auto mode
link currently points to /opt/jdk/jdk1.7.0_80/bin/javac
/opt/jdk/jdk1.7.0_80/bin/javac - priority 100
Current 'best' version is '/opt/jdk/jdk1.7.0_80/bin/javac'.
```
Another easy way to check your installation is:
```
java -version
```
The output should look like this:
```
java version "1.8.0_05"
Java(TM) SE Runtime Environment (build 1.8.0_05-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.5-b02, mixed mode)
```     -->
# Clone devstack
We're going to use git to clone devstack. To do this, go back to your terminal window and issue the following two commands:

```
cd /
sudo git clone https://git.openstack.org/openstack-dev/devstack -b stable/stein
```
Next, we have to create local config file. In this repo, I have included `local.conf` for serveral case, but the case we are going to use is `allinone` `multi-node`. Select local.conf file in `compute` or `control` folder and paste it to `local.conf` file in ubuntu server

```
cd devstack
sudo nano local.conf
```
Next we'll run a script to create a new user for OpenStack, then make that new user the owner of the devstack folder.
```
sudo /devstack/tools/create-stack-user.sh
sudo chown -R stack:stack /devstack
```
For the error `can not determine HOST_IP` we need to open `stackrc` in devstack folder go to line 749 and enter the HOST_IP manually
Now we need to execute the following command to begin the installation openstack. This will take several minutes to complete.
```
sudo su stack
/devstack/stack.sh
```
Drink a cup of tea and wait then you will have the OpenStack and OpenDayLight installed on your machine. The Compute node just need to repeat the same

# Install OSM Release SIX

## Requirement

MINIMUM: 2 CPUs, 4 GB RAM, 20GB disk and a single interface with Internet access
RECOMMENDED: 2 CPUs, 8 GB RAM, 40GB disk and a single interface with Internet access
Base image: Ubuntu16.04 (64-bit variant required)
```
wget https://osm-download.etsi.org/ftp/osm-6.0-six/install_osm.sh
chmod +x install_osm.sh
./install_osm.sh --elk_stack --pm_stack --vimemu
```
You will be asked if you want to proceed with the installation and configuration of LXD, juju, docker CE and the initialization of a local docker swarm, as pre-requirements. Please answer "y".

Then, some dialog messages related to LXD configuration will be shown. This is what you have to answer:
```
Do you want to configure the LXD bridge? Yes
Do you want to setup an IPv4 subnet? Yes
<< Default values apply for next questions >>
Do you want to setup an IPv6 subnet? No
```

# Install OpenVIM
## Requirement
1 vCPU (2 recommended)
4 GB RAM (4 GB are required to run OpenDaylight controller; if the ODL controller runs outside the VM, 2 GB RAM are enough)
40 GB disk
3 network interfaces to:
OSM network (to interact with RO)
DC intfrastructure network (to interact with the compute servers and switches)
Telco/VNF management network (to provide IP addresses via DHCP to the VNFs)
Base image: ubuntu-16.04-server-amd64

## Installation
```
wget -O install-openvim.sh "https://osm.etsi.org/gitweb/?p=osm/openvim.git;a=blob_plain;f=scripts/install-openvim.sh;hb=1ff6c02ecff38378a4d7366e223cefd30670602e"
chmod +x install-openvim.sh
sudo ./install-openvim.sh -q   # --help  for help on options
# NOTE: you can provide optionally the admin user (normally 'root') and password of the database.
```
Once installed, manage it with sudo service osm-openvim start|stop|restart
Logs are at /var/log/osm/openvim.log
Configuration file is at /etc/osm/openvimd.cfg
Thre is a CLI client called openvim. Type "openvim config" to see the configuration bash variables

## Openflow controller
For normal or OF only openvim modes you will need a openflow controller. The following openflow controllers are supported:
Floodlight version 0.90
```
git clone https://github.com/nfvlabs/openvim.git
sudo openvim/scripts/install-floodlight.sh
service-floodlight start
```


# Troubleshoot

## Tenant not allow to net-create with provider:physical_network
Default policy for Neutron only allows admin to create networks with provider tag. You can edit /etc/neutron/policy.json to allow none admin users to create networks with provider tags.
```
sudo nano /etc/neutron/policy.json
"create_network:provider:physical_network": "rule:admin_only"
```

## openstack network create: bad request (HTTP 400)
```
openstack network create mgmt --provider-network-type vlan --provider-physical-network physnet_em1 --provider-segment 500 --share
```
modified /opt/stack/neutron/etc/oslo-config-generator/openvswitch_agent.ini:
```
[ovs]
bridge_mappings = physnet:br-ex
```
modified /etc/neutron/plugins/ml2/ml2_conf.ini:
```
[ml2_type_vlan]
network_vlan_ranges = physnet
```
Then I rebooted the VM, ran source admin_openrc.sh (file downloaded from the Horizon UI where I logged in as admin) and the command for creating the network worked.

## Got "/opt/stack/requirements/.venv/bin/pip’: No such file or directory" error installing devstack
```
virtualenv /opt/stack/requirements/.venv/
```

## /opt/stack/ permission
```
sudo chown -R stack:stack /opt/stack
```

## Clean devstack
```
cd devstack
./unstack.sh
./clean.sh
cd ..
rm -rf devstack
sudo rm -rf /opt/stack
```
