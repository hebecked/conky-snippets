#!/bin/python

import sys, os
import subprocess

def get_info():
    cmd = subprocess.Popen(  ['mocp -i'],stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True, close_fds=True)
    stdout, stderr = cmd.communicate()
    if cmd.returncode:
        errmsg = stderr.strip()
        if 'server is not running' in errmsg:
            raise MocNotRunning(errmsg)
        else:
            raise MocError(errmsg)
    return stdout



def output_to_dict(output1):
    if not output1:
        return
    output = str( output1, encoding='utf8', errors='ignore' )
    lines = output.strip('\n').split('\n')
    if 'Running the server...' in lines[0]:
        del lines[0]
    return dict((key.lower(), value[1:]) for key, value in (line.split(':', 1) for line in lines))

def get_info_dict():
    dct = output_to_dict(get_info())
    if dct is None:
        return
    #dct['state'] = STATES[dct['state']]
    return dct

def convert_info_dict_to_conky():
    dict = get_info_dict()
	#for dic in dict:
	#if(dict[dic]!=''):
			#print("${color grey}",dic,":${color green}", dict[dic])
    print("${color grey}State:${color green}", dict['state'],"$alignr", end='')
    if(dict['state']=='PLAY'):
        print("${color grey}Time:${color green}", dict['currenttime'])
        print("${color grey}Samplerate:${color green}", dict['rate'],"$alignr${color grey}Bitrate:${color green}", dict['bitrate'])
        print("${color grey}File:${color green}", dict['file'])
        if(dict['title']!=''):
            print("${color grey}Title:${color green}", dict['title'].strip('#'))
        if(dict['songtitle']!=dict['title']):
            print("${color grey}Songtitle:${color green}", dict['songtitle'])
        if(dict['artist']!=''):
            print("${color grey}Artist:${color green}", dict['artist'])
        if(dict['album']!=''):
            print("${color grey}Album:${color green}", dict['album'])
    elif(dict['state']=='PAUSE'):
        if(dict['currenttime']!='00:00'):
            print("${color grey}Current time:${color green}", dict['currenttime'])
        else:
            print()
        print("${color grey}File:${color green}", dict['file'])
        if(dict['title']!=''):
            print("${color grey}Title:${color green}", dict['title'])


convert_info_dict_to_conky()
