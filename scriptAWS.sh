#!/bin/sh

aws configure < awsProfile 
export AWS_DEFAULT_FORMAT="text"

loop=`wc -l region`
echo "There are total $loop "

cnt=0
filename="region"
while read -r line
do
    name="$line"
    cnt=$((cnt+1))
    val=`echo "$line" | awk '{print ". Working on region: " $1 }'`
    echo "$cnt$val"
    regionName=`echo "$line" | awk '{print $2}'`
    #echo "region:$regionName"  
    aws ec2 describe-instances --output text --region $regionName --query Reservations[].Instances[].Tags[].Value
    aws ec2 describe-instances --output text --region $regionName --query Reservations[].Instances[].NetworkInterfaces[].PrivateIpAddresses[].Association[].PublicIp[]

    echo "-"
    sleep 1
done < "$filename"


