cd _includes
./upload.bat
cd ../

cd _layouts
./upload.ps1
cd ../

cd assets
./upload.bat
cd ../

git config --local user.name "HomunMage"
git config --local user.email "Homun@posetmage.com"
git remote set-url origin git@HO:HomunMage/Practice.git

git submodule update --recursive --remote

git pull
git add .
git commit -m "upload"
git push
