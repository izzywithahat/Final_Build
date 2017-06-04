sudo apt-get install ros-kinetic-angles
DIR = basename "$PWD"
if ["$DIR" != "Final_Build"]; then
    cd ..
fi
git submodule init
git submodule update
rm -rf build/
rm -rf devel/
catkin_make
