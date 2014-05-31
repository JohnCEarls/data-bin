#!/bin/bash
set -x
dir=~/MasterDirac/masterdirac
if [ -d $dir ]; then
    cd $dir
    vim "+UpdateTags -R . " "+qall"
    cd ~
fi
dir=~/DataDirac/datadirac
if [ -d $dir ]; then
    cd $dir
    vim "+UpdateTags -R . " "+qall"
    cd ~
fi
dir=~/PynamoDB/pynamodb
if [ -d $dir ]; then
    cd $dir
    vim "+UpdateTags -R . " "+qall"
    cd ~
fi
dir=~/tcdiracweb/tcdiracweb
if [ -d $dir ]; then
    cd $dir
    vim "+UpdateTags -R . " "+qall"
    cd ~
fi


dir=~/GPUDirac/gpudirac
if [ -d $dir ]; then
    cd $dir
    vim "+UpdateTags -R . " "+qall"
    cd ~
fi
