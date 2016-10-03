#-*- coding:utf-8 -*-

class threadSettings:

    #Crucial Settings on thread.
    #Initial Worker num.
    Init_WorkerNum              = 1
    #Indicate Each Monitor Inspects how many workers
    WorkerPer_Monitor           = 3
    #Worker vs Working Queue length lower bound.
    WorkervsQueueLowerBound     = 0.5
    #Worker vs Working Queue length upper bound.
    WorkervsQueueUpperBound     = 0.9
    #Worker number Swing around param.
    WorkerSwing                 = 0.07
    #Monitor check frequency.
    Monitor_check_time          = 0.01
    #Maximum quantity of workers.
    WorkerMaximum               = 5000
    #Minimum quantity of workers.
    MonitorMaximum              = 1000
    #Launch Worker Halting time avoiding of traffic jam.
    WorkerLaunchInterval        = 0.3
    #Stop Worker Halting time avoiding of traffic jam.
    WorkerStopInterval          = 0.3
    #Waiting time for worker when he discovers the queue is empty.
    WaitWhenQueueEmptyInterval  = 0.3
    #Halt time before a worker goes to end when queue is empty.
    SleepTimeBeforeEnd          = 3
    #Sign bit for monitor to detect if all works has been done.
    Switch_Halt                 = False
    Switch_Stop                 = False
    Counter                     = 0
    #Inputs from UserInterface.
    #target file type wanted and selected by user.
    target_filetype             = []
    #Only include file with certain key words.
    search_keywords             = []
    #sqli test starting url
    sql_start_url               = ""
    #Open file searching functionality.
    ISFILESEARCH                = True
    #Login_Info for trying to login pages.
    Login_Info                  = []
    #results put into the result_queue.
    result_queue                = None
    #Sign queue for stopping working.
    flag_queue                  = None
    #Event with pause.
    pauseEvent                  = None
    #Indicating how fierce methods will take to 
    #penetrate target system.
    sqlinjection_class          = 1
    #Debug Switch
    thread_debug                = True
    #Log switch
    log_open                    = True
    