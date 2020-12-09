# social_facility (residenze per anziani) update 

# aggiunge tag source=RAFVG
add_source = False
source = 'RAFVG'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Mpaaf>
# True -> relying only on geometric matching every time
no_dataset_id = True
# anagrafe regionale delle strutture turistico-ricettive
dataset_id = 'hquw-jvsj'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
#query = [('amenity', 'fuel'),('waterway', 'fuel')] both conditions
#query = [('amenity', 'fuel')],[('waterway', 'fuel')]  or condition
#query = [('amenity', 'fuel'),('disused:amenity','fuel')]  namespace disused and abandoned are implicit
#query = [('amenity', 'fuel'),('ref:mise','.*')] 
query = [('amenity', 'social_facility')]

# parameter --osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/10VJ 
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True


# tags to replace on matched OSM objects
master_tags = ('name','phone','operator')

delete_unmatched = False
#tag_unmatched = { 'fixme':'questo albero può essere abbattuto/declassificato' }


# max distance to search for a match in meters
#max_distance = 30 matched 0
#max_distance = 130 matched 15 (error suggesting merge different POIs)
max_distance = 150

