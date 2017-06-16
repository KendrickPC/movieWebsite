# Import modules = a module allowing me to logically organize my Python code.
# Grouping related code into a module makes the code easier to understand
# and use.
import fresh_tomatoes
import media
# This is my server-side code to store a list of NBA Finals highlights for the
# past two years. They include box art imagery and a youtube highlights URL.
# The first instance is the ("year, sport, and game #") grouped into a title.
# This is displayed on the front page.
# The second instance is a brief summary about the game.
# The third instance is an image from the game.
# The fourth instance is the youtube highlight URL link.

# begin 2015 season
NBA_Finals_2015_game_1 = media.Movie(
  "2015 NBA Finals game 1",
  "Lebron",
  "https://cdn-s3.si.com/s3fs-public/2015/06/05/lebron-james-cavaliers-warriors-2015-nba-finals-game-1.jpg",  # NOQA
  "https://www.youtube.com/watch?v=PZRVrK0WKRI&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK"  # NOQA
  )

NBA_Finals_2015_game_2 = media.Movie(
  "2015 NBA Finals game 2",
  "Lebron",
  "https://static.sportskeeda.com/wp-content/uploads/2015/06/lebron9-1433741652-800.jpg",  # NOQA
  "https://www.youtube.com/watch?v=2Ic-q2w3rS4&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK&index=2"  # NOQA
  )

NBA_Finals_2015_game_3 = media.Movie(
  "2015 NBA Finals game 3",
  "Lebron",
  "https://cdn-s3.si.com/s3fs-public/images/NBA-Finals-Game-3-u.jpg",
  "https://www.youtube.com/watch?v=ldNVPWhMhQM&index=3&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK"  # NOQA
  )

NBA_Finals_2015_game_4 = media.Movie(
  "2015 NBA Finals game 4",
  "Lebron",
  "http://img.bleacherreport.net/img/images/photos/003/432/347/hi-res-82252136f1c5cc4d9616cf1dfac58210_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top",  # NOQA
  "https://www.youtube.com/watch?v=f5MRavLgH_c&index=4&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK"  # NOQA
  )

NBA_Finals_2015_game_5 = media.Movie(
  "2015 NBA Finals game 5",
  "Lebron",
  "https://www.sikids.com/sites/default/files/sikids/pages/images/cms/imce/users/dantec/2015/06/nba-finals-2015-game5-header.jpg",  # NOQA
  "https://www.youtube.com/watch?v=NtY3a62LT2I&index=5&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK"  # NOQA
  )

NBA_Finals_2015_game_6 = media.Movie(
  "2015 NBA Finals game 6",
  "Lebron",
  "http://img.bleacherreport.net/img/images/photos/003/439/993/67d124e856d72ff6bef91327bf32636f_crop_north.jpg?1434515317&w=630&h=420",  # NOQA
  "https://www.youtube.com/watch?v=C1In0upa5w8&list=PLHggZn5Rw3pds6mSZ4xxOJjJ2awG7zVCK&index=6"  # NOQA
  )
# end 2015 season
# begin 2016 season
NBA_Finals_2016_game_1 = media.Movie(
  "2016 NBA Finals game 1",
  "Lebron",
  "https://pmcdeadline2.files.wordpress.com/2016/06/nba-finals-2016-game-1-june-2-2016.jpg?w=446&h=299&crop=1",  # NOQA
  "https://www.youtube.com/watch?v=3aiQEbjfv8Y"
  )

NBA_Finals_2016_game_2 = media.Movie(
  "2016 NBA Finals game 2",
  "Lebron",
  "http://i.cdn.turner.com/drp/nba/warriors/sites/default/files/getty-images-538304998.jpg",  # NOQA
  "https://www.youtube.com/watch?v=Ae72b10dYdU"
  )

NBA_Finals_2016_game_3 = media.Movie(
  "2016 NBA Finals game 3",
  "Lebron",
  "http://picture.youth.cn/qtdb/201606/W020160617430024529933.jpg",
  "https://www.youtube.com/watch?v=G-GI54oH_oo"
  )

NBA_Finals_2016_game_4 = media.Movie(
  "2016 NBA Finals game 4",
  "Lebron",
  "http://media.cleveland.com/plain-dealer/photo/2016/06/11/-b7ec6760e398c3d5.jpg",  # NOQA
  "https://www.youtube.com/watch?v=cs4FZWcQawQ"
  )

NBA_Finals_2016_game_5 = media.Movie(
  "2016 NBA Finals game 5",
  "Lebron",
  "https://cdn.nba.net/nba-drupal-prod/styles/tile_640w/http/i2.cdn.turner.com/nba/nba/dam/assets/160614103926-lebron-james-kyrie-irving-2016-nba-finals---game-five.1280x720.jpeg?itok=78_1FdtO",  # NOQA
  "https://www.youtube.com/watch?v=494lFLd4OXI"
  )

NBA_Finals_2016_game_6 = media.Movie(
  "2016 NBA Finals game 6",
  "Lebron",
  "http://img15.hostingpics.net/pics/924545133857848867104114521691518969397n.jpg",  # NOQA
  "https://www.youtube.com/watch?v=bzY9xOxltSs"
  )

NBA_Finals_2016_game_7 = media.Movie(
  "2016 NBA Finals game 7",
  "Lebron",
  "https://i.ytimg.com/vi/jPcpJ_J574A/maxresdefault.jpg",
  "https://www.youtube.com/watch?v=oxf17IJBm4A"
  )
# end 2016 season
# begin 2017 season
NBA_Finals_2017_game_1 = media.Movie(
  "2017 NBA Finals game 1",
  "KD",
  "http://media.gettyimages.com/photos/kevin-durant-of-the-golden-state-warriors-reacts-to-a-play-against-picture-id691331486",  # NOQA
  "https://www.youtube.com/watch?v=CT-j2HAhvn0"
  )

NBA_Finals_2017_game_2 = media.Movie(
  "2017 NBA Finals game 2",
  "KD",
  "https://cdn.nba.net/nba-drupal-prod/styles/tile_640w/http/nba.cdn.turner.com/nba/big/video/2017/06/05/dcc99633-50de-4e03-a1ee-b95eb487b03d.nba_1_1280x720.jpg?itok=FiFLnt8i",  # NOQA
  "https://www.youtube.com/watch?v=impWRRca50M"
  )

NBA_Finals_2017_game_3 = media.Movie(
  "2017 NBA Finals game 3",
  "KD",
  "https://img.bleacherreport.net/img/images/photos/003/678/388/hi-res-102088badb96e968ad486d23e51d1a7c_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top",  # NOQA
  "https://www.youtube.com/watch?v=tuDaNHmFm1U"
  )

NBA_Finals_2017_game_4 = media.Movie(
  "2017 NBA Finals game 4",
  "KD",
  "http://images.complex.com/complex/images/fl_lossy,q_auto/v1/xabzj1kuigykvittlztf/kd-lebron-draymond-zaza-game-4-nba-finals",  # NOQA
  "https://www.youtube.com/watch?v=5XVhr6aBAf8"
  )

NBA_Finals_2017_game_5 = media.Movie(
  "2017 NBA Finals game 5",
  "KD",
  "https://cdn.nba.net/nba-drupal-prod/styles/landscape/s3/2017-06/GettyImages-695396452%20%281%29.jpg?itok=7jgqcrcP",  # NOQA
  "https://www.youtube.com/watch?v=F49WUurTz-A"
  )
# end 2017 season

# set the movies that will be passed to the media file
movies = [
  NBA_Finals_2015_game_1, NBA_Finals_2015_game_2, NBA_Finals_2015_game_3,
  NBA_Finals_2015_game_4, NBA_Finals_2015_game_5, NBA_Finals_2015_game_6,
  NBA_Finals_2016_game_1, NBA_Finals_2016_game_2, NBA_Finals_2016_game_3,
  NBA_Finals_2016_game_4, NBA_Finals_2016_game_5, NBA_Finals_2016_game_6,
  NBA_Finals_2016_game_7,
  NBA_Finals_2017_game_1, NBA_Finals_2017_game_2, NBA_Finals_2017_game_3,
  NBA_Finals_2017_game_4, NBA_Finals_2017_game_5
  ]
# open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
