#!/bin/bash
read -p "请输入虚机名:" NF
cd /var/lib/libvirt/images/
qemu-img create -f qcow2 -b .node_base.qcow2 $NF.img 20G
cp /var/lib/libvirt/images/.node_base.xml  /etc/libvirt/qemu/$NF.xml
sed -i "s/node_base/$NF/" /etc/libvirt/qemu/$NF.xml
sed -i "s/node_base.img/$NF.img/" /etc/libvirt/qemu/$NF.xml

virsh define /etc/libvirt/qemu/$NF.xml

virsh start $NF

