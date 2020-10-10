#include <stdio.h>

const char* GNGGA()
{
	return "$GNGGA,054157.013,2307.1261,N,12016.4308,E,1,6,1.93,34.9,M,17.8,M,,*76\r\n";
}

const char* GNRMC()
{
        return "$GNRMC,143909.00,A,5107.0020216,N,11402.3294835,W,0.036,348.3,210307,0.0,E,A*31\r\n";
}

const char* GPSNMEA()
{
        int next;
        FILE *determine;

        determine = fopen("NMEA","r");
        fscanf(determine,"%d",&next);
	fclose(determine);

	determine = fopen("NMEA","w");

        if(next == 1) {
		fprintf(determine,"%d",0);
		fclose(determine);
                return GNRMC();
        }
	fprintf(determine,"%d",1);
	fclose(determine);
        return GNGGA();
}
