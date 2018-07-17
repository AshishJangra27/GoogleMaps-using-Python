import googlemaps as gm                                                         # To get location from Google Maps
import time                                                                     # Time for data-time
import confidential as cf                                                       # for our functions and google maps api details
ref = gm.Client(key=cf.api)                                                     # Connecting with google maps via our google maps api API

loc_short_name = loc_long_name = state_short_name = state_long_name = 'NA'       # Initialising all variable to NA
country_long_name = country_short_name = pincode  = addr = longitude = lattitude = 'NA'

print('                        ',time.ctime(),'                  ')                     # Print Current Datetime
print('')
des = str(input("         Enter any Location           :     "))                    # Taking input for Location

try:
    geocode_result = ref.geocode(des)[0]                                        # Recieving Full info of that perticulor location in form of a dict
                                                                                # It easy to understand if you prints geocode_result.
except:
    cf.offline(des)                                                             # Searching for offline if internet is not connected
                                                                                # cf.offline searches from offline saved file called (History.txt)
try:                                                                            # Accessing Locations from the Dictionary.
    loc_short_name = geocode_result['address_components'][0:1][0]['long_name']
    loc_long_name = geocode_result['address_components'][1:2][0]['long_name']
    state_short_name = geocode_result['address_components'][2:3][0]['short_name']
    state_long_name = geocode_result['address_components'][2:3][0]['long_name']
    country_long_name = geocode_result['address_components'][3:4][0]['long_name']
    country_short_name = geocode_result['address_components'][3:4][0]['short_name']
    pincode = geocode_result['address_components'][4:5][0]['short_name']
    addr = geocode_result['formatted_address']
    longitude = geocode_result['geometry']['location']['lng']
    lattitude = geocode_result['geometry']['location']['lat']
except:
    pass
                                                                                # Printing the values that we get from Previous try block

print('  *****************************************************************************')
print("         Location is           :    ",loc_short_name,'('+loc_long_name+')')
print("            State              :    ",state_long_name,'('+state_short_name+')')
print("           Country             :    ",country_long_name,'('+country_short_name+')')
print("       Overall Address         :    ",addr)
print('  *****************************************************************************')
print("          Longitude            :    ",longitude)
print("          Lattitude            :    ",lattitude)
print('  *****************************************************************************')
cf.save(des, loc_short_name, loc_long_name, state_long_name, state_short_name, country_long_name, country_short_name, addr, longitude, lattitude)
print("                            Location Saved Sucessfully                         ")
print('  *****************************************************************************')


