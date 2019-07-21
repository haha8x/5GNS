# openstack-network-slicing

## Labs, Workshops, and Documentation

* [lab0](/lab0/README.md) - Deploy DevStack and a Juniper router and setup a BGP session between them

## Links

* [Next Generation Mobile Networks Technical Documents](https://www.ngmn.org/publications/technical-deliverables.html)
* [NGMN - Network Slicing](https://www.ngmn.org/fileadmin/user_upload/160113_Network_Slicing_v1_0.pdf)


# Guide how to setup Openstack Ocata and Open Day Light using devstack
# System requirements
- Virtual machine on a real ESXi/KVM/Xen/etc. hypervisor, or a bare metal server with virtualization support
- 8 GB of RAM (minimum)
- 4 cores of CPU (minimum)
- 100 GB of hard disk space (minimum)
- An updated Ubuntu 16.04 LTS server
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
Next we need to install java 7 manualy
## Installing Oracle JDK
In this section, you will need sudo privileges
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
```    
# Clone devstack
We're going to use git to clone devstack. To do this, go back to your terminal window and issue the following two commands:

```
cd /
sudo git clone https://git.openstack.org/openstack-dev/devstack -b stable/ocata
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
