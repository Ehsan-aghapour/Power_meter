#compiler=aarch64-linux-android-clang++
compiler=armv7a-linux-android-clang++
target=armv7a-linux-androideabi$1-clang
#target=aarch64-linux-android$1-clang++
p=/home/ehsan/UvA/ARMCL/android-ndk-r21e-linux-x86_64/android-ndk-r21e/toolchains/llvm/prebuilt/linux-x86_64/bin/
cp $p/$target $p/$compiler

#XX=clang++ CC=clang scons Werror=0 -j16 debug=0 asserts=0 neon=1 opencl=1 os=android arch=armv7a 

#$compiler $2 -Iinclude/ -Llibs/ -lrknn_api -lstdc++ -llog -pie -Wl,-rpath,/system/usr/lib64/
$compiler $2 -o gpio
#scons 

rm $p/$compiler

adb push gpio /data/local/w
adb shell chmod +x /data/local/w/gpio
adb shell /data/local/w/gpio


