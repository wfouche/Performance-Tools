
def get_elapsed_time(t_begin, t_end):
    x = int(t_end - t_begin)
    hh = (x / 3600)
    mm = ((x - (hh*3600)) / 60)
    ss = (x - (hh*3600) - (mm*60))
    return "%02d:%02d:%02d"%(hh,mm,ss)

