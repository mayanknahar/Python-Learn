# How to use os module

import os

print(dir(os))    #prints all the methods in the imported os module
print(os.getcwd())  #prints the current working directory

'''os.chdir('path')   				changes the path of the working file i.e changes the directory
os.listdir()   						lists the total files in the working directory
os.mkdir('dir_name')   				creates the directory with the name given in the parenthesis
os.makedirs(dir_name/sub_dir)    	creates a level of directories at a time
os.rmdir('dir_name')   				deletes the directory with the name given in the parenthesis
os.removedirs(dir_name/sub_dir)    	deletes a level of directories at a time
os.rename('orginal','new')			renames the original folder with the new name
os.stat('dir_name')					returns the stats of the file i.e last modified time, size etc.
os.walk('path')						prints the directory tree
os.environ.get('HOME')				captures the home directory
os.path.join('path1','path2')		joins the two paths into a single path
os.path.dirname('path') 			gives the directory name of the path		
os.path.basename('path')			gives the basename(file name) of the path
os.path.split('path') 				prints both dir and base name..... dir first
os.path.isdir('path')				returns True if the path is a directory 
os.path.isfile('path') 				returns true if the path is a file
os.path.splitext('path')			returns name and extension of the path separately
'''

#How to use datetime module

import datetime

'''
datetime.date(year,month,day)			creates date with the given parameters
datetime.date.today()					returns todays date
datetime.timedelta(days=7)				creates a time delta of 7 days i.e gap of 7 days
total_seconds()							method to get total seconds in particular time
datetime.time(hrs,mins,sec,micro_secs)	creates time with thw given parameters
datetime.datetime(date,time)			creates both date and time with the parameters
datetime.timedelta(hours=12)   			creates time delta of 12 hrs
datetime.datetime.now()					same as today() but provides place for timezone
'''








