#-*- coding:utf-8 -*-

class threadSettings:

    #Crucial Settings on thread .
    Init_WorkerNum              = 1
    WorkerPer_Monitor           = 6
    WorkervsQueueLowerBound     = 1
    WorkervsQueueUpperBound     = 2
    WorkerSwing                 = 0.08
    Monitor_check_time          = 0.01
    WorkerMaximum               = 50000
    WorkerLaunchInterval        = 0.3
    WorkerStopInterval          = 0.3
    WaitWhenQueueEmptyInterval  = 0.3
    SleepTimeBeforeEnd          = 3
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