#!/bin/python
import ephem, time, subprocess, urllib2

sample = '44100'#25569
wavrate='11025'

def getTLE(name, list):

    line1 = ''
    line2 = ''
    line3 = ''

    for curentLine in list:

        if line2 != '':
            line3 = curentLine
            break

        if line1 != '':
            line2  = curentLine

        if name in curentLine:
            line1 = curentLine

    return line1, line2, line3

def findNextPass(LATITUDE, LONGITUDE):

    site = ephem.Observer()
    site.lat = LATITUDE
    site.lon = LONGITUDE
    site.date = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime())

    tleList = urllib2.urlopen("http://celestrak.com/NORAD/elements/noaa.txt").read().replace('\r', '').split('\n')

    line1, line2, line3 = getTLE('NOAA 15', tleList)
    NOAA15 = ephem.readtle(line1, line2, line3)

    line1, line2, line3 = getTLE('NOAA 18', tleList)
    NOAA18 = ephem.readtle(line1, line2, line3)

    line1, line2, line3 = getTLE('NOAA 19', tleList)
    NOAA19 = ephem.readtle(line1, line2, line3)

    next15 = site.next_pass(NOAA15)
    next18 = site.next_pass(NOAA18)
    next19 = site.next_pass(NOAA19)

    if next15[0] < next18[0] and next15[0]< next19[0]:
        return 'NOAA 15', next15

    if next15[0] > next18[0] and next18[0] < next19[0]:
        return 'NOAA 18', next18

    if next15[0] > next19[0] and next18[0] > next19[0]:
        return 'NOAA 19', next19

def waitForPass(satilite, nextPass):
    now = ephem.date(time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime()))#(time.time()/86400 + 25567)
    towait = (nextPass[0]-now) * 86400
    if nextPass[0] > now:
        print "waiting "+str(towait)+" seconds for "+satilite
        if towait > 30:
            time.sleep(30)
            waitForPass(satilite, nextPass)
        else:
            time.sleep(towait)

def recordPass(freq, recordLen, fileName):
    cmdline = ['rtl_fm',\
               '-f',str(freq),\
               '-s',sample,\
               '-g','43',\
               '-F','9',\
               '-A','fast',\
               '-E','dc',\
               fileName+'.raw']
    runForDuration(cmdline, recordLen * 86400)

    cmdline = ['sox','-t','raw','-r',sample,'-es','-b','16','-c','1','-V1',fileName+'.raw',fileName+'.wav','rate',wavrate]
    subprocess.call(cmdline)

def getFreq(satilite):
    if satilite == 'NOAA 15':
        return 137620000
    if satilite == 'NOAA 18':
        return 137912500
    if satilite == 'NOAA 19':
        return 137100000

def runForDuration(cmdline, duration):
    try:
        child = subprocess.Popen(cmdline)
        time.sleep(duration)
        child.terminate()
    except OSError as e:
        print "OS Error during command: "+" ".join(cmdline)
        print "OS Error: "+e.strerror

def ToImages(fileName):

    cmdline = ['/root/aptdec-1.7/atpdec',fileName+'.wav']
    subprocess.call(cmdline)
    cmdline = ['/root/aptdec-1.7/atpdec -o '+ fileName + '-Color.png -e d -i p -p /root/aptdec/palettes/WXtoImg-N18-HVC.png ',fileName+'.wav']
    subprocess.call(cmdline)

if __name__ == '__main__':
    #Your latitude in decimal degrees
    LATITUDE = '34.53'

    #Your longitude in decimal degrees
    LONGITUDE = '-83.99'
    while True:

        satilite, nextPass = findNextPass(LATITUDE, LONGITUDE)
        waitForPass(satilite, nextPass)

        fileName=('/mnt/'+satilite+''+('%s' % nextPass[0]).replace('/','-')).replace(' ','_')
        print "beginning pass "+fileName+" predicted end "+str(nextPass[0])

        recordPass(getFreq(satilite), nextPass[4]-nextPass[0],fileName)
        toImages(fileName)
