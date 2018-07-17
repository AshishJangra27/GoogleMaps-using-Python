api = 'goole_maps_api_goes_here'

def save(des, loc_short_name, loc_long_name, state_long_name, state_short_name, country_long_name, country_short_name, addr, longitude, lattitude):
    fd = open('History.txt','a+')
    fd.write(des)
    fd.write(' ')
    fd.write(loc_short_name)
    fd.write(' (')
    fd.write(loc_long_name)
    fd.write(') ')
    fd.write(state_long_name)
    fd.write(' (')
    fd.write(state_short_name)
    fd.write(') ')
    fd.write(country_long_name)
    fd.write(' ')
    fd.write(country_short_name)
    fd.write(' (')
    fd.write(addr)
    fd.write(') ')
    fd.write('Longitude: ')
    fd.write(str(longitude))
    fd.write(' ')
    fd.write('Lattitude: ')
    fd.write(str(lattitude))
    fd.write('\n')
    fd.close()

def offline(des):
    
    fd = open('History.txt','r')
    tot_map_list = fd.readlines()
    len_tot=  len(tot_map_list)
    sp_list=[]
    for i in range(0,len_tot):
        sp_list.append(tot_map_list[i].split())
    
    ref = 0
    for i in range(0,len_tot):
        if(sp_list[i][0] == des):
                print('  *****************************************************************************')
                print('                               You are Offline                                 ')
                print('                        This location is saved offline                         ')
                print('             Make sure to search new place with internet connected             ')
                print('  *****************************************************************************')
                print("         Location is           :    ",sp_list[i][0],sp_list[i][2])
                print("            State              :    ",sp_list[i][3],sp_list[i][4])
                print("           Country             :    ",sp_list[i][5],'('+sp_list[i][6]+')')
                print("       Overall Address         :    ",sp_list[i][0],'',sp_list[i][1],'',sp_list[i][2],'',sp_list[i][3],'',sp_list[i][4],'',sp_list[i][5])
                print('  *****************************************************************************')
                print("          Longitude            :    ",sp_list[i][-3])
                print("          Lattitude            :    ",sp_list[i][-1])
                print('  *****************************************************************************')
                ref = 1
                fd.close()
                break

    if ref == 0:
        print('Make Sure to check your Interenet Connection')
        print("We do not have ",des,' saved in offline saved history.')
        print('Internet Connection needed!')
