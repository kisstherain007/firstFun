import os
import sys
import requests
import shutil
# import Gittle
import modifyXML

try:
  import configparser
except ImportError:
  import ConfigParser

try:
  cf = configparser.ConfigParser()
  print('python3')
except Exception as e:
  cf = ConfigParser.ConfigParser()
  print('python2')

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

# alter("file1", "09876", "python")

def copyFiles(sourceDir, targetDir):
  for file in os.listdir(sourceDir):
    sourceFile = os.path.join(sourceDir, file)
    targetFile = os.path.join(targetDir, file)
    # print('sourceFile ' + sourceFile)
    # print('targetFile ' + targetFile)
    if os.path.isfile(sourceFile):
      if not os.path.exists(targetDir):
        os.makedirs(targetDir)
      if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
        # print('創建文件')
    if os.path.isdir(sourceFile):
      copyFiles(sourceFile, targetFile)

# *****************************************下载编译时需要的项目文件****************************************
# repo_url = 'ssh://zhoubo@192.168.2.12:29418/mobile/yidonghuli_new.git'
# repo_path = 'D:\\ReleaseProject\\project'
# repo = Gittle.clone(repo_url, repo_path)
# repo.auth(username="zhoubo", password="123456")

copyFiles(os.path.dirname(__file__) + '/copyfiles', 'D:\\ReleaseProject\\project')
os.chdir('D:\ReleaseProject')
os.system('D:\\ReleaseProject\\project\\gitclone.sh')
os.chdir(os.path.dirname(__file__))
# os.system('git clone ssh://zhoubo@192.168.2.12:29418/mobile/yidonghuli_new.git')

# *******************************************copy编译时需要的文件******************************************

# projectSourceDir = 'D:\developer\work\IdeaProjects\yidonghuli_new\YiDongHuiLi_Zpdyf_Basic'
# projectTargetDir = 'D:\\ReleaseProject\\project'
# copyFiles(projectSourceDir, projectTargetDir)

# projectSourceDir = 'D:\ReleaseProject\yidonghuli_new\YiDongHuiLi_Zpdyf_Basic'
projectTargetDir = 'D:\ReleaseProject\yidonghuli_new\YiDongHuiLi_Zpdyf_Basic'
# copyFiles(projectSourceDir, projectTargetDir)
pass

# 根据项目中的文件动态生成需要打包的apk医院名称和版本号
modifyXML.modifyProjectNameFromProject(projectTargetDir)
branchName = modifyXML.getReleaseBranchName(projectTargetDir)
alter(os.path.dirname(__file__) + '/copyfiles/add_branch.sh', '$', branchName)

sourceDir = os.path.dirname(__file__) + '/copyfiles'
copyFiles(sourceDir, projectTargetDir)
pass


# *************************************************编译apk************************************************
# print('开始打包')
# # # 切换到项目根据目录
# os.chdir(projectTargetDir)
# # print('切入到目录' + projectTargetDir)
# pass
# try:
#   # 执行命令清理ant之前生成缓存
#   os.system('ant clean')
#   # pass
#   # # 执行命令打包并且签名apk
#   os.system('ant release')
#   print('打包成功 ho(*￣︶￣*)o')
# except Exception as e:
#   print('打包失败')

# *************************************************创建上传分支************************************************
