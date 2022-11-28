# auto-iclicker-mark
Backgroud:

I was a TA for general chemistry class, my job is to mark the attended student to a sheet that the Dept sheet. But there are thousands of student (with their name and Edu ID), which makes me a huge amount time to check, and search and fill the mark symbol one-by-one. So I developed a script for automatically fill the mark symbol for the sheet.
First you have to use some screen-text recognizer (Umi-OCR) to make these name on the picture convert to text, and compare these text to the database (Dept sheet), if they can be found in the database, the name will be recorded as "attended" to a new file "student_sheet_new". With this coding, you can modify it very easily and use it for a large job.

Feature:
The coding implemented with a confidence compare. To be more specific, some written-by-student name is really hard to be translated by computer, so here a comparson module and a confidence value is given. If the confidence is larger than 0.6, is automatically mark this student, otherwise, manually comapre would be given via a GUI interface. If the confidence is too low, < 0.4, it would be ignored.



an script that comapre a name with the data base with GUI.

open demo

**main program**
1.py              # main program

**INPUT**
data.txt          # database with EID and name
screenshot.txt    # the text from screenshot list

**OUTPUT**
student_sheet_new # final result with marked student. order is the same as data.txt


please remember use GUI based IDE.



wangjiaao0720@utexas.edu
Jiaao WANG @Henkelman Group, UT Austin, United States
