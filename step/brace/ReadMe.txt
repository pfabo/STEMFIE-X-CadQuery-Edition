STEP files for brace components

brace_t_dd_hh_pp_ss[s]    basic form
    brace_t_dd_hh_pp          abbreviated forms
    brace_t_dd_hh
    brace_t_dd

    t  - brace type                            dd - brace size               hh - brace height
         B - simple brace                           01 ... 99 BU                  01 =    1 BU
         C - circle brace                                                         ...
         A - arc brace                                                            10 =   10 BU
         X - user defined non standard brace                                      12 =  1/2 BU 
                                                                                  14 =  1/4 BU
        
    ss - number of slots                       pp - number of holes if it does not match the size
         00 ... 99                                  00 ... 99

        
    brace_B_dd_hh_pp_ss
        dd - brace size
        pp - number of holes
        ss - number of slots 
        
    brace_C_dd_hh_pp_ss
        dd - brace radius
        hh - brace height     
        pp - number of holes
        ss - number of slots (TODO, not implemented)

    brace_A_dd_hh_pp_sss
        dd  - brace radius
        hh  - brace height, default value is 1/4 BU      
        pp  - number of holes
        sss - brace angle in [deg] 001 ... 180


    Examples
        brace_B_05          -> brace_B_05_14_05_00     standard brace Brace(5)
        brace_B_05_14_00    -> brace_B_05_14_00_00     brace without holes Brace(5, holes=False)
