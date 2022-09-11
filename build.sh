mkdir -p ./out/build

cd ./out/build

rm -rf *

cmake ../../

cmake --build . && echo "编译完成！"
