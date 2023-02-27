// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    // Abandoned Thrones
    RegisterBonfire(15110000, 5111950, 5, 180, 0);
    
    // General
    InitializeEvent(0, 15115101, 0); // Disable Gael Scenario
    InitializeEvent(0, 15115201, 0); // Filianore
    
    InitializeEvent(0, 15115102, 0); // Journey Menu
    InitializeEvent(0, 15115103, 0); // Pilgrim Angel
    InitializeEvent(0, 15115104, 0); // Beautiful Pulpa
    InitializeEvent(0, 15115105, 0); // Beautiful Pulpa
    
    // Map Warps
    InitializeEvent( 0, 15115750, 5111700, 5111900, 3000980, 3002953, 30, 0); // High Wall
    InitializeEvent( 1, 15115750, 5111701, 5111901, 3010970, 3012950, 30, 1); // Lothric Castle
    InitializeEvent( 2, 15115750, 5111702, 5111902, 3100974, 3102954, 31, 0); // Undead Settlement
    InitializeEvent( 3, 15115750, 5111703, 5111903, 3300976, 3302956, 33, 0); // Swamps of Farron
    InitializeEvent( 4, 15115750, 5111704, 5111904, 3800977, 3802957, 38, 0); // Depths of Carthus
    InitializeEvent( 5, 15115750, 5111705, 5111905, 3500973, 3502953, 35, 0); // Cathedral of the Deep
    InitializeEvent( 6, 15115750, 5111706, 5111906, 4000110, 4002955, 40, 0); // Blighted Cemetery
    InitializeEvent( 7, 15115750, 5111707, 5111907, 3200976, 3202956, 32, 0); // Archdragon Peak
    InitializeEvent( 8, 15115750, 5111708, 5111908, 3700977, 3702957, 37, 0); // Irithyll of the Boreal Valley
    InitializeEvent( 9, 15115750, 5111709, 5111909, 3900970, 3902950, 39, 0); // Profaned Depths
    InitializeEvent(10, 15115750, 5111710, 5111910, 4500971, 4502951, 45, 0); // Painted World
    InitializeEvent(11, 15115750, 5111711, 5111911, 5000971, 5002951, 50, 0); // Dreg Heap
    InitializeEvent(12, 15115750, 5111712, 5111912, 5100972, 5102952, 51, 0); // Ringed City
    
    // Vanilla
    //RegisterBonfire(15110001, 5111951, 5, 180, 0);
    //InitializeEvent(0, 15115800, 0);
    //InitializeEvent(0, 15115810, 0);
    //InitializeEvent(0, 15115811, 0);
    //InitializeEvent(0, 15115812, 0);
    //InitializeEvent(0, 15115847, 0);
    //InitializeEvent(0, 15115849, 0);
    //InitializeCommonEvent(20005840, 5111800);
    //InitializeCommonEvent(20005841, 5111800);
    //InitializeEvent(0, 15115850, 0);
    //InitializeEvent(0, 15115860, 0);
    //InitializeEvent(0, 15115889, 0);
    //InitializeCommonEvent(20005840, 5111850);
    //InitializeCommonEvent(20005841, 5111850);
    //InitializeEvent(0, 15115890, 0);
    
    //InitializeCommonEvent(20005110, 5110300, 5112800);
    //InitializeEvent(0, 15115300, 0);
    //InitializeCommonEvent(20005351, 5110240, 62600240, 55110981, 1073741824);
    //InitializeEvent(0, 15115891, 0);
    //InitializeCommonEvent(20006002, 5110850, 1838, 1835, 1839);
    //InitializeCommonEvent(20006031, 75110180, 5112801);
});

$Event(50, Default, function() {
    SetMapSoundState(5114801, Disabled);
    SetMapSoundState(5114802, Disabled);
    SetMapSoundState(5114803, Disabled);
    
    InitializeEvent(0, 15115200, 0); // Filianore
    
    // Vanilla
    //InitializeEvent(0, 15115100, 0);
});


$Event(15115100, Restart, function() {
    EndIf(EventFlag(15110800));
    SetCurrentMapCeremony(0);
});

$Event(15115200, Restart, function() {
    SetCharacterGravity(5110200, Disabled);
    SetCharacterMaphit(5110200, true);
});

$Event(15115201, Restart, function() {
    WaitFor(CharacterBackreadStatus(5110200));
    WaitFixedTimeFrames(1);
    ForceAnimationPlayback(5110200, 30000, true, false, true, 0, 1);
});

$Event(15115300, Restart, function() {
    if (!(!EventFlag(15110801) && !EventFlag(15110300))) {
        ChangeCharacterEnableState(5110300, Disabled);
        SetCharacterBackreadState(5110300, true);
        SetCharacterAnimationState(5110300, Disabled);
        EndEvent();
    }
L0:
    SetCharacterTalkRange(5110300, 100);
    SetEventFlag(75110200, OFF);
    WaitFor(EventFlag(15110800) || InArea(5110300, 5112300) || CharacterDead(5110300));
    if (!CharacterDead(5110300)) {
        ForceCharacterDeath(5110300, false);
    }
    SetEventFlag(15110300, ON);
});

$Event(15115800, Restart, function() {
    EndIf(EventFlag(15110800));
    WaitFor(HPRatio(5110800) == 0);
    WaitFixedTimeSeconds(2.67);
    PlaySE(5110800, SoundType.s_SFX, 777777777);
    WaitFixedTimeSeconds(3);
    HandleBossDefeatAndDisplayBanner(5110800, TextBannerType.HeirofFireDestroyed);
    DeleteMapSFX(5113820, true);
    DeleteMapSFX(5113821, true);
    DeleteMapSFX(5113822, true);
    DeleteMapSFX(5113823, true);
    SetEventFlag(15110800, ON);
    SetEventFlag(6327, ON);
    SetEventFlag(9327, ON);
});

$Event(15115810, Restart, function() {
    if (EventFlag(15110800)) {
        ChangeCharacterEnableState(5115800, Disabled);
        SetCharacterAnimationState(5115800, Disabled);
        ForceCharacterDeath(5115800, false);
        DeleteMapSFX(5113820, false);
        DeleteMapSFX(5113821, false);
        DeleteMapSFX(5113822, false);
        DeleteMapSFX(5113823, false);
        DeleteMapSFX(5113830, false);
        DeleteMapSFX(5113831, false);
        DeleteMapSFX(5113832, false);
        DeleteMapSFX(5113833, false);
        DeactivateObject(5116820, Disabled);
        DeactivateObject(5116821, Enabled);
        EndEvent();
    }
L0:
    DeleteMapSFX(5113820, false);
    DeleteMapSFX(5113821, false);
    DeleteMapSFX(5113822, false);
    DeleteMapSFX(5113823, false);
    DeleteMapSFX(5113830, false);
    DeleteMapSFX(5113831, false);
    DeleteMapSFX(5113832, false);
    DeleteMapSFX(5113833, false);
    DeactivateObject(5116820, Enabled);
    DeactivateObject(5116821, Disabled);
    SetCharacterAIState(5115800, Disabled);
    ChangeCharacterEnableState(5110801, Disabled);
    SetCharacterAnimationState(5110801, Disabled);
    SetCharacterAnimationState(5110800, Disabled);
    EndIf(
        CharacterType(10000, TargetType.BlackPhantom)
            || CharacterInvadeType(10000, 7)
            || CharacterInvadeType(10000, 21)
            || CharacterInvadeType(10000, 4));
    if (!EventFlag(15110801)) {
        WarpCharacterAndCopyFloor(5110801, TargetEntityType.Area, 5112804, -1, 5110801);
        DeactivateObject(5111810, Disabled);
        WaitFor(
            (!PlayerIsNotInOwnWorld()
                && EntityInRadiusOfEntity(10000, 5110801, 120, 1)
                && InArea(10000, 5112801)
                && !EventFlag(15115852))
                || HasDamageType(5110801, -1, DamageType.Unspecified));
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SendInvadingPhantomsHome(0);
        }
        if (!HasMultiplayerState(MultiplayerState.TryingtoCreateSession)) {
            PlayCutsceneAndWarpPlayer(51010005, CutscenePlayMode.SkippableWithFadeOut, 5112802, 51, 1, 10000);
        } else if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            PlayCutsceneAndWarpPlayer(51010005, CutscenePlayMode.UnskippableWithFadeOut, 5112802, 51, 1, 10000);
        } else if (!InArea(10000, 5112815)) {
            PlayCutsceneToPlayer(51010005, CutscenePlayMode.Unskippable, 10000);
        } else {
            PlayCutsceneAndWarpPlayer(51010005, CutscenePlayMode.UnskippableWithFadeOut, 5112816, 51, 1, 10000);
        }
        WaitFixedTimeFrames(1);
    } else {
L1:
        WaitFor(EventFlag(15115805) && InArea(10000, 5112800));
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SendInvadingPhantomsHome(0);
        }
    }
L2:
    DeactivateObject(5111810, Enabled);
    ChangeCharacterEnableState(5110801, Enabled);
    SetCharacterAnimationState(5110801, Enabled);
    SetCharacterAIState(5110801, Enabled);
    SetNetworkUpdateRate(5110801, true, CharacterUpdateFrequency.AlwaysUpdate);
    ForceAnimationPlayback(5110801, 3035, false, false, false, 0, 1);
    CreateReferredDamagePair(5110801, 5110800);
    SetCharacterHPBarDisplay(5110801, Disabled);
    DisplayBossHealthBar(Enabled, 5110800, 0, 906200);
    SetNetworkconnectedEventFlag(15110801, ON);
});

$Event(15115811, Restart, function() {
    EndIf(EventFlag(15110800));
    WaitFor((HPRatio(5110800) < 0.65 || HPRatio(5110801) == 0) && !PlayerIsNotInOwnWorld());
    if (!HasMultiplayerState(MultiplayerState.TryingtoCreateSession)) {
        PlayCutsceneChangeMapCeremonyAndWarpPlayer(51010010, CutscenePlayMode.SkippableWithFadeOut, 10, 1, 5112805, 51, 1, 10000);
    } else {
L1:
        if (!PlayerIsNotInOwnWorld()) {
            GotoIf(L2, CharacterHPValue(10000) <= 0);
            PlayCutsceneChangeMapCeremonyAndWarpPlayer(51010010, CutscenePlayMode.UnskippableWithFadeOut, 10, 1, 5112805, 51, 1, 10000);
            Goto(L9);
L2:
            PlayCutsceneToPlayerAndChangeCurrentMapCeremony(51010010, CutscenePlayMode.UnskippableWithFadeOut, 10, 1, 10000);
        } else {
L3:
            if (!InArea(10000, 5112810)) {
                if (CharacterHPValue(10000) > 0) {
                    PlayCutsceneChangeMapCeremonyAndWarpPlayer(51010010, CutscenePlayMode.Unskippable, 10, 1, 5112806, 51, 1, 10000);
                    Goto(L9);
                }
            }
L4:
            PlayCutsceneToPlayerAndChangeCurrentMapCeremony(51010010, CutscenePlayMode.Unskippable, 10, 1, 10000);
        }
    }
L9:
    WaitFixedTimeFrames(1);
    ChangeCharacterEnableState(5110801, Disabled);
    SetCharacterAnimationState(5110801, Disabled);
    WarpCharacterAndCopyFloor(5110800, TargetEntityType.Area, 5112807, -1, 5110800);
    ChangeCharacterEnableState(5110800, Enabled);
    SetCharacterAnimationState(5110800, Enabled);
    SetCharacterAIState(5110800, Enabled);
    SetNetworkUpdateRate(5110800, true, CharacterUpdateFrequency.AlwaysUpdate);
    ForceAnimationPlayback(5110800, 3037, false, false, false, 0, 1);
    SetEventFlag(15115802, ON);
    DeactivateObject(5116820, Disabled);
    DeactivateObject(5116821, Enabled);
    SpawnMapSFX(5113830);
    SpawnMapSFX(5113831);
    SpawnMapSFX(5113832);
    SpawnMapSFX(5113833);
});

$Event(15115812, Restart, function() {
    EndIf(EventFlag(15110800));
    WaitFor(EventFlag(15115802) && CharacterHasSpEffect(5110800, 16207));
    SetEventFlag(15115803, ON);
    DeleteMapSFX(5113830, true);
    DeleteMapSFX(5113831, true);
    DeleteMapSFX(5113832, true);
    DeleteMapSFX(5113833, true);
    SpawnMapSFX(5113820);
    SpawnMapSFX(5113821);
    SpawnMapSFX(5113822);
    SpawnMapSFX(5113823);
});

$Event(15115847, Restart, function() {
    SetNetworkSyncState(Disabled);
    EndIf(EventFlag(15110800));
    SetSpEffect(10000, 16189);
    WaitFixedTimeSeconds(0.3);
    WaitFor(!InArea(10000, 5112830));
    ClearSpEffect(10000, 16189);
    WaitFixedTimeSeconds(0.3);
    WaitFor(InArea(10000, 5112830));
    RestartEvent();
});

$Event(15115848, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    SetNetworkSyncState(Disabled);
    DeactivateObject(X4_4, Disabled);
    DeleteObjectfollowingSFX(X4_4, true);
    WaitFor(
        ((EventFlag(X12_4) || X12_4 == 0) && PlayerIsNotInOwnWorld())
            || ((EventFlag(X12_4) || X12_4 == 0) && !EventFlag(X0_4))
            || ((HasMultiplayerState(MultiplayerState.TryingtoCreateSession)
                || HasMultiplayerState(MultiplayerState.TryingtoJoinSession))
                && EventFlag(X0_4)));
    DeactivateObject(X4_4, Enabled);
    DeleteObjectfollowingSFX(X4_4, true);
    CreateObjectfollowingSFX(X4_4, 101, X8_4);
    WaitFor(
        !((EventFlag(X12_4) || X12_4 == 0) && PlayerIsNotInOwnWorld())
            && !((EventFlag(X12_4) || X12_4 == 0) && !EventFlag(X0_4))
            && !((HasMultiplayerState(MultiplayerState.TryingtoCreateSession)
                || HasMultiplayerState(MultiplayerState.TryingtoJoinSession))
                && EventFlag(X0_4)));
    RestartEvent();
});

$Event(15115849, Restart, function() {
    InitializeCommonEvent(20005800, 15110800, 5111800, 5112800, 15115805, 5111800, 5115800, 15110801, 0);
    InitializeEvent(0, 15115895, 15110800, 5111800, 5112800, 15115805, 5111800, 15115806, 15110801, 0, 5112810);
    if (!EventFlag(15110801)) {
        InitializeCommonEvent(20001838, 15110800, 15115805, 15115806, 15115810, 5114801, 5114802, 5114803, 15115802, 15115803);
    } else {
        InitializeCommonEvent(20005833, 15110800, 15115805, 15115806, 5112800, 5114801, 5114802, 5114803, 15115802, 15115803);
    }
    InitializeEvent(0, 15115848, 15110800, 5111800, 4, 15110801);
    InitializeCommonEvent(20005810, 15110800, 5111800, 5112800, 10000);
});

$Event(15115850, Restart, function() {
    EndIf(EventFlag(15110850));
    WaitFor(CharacterDead(5110850));
    SetEventFlag(15110850, ON);
    SetEventFlag(65100604, ON);
    EndIf(PlayerIsNotInOwnWorld());
    SetEventFlag(15115852, OFF);
});

$Event(15115860, Restart, function() {
    if (EventFlag(15110850)) {
        ChangeCharacterEnableState(5110850, Disabled);
        SetCharacterAnimationState(5110850, Disabled);
        ForceCharacterTreasure(5110850);
        SetCharacterBackreadState(5110850, true);
        EndEvent();
    }
L0:
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetEventFlag(15115851, OFF);
        SetEventFlag(15115852, OFF);
    }
    SetCharacterAIState(5110850, Disabled);
    ChangeCharacterEnableState(5110850, Disabled);
    SetCharacterBackreadState(5110850, true);
    SetCharacterAnimationState(5110850, Disabled);
    SetCharacterTalkRange(5110850, 100);
    SetEventFlag(75110150, OFF);
    EndIf(
        CharacterType(10000, TargetType.BlackPhantom)
            || CharacterInvadeType(10000, 7)
            || CharacterInvadeType(10000, 21));
    if (!EventFlag(15115851)) {
        WaitFor(
            (((EventFlag(15110800) && EventFlag(15110801)) || !EventFlag(15110801))
                && EntityInRadiusOfEntity(10000, 5110850, 60, 1)
                && InArea(10000, 5112851)
                && !PlayerIsNotInOwnWorld())
                || HasDamageType(5102850, -1, DamageType.Unspecified));
    } else {
L1:
        WaitFor(EventFlag(15115855));
    }
L2:
    SetEventFlag(15115851, ON);
    SetEventFlag(15115852, ON);
    ChangeCharacterEnableState(5110850, Enabled);
    SetCharacterBackreadState(5110850, false);
    SetCharacterAnimationState(5110850, Enabled);
    SetNetworkUpdateRate(5110850, true, CharacterUpdateFrequency.AlwaysUpdate);
    ActivateMultiplayerdependantBuffs(5110850);
    SetCharacterAIState(5110850, Enabled);
    ForceAnimationPlayback(5110850, 63010, false, false, false, 0, 1);
    SetEventFlag(15115855, ON);
});

$Event(15115861, Restart, function() {
    EndIf(EventFlag(15110850));
    EndIf(EventFlag(15110801));
    WaitFor(EventFlag(15115852) && EventFlag(15110801));
    ForceAnimationPlayback(5110850, 91030, false, false, false, 0, 1);
    WaitFixedTimeSeconds(2);
    ChangeCharacterEnableState(5110850, Disabled);
    SetCharacterAnimationState(5110850, Disabled);
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(EventFlag(15110800) && InArea(10000, 5112850));
    ChangeCharacterEnableState(5110850, Enabled);
    SetCharacterAnimationState(5110850, Enabled);
    WarpCharacterAndCopyFloor(5110850, TargetEntityType.Area, 5112852, -1, 5110850);
    RequestCharacterAnimationReset(5110850, Interpolation.Interpolated);
    ForceAnimationPlayback(5110850, 63010, false, false, false, 0, 1);
});

$Event(15115888, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    SetNetworkSyncState(Disabled);
    DeactivateObject(X4_4, Disabled);
    DeleteObjectfollowingSFX(X4_4, true);
    EndEvent();
    flagOnline = (!EventFlag(X12_4) || EventFlag(X24_4)) && PlayerIsNotInOwnWorld();
    flagCmp = (EventFlag(X16_4) || X16_4 == 0) && !EventFlag(X12_4);
    flagCmp2 = (EventFlag(X24_4) || X24_4 == 0) && !EventFlag(X20_4);
    onlineFlag = (HasMultiplayerState(MultiplayerState.TryingtoCreateSession)
        || HasMultiplayerState(MultiplayerState.TryingtoJoinSession))
        && EventFlag(X0_4);
    WaitFor(flagOnline || flagCmp);
    DeactivateObject(X4_4, Enabled);
    DeleteObjectfollowingSFX(X4_4, true);
    CreateObjectfollowingSFX(X4_4, 101, X8_4);
    flagOnline2 = (!EventFlag(X12_4) || EventFlag(X24_4)) && PlayerIsNotInOwnWorld();
    flagCmp3 = (EventFlag(X16_4) || X16_4 == 0) && !EventFlag(X12_4);
    flagCmp4 = (EventFlag(X24_4) || X24_4 == 0) && !EventFlag(X20_4);
    onlineFlag2 = (HasMultiplayerState(MultiplayerState.TryingtoCreateSession)
        || HasMultiplayerState(MultiplayerState.TryingtoJoinSession))
        && EventFlag(X0_4);
    WaitFor(!flagOnline2 && !flagCmp3);
    RestartEvent();
});

$Event(15115889, Restart, function() {
    InitializeEvent(0, 15115888, 15110890, 5111850, 2, 15110850, 15115851, 15110800, 15110801);
    InitializeCommonEvent(20005810, 15110890, 5111850, 5112850, 10000);
});

$Event(15115890, Restart, function() {
    EndIf(EventFlag(15110890));
    WaitFor(EventFlag(15110800) && EventFlag(15110850));
    SetEventFlag(15110890, ON);
});

$Event(15115891, Default, function() {
    EndIf(PlayerIsNotInOwnWorld());
    ClearSpEffect(10000, 4700);
    WaitFor(PlayerInMap(51, 1));
    SetSpEffect(10000, 4700);
});

$Event(15115895, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    SetNetworkSyncState(Disabled);
    EndIf(EventFlag(X0_4));
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetEventFlag(X12_4, OFF);
    }
    if (X24_4 != 0) {
        GotoIf(L0, EventFlag(X24_4));
        if (X28_4 != 0) {
            areaFlag |= InArea(10000, X28_4);
        }
        areaFlag |= EventFlag(X24_4);
        WaitFor(
            areaFlag && PlayerIsNotInOwnWorld() && CharacterType(10000, TargetType.WhitePhantom));
        GotoIf(L0, InArea(10000, X32_4));
    } else {
L0:
        WaitFor(
            !EventFlag(X0_4)
                && EventFlag(X12_4)
                && CharacterType(10000, TargetType.WhitePhantom)
                && ActionButtonInArea(X16_4, X4_4));
        RotateCharacter(10000, X8_4, 60060, true);
        time = ElapsedSeconds(3);
        WaitFor(CharacterType(10000, TargetType.WhitePhantom) && (InArea(10000, X8_4) || time));
        RestartIf(time.Passed);
    }
L1:
    SetEventFlag(X20_4, ON);
    RestartEvent();
});

$Event(15115896, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    SetNetworkSyncState(Disabled);
    EndIf(!PlayerIsNotInOwnWorld());
    WaitFor(
        PlayerIsNotInOwnWorld()
            && EventFlag(X0_4)
            && (HasMultiplayerState(MultiplayerState.TryingtoCreateSession)
                || HasMultiplayerState(MultiplayerState.TryingtoJoinSession))
            && ActionButtonInArea(X12_4, X4_4));
    RotateCharacter(10000, X8_4, 60060, true);
    RestartEvent();
});

$Event(15115700, Default, function() {
    if (!PlayerIsNotInOwnWorld()) {
        if (!AnyBatchEventFlags(1835, 1839)) {
            BatchSetNetworkconnectedEventFlags(1835, 1839, OFF);
            SetNetworkconnectedEventFlag(1835, ON);
        }
        if (EventFlag(1836) && EventFlag(70001074)) {
            BatchSetNetworkconnectedEventFlags(1835, 1839, OFF);
            SetNetworkconnectedEventFlag(1835, ON);
        }
        if (!AnyBatchEventFlags(1820, 1834)) {
            BatchSetNetworkconnectedEventFlags(1820, 1834, OFF);
            SetNetworkconnectedEventFlag(1820, ON);
        }
        if (EventFlag(1835)) {
            if (AnyBatchEventFlags(1820, 1822)) {
                BatchSetNetworkconnectedEventFlags(1820, 1834, OFF);
                SetNetworkconnectedEventFlag(1823, ON);
                BatchSetNetworkconnectedEventFlags(1835, 1839, OFF);
                SetNetworkconnectedEventFlag(1837, ON);
            }
        }
L9:
        SetEventFlag(70001074, OFF);
        if (!EventFlag(1838)) {
            SetEventFlag(75110150, OFF);
        }
    }
L10:
    NoOp();
});

// Disable Gael Scenario
$Event(15115101, Restart, function() {
    // Disable Shira
    ChangeCharacterEnableState(5110850, Disabled);
    SetCharacterAIState(5110850, Disabled);
    SetCharacterAnimationState(5110850, Disabled);
    
    // Disable Gael
    ChangeCharacterEnableState(5110800, Disabled);
    SetCharacterAIState(5110800, Disabled);
    SetCharacterAnimationState(5110800, Disabled);
    
    ChangeCharacterEnableState(5110801, Disabled);
    SetCharacterAIState(5110801, Disabled);
    SetCharacterAnimationState(5110801, Disabled);
    
    // Ringed Knight
    ChangeCharacterEnableState(5110240, Disabled);
    SetCharacterAIState(5110240, Disabled);
    SetCharacterAnimationState(5110240, Disabled);
    
    // Pygmy
    ChangeCharacterEnableState(5110300, Disabled);
    SetCharacterAIState(5110300, Disabled);
    SetCharacterAnimationState(5110300, Disabled);
    
    // Disable fogwall assets
    DeactivateObject(5111850, Disabled);
    
    // Disable skybox assets
    DeactivateObject(5111820, Disabled);
    DeactivateObject(5111821, Disabled);
    
    // Disable Gael's lightning map SFX
    DeleteMapSFX(5113820, false);
    DeleteMapSFX(5113821, false);
    DeleteMapSFX(5113822, false);
    DeleteMapSFX(5113823, false);
    DeleteMapSFX(5113830, false);
    DeleteMapSFX(5113831, false);
    DeleteMapSFX(5113832, false);
    DeleteMapSFX(5113833, false);
    
    SetCurrentMapCeremony(0);
});

// Journey Menu
$Event(15115102, Restart, function() {
    SetCharacterAIState(5110953, Disabled);
    SetCharacterAnimationState(5110953, Disabled);
    ChangeCharacterEnableState(5110953, Disabled);
    DeactivateObject(5111800, Disabled);
    DeleteObjectfollowingSFX(5111800, true);
    
    EndIf(EventFlag(25000100));
    
    ChangeCharacterEnableState(5110953, Enabled);
    DeactivateObject(5111800, Enabled);
    DeleteObjectfollowingSFX(5111800, true);
    CreateObjectfollowingSFX(5111800, 101, 4);

    WaitFor(EventFlag(25000100));
    
    ChangeCharacterEnableState(5110953, Disabled);
    DeactivateObject(5111800, Disabled);
    DeleteObjectfollowingSFX(5111800, true);
});

// The Last Pilgrim
$Event(15115103, Restart, function() {
    SetCharacterGravity(5110803, Disabled);
    SetCharacterAIState(5110804, Disabled);
    SetCharacterAnimationState(5110804, Disabled);
});

// Beautiful Pulpa
$Event(15115104, Restart, function() {
    SetCharacterAIState(5110806, Disabled);
    SetCharacterAnimationState(5110806, Disabled);
});

// Fallen Pygmy
$Event(15115105, Restart, function() {
    SetCharacterAIState(5110807, Disabled);
    SetCharacterAnimationState(5110807, Disabled);
});

// Map Warp
$Event(15115750, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_1, X20_1) {
    SetNetworkSyncState(Disabled);
    WaitFor(ActionButtonInArea(X4_4, X0_4));
    WarpPlayer(X16_1, X20_1, X8_4);
    SetPlayerRespawnPoint(X12_4);
});
