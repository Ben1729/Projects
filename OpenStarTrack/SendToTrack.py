import ephem, time

#Servo steps per degree
STEPS_PER_DEGREE = 27.30555

#Minimum Duty for stepper
MIN_DUTY = 2457

#Max Duty for stepper
MAX_DUTY = 7372

#Servo steps per degree
STEPS_PER_DEGREE = 27.30555

#Your latitude in decimal degrees
LATITUDE = '0.0'

#Your longitude in decimal degrees
LONGITUDE = '0.0' 

#Target data
target = ephem.star('polaris')

#Degrees minutes seconds to decimal degrees the pure form of degrees, this makes math for steps per degree easier.  steppers will most likely use 1/4 microsteping though.
def dms2dd(dms):
    parts = str(dms).split(':')
    dd = 0
    if int(parts[0]) < 0:
        dd = float(parts[0]) - float(parts[1])/60 - float(parts[2])/(60*60);
    else:
        dd = float(parts[0]) + float(parts[1])/60 + float(parts[2])/(60*60);

    return dd;

if __name__ == "__main__":

    site = ephem.Observer()
    site.lat = LATITUDE
    site.lon = LONGITUDE
    site.date = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime())

    target.compute(site)
    
    az = float(dms2dd(target.az))
    alt = float(dms2dd(target.alt))
    if az > 180:

        azimuth = ((az - 180)*STEPS_PER_DEGREE)+MIN_DUTY
        elevation = ((180-alt)*STEPS_PER_DEGREE)+MIN_DUTY

        #TODO Send to arduino Via com port
    else:
        azimuth = ((az)*STEPS_PER_DEGREE)+MIN_DUTY
        elevation = ((alt)*STEPS_PER_DEGREE)+MIN_DUTY

        #TODO Send to arduino Via com port
