To move a walk into the main, do

On branch master

1. get to directory src and put your md files there
2. rename filelist.txt as zz
3. python3 create-csv zz zz.csv
4. go to t2mioo.com and generate the links for zz.csv
5. downoad the resultant file
6. cd ..
7. python3/tools/cvt-auto.py
8. cd mdgithub
9. python3 ../tools/forward-link.py zz zz-response...
10. rm *-sav

11.check the mess in and push it

12. git checkout main
13. git checkout master -- mdgithub
14. edit README.md to include new chain
15. check in and push

Yaaa. You are done