USED_ACCOUNT_IDS = []


"""
Should look at if it is a better option to export data to database before the user session ends or 
directly after the information has been added. 

end:
    user closes out of application, stuff doesnt get saved 
    program crashes, stuff again doesnt get saved. 
    less active writing to file??
    
during:
    chances of loss of data is less?
    more writing while program is running? is this even a bad thing?
    


also, STOP PUTTING THIS OFF. your going to have to figure it out sooner or later and implement it 
review the stuff you found about context managers and sqlite. 
"""