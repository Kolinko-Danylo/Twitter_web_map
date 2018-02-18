import folium
import geocoder
import twitter_data


def info(dic):
    """
    dict -> str
    :return: information about twitter account.
    """
    inform = ['name: ', 'description :', 'location: ', 'followers_count: ',
              'screen_name: ', 'friends_count: ']
    # create hyperlink
    times, flag = dic['description'].count('http'), 0
    for i in range(times):
        flag = dic['description'].find('http', flag + 1)
        if flag != -1:
            new_location = dic['description'][flag:].split()[0]
            dic['description'] = dic['description'].replace(new_location,
                                                            '<a href="{}">link</a>'.format(
                                                                new_location))
    return ''.join([i.capitalize() + str(dic.get(i[:-2], '')) + '<br>'
                    for i in inform])


def map_creator(data):
    """
    list -> None
    :param data: list of the strings, where contains names of different users.
    Create folium map with icons, each icon corresponds with one
                                                            account location.
    """
    twi_fg = folium.FeatureGroup(name='Users')
    twi_map = folium.Map(location=geocoder.location('Lisabon'), zoom_start=2,
                         tiles='Stamen Toner')
    for i in data:
        user = twitter_data.account(i)
        place = user.get('location', False)
        if place:
            # get coordinates
            coor = geocoder.location(place)
            twi_fg.add_child(folium.Marker(location=coor, popup=info(user),
                                           icon=folium.Icon()))
    twi_map.add_child(twi_fg)
    twi_map.save('templates/Twi_map.html')
