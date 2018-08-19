__author__ = 'kosala atapattu'
import time
from ansible import errors

def net_interface_list(values=[]):
    return ','.join(str(':'.join(i)) for i in values)

def array_to_csv(values=[]):
    return ','.join(values)

def get_image_name (values, resttime, strict):
    from datetime import datetime
    from ansible import errors
    import json
    
    tf = "%Y-%m-%d %H:%M:%S"
    if resttime != "latest":
        if resttime is not None:
            try:
                restoretime = datetime.strptime (resttime, tf)
            except:
                raise errors.AnsibleFilterError('Icorrect date format ['+resttime+']')
    else:
        restoretime = datetime.now()

    for image in values['results']:
        # capture the start time and end time
        # this is in a try catch loop as some images does not have a begin
        # end pit, for example onvault images.
         
        if image['json']['result']['componenttype'] == '0':
            if image['json']['result']['mountedhost'] == '0':
                try: 
                    starttime = datetime.strptime (image['json']['result']['consistencydate'][:-4], tf)
                    endtime = datetime.strptime (image['json']['result']['endpit'], tf)
                    if  starttime < restoretime < endtime:
                        return image['json']['result']['backupname']
                except:
                    pass

# if LS image is not possbile, lets try to grab the closes image as long as we have set the strict_mode off

    if not strict:
        preferedtime = None
        for image in values['results']:
            try:
                imgtime =  datetime.strptime (image['json']['result']['consistencydate'][:-4], tf)
            except:
                raise errors.AnsibleFilterError(image['json']['result']['consistencydate'][:-4])
                # pass
            
            if preferedtime == None:
                preferedtime = imgtime
                if preferedtime > restoretime:
                    prevdiff = preferedtime - restoretime
                else:
                    prevdiff = restoretime - preferedtime

            # need to find the closest image
            
            if restoretime > imgtime:
                currdif = restoretime - imgtime
            else:
                currdif = imgtime - restoretime 
            
            if image['json']['result']['componenttype'] == "0":
                if image['json']['result']['mountedhost'] == '0':
                    if prevdiff.total_seconds() >= currdif.total_seconds(): #this is python 2.7 function
                        preferedtime = imgtime
                        preferedimg = image
                        prevdiff = currdif
    return preferedimg['json']['result']['backupname']

def gen_prov_options (poptions, capabilities):
    ret_out = ""
    for key in poptions:
        # if this provisioning option is defined
        if poptions[key] != '':
            # and this capability is available in this version of actifio
            for item in capabilities:
                if item['name'] == str(key):
                    ret_out += '<'+str(key)+'>'+str(poptions[key])+'</'+str(key)+'>'
    return '<provisioningoptions>'+ret_out+'</provisioningoptions>' 

def gen_prov_options_sqlg (poptions, capabilities, sdbs):
    ret_out = ""
    for key in poptions:
        # if this provisioning option is defined
        if poptions[key] != '':
            # and this capability is available in this version of actifio
            for item in capabilities:
                if item['name'] == str(key):
                    ret_out += '<'+str(key)+'>'+str(poptions[key])+'</'+str(key)+'>'
            if len(sdbs.split(',')) == 1 and str(key) == 'dbname':
                ret_out += '<'+str(key)+'>'+str(poptions[key])+'</'+str(key)+'>'

    return '<provisioningoptions>'+ret_out+'</provisioningoptions>'

class FilterModule(object):
    def filters(self):
        return {
            'net_interface_list': net_interface_list, 
            'get_image_name': get_image_name, 
            'array_to_csv': array_to_csv,
            'gen_prov_options': gen_prov_options,
            'gen_prov_options_sqlg': gen_prov_options_sqlg
            }
        
