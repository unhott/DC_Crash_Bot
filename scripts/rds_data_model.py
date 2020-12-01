from connect_to_rds import create_postgres_engine
import sqlalchemy

engine = create_postgres_engine("AWS_PostGIS", "postgres", "DEV")

engine.execute("""
CREATE SCHEMA IF NOT EXISTS raw_data AUTHORIZATION postgresadmin;
""")


engine.execute("""
CREATE TABLE IF NOT EXISTS vision_zero (
    OBJECTID VARCHAR NULL
    ,GLOBALID   VARCHAR NULL 
    ,REQUESTID VARCHAR NULL
    ,REQUESTTYPE VARCHAR NULL
    ,REQUESTDATE TIMESTAMP NULL
    ,STATUS VARCHAR NULL
    ,STREETSEGID VARCHAR NULL
    ,COMMENTS VARCHAR NULL
    ,USERTYPE VARCHAR NULL
    ,geometry geometry
    );
GRANT ALL PRIVILEGES ON vision_zero TO PUBLIC;
""")

engine.execute("""
CREATE TABLE IF NOT EXISTS crashes_raw (
    OBJECTID VARCHAR NULL
    ,CRIMEID VARCHAR NULL
    ,CCN VARCHAR NULL
    ,REPORTDATE TIMESTAMP NULL
    ,ROUTEID VARCHAR NULL
    ,MEASURE VARCHAR NULL
    ,_OFFSET VARCHAR NULL
    ,STREETSEGID VARCHAR NULL
    ,ROADWAYSEGID VARCHAR NULL
    ,FROMDATE TIMESTAMP NULL
    ,TODATE TIMESTAMP NULL
    ,MARID VARCHAR NULL
    ,ADDRESS VARCHAR NULL
    ,LATITUDE VARCHAR NULL
    ,LONGITUDE VARCHAR NULL
    ,XCOORD VARCHAR NULL
    ,YCOORD VARCHAR NULL
    ,WARD VARCHAR NULL
    ,EVENTID VARCHAR NULL
    ,MAR_ADDRESS VARCHAR NULL
    ,MAR_SCORE VARCHAR NULL
    ,MAJORINJURIES_BICYCLIST INT NULL
    ,MINORINJURIES_BICYCLIST INT NULL
    ,UNKNOWNINJURIES_BICYCLIST INT NULL
    ,FATAL_BICYCLIST INT NULL
    ,MAJORINJURIES_DRIVER INT NULL
    ,MINORINJURIES_DRIVER INT NULL
    ,UNKNOWNINJURIES_DRIVER INT NULL
    ,FATAL_DRIVER INT NULL
    ,MAJORINJURIES_PEDESTRIAN INT NULL
    ,MINORINJURIES_PEDESTRIAN INT NULL
    ,UNKNOWNINJURIES_PEDESTRIAN INT NULL
    ,FATAL_PEDESTRIAN INT NULL
    ,TOTAL_VEHICLES INT NULL
    ,TOTAL_BICYCLES INT NULL
    ,TOTAL_PEDESTRIANS INT NULL
    ,PEDESTRIANSIMPAIRED INT NULL
    ,BICYCLISTSIMPAIRED INT NULL
    ,DRIVERSIMPAIRED INT NULL
    ,TOTAL_TAXIS INT NULL
    ,TOTAL_GOVERNMENT INT NULL
    ,SPEEDING_INVOLVED INT NULL
    ,NEARESTINTROUTEID VARCHAR NULL
    ,NEARESTINTSTREETNAME VARCHAR NULL
    ,OFFINTERSECTION VARCHAR NULL
    ,INTAPPROACHDIRECTION VARCHAR NULL
    ,LOCATIONERROR VARCHAR NULL
    ,LASTUPDATEDATE TIMESTAMP NULL
    ,MPDLATITUDE VARCHAR NULL
    ,MPDLONGITUDE VARCHAR NULL
    ,MPDGEOX VARCHAR NULL
    ,MPDGEOY VARCHAR NULL
    ,BLOCKKEY VARCHAR NULL
    ,SUBBLOCKKEY VARCHAR NULL
    ,FATALPASSENGER INT NULL
    ,MAJORINJURIESPASSENGER INT NULL
    ,MINORINJURIESPASSENGER INT NULL
    ,UNKNOWNINJURIESPASSENGER INT NULL
    ,geometry geometry null
    );
GRANT ALL PRIVILEGES ON crashes_raw TO PUBLIC;
""")

engine.execute("""
CREATE TABLE IF NOT EXISTS all311 (
   OBJECTID VARCHAR NULL
    ,SERVICECODE VARCHAR NULL
    ,SERVICECODEDESCRIPTION VARCHAR NULL
    ,SERVICETYPECODEDESCRIPTION VARCHAR NULL
    ,ORGANIZATIONACRONYM VARCHAR NULL
    ,SERVICECALLCOUNT VARCHAR NULL
    ,ADDDATE VARCHAR NULL
    ,RESOLUTIONDATE VARCHAR NULL
    ,SERVICEDUEDATE VARCHAR NULL
    ,SERVICEORDERDATE VARCHAR NULL
    ,INSPECTIONFLAG VARCHAR NULL
    ,INSPECTIONDATE VARCHAR NULL
    ,INSPECTORNAME VARCHAR NULL
    ,SERVICEORDERSTATUS VARCHAR NULL
    ,STATUS_CODE VARCHAR NULL
    ,SERVICEREQUESTID VARCHAR NULL
    ,PRIORITY VARCHAR NULL
    ,STREETADDRESS VARCHAR NULL
    ,XCOORD VARCHAR NULL
    ,YCOORD VARCHAR NULL
    ,LATITUDE VARCHAR NULL
    ,LONGITUDE VARCHAR NULL
    ,CITY VARCHAR NULL
    ,STATE VARCHAR NULL
    ,ZIPCODE VARCHAR NULL
    ,MARADDRESSREPOSITORYID VARCHAR NULL
    ,WARD VARCHAR NULL
    ,DETAILS VARCHAR NULL
    ,geometry geometry null
    );
GRANT ALL PRIVILEGES ON all311 TO PUBLIC;
""")