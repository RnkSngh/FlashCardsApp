#maps bin # to number of seconds to wait until next card showing
bin_dict = {
    1:5,
    2:25,
    3:2*60,
    4:10*60,
    5:60*60,
    6:5*60*60,
    7:24*60*60,
    8:5*24*60*60,
    9:25*24*60*60,
    10:4*30*24*60*60,
    11:0, # Wods in 11 and bin -1 will not be selected in the get_word endpoint
    -1:0
}
