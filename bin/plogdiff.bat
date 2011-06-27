@echo off
rem Run python program, save output in log, compare new log to reference log 
python %1.py > %1.log
fc %1.log %1.ref      
