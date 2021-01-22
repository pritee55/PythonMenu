import os
import getpass



os.system("tput setaf 3")
print("""
\n\tARTH2020.2.20 Group 4
\n\tTEAM MEMBERS
\t1.Pritee Dharme
\t2.Suyog Shinde
\t3.Shrikant Luharia
\t4.Suraj Kumar
""")


os.system("tput setaf 5")
print("\n\t\t\tWelcome to my Automation menu!!")
os.system("tput setaf 7")
print("\n\t\t\t---------------------------")

passwd = getpass.getpass("Enter your password : ")

if passwd != "root":
   print("\n\tInvalid Password...")
   exit()

def task():
    print("""
\n
           Press 1 : To launch the Hadoop menu
           Press 2 : To launch the AWS menu
           Press 3 : To launch the Partition menu
           Press 4 : To launch the docker menu
           press 5 : To Launch the webserver
           Press 6 : Exit..
""")

    kite = int(input("\n\tEnter the option :"))


    if kite == 1:
        def hadoop():
            print("""
            \n
                            Welcome to hadoop menu
                            ----------------------
    
                    Press 1 to get into master menu
                    Press 2 to get into slave menu
                    Press 3 to get into client menu
                    Press 4 Exit..
        """)
            opt = int(input("\n\tEnter the option :"))

            if opt == 1:
                print("""
            \tPress 1 : To configure the master
            \tPress 2 : To start the master
            \tPress 3 : To stop master
            \tPress 4 : To check the proceses running 
            \tPress 5 : To check report 
            \tPress 6 : Exit    
                """)

                hopt = int(input("\n\tInput the option:"))
                if hopt == 1:
                    direc = input("\n\tEnter the directory name for master:")
                    os.system("mkdir {}".format(direc))
                    ipp = input("\n\tEnter the Master ip:")
                    os.system('cd /etc/hadoop')
                    cc = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(ipp)
                    text_file = open("/etc/hadoop/core-site.xml", 'w')
                    n = text_file.write(cc)
                    text_file.close()
                    dd ="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>s
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>
            """.format(direc)
                    hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
                    m = hdf_file.write(dd)
                    hdf_file.close()
                    os.system("hadoop namenode -format -Y")
                    print("Successfully configured the name node")
                elif hopt == 2:
                    os.system("cd /etc/hadoop")
                    os.system("hadoop-daemon.sh start namenode")
                    print("Successfully started the name node")
                elif hopt == 3:
                    os.system("cd /etc/hadoop")
                    os.system("hadoop-daemon.sh stop namenode")
                    print("Successfully stoped the name node")

                elif hopt == 4:
                    os.system("jps")
                elif hopt == 5:
                    os.system("hadoop dfsadmin --report")
                elif hopt == 6:
                    os.system("exit")
                else:
                    print("invalid option...")
                hadoop()
            elif opt == 2:
                print("""
                 \tPress 1 : To configure the datanode  
                 \tPress 2 : To start the slave
                 \tPress 3 : To stop slave
                 \tPress 4 : To check the proceses running
                 \tPress 5 : To check report 
                 \tPress 6 : Exit 
                """)
                hopt = int(input("\n\tInput the option.. "))
                if hopt == 1:
                    direc = input("\n\tEnter the directory name for slave:")
                    os.system("mkdir {}".format(direc))
                    ipp = input("\n\tEnter the Master ip:")
                    os.system('cd /etc/hadoop')
                    cc = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(ipp)
                    text_file = open("/etc/hadoop/core-site.xml", 'w')
                    n = text_file.write(cc)
                    text_file.close()
                    dd = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>
            """.format(direc)
                    hdf_file = open("/etc/hadoop/hdfs-site.xml", 'w')
                    m = hdf_file.write(dd)
                    hdf_file.close()
                    print("Successfully configured the data node")

                elif hopt == 2:
                    os.system("cd /etc/hadoop")
                    os.system("hadoop-daemon.sh start datanode")
                    print("Successfully started the data node")

                elif hopt == 3:
                    os.system("cd /etc/hadoop")
                    os.system("hadoop-daemon.sh stop datanode")
                    print("Successfully stoped the data node")

                elif hopt == 4:
                    os.system("jps")
                elif hopt == 5:
                    os.system("hadoop dfsadmin -report")
                elif hopt == 6:
                    os.system("exit")
                else:
                    print("\n\tinvalid option...")
                hadoop()

            elif opt == 3:
                print("""
                 \tPress 1 : To configure the client
                 \tPress 2 : To upload a file
                 \tPress 3 : To remove a file
                 \tPress 4 : To read a file
                 \tPress 5 : To list the files
                 \tPress 6 : To upload a file with default block size
                 \tPress 7 : Exit..")
                """)
                cip = int(input("\n\tInput the option:"))
                if cip == 1:
                    mip = input("\n\tEnter the master ip")
                    cc = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
        
<!-- Put site-specific property overrides in this file. -->
        
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>'''.format(mip)
                    text_file = open("/etc/hadoop/core-site.xml", 'w')
                    n = text_file.write(cc)
                    text_file.close()
                    print("Successfully configured the Client")

                elif cip == 2:
                    filep = input("\n\tEnter the full file path")
                    os.system("hadoop fs -put {} /".format(filep))
                    print("File Uploded successfully")

                elif cip == 3:
                    filep = input("\n\tEnter the full file name you want to remove :")
                    os.system("hadoop fs -rm /{}".format(filep))
                    print("File removed successfully")

                elif cip == 4:
                    filep = input("\n\tEnter the full file name you want to read :")
                    os.system("hadoop fs -cat /{}".format(filep))
                elif cip == 5:
                    os.system("hadoop fs ls /")
                elif cip == 6:
                    bs = int(input("Enter the Block size"))
                    filep = input("Enter the full file path")
                    os.system("hadoop fs -Ddfs.block.size={}M -put {} /".format(bs,filep))
                elif cip == 7:
                    os.system("exit")
                else:
                    print("\n\tInvalid option...")
            elif opt == 4:
                os.system("exit")

            else:
                print("\n\tinvalid option")
                hadoop()
            task()
        hadoop()
    elif kite == 2:
        def aws():
            print("""\n
    \tPress 1 : To launch the EC-2 menu
    \tPress 2 : To launch the S3 menu
    \tPress 3 : To launch the IAM menu
    \tPress 4 : To launch the CLOUDFRONT menu
    \tPress 5 : To configure the AWS CLI
    \tPress 6 : Exit..
    """)

            menu = int(input("\n\tEnter the option.. "))
            if menu == 1:
                print("""
    \n
    \tPress 1 : To launch the instances menu 
    \tPress 2 : To launch the volume menu
    \tPress 3 : To launch the Security group menu 
    \tPress 4 : To launch the Key pair menu 
    \tPress 5 : To launch the snapshot menu
    \tPress 6 : Exit..
    """)
                ola = int(input("\n\tEnter the option :"))
                if ola == 1:
                    print("""
                    \t Welcome to the instances menu 
                    \t 1.To describe instances press 1
                    \t 2.To Describe the instances type press 2
                    \t 3.To Run a new instance press 4
                    \t 4.To start a instance press 5
                    \t 5.To stop the instance press 6
                    \t 6.To reboot a instance press 6
                    \t 7.To terminate a instance press 7
                    \t 8. exit press 8")
                    
                    """)
                    im = int(input("\n\tInput the option:"))
                    if im == 1:
                        os.system("aws ec2 describe-instances")
                    elif im == 2:
                        os.system("aws ec2 describe-instances-types")
                    elif im == 3:
                        imageid = input("\n\tEnter the image id :")
                        inty = input("\n\tenter the instance type :")
                        subnetid = input("\n\tenter the subnet id :")
                        security = input("\n\tenter the security group id :")
                        keyname = input("\n\tenter the key name :")
                        os.system("aws ec2 run-instance --image-id {} --instance-type {} --count 1 --subnet-id {} --key-name {}".format(imageid,inty,subnetid,security,keyname,))
                    elif im == 4:
                        instanceid = input("\n\tEnter thr instance id")
                        os.system("aws ec2 start-instances --instance-ids {}".format(instanceid))
                    elif im == 5:
                        instanceid = input("\n\tEnter thr instance id")
                        os.system("aws ec2 stop-instances --instance-ids {}".format(instanceid))
                    elif im == 6:
                        instanceid = input("\n\tEnter thr instance id")
                        os.system("aws ec2 reboot-instances --instance-ids {}".format(instanceid))
                    elif im == 7:
                        instanceid = input("\n\tEnter thr instance id")
                        os.system("aws ec2 terminate-instances --instance-ids {}".format(instanceid))
                    elif im == 8:
                        os.system("exit")
                    else:
                        print("Choose the correct option")
                elif ola == 2:
                    print("""
                     \t 1.To create Volume press 1
                     \t 2.To delete Volume press 2
                     \t 3.To Modify Volume press 3
                     \t 4. To Attach Volume press 4
                     \t 5.To detach Volume press 5
                     \t 6. To Exit press 6
                    """)
                    im = int(input("\n\tEnter the option:"))
                    if im == 1:
                        vtype = input("\n\tEnter the Volume type:")
                        size = input("\n\tEnter the size of volume: ")
                        az = input("\n\tEnter the avaibility zone:")
                        os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(vtype,size,az))
                        print("Successfully created a volume")
                    elif im == 2:
                        vid = input("\n\tEnter the Volume ID:")
                        os.system("aws ec2 delete-volume --volume-id {}".format(vid))
                        print("Successfully deleted a volume")
                    elif im == 3:
                        vid =input("\n\tEnter the volume ID:")
                        size =int(input("\n\tEnter the size you want to change:"))
                        os.system("aws ec2 modify-volume --volume-id {} --size {}".format(vid,size))
                        print("Successfully increased the volume size")
                    elif im == 4:
                        device = input("\n\tEnter the device e.g /dev/shd:")
                        iid = input("\n\tEnter the instance id:")
                        vid = input("\n\tEnter the Volume id:")
                        os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(device,iid,vid))
                        print("Successfully decreased the volume size")
                    elif im == 5:
                        device = input("\n\tEnter the device e.g /dev/shd:")
                        iid = input("\n\tEnter the instance id:")
                        vid = input("\n\tEnter the Volume id:")
                        os.system("aws ec2 detach-volume --device {} --instance-id {} --volume-id {}".format(device,iid,vid))
                    elif im == 6:
                        os.system("exit")
                    else:
                        print("\n\tChoose the correct option:")
                elif ola == 3:
                    print("""
                    \t 1. To Describe security groups press 1
                    \t 2. To create a security group press 2
                    \t 3.To delete a security group press 3 
                    \t 4. Exit press 4
                    """)
                    se =int(input("\n\tInput the option:"))
                    if se == 1:
                        gn = input("\n\tEnter the groups names:")
                        os.system("aws ec2 describe-security-groups --group-names {}".format(   gn))
                    elif se == 2:
                        gn = input("\n\tEnter the group name:")
                        des = input("\n\tEnter the description")
                        os.system("aws ec2 create-security-group --group-name {} --description' {}' ".format(gn,des))
                    elif se ==3:
                        gn = input("\n\tEnter the group name:")
                        os.system("aws ec2 delete-security-group --group-name {}".format(gn))
                    elif se == 4:
                        os.system("exit")
                    else:
                        print("choose the correct option:")
                elif ola == 4:
                    print("""
                    \t 1.To describe key pairs press 1
                    \t 2.To create a new key pair press 1
                    \t 3.To Delete a key pair press 3
                    \t 4. To Exit press 4 
                    """)
                    keyy = int(input("\n\tInput the option:"))
                    if keyy == 1:
                        kn = input("\n\tEnter the key pair name:")
                        os.system("aws ec2 descibe-key-pairs --key-name {}".format(kn))
                    elif keyy == 2:
                        kn = input("\n\tEnter the key name:")
                        qe =input("\n\tEnter the query:")
                        os.system("aws ec2 create-key-pairs --key-name {} --query '{}' --output text > {}.pem".format(kn,qe,kn))
                    elif keyy == 3:
                        kn = input("\n\tEnter the key pair name:")
                        os.system("aws ec2 delete-key-pairs --key-name {}".format(kn))
                    elif keyy == 4:
                        os.system("exit")
                elif ola ==5:
                    print("""
                    \t 1.To describe snapshots press 1
                    \t 2.To create snapshots press 2
                    \t 3.To delete snapshots press 3
                    \t 4.To Exit
                    """)
                    snap = int(input("\n\tinput the option:"))
                    if snap == 1:
                        sid = input("\n\tEnter yours snapshot id:")
                        os.system("aws ec2 describe-snapshots --snapshot-ids {}".format(sid))
                    elif snap == 2:
                        vid =input("\n\tEnter the volume id:")
                        des = input("\n\tEnter the description for snapshot:")
                        os.system("aws ec2 create-snapshot --volume-id {} --description '{}'".format(vid,des))
                    elif snap == 3:
                        sid = input("\n\tEnter yours snapshot id:")
                        os.system("aws ec2 delete-snapshot --snapshot-id {}".format(sid))
                    elif snap == 4:
                        os.system("exit")
                    else:
                        print("\n\tchoose the correct option:")
                elif ola == 6:
                    os.system("exit")
                else:
                    print("Choose the correct option:")
                aws()
#S3 menu starts
            elif menu ==2:
                def option():
                    op = int(input('''
                    \n
                    ..............#WELCOME IN MAIN MENU#................
                
                    \n
                    Press 1 : To Create a S3 Bucket..
                    press 2 : To List all S3 Bucket..
                    Press 3 : To Create Bucket policies..
                    Press 4 : To Delete the Bucket..
                    Press 5 : To Delete Bucket Policies..
                    press 6 : exit..
                    \n
                    what can I help you..: '''))

                    if op == 1:
                        name1 = input("\n\tEnter your Bucket that you want..>> ")
                        name2 = input("\n\tEnter your AWS Region ..>> ")
                        os.system(
                            "aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(
                                name1, name2, name2))
                        print("\n....>>>Your Bucket is Successfully Created<<<....")
                        option()
                    elif op == 2:
                        os.system('aws s3api list-buckets --query "Bucket[].Name"')
                        print("\n....>>> Your All Buckets <<<....")
                        option()
                    elif op == 3:
                        print("\n\t Press 1 : To create bucket public..\n\t Press 2 : To make Image Public \n")
                        pr = int(input("Enter your choice..>> "))
                        if pr == 1:
                            name1 = input("\n\t Enter the name of Bucket..>> ")
                            os.system("aws s3api put-bucket-ac1 --public-read --bucket {}".format(name1))
                            print("\n....>>>Your Bucket is Now Public<<<....")
                        elif pr == 2:
                            name1 = input("\n\t Enter the name of bucket..>> ")
                            name2 = input("\n\t Enter your image name..>> ")
                            os.system(
                                "aws s3api put-object-ac1 --bucket {} --key {}.jpg --grant-read uri=http://acs.amazonaws.com/groups/global/AllUsers".format(
                                    name1, name2))
                            print("\n....>>>Your Image is now Public<<<....")

                        option()

                    elif op == 4:
                        name1 = input("\n\t Enter the name of bucket..>> ")
                        name2 = input("\n\t Enter the Region name..>> ")
                        os.system("aws s3api delete-bucket --bucket {} --region {}".format(name1, name2))
                        print("\n....>>> Your Bucket is Successfully Deleted <<<....")
                        option()
                    elif op == 5:
                        name1 = input("\n\t Enter the name of Bucket..>> ")
                        os.system("aws s3api delete-bucket-policy --bucket {}".format(name1))
                        print("\n....>>>Your Bucket Policies Successfully Deleted<<<....")
                        option()
                    elif op == 6:
                        os.system("exit")
                        os.system("tput setaf 3")
                        print("\n\n\t#########..THANK YOU..See you soon..#########")
                        os.system("tput setaf 7")
                        print("\n")

                    else:
                        print("Incorrect Choice,select correct option..")
                        anykey = input("\n\t Press Enter to go main menu")
                        option()
                option()
                aws()
            elif menu ==3:
                def option():
                    op = int(input('''
                      \n
                      ..............#WELCOME IN MAIN MENU#................
                
                      \n
                      Press 1 : To Create a IAM Group..
                      press 2 : To Create a IAM User..
                      Press 3 : To Add IAM User in IAM Group..
                      Press 4 : To Attach IAM managed policy to IAM User..
                      Press 5 : To Set Password to IAM User..
                      Press 6 : To Create Access and Public Key..
                      press 7 : exit..
                      \n
                      what can I help you..: '''))

                    if op == 1:
                        name1 = input("\n\tEnter Group name that you want..>> ")
                        os.system("aws iam create-group --group-name {}".format(name1))
                        print("\n\t....>>>Your IAM Group is Successfully Created<<<....")
                        option()
                    elif op == 2:
                        name2 = input("\n\tEnter User name that you want..>>")
                        os.system("aws iam create-user --user-name {}".format(name2))
                        print("\n\t....>>> Your IAM User is Successfully Created <<<....")
                        option()
                    elif op == 3:
                        name2 = input("\n\t Enter the name of IAM User..>> ")
                        name1 = input("\n\t Enter the name of IAM Group..>>")
                        os.system("aws iam add-user-to-group --user-name {} --group-name {}".format(name2, name1))
                        os.system("aws iam get-group --group-name {}".format(name1))
                        print("\n\t....>>>Your IAM User is Added in IAM Group Successfully <<<...")
                        option()

                    elif op == 4:
                        name2 = input("\n\t Enter the name of IAM User..>> ")
                        os.system("aws iam attach-user-policy --user-name {} --policy=arn:aws:iam::aws:policy/PowerUserAccess")
                        os.system("aws iam list-attached-user-policies --user-name {}".format(name2))
                        print("\n\t....>>> Your IAM Policy is Successfully Attached <<<....")
                        option()

                    elif op == 5:
                        name2 = input("\n\t Enter the name of IAM User..>> ")
                        name3 = input("\n\t Enter the Password that you want to give..>> ")
                        os.system(
                            "aws iam create-login-profile --user-name {} --password {} --password-reset-required".format(name2, name3))
                        print("\n\t....>>>Your Password is Successfully Set <<<....")
                        option()
                    elif op == 6:
                        name2 = input("\n\t Enter the name of IAM User..>> ")
                        os.system("aws iam create-access-key --user-name {}".format(name2))
                        print("\n\t ....>>> Your Key is Generated Successfully <<<....")
                        option()
                    elif op == 7:
                        os.system("exit")
                        os.system("tput setaf 3")
                        print("\n\n\t#########..THANK YOU..#########")
                        os.system("tput setaf 7")
                        print("\n")

                    else:
                        print("Incorrect Choice,select correct option..")
                        anykey = input("\n\t Press Enter to go main menu")
                        option()
            
                option()
                aws()
            elif menu == 4:
                print("""
                \n\t
                           To lauch the cloud front menu press 1
                
                """)
                op = int(input("\n\tEnter the option:"))

                if op == 1:
                    print("""
                    \t 1.To create distribution press 1
                    \t 2.To delete distribution press 2
                    \t 3.To list the distribution press 3
                    \t 4. to Exit press 4
                    """)
                    opt =int(input("\n\tInput the option:"))
                    if opt == 1:
                        odn = input("\n\tEnter the origin domain name:")
                        dro = input("\n\tEnter the default root object:")
                        os.system("aws cloudfront create-distribution --origin-domain-name {} --default-root-object {}".format(odn,dro))
                    elif opt == 2:
                        cid = input("\n\tEnter the distribution id:")
                        etag = input("\n\tEnter the distribution etag:")
                        os.system("aws cloudfront delete-distribution --id {} --if-match {}".format(cid,etag))
                    elif opt == 3:
                        os.system("aws cloudfront list-distributions: ")
                    elif opt == 4:
                        os.system("exit")
                    else:
                        print("Choose the correct option: ")
                else:
                    print("Invalid option...")
            elif menu == 5:
                os.system('\ncurl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"')
                os.system(" unzip awscliv2.zip ")
                os.system(" sudo ./aws/install ")
                os.system("\n sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")
                os.system("\n aws --version")
                os.system("\n aws configure")
                print("\n\t.....you configure successfully.....")

            elif menu == 6:
                os.system("exit")
            else:
                print("Invalid option...")
                aws()
        #task()
        aws()
        task()
    elif kite == 3:
        def par():
            print("""\n
        \tPress 1.To Enter the static partition menu
        \tPress 2.To Enter the LVM partition menu
        \tPress 3.Exit
        """)
            part = int(input("\n\tEnter the option.. "))
            if part ==1:
                def option():
                    op = int(input('''
                      \n
                      
        \tPress 1 : To Create a Static Partition..
        \tPress 2 : Format and mount partition..
        \tPress 3 : To increase size of Partition..
        \tPress 4 : To decrease size of partition..
        \tPress 5 : To delete the static partiton..
        \tpress 6 : exit..
                      \n
        what can I help you..: '''))

                    if op == 1:
                        os.system("\n yum install parted")
                        name1 = input("\n\tEnter your harddisk that you want..>> ")
                        part1 = input("\n\tEnter start point of partition..>> ")
                        part2 = input("\n\tEnter end point of partition..>> ")
                        os.system("parted {} mkpart primary ext4 {}G {}G;".format(name1, part1, part2))
                        os.system("lsblk")
                        option()
                    elif op == 2:
                        name3 = input("\n\t Enter the name of partition..>> ")
                        os.system("mkfs.ext4 {}".format(name3))
                        name4 = input("\n\t Enter the folder name that you want..>>")
                        os.system("mkdir \{}".format(name4))
                        os.system("mount {} {}".format(name3,name4))
                        os.system("lsblk")

                    elif op == 3:
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        size1 = input("\n\t Enter the incresing end point size..>> ")
                        os.system("parted {} resizepart {} {}G".format(name1, num1, size1))
                        os.system("lsblk")
                        option()
                    elif op == 4:
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        size2 = input("\n\t Enter the decreasing end point size..>> ")
                        os.system("parted {} resizepart {} {}G".format(name1, num1, size2))
                        os.system("lsblk")
                        option()
                    elif op == 5:
                        name1 = input("\n\t Enter the name of harddisk..>> ")
                        num1 = input("\n\t Enter the number of partition..>> ")
                        os.system("parted {} rm {}".format(name1, num1))
                        os.system("lsblk")
                        option()
                    elif op == 6:
                        os.system("exit")
                        os.system("tput setaf 3")
                        print("\n\n\t#########..THANK YOU..See you soon..#########")
                        os.system("tput setaf 7")
                        print("\n")

                    else:
                        print("Incorrect Choice,select correct option..")
                        anykey = input("\n\t Press Enter to go main menu")
                option()
                par()
            elif part == 2:
                def printme():
                    ch = int(input(''' 
                        \n
                    
        \tPress 1 : To see Hard disk information..
        \tPress 2 : To create a Physical Volume (PV)..
        \tPress 3 : To create a Volume Group (VG)..
        \tPress 4 : To create a Logical Volume (LV)..
        \tPress 5 : To format the Logical Volume (LV)..
        \tPress 6 : To create a Folder and Mount Logical Volume..
        \tPress 7 : To increase the LVM partition..
        \tPress 8 : To decrease the LVM partition..
        \tPress 9 : Exit..
                        \n
                        What can I help you : '''))
                    print("\t\n.........................###...........................\n")

                    if ch == 1:
                        os.system("\n fdisk -l")
                        os.system("tput setaf 3")
                        anykey = input("\n\t Press Enter to go main menu...>>")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 2:
                        os.system("\n fdisk -l")
                        Disk1 = input("\n\n\tEnter name of 1 st harddisk that you want >> ")
                        os.system("pvcreate {}".format(Disk1))
                        os.system("pvdisplay {}".format(Disk1))
                        Disk2 = input("\n\t Enter name of 2 nd harddisk that you want >> ")
                        os.system("pvcreate {}".format(Disk2))
                        os.system("pvdisplay {}".format(Disk2))
                        os.system("tput setaf 3")
                        print("\n\n\t>>>>>>>>>Your two physical volume(PV) created successfully<<<<<<<<<<")
                        anykey = input("\n\t Press Enter to go main menu...>>")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 3:
                        os.system("\n fdisk -l")
                        Disk1 = input("\n\n\tEnter name of 1 st harddisk that you want >> ")
                        Disk2 = input("\n\tEnter name of 2 nd harddisk that you want >> ")
                        name1 = input("\n\tGive name to your Volume Group(VG) >> ")
                        os.system("pvdisplay {}".format(Disk1))
                        os.system("pvdisplay {}".format(Disk2))
                        os.system("vgcreate {} {} {}".format(name1, Disk1, Disk2))
                        os.system("vgdisplay {}".format(name1))
                        os.system("tput setaf 3")
                        print("\n\n\t>>>>>>>>>>Your Volume Group(VG) {} created successfully<<<<<<<<< ".format(name1))
                        anykey = input("\n\t Press Enter to go main menu...>>")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 4:
                        os.system("\n fdisk -l")
                        # Disk1= input("\n\n\t Enter name of 1 st harddisk that you want >> ")
                        # Disk2= input("\n\t Enter name of 2 nd harddisk that you want >> ")
                        size1 = input("\n\t Enter size for your Logical Volume >> ")
                        name1 = input("\n\t Enter your Volume Group(VG) name >> ")
                        name2 = input("\n\t Give name to your Logical Volume(LV) >> ")
                        # os.system("pvcreate {}".format(Disk1))
                        # os.system("pvcreate {}".format(Disk2))
                        # os.system("vgcreate {} {} {}".format (name1,Disk1,Disk2))
                        os.system("vgdisplay {}".format(name1))
                        os.system("lvcreate --size {}G --name {} {} ".format(size1, name2, name1))
                        os.system("lvdisplay {}/{}".format(name1, name2))
                        os.system("tput setaf 3")
                        print("\n\n\t>>>>>>>>>Your Logical Volume(LV) {} created successfully<<<<<<<<<".format(name2))
                        anykey = input("\n\t Press Enter to go main menu...>>")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 5:
                        name2 = input("\n\n\tEnter the name of Volume Group >> ")
                        name3 = input("\n\n\tEnter the name of Logical Volume >> ")
                        os.system("mkfs.ext4 /dev/{}/{}".format(name2, name3))
                        os.system("tput setaf 3")
                        print("\n\n\t>>>>>>>>>Your Logical Volume Formated<<<<<<<<")
                        anykey = input("\n\t Press Enter to go main menu...>>")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 6:
                        folder1 = input("\n\n\t Enter folder name that you want >> ")
                        os.system("mkdir {}".format(folder1))
                        name2 = input("\n\tEnter the name of Volume Group >> ")
                        name3 = input("\n\tEnter the name of Logical Volume >> ")
                        os.system("mount /dev/{}/{} {}".format(name2, name3, folder1))
                        os.system("df -hT")
                        os.system("tput setaf 3")
                        print("\n\n\t>>>>>>>>Your Logical Volume mounted<<<<<<<<")
                        anykey = input("\n\t Press Enter to go main menu...>> ")
                        os.system("tput setaf 7")
                        printme()

                    elif ch == 7:
                        pr1 =  input("\n\n\tEnter the name of VG Partition..: ")
                        pr2 = input("\n\n\tEnter the name of LV Partition..:")
                        pr3 = input("\n\n\tEnter the increase size..: ")
                        os.system("lvextend --size +{}G /dev/{}/{}".format(pr3,pr1,pr2))
                        os.system("resize2fs /dev/{}/{}".format(pr1,pr2))
                        anykey = input("\n\t Press Enter to go main menu...>> ")
                        printme()

                    elif ch == 8:
                        pr1 = input("\n\n\tEnter the name of VG Partition..: ")
                        pr2 = input("\n\n\tEnter the name of LV Partition..:")
                        pr3 = input("\n\n\tEnter the decrease size..: ")
                        os.system("lvreduce -r -L {}G /dev/{}/{}".format(pr3, pr1, pr2))
                        anykey = input("\n\t Press Enter to go main menu...>> ")
                        printme()

                    elif ch == 9:
                        os.system("exit")
                        os.system("tput setaf 3")
                        print("\n\n\t#########..THANK YOU..See you soon..#########")
                        os.system("tput setaf 7")
                        print("\n")

                    else:
                        print("Incorrect Choice,select correct option..")
                        anykey = input("\n\t Press Enter to go main menu")
                        printme()
                printme()
                par()
            elif part == 3:
                os.system("exit")
        par()
        task()

    elif kite == 4:
        def dock():
            print("\n Let's  start docker")
            print("""
            \tPress  1 : To install docker  
            \tPress  2 : To start docker  
            \tPress  3 : To check status of docker  
            \tPress  4 : To install images of Docker  
            \tPress  5 : To check images of docker  
            \tPress  6 : To run container  top  of  docker  
            \tPress  7 : To run python top of container  
            \tPress  8 : Exit.. 
            """)
            i = int(input("Enter your choice..: "))
            if i == 1:
                os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                os.system("dnf install docker-ce --nobest -y")
                dock()
            elif i == 2:
                os.system("systemctl start docker")
                dock()
            elif i == 3:
                os.system("systemctl status docker")
                dock()
            elif i == 4:
                x = input("Enter image name..>>  ")
                os.system("docker pull {}".format(x))
                dock()
            elif i == 5:
                os.system("docker images")
                dock()
            elif i == 6:
                y = input("enter image name..>>  ")
                z = input("Give OS name that  you want..>>   ")
                os.system("docker run -it --name {} {}".format(z, y))
                dock()
            elif i == 7:
                y = input("enter image name..>>  ")
                z = input("Give OS name that  you want..>>   ")
                os.system("docker run -it --name {}  {}".format(z, y))
                os.system("yum install python3")
                os.system("python 3")
                dock()
            elif i == 8:
                os.system("exit")
            else:
                print("Invalid option...")
        dock()
        task()
    elif kite == 5:
        os.system("yum install httpd")
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
        task()

    elif kite == 6:
        os.system("exit")
        print("\n ........ THANK YOU .......")

    else:
        print("Invalid option...")
        task()

task()
