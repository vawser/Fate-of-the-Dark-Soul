LuaP		?	?h??}A       =(none)                    :          RegisterTableGoal        GOAL_BlueMan_SpearShield        REGISTER_GOAL_NO_SUB_GOAL        Goal        Update        Update_FinishOnNoSubGoal        Initialize 	       Activate        BlueMan_SpearShield_Hustle        CallFriend        BlueMan_SpearShield_ATT3004 
       ActBase01      p?@       Act01 
       ActBase02      r?@       Act02 
       ActBase03      t?@       Act03 
       ActBase04      x?@       Act04 
       ActBase05      z?@       Act05 
       ActBase06      |?@       Act06        AfterAction        Interrupt_UseItem         Interrupt_MovedEnd_OnFailedPath        Interrupt_FindAttack        Interrupt_Damaged        Interrupt_Shoot        GOAL_BlueMan_DirectSword     ??.A    ??.A    ??.A    ??.A     ?.A       GOAL_BlueMan_Deep        Interrupt_FindAttack_Default        BlueMan_Deep_ATT3002        BlueMan_Deep_Dance        BlueMan_Deep_KeepDist        BlueMan_Deep_Runaway     8?>A    :?>A    ;?>A    <?>A       GOAL_BlueMan_Erection     <?FA    =?FA       GOAL_BlueMan_PlayingDead     \?NA    ]?NA   ?]?NA3                                      _COMMON_InitEnemyAct        SetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE             
         ?   Y ˾ ?  ?  Y ?          E                            GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF 
       GetNumber                GetDist        TARGET_ENE_0        GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        GetTeamOrder        ORDER_TYPE_Role        GetNpcThinkParamID        HasSpecialEffectId     ?D?@       BlueMan_SpearShield_Hustle 
       SetNumber      ??@       CallFriend        ROLE_TYPE_Torimaki       T@       Torimaki_Act        ROLE_TYPE_Kankyaku        Kankyaku_Act       &@      N@       BlueMan_SpearShield_ATT3004        AfterAction        _COMMON_SetEnemyActRate        _COMMON_SelectEnemyAct      ?   ?? A  ?  ? ?? A  ?  ? ?? A  ?  ? K?  ??˿ ? 	??˿ A  
??K? 	 ??	? 
?? ? ??K?  ???? ? ?  ? ?  ?? @ T?      ?   Y ?? A  A  Y ?? ? ?? ? T? W? ?? ? T? ?     ?   Y ?? ? A  Y T? վ T?  ? ?? A ?  ?     Y T? վ T? ? ? ?? A   ?     Y T? W?? ?? E ? ?     ?   ?   
?E     ?     Y?? E     ?   A  Y??     ?     ??UF??       ?   ?	?? ?
 ? ?  
?E     ?     Y??          ?                 	          AddSubGoal        GOAL_COMMON_AttackTunableSpin       @     p?@       TARGET_ENE_0 
       DIST_None               ??      ??       ?>E  ?  ?   E 	? 
 Y??  ?          ?                           AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@     \?@       TARGET_ENE_0 
       DIST_None               ??      ??       GOAL_COMMON_LeaveTarget       @      @     [?@       GOAL_COMMON_SidewayMove        GetRandam_Int       .@      >@    >   ?>E  ?  ?   E 	? 
 Y??>E ?  ?  	? 
 Y??>E ?  ? ? 
? ? ? 	?  ? 	? 
?  Y ?>E ?  ?  	? 
 Y??>E ?  ? ? 
? ? ? 	?  ? 	? 
?  Y ?  ?          ?                          &@      *@               Approach_Act      x?@       AddSubGoal        GOAL_EnemyMultiAttack       ??      ??       TARGET_ENE_0       Y@         A  ?  ?   ?    ?	  
 ?Y  ?  ??? 
 E  ?  Y??  ?          ?                         p?@              N@      ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  L?}  	??
? ?  E    ?   ?Y 
??
?    ?  Y?
A 
 
?          ?                         r?@              N@      ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  L?}  	??
? ?  E    ?   ?Y 
??
?    ?  Y?
A 
 
?                                  t?@     v?@     @U@      N@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ??? 	? 
K@ A ? ?      ?  Y K@ ? ?      ?Y ?  ?                                  x?@              N@      ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  L?}A   	??
? ?  E    ?   ?Y 
??
?    ?  Y?
A 
 
?          8                        z?@              N@      ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       Y@         A  ?  L?}A   	??
? ?  E    ?   ?Y 
??
?    ?  Y?
? 
 
?          R                        |?@     ~?@     ?V@            ???@      Y@      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack          A  ?  ?  ??~A 	? 
K@ A ? ?      ?  Y K@ ? ?      ?Y A  ?          r                           GetRandam_Float               Y@     @U@      9@      I@!       GetWellSpace_Act_IncludeSidestep        ???? ˾ ?  ?  ? ?  T?  A ? A ?  ?  	?  
?  ?      ?   ?   ?  Y ?          ?                              ?          ?                              ?          ?                              ?          ?                          GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF        GetDist        TARGET_ENE_0       4@       GetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE               @      @       ClearSubGoal       N@      D@!       GetWellSpace_Act_IncludeSidestep        SetStringIndexedNumber        HIR_DAMAGE_AVOID       >@    B   ?? A  ?  ? K?  ??˿ ? ???? A ??????? A 	????W? T? ?? A 
??????? ?? ?? ?? A 
???? T? ?AY ?  ? 	? 
? ? ? ?   ?      ?   ?   ?  Y ?  ?? ? 
?? ? ??L?Y    ?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetRelativeAngleFromTarget        GetToTargetAngle        @      >@      @      ?      .@      .?       ClearSubGoal               N@      D@!       GetWellSpace_Act_IncludeSidestep     8   ?? A  ?  ? ?? A  ?  ? K?  ??˿  ???  	??W?? T? ?? ?? ?@ T? ?? ?? W? T? ?? ?? ?? T? ?AY ?  ? 	? 
 ? ? ? E  ?      ?   ?   ?  Y ?     ?          A                          _COMMON_InitEnemyAct        SetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE             
         ?   Y ˾ ?  ?  Y ?          g                          GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF        GetDist        TARGET_ENE_0                GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        GetTeamOrder        ORDER_TYPE_Role        ROLE_TYPE_Torimaki        Torimaki_Act        ROLE_TYPE_Kankyaku        Kankyaku_Act        _COMMON_SetEnemyActRate        _COMMON_SelectEnemyAct         AfterAction     O   ?? A  ?  ? ?? A  ?  ? ?? A  ?  ? K?  ??˿ ? 	??? ?? 	E ??	? 
? ??
վ T?  ? ?? ? E  ?    ?Y 
? վ T? ? ? ?? ? ?  ?    ?Y ?      ?   A  Y?E     ?     ?????  ?    ?    ??   ? ?  FC     ?     Y??          ?                        p?@     r?@      T@      N@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ?? 	? 
K@ A ? ?      ?  Y K@ ? ?      ?Y ?  ?          ?                        t?@     v?@     x?@     ?V@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ?? 	? 
K@ A ? ?      ?  Y K@ ? ?  ?   ?  Y??  ?          ?                        z?@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?}A  ?  ??	E ? ?       ?  Y 	??	E ? ?  ?  Y?	 	 	?                                  ~?@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       Y@         A  ?}A  ?  ??	E ? ?       ?  Y 	??	E ?  ?  ?  Y?	? 	 	?          *                        ??@              ??      >@       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       Y@         A  ?}A  ?  ??	E ? ?       ?  Y 	??	E ?  ?  ?  Y?	? 	 	?          D                	           GetRandam_Float               Y@      >@      4@      *@      @!       GetWellSpace_Act_IncludeSidestep        ???? ˾ ?  ?  ? ?  T? ?    A ?  ? 	? 
  ?      ?   ?   ?  Y ?          v                              ?          |                              ?          ?                              ?          ?                          GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF        GetDist        TARGET_ENE_0       4@       GetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE               @      @       ClearSubGoal      @P@     ?A@!       GetWellSpace_Act_IncludeSidestep        SetStringIndexedNumber        HIR_DAMAGE_AVOID       .@    B   ?? A  ?  ? K?  ??˿ ? ???? A ??????? A 	????W? T? ?? A 
??????? ?? ?? ?? A 
???? T? ?AY ? ? 	? 
? ? ? ?   ?      ?   ?   ?  Y ?  ?? ? 
?? ? ??L?Y    ?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetRelativeAngleFromTarget        GetToTargetAngle        @      >@      @      ?      .@      .?       ClearSubGoal              @P@     ?A@!       GetWellSpace_Act_IncludeSidestep     8   ?? A  ?  ? ?? A  ?  ? K?  ??˿  ???  	??W?? T? ?? ?? ?@ T? ?? ?? W? T? ?? ?? ?? T? ?AY ? ? 	? 
? ? ?  E  ?      ?   ?   ?  Y ?     ?                                    _COMMON_InitEnemyAct        SetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE         	       SetTimer              ?   Y ˾ ?  ?  Y ?? ?  ?  Y ?          B                          GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF 
       GetNumber                GetDist        TARGET_ENE_0        GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        GetTeamOrder        ORDER_TYPE_Role       @       IsFinishTimer        BlueMan_Deep_Dance 
       SetNumber        ROLE_TYPE_Torimaki        BlueMan_Deep_KeepDist        ROLE_TYPE_Kankyaku        Kankyaku_Act       @     @P@       _COMMON_SetEnemyActRate        _COMMON_SelectEnemyAct         AfterAction     u   ?? A  ?  ? ?? A  ?  ? ?? A  ?  ? K?  ??˿ ? 	??K?  
??? 	?? 
? ??
K?  ??? ?? ? T? ?? ?? ? ? ??? U T? ?     ?   Y ?? ? A  Y T? ?> ? E ? T? ?     ?   Y ?? ?> T? ? ? ?? ?   ?     Y ?
? ?? ?? ?? A  ?  ? D T? ?     ?   Y ? ?     ?   A  Y?     ?     ???D??       ?   ??? ?	 ? ?  	E     ?    ?Y??          ?                         "@      &@               Approach_Act      t?@       AddSubGoal        GOAL_EnemyMultiAttack       ??      ??       TARGET_ENE_0       Y@         A  ?  ?   ?    ?	  
 ?Y  ?  ??? 
 E  ?  Y??  ?          ?                
          AddSubGoal        GOAL_COMMON_AttackTunableSpin       4@     |?@       TARGET_NONE 
       DIST_None               ??      ??      Y@       ?>E  ?  ?   E 	? 
 Y?A  ?          ?                          AddSubGoal        GOAL_COMMON_LeaveTarget       @       TARGET_ENE_0       @      ??      ??       GOAL_COMMON_AttackTunableSpin       $@     x?@
       DIST_None        GOAL_COMMON_SidewayMove        GetRandam_Int               .@      >@      Y@    .   ?>E  ?  ?   ?  	? 
? Y??>?  A ?  ? 	? 
? Y??>E  ?  ?   ?  	? 
? Y??>? ?  ?  ?? A 
A ? ?? 	? ? ? 	? 
? ͿY?  ?          ?                
          AddSubGoal        GOAL_COMMON_AttackTunableSpin       4@     |?@       TARGET_ENE_0 
       DIST_None               ??      ??      Y@       ?>E  ?  ?   E 	? 
 Y?A  ?          ?                        p?@     r?@     @P@              ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ??~?  ?  	??
? ?  E    ?   ?Y 
??
?        ?Y 
A 
 
?          ?                        t?@              ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?}A  A  K?	 A ? ?      ?  Y 	K?	 ? ?  ?  Y?	? 	 	?                                  v?@              ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?}A  A  K?	 A ? ?      ?  Y 	K?	 ? ?  ?  Y?	? 	 	?          !                        x?@              N@      ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  L?}A  A  	??
E ? ?     ?   ?Y 
??
E ? ?  ?  Y?
 
 
?          <                           GetRandam_Float               Y@      >@     ?F@      9@!       GetWellSpace_Act_IncludeSidestep        ???? ˾ ?  ?  ? ?  T? ?   A ? ?  ?  	?  
?  ?      ?   ?   ?  Y ?          o                          GetRandam_Int       ??      Y@
       GetHpRate        TARGET_SELF        GetDist        TARGET_ENE_0       4@       GetStringIndexedNumber        HIR_DAMAGE_AVOID_FATE               @      @       ClearSubGoal      @P@     ?A@!       GetWellSpace_Act_IncludeSidestep        SetStringIndexedNumber        HIR_DAMAGE_AVOID       .@    B   ?? A  ?  ? K?  ??˿ ? ???? A ??????? A 	????W? T? ?? A 
??????? ?? ?? ?? A 
???? T? ?AY ? ? 	? 
? ? ? ?   ?      ?   ?   ?  Y ?  ?? ? 
?? ? ??L?Y    ?          ?    
                      _COMMON_InitEnemyAct        GuardMoveOdds         	       WaitOdds        GuardWaitOdds        SideWayOdds       $@
       LeaveOdds        SideStepOdds        BackStepOdds        KeepDistOdds 	       NoneOdds        MinDist ffffff@       MaxDist ffffff@       _COMMON_SetEnemyActRate       ??       _COMMON_SelectEnemyAct       Y@        AfterAction     -         ?   Y 	?} 	?~ 	? 	? 	?? 	?? 	?? 	?? 	?? ?A? IB?      ?   A Y??     ?     ??? ????  ?    ?   ?	?? ??C     ?     	Y??          ?                        p?@     r?@      T@              ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ??~?  ?  	??
? ?  E    ?   ?Y 
??
?        ?Y 
A 
 
?          ?                        t?@              ??       AddSubGoal        GOAL_EnemyBeforeAttack       @       TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?}A  A  K?	 A ? ?      ?  Y 	K?	 ? ?  ?  Y?	? 	 	?          ?                           GetRandam_Float               Y@      I@      $@      4@!       GetWellSpace_Act_IncludeSidestep        ???? ˾ ?  ?  ? ?  T? ?   A A ?  ? 	A 
?  ?      ?   ?   ?  Y ?          C    
                      _COMMON_InitEnemyAct        GuardMoveOdds         	       WaitOdds       ??       GuardWaitOdds        SideWayOdds 
       LeaveOdds        SideStepOdds        BackStepOdds        KeepDistOdds 	       NoneOdds        MinDist ffffff@       MaxDist ffffff@       _COMMON_SetEnemyActRate        _COMMON_SelectEnemyAct       Y@        AfterAction     -         ?   Y 	?} ??~ 	? 	?? 	?? 	?? 	?? 	?? ??? ?A? IB?      ?    Y?E     ?     ??? U???  ?    ?   ?	?? ??C     ?     	Y??          n                        p?@      T@      @               AddSubGoal        GOAL_EnemyBeforeAttack        TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ?  ??	E ?  ? ?      ?  Y 	??	 ? ?  ?  Y?	? 	 	?          ?                        t?@     ?V@      @               AddSubGoal        GOAL_EnemyBeforeAttack        TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ?  ??	E ?  ? ?      ?  Y 	??	 ? ?  ?  Y?	? 	 	?          ?                        v?@     ?V@      @               AddSubGoal        GOAL_EnemyBeforeAttack        TARGET_ENE_0        TARGET_SELF        GOAL_EnemyMultiAttack       ??      ??      Y@         A  ?  ?  ?  ??	E ?  ? ?      ?  Y 	??	 ? ?  ?  Y?	? 	 	?          ?                           GetRandam_Float               Y@       AddSubGoal        GOAL_EnemyAfterAction        @      @       TARGET_ENE_0        GuardMoveOdds 	       WaitOdds        GuardWaitOdds        SideWayOdds 
       LeaveOdds        SideStepOdds        BackStepOdds        KeepDistOdds 	       NoneOdds        MinDist        MaxDist        ??T? ˾ ?  ?  ? ?  ?? ??E ˾ ? 	? 
?   	?@ 
A FA ?A ?A B FB ?B ?B C FC Y??  ?      E  A  Y? ?   E  ? Y? ?   E I  ?   "  I ? ?   b  I?? ?     ?   G  "  ?  ?   ??? ?   b I?? ?   IB? ?   ? I ? ?   	Å ?   ? I?? ?   ?C? ?   " I ? ?   ?Ĉ ?   b I?? ?   IE? ?   ? I ? ?   ? I?? ?   " I ? ?   b I?? ?   ? I ? ?   ? I?? ?   " I ?    ? ? Y? ?   ? ? Y? ?   E I  ?   b I ? ?   ? I?? ?   ?ǂ ?   ? I?? ?   ?G? ?   " I ? ?   	ȅ ?   b I?? ?   IH? ?   ? I ? ?   ?Ȉ ?   ? I?? ?   " I?? ?   b I ? ?   ? I?? ?   ? I ? ?   " I?? ?   b I ?    E
 A
 Y? ?   E
 ? Y? ?   ?
 I ? ?   E I  ?   ? I ? ?   ? I?? "  ?
  b    ?  G  ?  ?  ?   Iʂ ?   "	 I?? ?   ?J? ?   b	 I ? ?   ?ʅ ?   ?	 I?? ?   	K? ?   ?	 I ? ?   "
 I?? ?   b
 I??    ? ? Y? ?   ? ? Y? ?   ?
 I ? ?   E I  ?   ?
 I?? ?   ?˂ ?   ?
 I?? ?   ?K? ?   " I ? ?   b I??    ? ? Y? ?   ? ? Y? ?   E I  ?   ? I?? ?   Î ?   ? I?? ?   ?L? ?   " I ? ?   ?̅ ?   b I?? ?   ? I?? ?  