# Norah Lin's New Homework #5 (in 4107029007/aiot_hw5)(initial setup)
from local generate a new repository on github my test
## Lecture 14: IoT Flask Web (github, vs code)

### Step 1 : Development Environment Setup in aiot_hw5
1. Please install vs code, register github, install git for windows
2. (check-point 1) github create a new repository (aiot0524)
3. go to vs code clone this repository (choose new branch) 
4. vs code 安裝 python extension 
5. pip install flask, pandas, sklearn 
  * 快捷鍵 ctrl+shift+p ===> package manager 叫出 (git clone....)
  * 快捷鍵 ctrl+' ==> 叫出終端機 
6. (check-point 2) 為了要upload local file to github from local要終端機 C:> 設定下面 (不設定 branch default ='main')
   * C:> git config --global user.name "username"
   * C:> git config --global user.email useremail@gmail.com
   
7. C:> git remote add origin https://github.com/huanchen1107/aiot_0524.git 

if you want to change

git remote add origin https://github.com/4107029007/aiot_hw5.git
git branch -M main
git push -u origin main
(如果出現 fatal: remote origin already exists，先執行git remote rm origin再繼續執行)




