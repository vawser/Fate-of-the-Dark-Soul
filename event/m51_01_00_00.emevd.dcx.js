// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    // World's End
    RegisterBonfire(15110000, 5111950, 5, 180, 0);
    
    // General
    InitializeEvent(0, 15115101, 0); // Disable Gael Scenario
    InitializeEvent(0, 15115201, 0); // Filianore
    
    InitializeEvent(0, 15115102, 0); // Journey Menu
    InitializeEvent(0, 15115103, 0); // Pilgrim Angel
    InitializeEvent(0, 15115104, 0); // Beautiful Pulpa
    InitializeEvent(0, 15115105, 0); // Fallen Pygmy
    InitializeEvent(0, 15115106, 0); // Pygmy Merchant
    InitializeEvent(0, 15115107, 0); // Slave Knight Gael
    
    // Map Warps
    InitializeEvent( 0, 15115750, 5111700, 5111900, 3000980, 3002953, 30, 0); // High Wall
    InitializeEvent( 1, 15115750, 5111701, 5111901, 3010970, 3012950, 30, 1); // Lothric Castle
    InitializeEvent( 2, 15115750, 5111702, 5111902, 3100974, 3102954, 31, 0); // Undead Settlement
    InitializeEvent( 3, 15115750, 5111703, 5111903, 3300976, 3302956, 33, 0); // Swamps of Farron
    InitializeEvent( 4, 15115750, 5111704, 5111904, 3800977, 3802957, 38, 0); // Depths of Carthus
    InitializeEvent( 5, 15115750, 5111705, 5111905, 3500974, 3502954, 35, 0); // Cathedral of the Deep
    InitializeEvent( 7, 15115750, 5111707, 5111907, 3200976, 3202956, 32, 0); // Archdragon Peak
    InitializeEvent( 8, 15115750, 5111708, 5111908, 3700977, 3702957, 37, 0); // Irithyll of the Boreal Valley
    InitializeEvent( 9, 15115750, 5111709, 5111909, 3900970, 3902950, 39, 0); // Profaned Depths
    InitializeEvent(10, 15115750, 5111710, 5111910, 4500971, 4502951, 45, 0); // Painted World
    InitializeEvent(11, 15115750, 5111711, 5111911, 5000971, 5002951, 50, 0); // Dreg Heap
    InitializeEvent(12, 15115750, 5111712, 5111912, 5100972, 5102952, 51, 0); // Ringed City
    InitializeEvent(13, 15115750, 5111713, 5111913, 3000976, 3002956, 30, 0); // Consumed King's Garden
    
    InitializeEvent(14, 15115750, 5111714, 5111906, 4000975, 4002955, 40, 0); // Blighted Cemetery
    InitializeEvent(15, 15115750, 5111715, 5111914, 4100970, 4102950, 41, 0); // Convergence of the Kingdoms

    // Boss Clear Markers
    InitializeEvent(0, 15115760, 0);
    
    // Dummy Activation
    InitializeEvent(0, 15115770, 0);
    
    // Prison Fogwall
    InitializeEvent(0, 15115780, 0);
    
    //-----------------------
    // Slave Knight Gael - Post-Warp
    //-----------------------
    EndIf(!EventFlag(25000121));
    SetEventFlag(25000121, OFF);
    
    SetCurrentMapCeremony(10);
    
    // Disable all the hub characters
    ChangeCharacterEnableState(5115800, Disabled);
    SetCharacterAnimationState(5115800, Disabled);
    
    // Disable interactable hub objects
    DeactivateObject(5115801, Disabled);
    
    // Boss
    InitializeEvent(0, 15115800, 0);
    InitializeEvent(0, 15115810, 0);
    InitializeEvent(0, 15115811, 0);
    InitializeEvent(0, 15115812, 0);
    InitializeEvent(0, 15115847, 0);
    InitializeEvent(0, 15115849, 0);
    InitializeCommonEvent(20005840, 5111800);
    InitializeCommonEvent(20005841, 5111800);
    
    // Misc
    InitializeEvent(0, 15115891, 0);
    InitializeCommonEvent(20006031, 75110180, 5112801);
});

$Event(50, Default, function() {
    SetMapSoundState(5114801, Disabled);
    SetMapSoundState(5114802, Disabled);
    SetMapSoundState(5114803, Disabled);
    
    InitializeEvent(0, 15115200, 0); // Filianore
    
    //-----------------------
    // Slave Knight Gael - Post-Warp
    //-----------------------
    EndIf(!EventFlag(25000121));
    
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
    SetEventFlag(25000130, ON);
    
    // Accursed
    InitializeEvent(0, 15115801, 0);

    WaitFixedTimeSeconds(20.0);
    
    WarpPlayer(51, 1, 5110970);
    SetPlayerRespawnPoint(5112950);
});

// Accursed
$Event(15115801, Restart, function() {
    EndIf(!EventFlag(25000104));
    EndIf(EventFlag(25000131));
    
    SetEventFlag(25000131, ON); // End Accursed detriments
    
    // Remove Accursed Notes
    RemoveItemFromPlayer(ItemType.Goods, 8000, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8001, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8002, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8003, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8004, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8005, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8006, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8007, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8008, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8009, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8010, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8011, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8012, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8013, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8014, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8015, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8016, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8017, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8018, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8019, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8020, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8021, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8022, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8023, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8024, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8025, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8026, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8027, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8028, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8029, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8030, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8031, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8032, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8033, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8034, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8035, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8036, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8037, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8038, -99);
    RemoveItemFromPlayer(ItemType.Goods, 8039, -99);
    
    AwardItemLot(3900);
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
    // Disable Gael
    ChangeCharacterEnableState(5110800, Disabled);
    SetCharacterAIState(5110800, Disabled);
    SetCharacterAnimationState(5110800, Disabled);
    
    ChangeCharacterEnableState(5110801, Disabled);
    SetCharacterAIState(5110801, Disabled);
    SetCharacterAnimationState(5110801, Disabled);
    
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
    SetCharacterAIState(5110810, Disabled);
    SetCharacterAnimationState(5110810, Disabled);
    ChangeCharacterEnableState(5110810, Disabled);
    DeactivateObject(5111800, Disabled);
    DeleteObjectfollowingSFX(5111800, true);
    
    EndIf(EventFlag(25000100));
    
    ChangeCharacterEnableState(5110810, Enabled);
    DeactivateObject(5111800, Enabled);
    DeleteObjectfollowingSFX(5111800, true);
    CreateObjectfollowingSFX(5111800, 101, 4);

    WaitFor(EventFlag(25000100));
    
    ChangeCharacterEnableState(5110810, Disabled);
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

// Pygmy Merchant
$Event(15115106, Restart, function() {
    SetCharacterAIState(5110808, Disabled);
});

// Slave Knight Gael
$Event(15115107, Restart, function() {
    ChangeCharacterEnableState(5110811, Disabled);
    SetCharacterAIState(5110811, Disabled);
    
    SetCharacterAIState(5110809, Disabled);
    SetCharacterAnimationState(5110809, Disabled);
    
    EndIf(!EventFlag(25000130)); 
    
    // Hide big Gael
    ChangeCharacterEnableState(5110802, Disabled);
    SetCharacterAnimationState(5110802, Disabled);
    
    // Show player-type Gael corpse
    ChangeCharacterEnableState(5110811, Enabled);
    SetCharacterAnimationState(5110811, Enabled);
    ForceAnimationPlayback(5110811, 90380, true, false, true, 0, 1);
});

// Map Warp
$Event(15115750, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_1, X20_1) {
    SetNetworkSyncState(Disabled);
    EndIf(EventFlag(25000121)); // End if in Gael boss stage
    WaitFor(ActionButtonInArea(X4_4, X0_4));
    WarpPlayer(X16_1, X20_1, X8_4);
    SetPlayerRespawnPoint(X12_4);
});

// Boss Clear Markers
$Event(15115760, Restart, function() {
    SetNetworkSyncState(Disabled);
    EndIf(EventFlag(25000121)); // End if in Gael boss stage
    
    DeleteMapSFX(5113870, false);
    DeleteMapSFX(5113871, false);
    DeleteMapSFX(5113872, false);
    DeleteMapSFX(5113873, false);
    DeleteMapSFX(5113874, false);
    DeleteMapSFX(5113875, false);
    DeleteMapSFX(5113876, false);
    DeleteMapSFX(5113877, false);
    DeleteMapSFX(5113878, false);
    DeleteMapSFX(5113879, false);
    DeleteMapSFX(5113880, false);
    DeleteMapSFX(5113881, false);
    DeleteMapSFX(5113882, false);
    DeleteMapSFX(5113883, false);
    DeleteMapSFX(5113884, false);
    
    //-----------------
    // No Clear VFX
    //-----------------
    // High Wall
    SpawnMapSFX(5113857);
    // Lothric Castle
    SpawnMapSFX(5113856);
    // Undead Settlement
    SpawnMapSFX(5113855);
    // Irithyll
    SpawnMapSFX(5113854);
    // Profaned Depths
    SpawnMapSFX(5113853);
    // Swamps of Farron
    SpawnMapSFX(5113852);
    // Cathedral of the Deep
    SpawnMapSFX(5113851);
    // Depths of Carthus
    SpawnMapSFX(5113850);
    // Archdragon Peak
    SpawnMapSFX(5113861);
    // Ariandel
    SpawnMapSFX(5113860);
    // Dreg Heap
    SpawnMapSFX(5113859);
    // Ringed City
    SpawnMapSFX(5113858);
    // Consumed King's Garden
    SpawnMapSFX(5113862);
    // Blighted Cemetery
    SpawnMapSFX(5113863);
    // Convergence of the Kingdoms
    SpawnMapSFX(5113864);
    
    //-----------------
    // Clear VFX
    //-----------------
    // High Wall
    if(EventFlag(9300) && EventFlag(9301))
    {
        DeleteMapSFX(5113857, false);
        SpawnMapSFX(5113877);
    }
    
    // Consumed King's Garden
    if(EventFlag(9302))
    {
        DeleteMapSFX(5113862, false);
        SpawnMapSFX(5113882);
    }
    
    // Undead Settlement
    if(EventFlag(9303))
    {
        DeleteMapSFX(5113855, false);
        SpawnMapSFX(5113875);
    }
    
    // Archdragon Peak
    if(EventFlag(9304) && EventFlag(9305))
    {
        DeleteMapSFX(5113861, false);
        SpawnMapSFX(5113881);
    }
    
    // Swamps of Farron
    if(EventFlag(9306) && EventFlag(9307))
    {
        DeleteMapSFX(5113852, false);
        SpawnMapSFX(5113872);
    }
    
    // Lothric Castle
    if(EventFlag(9308) && EventFlag(9309))
    {
        DeleteMapSFX(5113856, false);
        SpawnMapSFX(5113876);
    }
    
    // Cathedral of the Deep
    if(EventFlag(9311))
    {
        DeleteMapSFX(5113851, false);
        SpawnMapSFX(5113871);
    }
    
    // Irithyll
    if(EventFlag(9313) && EventFlag(9314))
    {
        DeleteMapSFX(5113854, false);
        SpawnMapSFX(5113874);
    }
    
    // Depths of Carthus
    if(EventFlag(9315) && EventFlag(9317))
    {
        DeleteMapSFX(5113850, false);
        SpawnMapSFX(5113870);
    }
    
    // Profaned Depths
    if(EventFlag(9318))
    {
        DeleteMapSFX(5113853, false);
        SpawnMapSFX(5113873);
    }
    
    // Ariandel
    if(EventFlag(9322) && EventFlag(9323))
    {
        DeleteMapSFX(5113860, false);
        SpawnMapSFX(5113880);
    }
    
    // Dreg Heap
    if(EventFlag(9324))
    {
        DeleteMapSFX(5113859, false);
        SpawnMapSFX(5113879);
    }
    
    // Ringed City
    if(EventFlag(9325) && EventFlag(9326))
    {
        DeleteMapSFX(5113858, false);
        SpawnMapSFX(5113878);
    }
    
    // Blighted Cemetery
    if(EventFlag(9320))
    {
        DeleteMapSFX(5113863, false);
        SpawnMapSFX(5113883);
    }
    
    // Convergence of the Kingdoms
    if(EventFlag(9321))
    {
        DeleteMapSFX(5113864, false);
        SpawnMapSFX(5113884);
    }
});

// Dummy Activation
$Event(15115770, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_1, X20_1) {
    EndIf(EventFlag(25000121)); // End if in Gael boss stage
    
    // Disable Dummy
    SetCharacterAIState(5110852, Disabled);
    
    WaitFor(ActionButtonInArea(20000, 5110852));
    
    SetCharacterAIState(5110852, Enabled);
});

// Prison Fogwall
$Event(15115780, Restart, function() {
    EndIf(!EventFlag(25000132));
    
    WaitFixedTimeSeconds(1.0);
    
    DeactivateObject(5111850, Enabled);
    DeleteObjectfollowingSFX(5111850, true);
    CreateObjectfollowingSFX(5111850, 101, 4);
});
