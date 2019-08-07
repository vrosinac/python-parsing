

	#!/usr/bin/env python

#   with open("Zoe.html", "rb") as infile, open("Zoe1.html", "wb") as outfile:


import re

#vdb1file = open("platform-deployment-local-extract.log", "r")
vdb1file = open("platform-deployment-local-extract.log", "r")
vdb2 = open("platform-deployment-local-extract-PARSED.log", "w", newline='\r\n')
vdb1 = iter(vdb1file)

while True:
print("begining while")
line1 = next(vdb1)
line2 = "EMPTY LINE"
match1 =  re.search("(.*)TIZONE.(.*)", line1)
if match1:
  print("match1")
  match_select =  re.search("(.*)SELECT(.*)", line1)
  if match_select:
   print("match_select:")
   print(line1)
   line1 = next(vdb1)
   print(line1)
   match_select_duration =  re.search("(.*)DEBUG(.*)TimedLogger(.*)TIZONE.(.*)WHERE(.*)duration:(.*)", line1)
   if match_select_duration:
    print("match_select_duration")
    line2 = "\n" + match_select_duration.group(1) +  " ; SELECT ; " + match_select_duration.group(4) + " ; " + match_select_duration.group(6) + "\n"
  else:
   match_insert = re.search("(.*)INSERT(.*)TIZONE.(.*)", line1)
   if match_insert:
    print("matchinsert")
    tablename = match_insert.group(3)
    parsed_time = match_insert.group(1)
    line1 = next(vdb1)
    match_insert_duration =  re.search("(.*)DEBUG(.*)Complete: SQL Update duration:(.*)", line1)
    if match_insert_duration:
     print("matchinsertduration")
     line2= "\n" + match_insert_duration.group(1) +  " ; INSERT ; " + tablename + " ; " +  match_insert_duration.group(3) + "\n"
    else:
     line2 = "ERROR: INSERT STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time
     print(line2)
     #vdb2.write("ERROR, INSERT STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time)
   else:
    match_update = re.search("(.*)UPDATE(.*)TIZONE.(.*)SET(.*)", line1)
    if match_update:
     print("match_update")
     tablename = match_update.group(3)
     parsed_time = match_update.group(1)
     line1 = next(vdb1)
     match_update_duration =  re.search("(.*)DEBUG(.*)Complete: SQL Update duration:(.*)", line1)
     if match_update_duration:
      print("match_update_duration")
      line2= "\n" + match_update_duration.group(1) +  " ; UPDATE ; " + tablename + " ; " +  match_update_duration.group(3) + "\n"
     else:
      line2="ERROR: UPDATE STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time
      print(line2)
      #vdb2.write("ERROR, UPDATE STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time)
     a=1
    else:
     match_delete = re.search("(.*)DELETE(.*)TIZONE.(.*)WHERE(.*)", line1)
     if match_delete:
      print("match_delete")
      tablename = match_delete.group(3)
      parsed_time = match_delete.group(1)
      line1 = next(vdb1)
      match_delete_duration =  re.search("(.*)DEBUG(.*)Complete: SQL Update duration:(.*)", line1)
      if match_delete_duration:
       print("match_delete_duration")
       line2= "\n" + match_delete_duration.group(1) +  " ; DELETE ; " + tablename + " ; " +  match_delete_duration.group(3) + "\n"
      else:
       line2="ERROR: DELETE STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time
       print(line2)
      #vdb2.write("ERROR, DELETE STATEMENT NOT PARSED, TABBLE" + tablename + " LINE:"+ parsed_time)
     a=2
    a=1
   a=0
  if line2 != "EMPTY LINE":
   vdb2.write(line2)
a=2
a=1,
a=2
vdb2.close()
