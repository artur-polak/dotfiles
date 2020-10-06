#/bin/bash
for f in `ls -d */`
do
    test -d "$f.git" &&  echo -e "\n$f" && git --git-dir=$f.git --work-tree=$f pull -q && git --git-dir=$f.git --work-tree=$f status -s -b
done
