LuaP		?	?h??}A       =(none)                               RegisterTableGoal        GOAL_NPC_SnakeShaman_Minion1        REGISTER_GOAL_NO_SUB_GOAL        Goal        Initialize 	       Activate        NPC_SnakeShaman_Minion1_Act19        NPC_SnakeShaman_Minion1_Act01        NPC_SnakeShaman_Minion1_Act02        NPC_SnakeShaman_Minion1_Act03        NPC_SnakeShaman_Minion1_Act04        NPC_SnakeShaman_Minion1_Act05        NPC_SnakeShaman_Minion1_Act06        NPC_SnakeShaman_Minion1_Act20        NPC_SnakeShaman_Minion1_Act21        NPC_SnakeShaman_Minion1_Act22        NPC_SnakeShaman_Minion1_Act23        NPC_SnakeShaman_Minion1_Act24        NPC_SnakeShaman_Minion1_Act25        NPC_SnakeShaman_Minion1_Act40        NPC_SnakeShaman_Minion1_Act41        NPC_SnakeShaman_Minion1_Act42        NPC_SnakeShaman_Minion1_Act43        NPC_SnakeShaman_Minion1_Act44        NPC_SnakeShaman_Minion1_Act45        NPC_SnakeShaman_Minion1_Act46        NPC_SnakeShaman_Minion1_Act47        NPC_SnakeShaman_Minion1_Act48 -       NPC_SnakeShaman_Minion1_ActAfter_AdjustSpace        Update 
       Terminate 
       Interrupt            L                            ?          S                 X          AddSubGoal        GOAL_NPC_BlackGhost_Battle        @       Init_Pseudo_Global        SetStringIndexedNumber        Dist_Rolling ??????@       Dist_BackStep ??????@       AddDistWalk                AddDistRun ????????       Common_Clear_Param        GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0 
       GetHpRate        TARGET_SELF        GetSp        GetMp 
       GetNumber !       AddObserveSpecialEffectAttribute    p?
?A       IsBothHandMode        Madmode        HasSpecialEffectId       H@ffffff??      4@      @      @      I@      @      $@      5@      6@      7@      8@      >@     ?D@      D@     ?E@      @      9@     ??@       IsTargetGuard        SpaceCheck      ?f@       GetStringIndexedNumber      ?F@     ?F?     ?V@     ?V?     ?`@     ?`?       REGIST_FUNC        NPC_SnakeShaman_Minion1_Act01        NPC_SnakeShaman_Minion1_Act02        NPC_SnakeShaman_Minion1_Act03        NPC_SnakeShaman_Minion1_Act04        NPC_SnakeShaman_Minion1_Act05        NPC_SnakeShaman_Minion1_Act06       3@       NPC_SnakeShaman_Minion1_Act19        NPC_SnakeShaman_Minion1_Act20        NPC_SnakeShaman_Minion1_Act21        NPC_SnakeShaman_Minion1_Act22        NPC_SnakeShaman_Minion1_Act23        NPC_SnakeShaman_Minion1_Act24        NPC_SnakeShaman_Minion1_Act25        NPC_SnakeShaman_Minion1_Act40        NPC_SnakeShaman_Minion1_Act41       E@       NPC_SnakeShaman_Minion1_Act42        NPC_SnakeShaman_Minion1_Act43       F@       NPC_SnakeShaman_Minion1_Act44        NPC_SnakeShaman_Minion1_Act45       G@       NPC_SnakeShaman_Minion1_Act46      ?G@       NPC_SnakeShaman_Minion1_Act47        NPC_SnakeShaman_Minion1_Act48 -       NPC_SnakeShaman_Minion1_ActAfter_AdjustSpace        Common_Battle_Activate     ?  ?>E  ?  Y ?   ?   Y??? A ? Y ?? ?  Y ?? A ? Y ?? ?  Y 
  
  
  E  ?   ?	Y ? ?  	? ?? ? 	??K?  
???? 	 ??	? 
 ??
K? ? ????  A Y ?  ?? ? ? ? ? T ? ? ? ??  A ?  ?? ?  ??X T ? ??? F ?? ?  ??X T? V?? ? ? ?? T ? ??? G ?? W? ?? ?G~IƏ	A?	???H?II?IB??? ?B?? ?? ?? ׁ? ? ?ǄIB~IF?Iƒ?? ?ǄIB~IF?Iƒ?? ׁ? ?? ?Ȅ?G~	A??ȓ	??? ??	??	??	A?	??	A?	A?	??	A?? ?? T? ?Ȅ?G~	A?	??	??	??	???G??ǐ	A?	A?Iɒ	A?? ׁ? T? IɄ?G~	A?	??	??	??IƏIF?	???G?	A?	??	A?? ?ȄIF~IF?	??	??	??IƏ?G?	??	A?	A?	??	A???  ? ?   ? 	A??? ? ?? ? ? ??G	~E  ?   ? K? ? ??    U  ? 	??E  ?   A K? A ??    U ?? E  ?    K? A ??    U  ? 	A?E  ?   ? K? A ??    U ?? E  ?   ? K? A ??    U  ? 	??E  ?   A K? A ??    U ?? E  ?    K? A ??    U  ? 	A?E  ?   ? K? A ??    U  ? 	A?E  ?   ? ? ??  U  ? 	A?E  ?   ? ? ??  U T? E  ?   ? ? ??  U  ? 	??V? ? 	??	??	A?	??	A??  ?   ? ? 	???  ?    ? 	~?  ?   E ? 	??  ?   ? ? 	???  ?   ? ? 	???  ?    ? 	???  ?   ? ? 	???  ?   ? ? 	???  ?    ? 	???  ?   E ? 	??  ?   ? ? 	???  ?   ? ? 	??  ?    ? 	??  ?   E ? 	???  ?   ? ? 	??  ?    ? 	???  ?   E ? 	??  ?   ? ? 	??  ?    ? 	??  ?   ? ? 	???  ?    ? 	???  ?   E ? 	???  ?   ? ? ?  ?    ?     ?Y??          \                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF 333333@               IsBothHandMode ffffff@       GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@       NPC_ATK_ButtonTriangle        @????????      @      I@       NPC_Approach_Act_Flex        GOAL_COMMON_AttackTunableSpin        NPC_ATK_R1        GOAL_COMMON_LeaveTarget        GetWellSpace_Odds     a   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ???  ?@ 	? ??	?	T ? ? ?  KA 	 ??	?	E 
?? ? ? 	?  E  ?   Y?	?@ 	? ??	?	? ? 	?  ?  ?   Y?	 ?	??
???  A  ?VD  ?       ?  ?   ?     ?  Y ? E  ?   ?  Y?? ? ?   ?    Y??     ?          ?                $          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF 333333@       IsBothHandMode ffffff@               GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@????????       @      D@       NPC_Approach_Act_Flex       I@       IsInsideTarget        AI_DIR_TYPE_L      ?f@       GOAL_COMMON_SidewayMove 333333??     ?R@     ?V@       NPC_ATK_L1Hold        NPC_ATK_R1        GOAL_COMMON_AttackTunableSpin       N@       GetWellSpace_Odds     ?   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ??? ?  ?@ 	? ??	?	T ? A ? KA 	 ??	?	E 
?? ? ? 	?  E  ? ? ? Y?	 ?	?
? ? ?  ?C  ? ? ?@ ? ???? ?  ?
 ??  ?     ?  ?   ?     ?  Y WD T	? ? ?? W? T? ?D  E ? ???T? ? ?   ? ?> A ? ? ? ? ? Y ? ? ?   A  ?> A ? ? ? ? ? Y ?~ ?? ? ?     ?? ? Y?? ?    ? ? ? Y?? E    ? ? ? Y?T? ?? ?? ? ?     ?? ? Y?? E    ? ? ? Y?? ? E     ?? ? Y??  ? ?  ?          ?                &          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff@       IsBothHandMode       @               GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@????????       @      D@       NPC_Approach_Act_Flex       I@       IsInsideTarget        AI_DIR_TYPE_L      ?f@       GOAL_COMMON_SidewayMove 333333??     ?R@     ?V@       NPC_ATK_L1Hold       T@     ?P@       NPC_ATK_R2        GOAL_COMMON_AttackTunableSpin        NPC_ATK_R2_Hold        GetWellSpace_Odds     ?   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ??? ?  ?@ 	? ??	?	T ? A ? KA 	 ??	?	E 
?? ? ? 	?  E  ? ? ? Y?	 ?	?
? ? ?  ?C  ? ? ?@ ? ???? ?  ?
 ??  ?     ?  ?   ?     ?  Y WD T	? ? ?? W? T? ?D  E ? ???T? ? ?   ? ?> A ? ? ? ? ? Y ? ? ?   A  ?> A ? ? ? ? ? Y ?? ?? ր? ? WD ?? ? ?  ?   ?? ? Y?? ?  ?  ? ? ? Y?? ?E ?? ? ?  ?   ?? ? Y?? ?  	  ? ? ? Y??	? ? ?  	   ?? ? Y?? ?  ?  ? ? ? Y?? WD T? ? ?  	   ?? ? Y?? ? ?  ?   ?? ? Y??  G	 E	  ?          t                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff??       IsBothHandMode                GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@????????       @      >@       NPC_Approach_Act_Flex        GOAL_COMMON_AttackTunableSpin        NPC_ATK_Up_R1        GetWellSpace_Odds     Q   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ??? ?  ?@ 	? ??	?	T ? ? A A 	? ??	?	 
?? ? ?? 	? ?   A A A Y?	 ?	??
A A ? ? ?C  ? A ?@ ? ???? ?  ?
 ??  E     ?  ?   ?     ?  Y ?? ? ? ?  A A A Y??     ?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff@       IsBothHandMode 333333@               GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@????????       @      D@       NPC_Approach_Act_Flex        GOAL_COMMON_AttackTunableSpin        NPC_ATK_Up_R2        GetWellSpace_Odds     Q   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ??? ?  ?@ 	? ??	?	T ? A ? KA 	 ??	?	E 
?? ? ? 	?  E  ? ? ? Y?	 ?	?
? ? ?  ?C  ? ? ?@ ? ???? ?  ?
 ??  ?     ?  ?   ?     ?  Y ? ?    ? ? ? Y??  G E  ?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff??               GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@       IsBothHandMode        NPC_ATK_ButtonTriangle        @????????      N@       GOAL_COMMON_AttackTunableSpin        NPC_ATK_L2        GetWellSpace_Odds     E   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ???  ?@ 	? ??	?	? 
?? ? ?? 	E ? ?     Y?	?B 	? ??	X?	? ?? 	E ? ?     Y?	 ?	??
L??   ? ?C  ?  ?? ? ? ?     Y??     ?                                    GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff??               GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@       SpaceCheck      ?f@       GetStringIndexedNumber        Dist_BackStep        NPC_ATK_ButtonXmark        IsBothHandMode        NPC_ATK_ButtonTriangle        @????????      N@       GOAL_COMMON_AttackTunableSpin        NPC_ATK_L2        GetWellSpace_Odds     Y   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ???  ?@ 	? ??	?	? 
?? ? ?? 	E ? ?     Y?	E 	   
 ? ? KC  ??  	? 
?? ? ?? 	E ? E     Y?	D 	? ??	?	? ?? 	E ? ?     Y?	 ?	??
???  A  E  ?  ?? ? ?      Y??  G E  ?          0                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF ffffff@      @       IsBothHandMode ??????@      ??       GetEquipWeaponIndex        ARM_R        WEP_Primary        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ArrowKeyRight      8?@              D@      I@       GOAL_COMMON_DashTarget       @       GOAL_COMMON_AttackTunableSpin        NPC_ATK_R1        NPC_ATK_R2        GetWellSpace_Odds     U   ?> A  ?  ? ?> A  ?  ? K?  ???? ? ???  ?@ 	? ??	?	T ? ? ? ?A 	E ??	?	? 
?? ? K? 	 A ?  ?   Y?	 ?	?C  ? ? ? T? K? 
?    ??   Y 
K? 
E A ?  ?   Y?
? K? 
?    ??   Y 
K? 
E A ?  ?   Y?
?  
 
 
 
?          z                          GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       GetSp        TARGET_SELF        SpaceCheck      ?f@       GetStringIndexedNumber        Dist_BackStep        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ButtonXmark      8?@              T@      N@ffffff@????????      I@       GetEquipWeaponIndex        ARM_R        WEP_Primary        IsBothHandMode ??????@       GOAL_COMMON_NPCStepAttack        GetWellSpace_Odds     C   ?> E  ??? ?   ? ? ?   ? ?? ? ???     ? 	 
?@ ? ??  ? ? ? K?  	A 
? E  ?   Y??B T? ?? ?? ?  A 	D 
? ??
 ? ?? ?D 
? ??
 
T ? ?  K? 
? A E   ?   ?Y 
    ?          ?                          GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       GetSp        TARGET_SELF       @       SpaceCheck                GetStringIndexedNumber        Dist_Rolling        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_Up_ButtonXmark      8?@     ?F@     ?F?      I@       NPC_ATK_UpLeft_ButtonXmark        NPC_ATK_UpRight_ButtonXmark      ?Q@333333@       GetEquipWeaponIndex        ARM_R        WEP_Primary        IsBothHandMode ffffff@       GOAL_COMMON_NPCStepAttack        GetWellSpace_Odds     ?   ?> E  ??? ?   ? ? ?   ? ?? ? ??׀? ?      ? 	A 
A ? ??  ? ? T? ?? E 	? 
? E   A A Y???      ? 	? 
A ? ??  ? ? ?
?      ? 	A 
A ? ??  ? ? T? WC T? ?? E 	? 
 E   A A Y?
? ?? E 	? 
E E   A A Y??? ?? E 	? 
 E   A A Y??      ? 	A 
A ? ??  ? ? T? ?? E 	? 
E E   A A Y??? ?? T? ?? ?? ? ? ? 	?D 
E ??
? ? ?? KE 
? ??
 
T ?   ?? 
E ? E   ?   ?Y 
 ? ?  ?          ?                          GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       GetSp        TARGET_SELF        SpaceCheck      ?V@     ?V?       GetStringIndexedNumber        Dist_Rolling       I@       AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_Left_ButtonXmark      8?@               NPC_ATK_Right_ButtonXmark      ?Q@333333@       @       GetEquipWeaponIndex        ARM_R        WEP_Primary        IsBothHandMode ffffff@       GOAL_COMMON_NPCStepAttack        GetWellSpace_Odds     z   ?> E  ??? ?   ? ? ?   ? ?? ? ???     ? 	A 
A ? ??  ? ? ?
? ?     ? 	 
A ? ??  ? ? T? ?A T? ?? ? 	? 
 E  A ? ? Y?
? ?? ? 	? 
? E  A ? ? Y??? ?? ? 	? 
 E  A ? ? Y?? ?     ? 	 
A ? ??  ? ? T? ?? ? 	? 
? E  A ? ? Y??? ?? T? ?? ?? ćć 	KD 
 ??
E ? ?? E 
? ??
 
T ? ĊĊ?? 
 ? E   ?   ?Y 
 G E  ?          7                           GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       GetSp        TARGET_SELF        SpaceCheck      ?f@       GetStringIndexedNumber        Dist_Rolling        AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_Down_ButtonXmark      8?@             ?`@     ?`?      I@       NPC_ATK_DownLeft_ButtonXmark        NPC_ATK_DownRight_ButtonXmark      ?Q@333333@      @       GetEquipWeaponIndex        ARM_R        WEP_Primary        IsBothHandMode ffffff@       GOAL_COMMON_NPCStepAttack        GetWellSpace_Odds     ?   ?> E  ??? ?   ? ? ?   ? ?? ? ??W? ? ?     ? 	 
?@ ? ??  ? ? T? K?  	A 
? E  ?   Y??? ?     ? 	? 
?@ ? ??  ? ? ?
? ?     ? 	A 
?@ ? ??  ? ? T? WC T? K?  	A 
 E  ?   Y?
? K?  	A 
E E  ?   Y??? K?  	A 
 E  ?   Y?? ?     ? 	A 
?@ ? ??  ? ? T? K?  	A 
E E  ?   Y??? ?? T? ?? ?? ?Ĉ?Ĉ? 	?D 
? ??
? ? ?? ?E 
? ??
 
T ? ?ċ?ċK? 
? A E   ?   ?Y 
 ? ?  ?          }                          ChangeEquipItem       @       SetStringIndexedNumber 	       Firebomb        GetStringIndexedNumber       ??       AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_ButtonSquare        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?> A  Y?? ?  ?? ?  ????Y ? ?  E ? ? 	 
 Y?? G E  ?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF       $@              @       IsBothHandMode        Guard        NPC_ATK_L1Hold      8?@       SpaceCheck      ?V@     ?V?       IsInsideTarget        AI_DIR_TYPE_R      ?f@       GetWellSpace_Odds        AddSubGoal        GOAL_COMMON_SidewayMove      ?R@    q   ?> A  ?  ? K?  ???? ? ???  A A 	? ??	?	?? W ? ? ?? T ?  	? 	A T? W ? ? ? T ?  	? 	 	? 
    ?  A  ??
? ? T? ? 
    ? ? A  ??
? ? ?? ?B 
 ? ? ??
 
T ?  	?? A  	?  	?? ? 
    ? ? A  ??
? ? T ? A  	? ? ?  
 
 
 
? T? ?? 
?     ??> ? ? ?   ?  Y 
? ?? 
?     ??> ? ? ? ? ?  Y 
?  
 
 
 
?          ?                          GetRandam_Int       ??      Y@       GetDist        TARGET_ENE_0        GetSp        TARGET_SELF       >@        ????????      @       IsBothHandMode        NPC_ATK_L1Hold      8?@       AddSubGoal        GOAL_COMMON_LeaveTarget        GetWellSpace_Odds     :   ?> A  ?  ? K?  ???? ? ???  A ? 	?  
KA ? ????? W ? ? ??  ?  
A ? W ? ? ?  ?  
? T? ? ?     ?     Y?? ? ?     ? ?   Y??     ?                             !       AddObserveSpecialEffectAttribute        TARGET_SELF      ??@       ChangeEquipItem                AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_ButtonSquare        TARGET_ENE_0      8?@       GetWellSpace_Odds       Y@       ?> E  ?  Y K?  Y?˿ ? ?  E ? 	 
 Y? ? ?  ?                                     ChangeEquipItem       ??       AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_ButtonSquare        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?> A  Y?? ?   E ? ? 	 
 Y?? G E  ?          ,                	          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_ArrowKeyRight        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?? E  ?  ?   A 	? 
? Y? ? ?  ?          8                	          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_ArrowKeyLeft        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?? E  ?  ?   A 	? 
? Y? ? ?  ?          D                	          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_Gesture00        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?? E  ?  ?   A 	? 
? Y? ? ?  ?          P                	          AddSubGoal        GOAL_COMMON_AttackTunableSpin       $@       NPC_ATK_Gesture03        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?? E  ?  ?   A 	? 
? Y? ? ?  ?          \                	          AddSubGoal )       GOAL_COMMON_ComboTunable_SuccessAngle180       $@       NPC_ATK_ButtonTriangle        TARGET_ENE_0      8?@               GetWellSpace_Odds       Y@       ?? E  ?  ?   A 	? 
? Y? ? ?  ?          g                           ?          n                          Update_Default_NoSubGoal              ?      ?          x                           ?          ?    
                      GetSp        TARGET_SELF        GetDist        TARGET_ENE_0        GetRandam_Int       ??      Y@       IsInterupt        INTERUPT_FindAttack       @      4@      I@       ClearSubGoal        NPC_SnakeShaman_Minion1_Act40 	       paramTbl     !   ?? E  ??? ?  ???? A ? ? K?  ?? ?? ?@ ? ? ? ?? W? ? ?AY E  ?   ? 	Y ?     ?  F      E  A  Y? ?   E  ? Y? ?   "  I  ?   b  I? ?   ?  ?   ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?  ?  "    b  G  ?  ?  ?  ?  "    ?   b I?? ?   ? I ? ?   ? I?? ?  