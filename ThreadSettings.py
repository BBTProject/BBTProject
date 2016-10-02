#-*- coding:utf-8 -*-

class threadSettings:

    #Crucial Settings on thread .
    Init_WorkerNum              = 1
    WorkerPer_Monitor           = 5
    WorkervsQueueLowerBound     = 2
    WorkervsQueueUpperBound     = 4
    WorkerSwing                 = 0.1
    Monitor_check_time          = 0.01
    WorkerMaximum               = 1000
    MonitorMaximum              = 300
    WorkerLaunchInterval        = 0.3
    WorkerStopInterval          = 0.3
    WaitWhenQueueEmptyInterval  = 0.3
    SleepTimeBeforeEnd          = 2
    Switch_Halt                 = False
    Switch_Stop                 = False
    #Inputs from UserInterface.
    target_filetype             = []
    search_keywords             = []
    sql_start_url               = ""
    ISFILESEARCH                = True
    Login_Info                  = []
    result_queue                = None
    flag_queue                  = None
    pauseEvent                  = None
    
    #Debug Switch
    thread_debug            = True
    log_open                = True