LuaP		?	?h??}A       =(none)                              RegisterTableGoal &       GOAL_610000_PowerKnight_BigBow_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate ,       GOAL_610000_PowerKnight_BigBow_Battle_Act01 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act02 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act03 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act04 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act05 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act20 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act21 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act22 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act23        Update 
       Terminate 
       Interrupt ;       GOAL_610000_PowerKnight_BigBow_Battle_ActAfter_AdjustSpace            ,                            ?          3                 9          Init_Pseudo_Global        SetStringIndexedNumber        Dist_SideStep       @       Dist_BackStep        Common_Clear_Param        GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkattr_doAdmirer        GetEventRequest 
       GetHpRate        TARGET_SELF !       AddObserveSpecialEffectAttribute      >?@       HasSpecialEffectId      ??@       IsInsideTargetRegion     ?,QA       GetNpcThinkParamID     ܝ"A    ??"A    ??"A       @      @       IsInsideTarget        AI_DIR_TYPE_B      ?f@      4@      7@      (@    ???@    ???@   ??,QA       AddSubGoal        GOAL_COMMON_Wait                @      @       REGIST_FUNC ,       GOAL_610000_PowerKnight_BigBow_Battle_Act01 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act02 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act03 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act04 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act05 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act20       5@,       GOAL_610000_PowerKnight_BigBow_Battle_Act21       6@,       GOAL_610000_PowerKnight_BigBow_Battle_Act22 ,       GOAL_610000_PowerKnight_BigBow_Battle_Act23        DeleteObserve ;       GOAL_610000_PowerKnight_BigBow_Battle_ActAfter_AdjustSpace        Common_Battle_Activate     ?      ?   Y?˾ ?  ?  Y ˾  ?  Y 
  
  
  E  ?   ?	Y ? ? ???? A 	? 
? K?  
???? 	? 	? 
? ??
?? ? A Y ? ? ? ? ?T? ?? ? A ? ??? ? ? U??? ? ? ??? ? ? ? ?? T ? 	A??? 	??? ?? ? E ? ???T ? 	???? ? ? A ? ?T ? 	A??? ??? ?? ? ? ? ? X?T? ? ? ? ? X?T ? 	???? 	?~T? ?? ? 	 ? ?? ?G?	 A ? ?	 ?	 ?	 Y ?? ?? T ? 	???? ? ? U??? ? ? ??? ? ? ? ?? T ? 	A? ? 	???
  ?   ?
 ? ɂ??
  ?    ? ???
  ?   E ? ɂ??
  ?   ? ? ɂ??
  ?   ? ? ɂ~?
  ?    ? ɂ??
  ?   ? ? ɂ??
  ?    ? ɂ??
  ?   E ? ??? ?	 Y??
  ?   ? ?   ?    ?   ? ?Y??          ?                         p?@     8?@               GetRandam_Int       ??      Y@       AddSubGoal        GOAL_COMMON_Wait        GetRandam_Float ????????       TARGET_ENE_0        GOAL_COMMON_AttackTunableSpin       $@333333??      @       GetWellSpace_Odds     .     A  ?  ?  K?  	A 
? ? ? 
?@ ?  A ? ? ?  ?  ?  Y ? ? 
  ??    ?  ?  ?  Y?? ? 
?@ A ? ? ? ?  ?  ?  Y A ? ?  ?          ?                 
          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@     p?@       TARGET_ENE_0        SuccessDist 	       TurnTime        FrontAngle                GetWellSpace_Odds        ?? E  ?  ?   E 	? 
?   Y? G E  ?          ?                 
          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@      ?@       TARGET_ENE_0        SuccessDist 	       TurnTime        FrontAngle                GetWellSpace_Odds        ?? E  ?  ?   E 	? 
?   Y? G E  ?          ?                         r?@     t?@     8?@               GetRandam_Int       ??      Y@       AddSubGoal        GOAL_COMMON_Wait        GetRandam_Float ????????       TARGET_ENE_0 #       GOAL_COMMON_ComboAttackTunableSpin       @       SetLifeEndSuccess        GOAL_COMMON_ComboFinal       $@333333??      @       AddObserveRegion    ??,QA       GetWellSpace_Odds     @     A  ?  ?  ?  ?? A 
? ? K? 	 ?@ ?  ? ? ? ?  ?  ?  Y 	K? 	 A  ??  ?   ??  ?  ??	?	? Y?	K? 	?    ? ?  ?  ?  Y?	K? 	 ?@ A ? ? ? ?  ?  ?  Y 	KC 	?  ?  Y?	? 	G 	E 	 	?          ?                         z?@     8?@               GetRandam_Int       ??      Y@       AddSubGoal        GOAL_COMMON_Wait        GetRandam_Float ????????       TARGET_ENE_0        GOAL_COMMON_AttackTunableSpin       $@333333??      @       GetWellSpace_Odds     .     A  ?  ?  K?  	A 
? ? ? 
?@ ?  A ? ? ?  ?  ?  Y ? ? 
  ??    ?  ?  ?  Y?? ? 
?@ A ? ? ? ?  ?  ?  Y A ? ?  ?              	                      AddSubGoal        GOAL_COMMON_Turn        @       TARGET_ENE_0      ?V@       GetWellSpace_Odds                ?? E  ?  ?   Y ? G E  ?          %                          IsInsideTarget        TARGET_ENE_0        AI_DIR_TYPE_R      ?f@       AddSubGoal        GOAL_COMMON_SidewayMove 333333@              N@      ??       GetWellSpace_Odds     !   ?> E  ?  ?  ????? ?? E ? E  ?  	? 
? ? Y T? ?? E ? E  A  	? 
? ? Y ? ? ?  ?          5                	          AddSubGoal        GOAL_COMMON_LeaveTarget       @       TARGET_ENE_0       ??      ??      ??       GetWellSpace_Odds                ?? E  ?  ?   ?  	? 
? Y? ? ?  ?          A                          AddSubGoal        GOAL_COMMON_Wait       ??       TARGET_ENE_0                GetWellSpace_Odds        ?? E  ?  ?    	 
Y  G E  ?          M                          Update_Default_NoSubGoal              ?      ?          U                           ?          ^                          IsInterupt        INTERUPT_Inside_ObserveArea        IsInsideObserve                ClearSubGoal        AddSubGoal        GOAL_COMMON_ComboFinal       $@     t?@       TARGET_ENE_0      8?@       DeleteObserve        INTERUPT_Damaged        IsInsideTargetRegion    ??,QA       HasSpecialEffectId        TARGET_SELF     ???@,       GOAL_610000_PowerKnight_BigBow_Battle_Act02 	       paramTbl     /   ?? E  ????? ? ?  ???T? ??Y ??? ?  E ? 	?  
?  Y?K? ?  Y???  ???? ?? E ? ? ??? K?  A ? ?? ?  ?   ? Y ?          x                           ?  ,      E  A  Y? ?   E  ? Y? ?   "  I  ?   b  I? ?   ?  ?   ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?   ? I?? ?   " I ? ?   b I?? ?  ?  ?  