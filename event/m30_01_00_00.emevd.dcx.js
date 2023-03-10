// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    //RegisterBonfire(13010000, 3011950, 5, 180, 0);
    //RegisterBonfire(13010002, 3011952, 5, 180, 0);
    //InitializeCommonEvent(20005500, 13010800, 13010001, 3010951, 3011951);
    
    // Bonfires - Skip if in Flameless
    if(!EventFlag(25000141))
    {
        RegisterBonfire(13010001, 3011951, 5, 180, 0); // Dragonslayer Armour
    }
    else
    {
        DeactivateObject(3011951, Disabled);
    }
    
    // Fogwalls
    DeactivateObject(3011273, Enabled);
    DeleteObjectfollowingSFX(3011273, true);
    CreateObjectfollowingSFX(3011273, 101, 4);
    
    DeactivateObject(3011274, Enabled);
    DeleteObjectfollowingSFX(3011274, true);
    CreateObjectfollowingSFX(3011274, 101, 4);
    
    // Tracker Isabell - Reward
    InitializeCommonEvent(20005341, 13010235, 3010235, 70060); 
    
    InitializeEvent(0, 13015470, 0);
    InitializeCommonEvent(20005780, 3011750, 3);
    InitializeCommonEvent(20005780, 3011751, 3);
    InitializeCommonEvent(20005780, 3011753, 3);
    InitializeCommonEvent(20005400, 3010300);
    InitializeCommonEvent(20005400, 3010301);
    InitializeCommonEvent(20005110, 3010350, 3012380);
    InitializeCommonEvent(20005132, 3010413, 1084227584, 3012460);
    InitializeCommonEvent(20005201, 3010414, 700, 1700, 3012480, 0);
    InitializeCommonEvent(20005201, 3010415, 700, 1700, 3012480, 1053609165);
    InitializeCommonEvent(20005210, 3010417, 700, 1700, 1102053376);
    InitializeCommonEvent(20005110, 3010418, 3012380);
    InitializeCommonEvent(20005110, 3010419, 3012380);
    InitializeCommonEvent(20005210, 3010420, 700, 1700, 1077936128);
    InitializeCommonEvent(20005110, 3010430, 3012340);
    InitializeCommonEvent(20005330, 3010431, 3012450, 13015231);
    InitializeCommonEvent(20005110, 3010432, 3012450);
    InitializeCommonEvent(20005110, 3010450, 3012604);
    InitializeCommonEvent(20005111, 3010451, 3010, 3012605);
    InitializeEvent(0, 13015310, 3010460, 706, 1706);
    InitializeCommonEvent(20005110, 3010500, 3012600);
    InitializeCommonEvent(20005215, 3010501, 710, 1710, 1084227584, 1061997773);
    InitializeCommonEvent(20005215, 3010502, 710, 1710, 1084227584, 1067030938);
    InitializeCommonEvent(20005220, 3010503, 703, 1703);
    InitializeCommonEvent(20005220, 3010504, 706, 1706);
    InitializeCommonEvent(20005220, 3010506, 706, 1706);
    InitializeCommonEvent(20005202, 3010507, 710, 1710, 3012530);
    InitializeCommonEvent(20005110, 3010508, 3012600);
    InitializeCommonEvent(20005110, 3010510, 3012472);
    InitializeCommonEvent(20005110, 3010511, 3012472);
    InitializeCommonEvent(20005202, 3010512, 710, 1710, 3012531);
    InitializeCommonEvent(20005200, 3010520, 706, 1706, 3012435);
    InitializeCommonEvent(20005201, 3010521, 706, 1706, 3012435, 1056964608);
    InitializeCommonEvent(20005215, 3010538, 710, 1710, 1084227584, 1060320051);
    InitializeCommonEvent(20005200, 3010539, 703, 1703, 3012600);
    InitializeCommonEvent(20005220, 3010549, 705, 1705);
    InitializeCommonEvent(20005110, 3010551, 3012430);
    InitializeCommonEvent(20005119, 3010557, 3012338, 3012339, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005119, 3010558, 3012338, 3012339, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005110, 3010562, 3012335);
    InitializeCommonEvent(20005110, 3010563, 3012440);
    InitializeCommonEvent(20005110, 3010564, 3012440);
    InitializeCommonEvent(20005110, 3010565, 3012335);
    InitializeCommonEvent(20005110, 3010566, 3012440);
    InitializeCommonEvent(20005202, 3010567, 710, 1710, 3012530);
    InitializeCommonEvent(20005110, 3010568, 3012600);
    InitializeCommonEvent(20005200, 3010569, 703, 1703, 3012470);
    InitializeCommonEvent(20005122, 3010570, 3000, 1084227584);
    InitializeCommonEvent(20005110, 3010571, 3012471);
    InitializeCommonEvent(20005202, 3010572, 710, 1710, 3012530);
    InitializeCommonEvent(20005220, 3010573, 703, 1703);
    InitializeCommonEvent(20005220, 3010574, 706, 1706);
    InitializeEvent(0, 13015230, 0);
    InitializeCommonEvent(20005110, 3010610, 3012490);
    InitializeCommonEvent(20005341, 13010590, 3010610, 13103000);
    InitializeCommonEvent(20000343, 13010591, 3010300, 21201100);
    InitializeCommonEvent(20000343, 13010592, 3010301, 21201000);
    InitializeCommonEvent(20005341, 13010593, 3010310, 21504000);
    InitializeCommonEvent(20005341, 13010593, 3010311, 21504010);
    InitializeEvent(0, 13015550, 3010830);
    InitializeEvent(0, 13015551, 3010831);
    InitializeEvent(0, 13015555, 0);
    InitializeEvent(0, 13015590, 13010890, 3010830, 20);
    InitializeEvent(1, 13015590, 13010891, 3010831, 30);
    InitializeEvent(0, 13015556, 3010835, 13010895, 13010890, 13015550);
    InitializeEvent(0, 13015557, 3010836, 13010896, 13010891);
    InitializeEvent(0, 13015558, 3010835, 3010830, 13010895, 40);
    InitializeEvent(0, 13015559, 3010836, 3010831, 13010896, 41);
    InitializeEvent(0, 13015580, 0);
    InitializeEvent(0, 13015581, 0);
    InitializeEvent(0, 13015585, 0);
    InitializeCommonEvent(20005410, 3010551, 3005);
    InitializeCommonEvent(20005411, 3010551, 3010555, 703, 1703, 1053609165);
    InitializeCommonEvent(20005411, 3010551, 3010556, 705, 1705, 1061997773);
    InitializeCommonEvent(20005411, 3010551, 3010560, 703, 1703, 1063675494);
    InitializeCommonEvent(20005411, 3010551, 3010561, 703, 1703, 1065353216);
    InitializeCommonEvent(20005415, 13011500, 3010500, 3010600, 706, 1706, 0, 13015501, 13015502);
    InitializeCommonEvent(20005415, 13011510, 3010539, 3010602, 703, 1703, 0, 13015503, 13015504);
    InitializeCommonEvent(20005415, 13011520, 3010568, 3010604, 703, 1703, 0, 13015505, 13015506);
    InitializeCommonEvent(20005520, 13010500, 3011450, 3014300);
    InitializeCommonEvent(20005520, 13010501, 3011451, 3014301);
    InitializeCommonEvent(20005520, 13010502, 3011452, 3014302);
    InitializeCommonEvent(20005520, 13010503, 3011453, 3014303);
    InitializeCommonEvent(20005520, 13010504, 3011454, 3014304);
    InitializeCommonEvent(20005520, 13010510, 3011460, 3014310);
    InitializeCommonEvent(20005520, 13010511, 3011461, 3014311);
    InitializeCommonEvent(20005520, 13010512, 3011462, 3014312);
    InitializeCommonEvent(20005520, 13010514, 3011464, 3014314);
    InitializeCommonEvent(20005530, 13015400, 3011300);
    InitializeCommonEvent(20005530, 13015401, 3011301);
    InitializeCommonEvent(20005530, 13015402, 3011302);
    InitializeCommonEvent(20005530, 13015403, 3011303);
    InitializeCommonEvent(20005530, 13015404, 3011304);
    InitializeCommonEvent(20005530, 13015405, 3011305);
    InitializeCommonEvent(20005530, 13015406, 3011306);
    InitializeCommonEvent(20005530, 13015407, 3011307);
    InitializeCommonEvent(20005530, 13015408, 3011308);
    InitializeCommonEvent(20005530, 13015409, 3011309);
    InitializeCommonEvent(20005530, 13015410, 3011310);
    InitializeCommonEvent(20005530, 13015411, 3011311);
    InitializeCommonEvent(20005530, 13015412, 3011312);
    InitializeCommonEvent(20005530, 13015413, 3011313);
    InitializeCommonEvent(20005530, 13015414, 3011314);
    InitializeCommonEvent(20005530, 13015415, 3011315);
    InitializeCommonEvent(20005530, 13015416, 3011316);
    InitializeCommonEvent(20005530, 13015417, 3011317);
    InitializeCommonEvent(20005530, 13015418, 3011318);
    InitializeCommonEvent(20005530, 13015419, 3011319);
    InitializeCommonEvent(20005530, 13015420, 3011320);
    InitializeCommonEvent(20005530, 13015421, 3011321);
    InitializeCommonEvent(20005530, 13015422, 3011322);
    InitializeCommonEvent(20005530, 13015423, 3011323);
    InitializeCommonEvent(20005530, 13015424, 3011324);
    InitializeCommonEvent(20005530, 13015425, 3011325);
    InitializeCommonEvent(20005530, 13015426, 3011326);
    InitializeCommonEvent(20005530, 13015427, 3011327);
    InitializeCommonEvent(20005530, 13015428, 3011328);
    InitializeCommonEvent(20005530, 13015429, 3011329);
    InitializeCommonEvent(20005530, 13015430, 3011330);
    InitializeCommonEvent(20005530, 13015431, 3011331);
    InitializeCommonEvent(20005650, 13010310, 3011390);
    InitializeCommonEvent(20005622, 13010450, 13010452, 3011400, 3011401, 3011402, 13011450);
    InitializeCommonEvent(20005628, 13010451, 3011402, 3012401);
    InitializeCommonEvent(20005620, 13010460, 13010462, 3011410, 3011411, 3011412, 13011460);
    InitializeCommonEvent(20005628, 13010461, 3011412, 3012411);
    InitializeEvent(0, 13015225, 0);
    InitializeEvent(0, 13014522, 0);
    SetObjectInvulnerability(3011500, Enabled);
    SetObjectInvulnerability(3011501, Enabled);
    InitializeEvent(0, 13015200, 13010300, 13010302, 3011491, 13011300);
    InitializeEvent(0, 13015202, 0);
    InitializeEvent(0, 13015210, 13010301, 3011491);
    InitializeCommonEvent(20005610, 13010550, 3012421, 3012420);
    InitializeCommonEvent(20005611, 13010550, 13011580, 3011420, 300320);
    InitializeEvent(0, 13014242, 0);
    RegisterLadder(13010670, 13010671, 3011670);
    RegisterLadder(13010672, 13010673, 3011671);
    RegisterLadder(13010674, 13010675, 3011672);
    RegisterLadder(13010676, 13010677, 3011673);
    InitializeCommonEvent(20005523, 3011270, 1);
    InitializeCommonEvent(20005523, 3011271, 1);
    InitializeCommonEvent(20005523, 3011272, 2);
    InitializeEvent(0, 13015810, 0);
    InitializeEvent(0, 13015811, 0);
    InitializeEvent(0, 13015812, 0);
    InitializeEvent(0, 13015820, 0);
    InitializeEvent(0, 13015815, 0);
    InitializeEvent(0, 13015830, 3010812, 1067030938);
    InitializeCommonEvent(20006010, 73010952, 69003);
    InitializeCommonEvent(20006031, 73010953, 3012750);
});

$Event(50, Default, function() {
    SetCharacterAnimationState(3010790, Disabled);
    SetCharacterGravity(3010790, Disabled);
    SetCharacterMaphit(3010790, true);
    SetMapSoundState(3012803, Disabled);
    SetMapSoundState(3012804, Disabled);
});

$Event(13014242, Restart, function() {
    EndIf(!PlayerIsNotInOwnWorld());
    if (!EventFlag(13010550)) {
        EndEvent();
    }
L0:
    ReproduceObjectAnimation(3011420, 1);
    EndEvent();
});

$Event(13014522, Restart, function() {
    InitializeCommonEvent(20005623, 13010450, 13010452, 3011400, 3011401, 3014401, 3011402, 3014402, 3012401, 3012402, 13011450, 13014450, 13010451);
    InitializeEvent(0, 13015220, 13010460, 3011410, 3011411, 3014411, 3011413, 3014413, 3011412, 3014412);
});

$Event(13015200, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetEventFlag(X12_4, OFF);
    }
    if (!EventFlag(X0_4)) {
        ForceAnimationPlayback(X8_4, 0, false, false, true, 0, 1);
        SetEventFlag(X4_4, OFF);
        EndEvent();
    }
L0:
    ForceAnimationPlayback(X8_4, 2, false, false, true, 0, 1);
    SetEventFlag(X4_4, ON);
    EndEvent();
});

$Event(13015201, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X20_4))) {
        if (!EventFlag(X4_4)) {
            if (NumberOfClientsOfType(ClientType.Invader) != 0) {
                SetObjactState(X12_4, 304874, Enabled);
            }
            obj = ObjActEventFlag(X16_4);
            WaitFor(obj || EventFlag(X0_4));
            if (NumberOfClientsOfType(ClientType.Invader) != 0) {
                SetObjactState(X12_4, -1, Disabled);
            }
            if (NumberOfClientsOfType(ClientType.Invader) != 0) {
                SetNetworkconnectedEventFlag(X20_4, ON);
                SetNetworkconnectedEventFlag(X0_4, ON);
            }
            SetEventFlag(X4_4, ON);
            if (!obj.Passed) {
                GotoIf(L0, EventFlag(X24_4));
                ForceAnimationPlayback(X8_4, 1, false, true, true, 0, 1);
            } else {
L0:
                SetNetworkconnectedEventFlag(X24_4, ON);
                WaitFixedTimeSeconds(2);
                ForceAnimationPlayback(X8_4, 1, false, true, true, 0, 1);
                ForceAnimationPlayback(X12_4, 3, false, false, true, 0, 1);
                SetNetworkconnectedEventFlag(X24_4, OFF);
            }
L1:
            WaitFor(ObjectBackread(X8_4));
            if (NumberOfClientsOfType(ClientType.Invader) != 0) {
                SetNetworkconnectedEventFlag(X20_4, OFF);
            }
            RestartEvent();
        }
L2:
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SetObjactState(X12_4, 304874, Enabled);
        }
        obj2 = ObjActEventFlag(X16_4);
        WaitFor(obj2 || !EventFlag(X0_4));
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SetObjactState(X12_4, -1, Disabled);
        }
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SetNetworkconnectedEventFlag(X20_4, ON);
            SetNetworkconnectedEventFlag(X0_4, OFF);
        }
        SetEventFlag(X4_4, OFF);
        if (!obj2.Passed) {
            GotoIf(L3, EventFlag(X24_4));
            SetEventFlag(X28_4, ON);
            ForceAnimationPlayback(X8_4, 3, false, true, true, 0, 1);
        } else {
L3:
            SetNetworkconnectedEventFlag(X24_4, ON);
            WaitFixedTimeSeconds(2);
            SetEventFlag(X28_4, ON);
            ForceAnimationPlayback(X8_4, 3, false, true, true, 0, 1);
            ForceAnimationPlayback(X12_4, 3, false, false, true, 0, 1);
            SetNetworkconnectedEventFlag(X24_4, OFF);
        }
L4:
        WaitFor(ObjectBackread(X8_4));
        SetEventFlag(X28_4, OFF);
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SetNetworkconnectedEventFlag(X20_4, OFF);
        }
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X20_4));
    RestartEvent();
});

$Event(13015202, End, function() {
    InitializeEvent(0, 13015201, 13010300, 13010302, 3011491, 3011490, 3014500, 13011300, 13014300, 13010301);
});

$Event(13015210, Restart, function(X0_4, X4_4) {
    WaitFor(EventFlagState(CHANGE, TargetEventFlagType.EventFlag, X0_4));
    WaitFixedTimeFrames(2);
    if (EventFlag(X0_4)) {
        WaitFixedTimeSeconds(1.3);
        CreateDamagingObject(13015211, X4_4, 40, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015212, X4_4, 41, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015213, X4_4, 42, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015214, X4_4, 43, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015215, X4_4, 44, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015216, X4_4, 45, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015217, X4_4, 46, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        CreateDamagingObject(13015218, X4_4, 47, 5300, DamageTargetType.Character, 0.8, 0.5, 0);
        RestartEvent();
    }
L0:
    WaitFixedTimeSeconds(2);
    RestartEvent();
});

$Event(13015220, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    WaitFor(EventFlag(13010461));
    if (!EventFlag(X0_4)) {
        SetObjactState(X16_4, 304873, Enabled);
        SetObjactState(X8_4, -1, Disabled);
        SetObjactState(X24_4, -1, Disabled);
        obj = ObjActEventFlag(X20_4);
        obj2 = ObjActEventFlag(X28_4);
        WaitFor(obj || obj2 || EventFlag(X0_4) || InArea(10000, 3012411) || InArea(10000, 3012412));
        SetObjactState(X16_4, -1, Disabled);
        SetObjactState(X24_4, -1, Disabled);
        GotoIf(L0, obj.Passed);
        GotoIf(L1, obj2.Passed);
        ForceAnimationPlayback(X4_4, 21, false, true, true, 0, 1);
        Goto(L2);
L0:
        WaitFixedTimeSeconds(2);
        ForceAnimationPlayback(X4_4, 21, false, true, true, 0, 1);
        ForceAnimationPlayback(X16_4, 3, false, false, true, 0, 1);
        Goto(L2);
L1:
        WaitFixedTimeSeconds(2);
        ForceAnimationPlayback(X4_4, 21, false, true, true, 0, 1);
        ForceAnimationPlayback(X24_4, 3, false, false, true, 0, 1);
        Goto(L2);
L2:
        WaitFor(!AllPlayersInArea(3012412) && !AllPlayersInArea(3012413));
        ForceAnimationPlayback(X4_4, 110, false, true, true, 0, 1);
        ForceAnimationPlayback(X4_4, 10, false, true, true, 0, 1);
        SetEventFlag(X0_4, ON);
        SetObjactState(X8_4, -1, Enabled);
        SetObjactState(X24_4, -1, Disabled);
        RestartEvent();
    }
L3:
    SetObjactState(X8_4, 304873, Enabled);
    SetObjactState(X16_4, -1, Disabled);
    SetObjactState(X24_4, -1, Disabled);
    obj3 = ObjActEventFlag(X12_4);
    obj4 = ObjActEventFlag(X28_4);
    WaitFor(obj3 || obj4 || !EventFlag(X0_4) || InArea(10000, 3012412) || InArea(10000, 3012413));
    SetObjactState(X8_4, -1, Disabled);
    SetObjactState(X24_4, -1, Disabled);
    GotoIf(L4, obj3.Passed);
    GotoIf(L5, obj4.Passed);
    ForceAnimationPlayback(X4_4, 12, false, true, true, 0, 1);
    Goto(L6);
L4:
    WaitFixedTimeSeconds(2);
    ForceAnimationPlayback(X4_4, 12, false, true, true, 0, 1);
    ForceAnimationPlayback(X8_4, 3, false, false, true, 0, 1);
    Goto(L6);
L5:
    WaitFixedTimeSeconds(2);
    ForceAnimationPlayback(X4_4, 12, false, true, true, 0, 1);
    ForceAnimationPlayback(X24_4, 3, false, false, true, 0, 1);
    Goto(L6);
L6:
    WaitFor(!AllPlayersInArea(3012411) && !AllPlayersInArea(3012412));
    ForceAnimationPlayback(X4_4, 120, false, true, true, 0, 1);
    ForceAnimationPlayback(X4_4, 20, false, true, true, 0, 1);
    SetEventFlag(X0_4, OFF);
    SetObjactState(X16_4, 304873, Enabled);
    SetObjactState(X24_4, -1, Disabled);
    RestartEvent();
});

$Event(13015225, Restart, function() {
    EndIf(EventFlag(13010461));
    WaitFor(InArea(10000, 3012412) && !EventFlag(13010461));
    DisplayGenericDialog(10010170, PromptType.OKCANCEL, NumberofOptions.OneButton, -1, 3);
    WaitFor(!InArea(10000, 3012412));
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(13015230, Restart, function() {
    EndIf(ThisEventSlot());
    WaitFor(
        (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.Hollow)
            || CharacterType(10000, TargetType.WhitePhantom))
            && InArea(10000, 3012451))
            || EventFlag(13015231));
    ClearCharactersAITarget(3010505);
    SetSpEffect(3010505, 5000);
    ChangeCharacterPatrolBehavior(3010505, 3014300);
    SetEventFlag(13015231, ON);
    WaitFor(CharacterAIState(3010505, AIStateType.Combat));
    ClearSpEffect(3010505, 5000);
});

$Event(13015310, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    ForceAnimationPlayback(X0_4, X4_4, true, false, false, 0, 1);
    WaitFor(
        (EntityInRadiusOfEntity(10000, X0_4, 3, 1)
            && CharacterBackreadStatus(X0_4)
            && CharacterHasSpEffect(X0_4, 5450)
            && ((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
                || CharacterType(10000, TargetType.Alive)
                || CharacterType(10000, TargetType.Hollow)
                || CharacterType(10000, TargetType.WhitePhantom)))
            || CharacterDamagedBy(X0_4, 10000)
            || CharacterDead(3010418)
            || CharacterDead(3010419));
    EndIf(!CharacterHasSpEffect(X0_4, 5450));
    ForceAnimationPlayback(X0_4, X8_4, false, false, false, 0, 1);
    RequestCharacterAIReplan(X0_4);
});

$Event(13015470, Restart, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(ObjectBackread(3011600));
    WaitFixedTimeFrames(5);
    ShowObjectByMapCeremony(3011600, 10, 2000);
    ShowObjectByMapCeremony(3011601, 30, 1400);
    ShowObjectByMapCeremony(3011602, 10, 790);
    ShowObjectByMapCeremony(3011605, 20, 1010);
    ShowObjectByMapCeremony(3011606, 40, 710);
    ShowObjectByMapCeremony(3011607, 20, 1400);
    ShowObjectByMapCeremony(3011610, 10, 4320);
    ShowObjectByMapCeremony(3011611, 40, 3800);
    ShowObjectByMapCeremony(3011612, 30, 4420);
    ShowObjectByMapCeremony(3011613, 40, 0);
    ShowObjectByMapCeremony(3011615, 110, 0);
    ShowObjectByMapCeremony(3011616, 110, 290);
    ShowObjectByMapCeremony(3011617, 110, 440);
    ShowObjectByMapCeremony(3011628, 110, 880);
    ShowObjectByMapCeremony(3011631, 110, 1640);
    ShowObjectByMapCeremony(3011620, 120, 470);
    ShowObjectByMapCeremony(3011621, 120, 680);
    ShowObjectByMapCeremony(3011622, 120, 920);
    ShowObjectByMapCeremony(3011629, 120, 1250);
    ShowObjectByMapCeremony(3011632, 120, 2070);
    ShowObjectByMapCeremony(3011625, 130, 1030);
    ShowObjectByMapCeremony(3011626, 130, 1280);
    ShowObjectByMapCeremony(3011627, 130, 1440);
    ShowObjectByMapCeremony(3011630, 130, 1880);
    ShowObjectByMapCeremony(3011633, 130, 2640);
    ShowObjectByMapCeremony(3011636, 10, 3100);
    ShowObjectByMapCeremony(3011637, 20, 2500);
    ShowObjectByMapCeremony(3011638, 40, 2300);
    ShowObjectByMapCeremony(3011639, 10, 2110);
    ShowObjectByMapCeremony(3011640, 20, 1920);
    ShowObjectByMapCeremony(3011641, 30, 2400);
    ShowObjectByMapCeremony(3011642, 40, 4790);
    ShowObjectByMapCeremony(3011643, 20, 4900);
    ShowObjectByMapCeremony(3011644, 30, 5490);
    ShowObjectByMapCeremony(3011645, 110, 1000);
    ShowObjectByMapCeremony(3011646, 110, 1290);
    ShowObjectByMapCeremony(3011647, 110, 1440);
    ShowObjectByMapCeremony(3011648, 110, 1880);
    ShowObjectByMapCeremony(3011649, 110, 2640);
    ShowObjectByMapCeremony(3011650, 120, 1470);
    ShowObjectByMapCeremony(3011651, 120, 1680);
    ShowObjectByMapCeremony(3011652, 120, 1920);
    ShowObjectByMapCeremony(3011653, 120, 2250);
    ShowObjectByMapCeremony(3011654, 120, 3200);
    ShowObjectByMapCeremony(3011655, 130, 2030);
    ShowObjectByMapCeremony(3011656, 130, 2280);
    ShowObjectByMapCeremony(3011657, 130, 2440);
    ShowObjectByMapCeremony(3011658, 130, 2880);
    ShowObjectByMapCeremony(3011659, 130, 3640);
    WaitFor(!ObjectBackread(3011600));
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(13015475, Restart, function() {
    EndIf(ThisEventSlot());
    WaitFixedTimeSeconds(0.1);
    IssueShortWarpRequest(3010501, TargetEntityType.Area, 3012510, -1);
    IssueShortWarpRequest(3010502, TargetEntityType.Area, 3012511, -1);
    IssueShortWarpRequest(3010538, TargetEntityType.Area, 3012512, -1);
});

$Event(13015550, Restart, function(X0_4) {
    SetCharacterAIState(X0_4, Disabled);
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetCharacterGravity(X0_4, Disabled);
    SetCharacterMaphit(X0_4, true);
    EndIf(EventFlag(13010895));
    if (!EventFlag(13010890)) {
        if (EventFlag(13010580)) {
            ChangeCharacterEnableState(X0_4, Enabled);
            SetCharacterAnimationState(X0_4, Enabled);
            SetCharacterImmortality(X0_4, Enabled);
            ForceAnimationPlayback(X0_4, 30000, true, false, false, 0, 1);
            EndEvent();
        }
L0:
        WaitFor(EventFlag(13010580));
        WaitFixedTimeSeconds(0);
        ChangeCharacterEnableState(X0_4, Enabled);
        SetCharacterAnimationState(X0_4, Enabled);
        SetCharacterImmortality(X0_4, Enabled);
        ForceAnimationPlayback(X0_4, 20006, false, true, false, 0, 1);
        EndEvent();
    }
L1:
    ChangeCharacterEnableState(X0_4, Enabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetCharacterImmortality(X0_4, Enabled);
    ForceAnimationPlayback(X0_4, 30002, true, false, false, 0, 1);
    SetCharacterHPBarDisplay(X0_4, Disabled);
    SetLockOnPoint(X0_4, 220, Disabled);
    WaitFixedTimeFrames(1);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.Every5Frames);
});

$Event(13015551, Restart, function(X0_4) {
    SetCharacterAIState(X0_4, Disabled);
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetCharacterGravity(X0_4, Disabled);
    SetCharacterMaphit(X0_4, true);
    EndIf(EventFlag(13010896));
    ChangeCharacterEnableState(X0_4, Enabled);
    if (!EventFlag(13010891)) {
        SetCharacterAnimationState(X0_4, Enabled);
    }
    SetCharacterImmortality(X0_4, Enabled);
    if (!EventFlag(13010891)) {
        if (EventFlag(13010580)) {
            ForceAnimationPlayback(X0_4, 30000, true, false, false, 0, 1);
            EndEvent();
        }
L0:
        ForceAnimationPlayback(X0_4, 30001, true, false, false, 0, 1);
        WaitFor(
            ((CharacterType(10000, TargetType.Alive) || CharacterType(10000, TargetType.Hollow))
                && InArea(10000, 3012320))
                || HasDamageType(X0_4, 10000, DamageType.Unspecified));
        ForceAnimationPlayback(X0_4, 20004, false, false, false, 0, 1);
        SetEventFlag(13010580, ON);
        SetEventFlag(9420, ON);
        EndEvent();
    }
L1:
    ChangeCharacterEnableState(X0_4, Enabled);
    SetCharacterAnimationState(X0_4, Disabled);
    ForceAnimationPlayback(X0_4, 30002, true, false, false, 0, 1);
    SetCharacterHPBarDisplay(X0_4, Disabled);
    SetLockOnPoint(X0_4, 220, Disabled);
    WaitFixedTimeFrames(1);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.Every5Frames);
});

$Event(13015555, Restart, function() {
    EndIf(EventFlag(13010890));
    CreateNPCPart(3010831, 10, NPCPartType.Part3, 100, 1, 1, false, false);
    WaitFor(EventFlag(13015550) && EventFlag(13015551));
    CreateNPCPart(3010830, 10, NPCPartType.Part3, 100, 1, 1, false, false);
    WaitFor(
        NPCPartHP(3010830, 10) <= 1
            || NPCPartHP(3010831, 10) <= 1
            || HPRatio(3010830) <= 0.001
            || HPRatio(3010831) <= 0.001);
    SetEventFlag(13010890, ON);
    GotoIf(L0, NPCPartHP(3010830, 10) <= 0);
    GotoIf(L1, NPCPartHP(3010831, 10) <= 0);
    GotoIf(L0, HPRatio(3010830) <= 0.001);
    GotoIf(L1, HPRatio(3010831) <= 0.001);
L0:
    SetCharacterHPBarDisplay(3010830, Disabled);
    SetLockOnPoint(3010830, 220, Disabled);
    ForceAnimationPlayback(3010830, 20005, false, false, false, 0, 1);
    SetCharacterAnimationState(3010830, Disabled);
    WaitFixedTimeSeconds(3);
    SetCharacterHPBarDisplay(3010831, Disabled);
    SetLockOnPoint(3010831, 220, Disabled);
    SetCharacterAnimationState(3010831, Disabled);
    ForceAnimationPlayback(3010831, 20005, false, true, false, 0, 1);
    SetNetworkUpdateRate(3010830, true, CharacterUpdateFrequency.Every5Frames);
    SetNetworkUpdateRate(3010831, true, CharacterUpdateFrequency.Every5Frames);
    EndEvent();
L1:
    SetCharacterHPBarDisplay(3010831, Disabled);
    SetLockOnPoint(3010831, 220, Disabled);
    ForceAnimationPlayback(3010831, 20005, false, false, false, 0, 1);
    SetCharacterAnimationState(3010831, Disabled);
    WaitFixedTimeSeconds(3);
    SetCharacterHPBarDisplay(3010830, Disabled);
    SetLockOnPoint(3010830, 220, Disabled);
    SetCharacterAnimationState(3010830, Disabled);
    ForceAnimationPlayback(3010830, 20005, false, true, false, 0, 1);
    SetNetworkUpdateRate(3010830, true, CharacterUpdateFrequency.Every5Frames);
    SetNetworkUpdateRate(3010831, true, CharacterUpdateFrequency.Every5Frames);
    EndEvent();
});

$Event(13015556, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetLockOnPoint(X0_4, 220, Disabled);
    EndIf(EventFlag(X4_4));
    WaitFor(EventFlag(X12_4));
    if (!EventFlag(X8_4)) {
        ForceAnimationPlayback(X0_4, 700, true, false, false, 0, 1);
        ChangeCharacterEnableState(X0_4, Enabled);
        SetCharacterAnimationState(X0_4, Enabled);
        SetCharacterAIState(X0_4, Disabled);
        SetCharacterGravity(X0_4, Disabled);
        SetCharacterInvincibility(X0_4, Enabled);
        SetCharacterHPBarDisplay(X0_4, Disabled);
        SetCharacterMaphit(X0_4, true);
        WaitFor(EventFlag(X8_4));
        SetCharacterAIState(X0_4, Enabled);
        SetLockOnPoint(X0_4, 220, Enabled);
        SetCharacterInvincibility(X0_4, Disabled);
        SetCharacterHPBarDisplay(X0_4, Enabled);
        ForceAnimationPlayback(X0_4, 1700, false, false, false, 0, 1);
    }
L0:
    ChangeCharacterEnableState(X0_4, Enabled);
    SetCharacterAnimationState(X0_4, Enabled);
    SetCharacterAIState(X0_4, Enabled);
    SetLockOnPoint(X0_4, 220, Enabled);
    SetCharacterInvincibility(X0_4, Disabled);
    SetCharacterHPBarDisplay(X0_4, Enabled);
    WaitFor(HPRatio(X0_4) <= 0);
    SetEventFlag(X4_4, ON);
    SetNetworkUpdateRate(3010830, true, CharacterUpdateFrequency.AlwaysUpdate);
    ForceAnimationPlayback(3010830, 20007, false, false, true, 0, 1);
    WaitFixedTimeSeconds(6.8);
    ForceCharacterDeath(3010830, true);
    ChangeCharacterEnableState(3010830, Disabled);
    SetCharacterAnimationState(3010830, Disabled);
    SetNetworkUpdateRate(3010830, false, CharacterUpdateFrequency.NoUpdate);
    AwardItemLot(31411000);
});

$Event(13015557, Restart, function(X0_4, X4_4, X8_4) {
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetLockOnPoint(X0_4, 220, Disabled);
    SetCharacterHPBarDisplay(X0_4, Disabled);
    SetCharacterMaphit(X0_4, true);
    EndIf(EventFlag(X4_4));
    ChangeCharacterEnableState(X0_4, Enabled);
    SetCharacterAnimationState(X0_4, Enabled);
    SetCharacterAIState(X0_4, Disabled);
    SetCharacterGravity(X0_4, Disabled);
    SetCharacterInvincibility(X0_4, Enabled);
    if (!EventFlag(X8_4)) {
        ForceAnimationPlayback(X0_4, 700, true, false, false, 0, 1);
        ChangeCharacterEnableState(X0_4, Enabled);
        SetCharacterAnimationState(X0_4, Enabled);
        SetCharacterAIState(X0_4, Disabled);
        SetCharacterGravity(X0_4, Disabled);
        SetCharacterInvincibility(X0_4, Enabled);
        SetCharacterHPBarDisplay(X0_4, Disabled);
        SetCharacterMaphit(X0_4, true);
        WaitFor(EventFlag(X8_4));
        SetCharacterAIState(X0_4, Enabled);
        SetCharacterInvincibility(X0_4, Disabled);
        SetCharacterHPBarDisplay(X0_4, Enabled);
        SetLockOnPoint(X0_4, 220, Enabled);
        ForceAnimationPlayback(X0_4, 1700, false, true, false, 0, 1);
    }
L0:
    SetCharacterAIState(X0_4, Enabled);
    SetCharacterInvincibility(X0_4, Disabled);
    SetCharacterHPBarDisplay(X0_4, Enabled);
    SetLockOnPoint(X0_4, 220, Enabled);
    WaitFor(HPRatio(X0_4) <= 0);
    SetEventFlag(X4_4, ON);
    SetNetworkUpdateRate(3010831, true, CharacterUpdateFrequency.AlwaysUpdate);
    ForceAnimationPlayback(3010831, 20007, false, false, true, 0, 1);
    WaitFixedTimeSeconds(6.8);
    ForceCharacterDeath(3010831, true);
    ChangeCharacterEnableState(3010831, Disabled);
    SetCharacterAnimationState(3010831, Disabled);
    SetNetworkUpdateRate(3010831, false, CharacterUpdateFrequency.NoUpdate);
    AwardItemLot(31411100);
});

$Event(13015558, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(EventFlag(X8_4));
    WaitFor(CharacterBackreadStatus(X0_4));
    CharacterWarpRequest(X0_4, TargetEntityType.Character, X4_4, X12_4);
    if (!EntityInRadiusOfEntity(10000, X0_4, 10, 1)) {
        WaitFixedTimeSeconds(5);
        RestartEvent();
    }
    WaitFixedTimeFrames(5);
    RestartEvent();
});

$Event(13015559, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(EventFlag(X8_4));
    WaitFor(CharacterBackreadStatus(X0_4));
    CharacterWarpRequest(X0_4, TargetEntityType.Character, X4_4, X12_4);
    if (!EntityInRadiusOfEntity(10000, X0_4, 10, 1)) {
        WaitFixedTimeSeconds(5);
        RestartEvent();
    }
    WaitFixedTimeFrames(5);
    RestartEvent();
});

$Event(13015580, Restart, function() {
    EndIf(EventFlag(13010890));
    WaitFor(
        ((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.Hollow)
            || CharacterType(10000, TargetType.WhitePhantom))
            && InArea(10000, 3012300));
    SetSpEffect(3010830, 11021);
    SetSpEffect(3010830, 11023);
    WaitFixedTimeFrames(190);
    RestartEvent();
});

$Event(13015581, Restart, function() {
    EndIf(EventFlag(13010890));
    WaitFor(
        InArea(10000, 3012310)
            && (HasDamageType(3010830, -1, DamageType.Unspecified)
                || HasDamageType(3010831, -1, DamageType.Unspecified)));
    SetSpEffect(3010830, 11022);
    WaitFixedTimeFrames(190);
    RestartEvent();
});

$Event(13015585, Restart, function() {
    EndIf(EventFlag(13010890));
    WaitFor(
        ((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.Hollow)
            || CharacterType(10000, TargetType.WhitePhantom))
            && (InArea(10000, 3012300) || InArea(10000, 3012301)));
    SetSpEffect(3010831, 11031);
    SetSpEffect(3010831, 11032);
    WaitFixedTimeFrames(150);
    RestartEvent();
});

$Event(13015590, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(EventFlag(X0_4));
    WaitFor(CharacterHasEventMessage(X4_4, X8_4));
    SetEventFlag(X0_4, ON);
});

$Event(13015810, Restart, function() {
    SetCharacterAIState(3010800, Disabled);
    ChangeCharacterEnableState(3010800, Disabled);
    SetCharacterAnimationState(3010800, Disabled);
    SetCharacterGravity(3010800, Disabled);
    SetCharacterGravity(3010801, Disabled);
    SetCharacterMaphit(3010801, true);
    SetCharacterGravity(3010802, Disabled);
    SetCharacterMaphit(3010802, true);
    SetCharacterAIState(3010801, Disabled);
    ChangeCharacterEnableState(3010801, Disabled);
    SetCharacterAnimationState(3010801, Disabled);
    SetCharacterAIState(3010802, Disabled);
    ChangeCharacterEnableState(3010802, Disabled);
    SetCharacterAnimationState(3010802, Disabled);
    EndIf(EventFlag(13010800));
    ChangeCharacterEnableState(3010800, Enabled);
    ChangeCharacterEnableState(3010801, Enabled);
    SetCharacterAnimationState(3010801, Enabled);
    ChangeCharacterEnableState(3010802, Enabled);
    SetCharacterAnimationState(3010802, Enabled);
    if (!ThisEventSlot()) {
        ForceAnimationPlayback(3010800, 700, true, false, false, 0, 1);
        WaitFor(EventFlag(13015805) && InArea(10000, 3012830));
        WaitFixedTimeSeconds(2);
        ForceAnimationPlayback(3010800, 1700, false, false, false, 0, 1);
    }
L0:
    SetCharacterGravity(3010800, Enabled);
    SetCharacterAnimationState(3010800, Enabled);
    SetCharacterAIState(3010800, Enabled);
    SetNetworkUpdateRate(3010800, true, CharacterUpdateFrequency.AlwaysUpdate);
    ActivateMultiplayerdependantBuffs(3010800);
    ActivateMultiplayerdependantBuffs(3010801);
    ActivateMultiplayerdependantBuffs(3010802);
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetNetworkUpdateAuthority(3010800, AuthorityLevel.Forced);
        SetNetworkUpdateAuthority(3010801, AuthorityLevel.Forced);
        SetNetworkUpdateAuthority(3010802, AuthorityLevel.Forced);
    }
    DisplayBossHealthBar(Enabled, 3010800, 0, 903160);
});

$Event(13015811, Restart, function() {
    EndIf(EventFlag(13010800));
    SetCharacterInvincibility(3010801, Enabled);
    SetCharacterInvincibility(3010802, Enabled);
    WaitFor(HPRatio(3010800) <= 0.7 && CharacterDamagedBy(3010800, 10000));
    ForceAnimationPlayback(3010800, 20000, false, true, false, 0, 1);
    SetNetworkUpdateRate(3010801, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetCharacterAIState(3010801, Enabled);
    SetNetworkUpdateRate(3010802, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetCharacterAIState(3010802, Enabled);
    SetCharacterInvincibility(3010801, Disabled);
    SetCharacterInvincibility(3010802, Disabled);
});

$Event(13015812, Restart, function() {
    EndIf(EventFlag(13010800));
    WaitFor(HPRatio(3010800) <= 0);
    WaitFixedTimeSeconds(3.5);
    PlaySE(3010800, SoundType.s_SFX, 777777777);
    WaitFor(CharacterDead(3010800));
    WaitFixedTimeSeconds(3.5);
    DisplayBossHealthBar(Disabled, 3010800, 0, 903160);
    DeactivateObject(3011800, Disabled);
    HandleBossDefeat(3010800);
    SetNetworkUpdateRate(3010800, false, CharacterUpdateFrequency.AlwaysUpdate);
    ChangeCamera(-1, -1);
    ForceCharacterDeath(3010801, false);
    SetNetworkUpdateRate(3010801, false, CharacterUpdateFrequency.AlwaysUpdate);
    ForceCharacterDeath(3010802, false);
    SetNetworkUpdateRate(3010802, false, CharacterUpdateFrequency.AlwaysUpdate);
    SetEventFlag(13010800, ON);
    SetEventFlag(9308, ON);
    SetEventFlag(6308, ON);
});

$Event(13015815, Restart, function() {
    EndIf(EventFlag(13010800));
    SetNetworkSyncState(Disabled);
    WaitFor(EventFlag(13015805) && InArea(10000, 3012830));
    ChangeCamera(3160, 3160);
});

$Event(13015830, Restart, function(X0_4, X4_4) {
    SetCharacterAIState(X0_4, Disabled);
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterAnimationState(X0_4, Disabled);
    SetCharacterGravity(X0_4, Disabled);
    SetCharacterMaphit(X0_4, true);
    EndIf(EventFlag(13010800));
    EndIf(ThisEventSlot());
    ChangeCharacterEnableState(X0_4, Enabled);
    ForceAnimationPlayback(X0_4, 30000, true, false, false, 0, 1);
    WaitFor(InArea(10000, 3012830));
    WaitFixedTimeSeconds(X4_4);
    ForceAnimationPlayback(X0_4, 20000, false, true, false, 0, 1);
    WaitFixedTimeFrames(1);
    ChangeCharacterEnableState(X0_4, Disabled);
});

$Event(13015820, Restart, function() {
    InitializeCommonEvent(20005800, 13010800, 3011800, 3012801, 13015805, 3011800, 0, 0, 3012800);
    InitializeCommonEvent(20005801, 13010800, 3011800, 3012801, 13015805, 3011800, 13015806);
    InitializeCommonEvent(20001836, 13010800, 13015805, 13015806, 13015810, 3012803, 3012804, 13015811);
    InitializeCommonEvent(20005820, 13010800, 3011800, 3, 0);
    InitializeCommonEvent(20005820, 13010800, 3011801, 3, 0);
    InitializeCommonEvent(20005810, 13010800, 3011800, 3012801, 10000);
});
