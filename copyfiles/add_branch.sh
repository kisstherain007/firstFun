
echo "创建release分支"

# 创建分支->master
git checkout -b release-$ master

#上传分支
git push origin release-$



#删除本地分支
#git branch –d name
# 删除远程分支
# git push origin --delete [branch-name]