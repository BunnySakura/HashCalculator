cmake_minimum_required(VERSION 3.20)

# 项目名
project(HashCalculator)

# C++标准
set(CMAKE_CXX_STANDARD 17)

# 查找当前目录下的所有源文件，并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 添加模块
find_package(wxWidgets CONFIG REQUIRED)
find_package(OpenSSL REQUIRED)  

# 根据平台指定生成目标
if(UNIX)
    message("current platform: Linux ")
    add_executable(${PROJECT_NAME} UNIX ${DIR_SRCS})

elseif(WIN32)
    message("current platform: Windows ")
    set(APP_ICON_RESOURCE_WINDOWS "${CMAKE_CURRENT_SOURCE_DIR}/resources/logo.rc")
    add_executable(${PROJECT_NAME} WIN32 ${DIR_SRCS} ${APP_ICON_RESOURCE_WINDOWS})

else()
    message("current platform: unkonw ")
endif()

# 添加静态链接库
target_link_libraries(${PROJECT_NAME} PRIVATE wx::core wx::base)
target_link_libraries(${PROJECT_NAME} PRIVATE OpenSSL::Crypto)
