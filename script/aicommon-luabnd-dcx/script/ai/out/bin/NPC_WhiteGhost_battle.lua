LuaP		?	?h??}A       =(none)                              RegisterTableGoal        GOAL_NPC_WhiteGhost_Battle        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate !       GOAL_NPC_WhiteGhost_Battle_Act01 !       GOAL_NPC_WhiteGhost_Battle_Act02 !       GOAL_NPC_WhiteGhost_Battle_Act03 !       GOAL_NPC_WhiteGhost_Battle_Act04 !       GOAL_NPC_WhiteGhost_Battle_Act05 !       GOAL_NPC_WhiteGhost_Battle_Act06 !       GOAL_NPC_WhiteGhost_Battle_Act07 !       GOAL_NPC_WhiteGhost_Battle_Act08 !       GOAL_NPC_WhiteGhost_Battle_Act09 !       GOAL_NPC_WhiteGhost_Battle_Act10         WhiteGhost_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt                                        ?                           3          Common_Clear_Param        GetRandam_Int       ??      Y@       GetExcelParam /       AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer        IsSearchTarget        TARGET_ENE_0        GetEventRequest       @       GetDist        TARGET_LOCALPLAYER 
       GetHpRate        TARGET_SELF        GetNpcThinkParamID     @??@       SetEventMoveTarget    ??oHA	       homeDist        POINT_EVENT       >@       IsInsideTargetRegion     ?oHA   ??oHA       SetStringIndexedNumber        NPC_PointFrontWall     ?oHA      @      (@    ?oHA      @      $@      @       @      .@       REGIST_FUNC !       GOAL_NPC_WhiteGhost_Battle_Act01 !       GOAL_NPC_WhiteGhost_Battle_Act02 !       GOAL_NPC_WhiteGhost_Battle_Act03 !       GOAL_NPC_WhiteGhost_Battle_Act04 !       GOAL_NPC_WhiteGhost_Battle_Act05 !       GOAL_NPC_WhiteGhost_Battle_Act06       @!       GOAL_NPC_WhiteGhost_Battle_Act07        @!       GOAL_NPC_WhiteGhost_Battle_Act08       "@!       GOAL_NPC_WhiteGhost_Battle_Act09 !       GOAL_NPC_WhiteGhost_Battle_Act10         WhiteGhost_ActAfter_AdjustSpace        Common_Battle_Activate     ?   
  
  
     ?   ?	Y ˾ ?  ?  	? ?? E 	??? ? 
???? 	? 	?? 
A ??
? ? ??? ? ???? E ??? ? UB T
? ?? A Y?? ? ???   ?T ? ?? ?? ?? E ? ? X T? ?? E ? ?  T? ?? A ? Y I??? ? T ? I?~? ?? A A Y I???? I??? U? T? ?F T ? I???? I??? ? ??   ? T ? I?~T
? ׂ? T ? I?~T	? I?~?? ? ??   ? T ? I?~? ?? T ? I?~? I???? ?? ??   ? T ? I???? ?? T ? I???? I??T?   ? T ? I??? ?? T ? I?? ? I???  ?   	 ? ?~?  ?   E	 ? ????  ?   ?	 ? ????  ?   ?	 ? ???  ?   
 ? ???  ?   E
 ? ????  ?   ?
 ? ???  ?   E ? ???  ?   ? ? ???  ?    ? ????  ?   E ? ?  ?    ?     ?Y??          ?                           GetDist        TARGET_LOCALPLAYER       @       ClearSubGoal        AddSubGoal        GOAL_COMMON_ApproachTarget        @       TARGET_SELF       ??      ??       GOAL_COMMON_AttackTunableSpin ????????     ?a@            1   ?> E  ??? ? K? Y ?? E ? E  ? 	? 
? A Y??? ? ?  E  	A 
A A Y??? K? Y ?? E ? E  ? 	? 
  A Y??? ? ?  E  	A 
A A Y?A  ?          ?                           AddSubGoal        GOAL_COMMON_LeaveTarget        @       TARGET_LOCALPLAYER      8?@       TARGET_SELF       ??      ??       GOAL_COMMON_AttackTunableSpin ????????     ?a@               ?? E  ?  ?   E 	? 
? Y???  A ? E ? 	? 
? Y??  ?          ?                           GetStringIndexedNumber        NPC_PointFrontWall        POINT_EVENT        SetEventMoveTarget 333333??       AddSubGoal        GOAL_COMMON_AttackTunableSpin      ?a@       TARGET_SELF       ??      ??               GOAL_COMMON_ApproachTarget        @????????    (   ?> A  ???  K?  ?Y??? T? ˿ ?  ? 	 
? ? ? Y?T? ˿  A ?  	 
   ? Y?˿ ? ? ? 	 
? ? ? Y??  ?          ?                                      ?          ?                           AddSubGoal        GOAL_COMMON_AttackTunableSpin 333333??     ?a@       TARGET_SELF       ??      ??               ?? E  ?  ?   ? 	? 
? Y??  ?          ?                           GetStringIndexedNumber        NPC_PointFrontWall        POINT_EVENT        SetEventMoveTarget 333333??       AddSubGoal        GOAL_COMMON_AttackTunableSpin      ?a@       TARGET_SELF       ??      ??               GOAL_COMMON_ApproachTarget       @????????    (   ?> A  ???  K?  ?Y??? T? ˿ ?  ? 	 
? ? ? Y?T? ˿  A ?  	 
   ? Y?˿ ? ? ? 	 
? ? ? Y??  ?          ?                                      ?                                               ?          
                                     ?                                               ?                                     ?          !                          Update_Default_NoSubGoal              ?      ?          )                           ?          2                              ?  .      E  A  Y? ?   E  ? Y? ?   "  I  ?   b  I? ?   ?  ?   ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?  ?  "    ?   b I?? ?   ? I ? ?   ? I?? ?  