// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    //RegisterBonfire(14000000, 4001950, 5, 180, 0);
    //RegisterBonfire(14000001, 4001951, 5, 180, 0);
    //RegisterBonfire(14000003, 4001953, 5, 180, 0);
    //InitializeCommonEvent(20005500, 14000800, 14000002, 4000952, 4001952);
    //InitializeCommonEvent(20005500, 14000830, 14000004, 4000954, 4001954);
    
    // Bonfires
    RegisterBonfire(14000002, 4001952, 5, 180, 0); // Iudex Gundyr
    
    // Loading Screen Tips
    InitializeEvent(0, 14005480, 74000012);
    InitializeEvent(0, 14005481, 0);
    
    // Hollows
    InitializeCommonEvent(20005120, 4000202, 1091043328);
    InitializeCommonEvent(20005210, 4000204, 703, 1703, 1091043328);
    InitializeCommonEvent(20005132, 4000205, 1092616192, 4002205);
    InitializeCommonEvent(20005132, 4000207, 1065353216, 4002207);
    InitializeCommonEvent(20005130, 4000209, 1098907648, 4002207);
    InitializeCommonEvent(20005213, 4000210, 705, 1705, 1075838976, 4002210);
    InitializeCommonEvent(20005110, 4000211, 4002248);
    InitializeCommonEvent(20005210, 4000212, 703, 1703, 1082130432);
    InitializeCommonEvent(20005200, 4000213, 705, 1705, 4002213);
    InitializeCommonEvent(20005210, 4000214, 703, 1703, 1077936128);
    InitializeCommonEvent(20005150, 4000215);
    InitializeCommonEvent(20005200, 4000216, 703, 1703, 4002216);
    InitializeCommonEvent(20005200, 4000217, 703, 1703, 4002216);
    InitializeCommonEvent(20005200, 4000218, 706, 1706, 4002218);
    InitializeCommonEvent(20005200, 4000219, 706, 1706, 4002216);
    InitializeCommonEvent(20005201, 4000220, 703, 1703, 4002220, 1065353216);
    InitializeCommonEvent(20005201, 4000221, 706, 1706, 4002220, 1069547520);
    InitializeCommonEvent(20005210, 4000239, 703, 1703, 1082130432);
    InitializeCommonEvent(20005120, 4000240, 1097859072);
    InitializeCommonEvent(20005220, 4000241, 706, 1706);
    InitializeCommonEvent(20005290, 4000242, 705, 1705);
    InitializeCommonEvent(20005220, 4000243, 703, 1703);
    InitializeCommonEvent(20005110, 4000244, 4002244);
    InitializeCommonEvent(20005292, 4000245, 703, 1703);
    InitializeCommonEvent(20005290, 4000246, 703, 1703);
    InitializeCommonEvent(20005110, 4000247, 4002248);
    
    // Ravenous Crystal Lizard
    InitializeCommonEvent(20005341, 14000380, 4000380, 31002000);
    
    // Crystal Lizard
    InitializeCommonEvent(20005341, 14000390, 4000390, 21509500);
    
    // Sword Master
    InitializeCommonEvent(20005342, 9500, 4000500);
    
    // Tower Lift
    InitializeCommonEvent(20005620, 14000400, 14001400, 4001400, 4001401, 4001402, 14001401);
    InitializeEvent(0, 14005401, 0);
    
    // Ladder
    InitializeEvent(0, 14005420, 0);
    
    // Kick-down Ladder
    InitializeCommonEvent(20005640, 14000426, 4001426, 14005426, 14005427, $LAYERS(0));
    
    // Firelink Shrine Music
    InitializeEvent(0, 14005450, 0, $LAYERS(0));
    
    DeactivateObject(4001801, Disabled);
    
    // Area Message
    InitializeEvent(0, 14005470, 0, $LAYERS(1));
    InitializeEvent(0, 14005471, 0, $LAYERS(1));
    InitializeEvent(0, 14005472, 0, $LAYERS(1));
    InitializeEvent(0, 14005473, 0, $LAYERS(1));
    InitializeEvent(0, 14005474, 0, $LAYERS(1));
    
    // Message
    InitializeEvent(0, 14005445, 0);
    
    InitializeCommonEvent(20005610, 14000410, 4002410, 4002411);
    InitializeCommonEvent(20005611, 14000410, 4003252, 4001252, 1400340);
    InitializeCommonEvent(20005613, 14000425, 4003250, 4001250, 3400340, 10010873);
    InitializeEvent(0, 14005441, 0, $LAYERS(0));
    InitializeCommonEvent(20005650, 14000430, 4001430);
    InitializeCommonEvent(20005650, 14000431, 4001431);
    InitializeCommonEvent(20005650, 14000432, 4001432);
    InitializeCommonEvent(20005650, 14000433, 4001433);
    InitializeCommonEvent(20005650, 14000434, 4001434);
    InitializeCommonEvent(20005650, 14000435, 4001435);
    InitializeCommonEvent(20005520, 14000600, 4001600, 4004600);
    InitializeCommonEvent(20005520, 14000601, 4001601, 4004601);
    InitializeCommonEvent(20005523, 4001210, 2);
    InitializeCommonEvent(20005523, 4001211, 1);
    InitializeCommonEvent(20005523, 4001212, 1);
    InitializeCommonEvent(20005523, 4001213, 2);
    InitializeCommonEvent(20005524, 4001218, 9512);
    InitializeCommonEvent(20005525, 54000300, 4000300, 4001728, 62, $LAYERS(1));
    InitializeCommonEvent(20005526, 54000330, 4000330, 4001221, 62, 13300800, $LAYERS(1));
    
    // Iudex Gundyr
    InitializeEvent(0, 14005800, 0, $LAYERS(0));
    InitializeEvent(0, 14005810, 0, $LAYERS(0));
    InitializeEvent(0, 14005811, 0, $LAYERS(0));
    InitializeEvent(0, 14005812, 0, $LAYERS(0));
    InitializeEvent(0, 14000816, 0, $LAYERS(0));
    InitializeEvent(0, 14005813, 0, $LAYERS(0));
    InitializeEvent(0, 14005820, 0, $LAYERS(0));
    
    InitializeCommonEvent(20005840, 4001800, $LAYERS(1, 2, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005841, 4001800, $LAYERS(1, 2, 3, 4, 5, 6, 7, 8, 9));
    
    // Sword Master: Phantom
    InitializeCommonEvent(20005701, 14000830, 14004190, 14005190, 4000190, 4002190, 9500, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005711, 14004190, 14005835, 4000190, 4002800, 4002805, 14000831, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005720, 14004190, 14005190, 14000830, 4000190, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005714, 14004190, 14005835, 4000190, 4002806, 14000831, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    
    // Daughter of Crystal Kreimhild: Inavder
    InitializeCommonEvent(20005750, 14000830, 14000197, 14004197, 14005197, 4000197, 4002197, 4002198, 0, 0, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005721, 14004197, 14005197, 14000197, 4000197, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    InitializeCommonEvent(20005760, 14000197, 14004197, 14005197, 4000197, $LAYERS(1, 3, 4, 5, 6, 7, 8, 9));
    
    InitializeCommonEvent(20006002, 4000705, 1038, 1035, 1039, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000125, 70000102, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000126, 70000106, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000127, 70000104, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000128, 70000175, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000129, 70000110, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000130, 70000115, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000131, 70000103, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000107, 70000116, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000132, 70000108, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000133, 70000115, $LAYERS(0));
    InitializeCommonEvent(20006020, 70000153, 70000152, $LAYERS(0));
    
    InitializeCommonEvent(20006030, 4001727, 4000, 2, 61610, 50006162, 50006163, 1286, $LAYERS(0));
    InitializeCommonEvent(20006031, 74000393, 4002727, $LAYERS(0));
   
    InitializeCommonEvent(20006030, 4001750, 4000, 3, 60410, 50006041, 50006042, 1045, $LAYERS(0));

    InitializeEvent(0, 14000490, 0, $LAYERS(0));
    InitializeEvent(0, 14000491, 0, $LAYERS(0));
    
    InitializeCommonEvent(20006030, 4001760, 4000, 2, 60730, 50006074, 50006074, 74000825, $LAYERS(0));

    InitializeCommonEvent(20006030, 4001780, 4000, 1, 60810, 50006081, 50006081, 74000790, $LAYERS(0));
    
});

$Event(50, Default, function() {
    InitializeEvent(0, 14005103, 0, $LAYERS(0, 3, 4, 5, 6, 7, 8, 9));
    InitializeEvent(0, 14005104, 0, $LAYERS(1, 2, 3, 4, 5, 6, 7, 8, 9));
    InitializeEvent(0, 14000401, 0);
    InitializeEvent(0, 14000100, 0, $LAYERS(0, 2, 3, 4, 5, 6, 7, 8, 9)); // Player Start
    SetMapSoundState(4004800, Disabled);
    SetMapSoundState(4004801, Disabled);
    SetMapSoundState(4004830, Disabled);
    SetMapSoundState(4004831, Disabled);
    SetMapSoundState(4004450, Disabled);
    SetMapSoundState(4004460, Disabled);
    SetMapSoundState(4003700, Disabled);
    SetMapSoundState(4003701, Disabled);
});

// Player Start
$Event(14000100, Default, function() {
    EndIf(ThisEventSlot());
    EndIf(PlayerIsNotInOwnWorld());
    EndIf(!PlayerInMap(40, 0));
    EndIf(!MapCeremony(40, 0, 0));

    // Only award Hollow Fragments in NG0
    if (GameCycle() <= 1) 
    {
        AwardItemLot(100);
    }
    
    // Warp to new shrine
    WarpPlayer(51, 1, 5110973);
    SetPlayerRespawnPoint(5112953);
    SetNetworkInteractionState(Enabled);
    SaveRequest(0);
    SetEventFlag(14000100, ON);
});

$Event(14005103, Default, function() {
    WaitFor(!PlayerIsNotInOwnWorld() && !EventFlag(131));
    ActivateHit(4004109, Enabled);
    ActivateHit(4004100, Disabled);
});

$Event(14005104, Default, function() {
    ActivateHit(4004109, Enabled);
    ActivateHit(4004100, Disabled);
});

$Event(14000401, Default, function() {
    EndIf(ThisEventSlot());
    SetEventFlag(14000400, ON);
    EndEvent();
});

$Event(14005401, Restart, function() {
    InitializeCommonEvent(20005621, 14000400, 14001400, 4001400, 4001401, 4003401, 4001402, 4003402, 4002401, 4002402, 14001401, 14004400, 0);
});

$Event(14005420, Restart, function() {
    RegisterLadder(14000420, 14000421, 4001420);
});

$Event(14005441, Restart, function() {
    DeleteObjectfollowingSFX(4001500, false);
    DeleteObjectfollowingSFX(4001501, false);
    DeleteObjectfollowingSFX(4001502, false);
    DeleteObjectfollowingSFX(4001503, false);
    DeleteObjectfollowingSFX(4001510, false);
    DeleteObjectfollowingSFX(4001511, false);
    DeleteObjectfollowingSFX(4001512, false);
    DeleteObjectfollowingSFX(4001513, false);
    DeleteObjectfollowingSFX(4001514, false);
    DeleteObjectfollowingSFX(4001515, false);
    DeleteObjectfollowingSFX(4001516, false);
    DeleteObjectfollowingSFX(4001517, false);
    DeleteObjectfollowingSFX(4001518, false);
    DeleteObjectfollowingSFX(4001519, false);
    DeleteObjectfollowingSFX(4001520, false);
    DeleteObjectfollowingSFX(4001521, false);
    DeleteObjectfollowingSFX(4001522, false);
    DeleteObjectfollowingSFX(4001523, false);
    DeleteObjectfollowingSFX(4001524, false);
    DeleteObjectfollowingSFX(4001525, false);
    DeleteObjectfollowingSFX(4001526, false);
    DeleteObjectfollowingSFX(4001527, false);
    DeleteObjectfollowingSFX(4001528, false);
    DeleteObjectfollowingSFX(4001529, false);
    DeleteObjectfollowingSFX(4001530, false);
    DeleteObjectfollowingSFX(4001531, false);
    DeleteObjectfollowingSFX(4001532, false);
    DeleteObjectfollowingSFX(4001533, false);
    DeleteObjectfollowingSFX(4001534, false);
    DeleteObjectfollowingSFX(4001535, false);
    DeleteObjectfollowingSFX(4001536, false);
    DeleteObjectfollowingSFX(4001537, false);
    DeleteObjectfollowingSFX(4001538, false);
    DeleteObjectfollowingSFX(4001539, false);
    DeleteObjectfollowingSFX(4001540, false);
    DeleteObjectfollowingSFX(4001541, false);
    DeleteObjectfollowingSFX(4001542, false);
    DeleteObjectfollowingSFX(4001543, false);
    DeleteObjectfollowingSFX(4001544, false);
    DeleteObjectfollowingSFX(4001545, false);
    DeleteObjectfollowingSFX(4001546, false);
    DeleteObjectfollowingSFX(4001547, false);
    DeleteObjectfollowingSFX(4001548, false);
    DeleteObjectfollowingSFX(4001549, false);
    DeleteObjectfollowingSFX(4001550, false);
    DeleteObjectfollowingSFX(4001551, false);
    DeleteObjectfollowingSFX(4001552, false);
    DeleteObjectfollowingSFX(4001553, false);
    DeleteObjectfollowingSFX(4001554, false);
    DeleteObjectfollowingSFX(4001555, false);
    DeleteObjectfollowingSFX(4001556, false);
    DeleteObjectfollowingSFX(4001557, false);
    DeleteObjectfollowingSFX(4001558, false);
    DeleteObjectfollowingSFX(4001559, false);
    DeleteObjectfollowingSFX(4001560, false);
    DeleteObjectfollowingSFX(4001561, false);
    DeleteObjectfollowingSFX(4001562, false);
    DeleteObjectfollowingSFX(4001563, false);
    DeleteObjectfollowingSFX(4001564, false);
    DeleteObjectfollowingSFX(4001565, false);
    DeleteObjectfollowingSFX(4001566, false);
    DeleteObjectfollowingSFX(4001567, false);
    DeleteObjectfollowingSFX(4001568, false);
    DeleteObjectfollowingSFX(4001569, false);
    CreateObjectfollowingSFX(4001500, 200, 800022);
    CreateObjectfollowingSFX(4001501, 200, 800022);
    CreateObjectfollowingSFX(4001502, 200, 800022);
    CreateObjectfollowingSFX(4001503, 200, 800022);
    CreateObjectfollowingSFX(4001510, 200, 839010);
    CreateObjectfollowingSFX(4001511, 200, 839010);
    CreateObjectfollowingSFX(4001512, 200, 839010);
    CreateObjectfollowingSFX(4001513, 200, 839010);
    CreateObjectfollowingSFX(4001514, 200, 839010);
    CreateObjectfollowingSFX(4001515, 200, 839010);
    CreateObjectfollowingSFX(4001516, 200, 839010);
    CreateObjectfollowingSFX(4001517, 200, 839010);
    CreateObjectfollowingSFX(4001518, 200, 839010);
    CreateObjectfollowingSFX(4001519, 200, 839010);
    CreateObjectfollowingSFX(4001520, 200, 839010);
    CreateObjectfollowingSFX(4001521, 200, 839010);
    CreateObjectfollowingSFX(4001522, 200, 839010);
    CreateObjectfollowingSFX(4001523, 200, 839010);
    CreateObjectfollowingSFX(4001524, 200, 839010);
    CreateObjectfollowingSFX(4001525, 200, 839010);
    CreateObjectfollowingSFX(4001526, 200, 839010);
    CreateObjectfollowingSFX(4001527, 200, 839010);
    CreateObjectfollowingSFX(4001528, 200, 839010);
    CreateObjectfollowingSFX(4001529, 200, 839010);
    CreateObjectfollowingSFX(4001530, 200, 839010);
    CreateObjectfollowingSFX(4001531, 200, 839010);
    CreateObjectfollowingSFX(4001532, 200, 839010);
    CreateObjectfollowingSFX(4001533, 200, 839010);
    CreateObjectfollowingSFX(4001534, 200, 839010);
    CreateObjectfollowingSFX(4001535, 200, 839010);
    CreateObjectfollowingSFX(4001536, 200, 839010);
    CreateObjectfollowingSFX(4001537, 200, 839010);
    CreateObjectfollowingSFX(4001538, 200, 839010);
    CreateObjectfollowingSFX(4001539, 200, 839010);
    CreateObjectfollowingSFX(4001540, 200, 839010);
    CreateObjectfollowingSFX(4001541, 200, 839010);
    CreateObjectfollowingSFX(4001542, 200, 839010);
    CreateObjectfollowingSFX(4001543, 200, 839010);
    CreateObjectfollowingSFX(4001544, 200, 839010);
    CreateObjectfollowingSFX(4001545, 200, 839010);
    CreateObjectfollowingSFX(4001546, 200, 839010);
    CreateObjectfollowingSFX(4001547, 200, 839010);
    CreateObjectfollowingSFX(4001548, 200, 839010);
    CreateObjectfollowingSFX(4001549, 200, 839010);
    CreateObjectfollowingSFX(4001550, 200, 839010);
    CreateObjectfollowingSFX(4001551, 200, 839010);
    CreateObjectfollowingSFX(4001552, 200, 839010);
    CreateObjectfollowingSFX(4001553, 200, 839010);
    CreateObjectfollowingSFX(4001554, 200, 839010);
    CreateObjectfollowingSFX(4001555, 200, 839010);
    CreateObjectfollowingSFX(4001556, 200, 839010);
    CreateObjectfollowingSFX(4001557, 200, 839010);
    CreateObjectfollowingSFX(4001558, 200, 839010);
    CreateObjectfollowingSFX(4001559, 200, 839010);
    CreateObjectfollowingSFX(4001560, 200, 839010);
    CreateObjectfollowingSFX(4001561, 200, 839010);
    CreateObjectfollowingSFX(4001562, 200, 839010);
    CreateObjectfollowingSFX(4001563, 200, 839010);
    CreateObjectfollowingSFX(4001564, 200, 839010);
    CreateObjectfollowingSFX(4001565, 200, 839010);
    CreateObjectfollowingSFX(4001566, 200, 839010);
    CreateObjectfollowingSFX(4001567, 200, 839010);
    CreateObjectfollowingSFX(4001568, 200, 839010);
    CreateObjectfollowingSFX(4001569, 200, 839010);
});

$Event(14005445, Restart, function() {
    EndIf(!EventFlag(131));
    SetVisibilityOfMessage(4004222, Disabled);
});

$Event(14005450, Default, function() {
    SetNetworkSyncState(Disabled);
    EndIf(PlayerIsNotInOwnWorld());
    EnableMapSoundWithFade(4004450, Disabled, 5);
    EnableMapSoundWithFade(4004460, Disabled, 5);
    WaitFixedTimeSeconds(0.5);
    WaitFor(
        (PlayerStandingOnHit(4004100)
            || PlayerStandingOnHit(4004101)
            || PlayerStandingOnHit(4004102)
            || PlayerStandingOnHit(4004103)
            || PlayerStandingOnHit(4004104)
            || PlayerStandingOnHit(4004109))
            && !EventFlag(74000122));
    if (EventFlag(50006020)) {
        EnableMapSoundWithFade(4004450, Enabled, 5);
    } else {
        EnableMapSoundWithFade(4004460, Enabled, 5);
    }
    WaitFixedTimeSeconds(0.5);
    hit = PlayerStandingOnHit(4004100)
        || PlayerStandingOnHit(4004101)
        || PlayerStandingOnHit(4004102)
        || PlayerStandingOnHit(4004103)
        || PlayerStandingOnHit(4004104)
        || PlayerStandingOnHit(4004109);
    flag = EventFlagState(CHANGE, TargetEventFlagType.EventFlag, 50006020);
    WaitFor(!hit || flag);
    RestartIf(!flag.Passed);
    EnableMapSoundWithFade(4004450, Disabled, 5);
    EnableMapSoundWithFade(4004460, Disabled, 5);
    WaitFixedTimeSeconds(3);
    RestartEvent();
});

$Event(14005470, Default, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(!PlayerStandingOnHit(4004120) && PlayerInMap(40, 0));
    if (!PlayerIsNotInOwnWorld()) {
        EndIf(!EventFlag(743));
    }
L0:
    SetAreaWelcomeMessageState(Disabled);
    DisplayAreaWelcomeMessage(4010);
    SetEventFlag(743, OFF);
});

$Event(14005471, Restart, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(
        !EventFlag(74000013)
            && PlayerInMap(40, 0)
            && !PlayerStandingOnHit(4004120)
            && !CharacterDead(10000));
    SetAreaWelcomeMessageState(Disabled);
    WaitFixedTimeSeconds(3);
    RestartEvent();
});

$Event(14005472, Restart, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(PlayerInMap(40, 0) && CharacterDead(10000));
    WaitFixedTimeFrames(1);
    SetAreaWelcomeMessageState(Enabled);
    SetEventFlag(743, ON);
});

$Event(14005473, Restart, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(PlayerInMap(40, 0) && CharacterHasSpEffect(10000, 3220));
    SetAreaWelcomeMessageState(Enabled);
    SetEventFlag(743, ON);
});

$Event(14005474, Restart, function() {
    SetNetworkSyncState(Disabled);
    WaitFor(PlayerInMap(40, 0) && EventFlag(74000013));
    SetAreaWelcomeMessageState(Enabled);
    SetEventFlag(743, ON);
});

$Event(14005480, Default, function(X0_4) {
    EndIf(PlayerIsNotInOwnWorld());
    SetEventFlag(X0_4, OFF);
    WaitFor(EventFlag(X0_4));
    SetEventFlag(X0_4, OFF);
    DisableLoadingScreenTips(true);
    SetEventFlag(30, ON);
});

$Event(14005481, Restart, function() {
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(PlayerInMap(40, 0));
    DisableLoadingScreenTips(false);
});

$Event(14000490, Default, function() {
    InitializeCrowTrade(ItemType.Goods, 350, 4300, 70001000, 74000996);
    InitializeCrowTrade(ItemType.Goods, 2118, 4301, 70001007, 74000996);
    InitializeCrowTrade(ItemType.Goods, 2143, 4302, 70001001, 74000996);
    InitializeCrowTrade(ItemType.Goods, 374, 4303, 70001002, 74000996);
    InitializeCrowTrade(ItemType.Goods, 240, 4304, 6792, 74000996);
    InitializeCrowTrade(ItemType.Goods, 241, 4305, 6791, 74000996);
    InitializeCrowTrade(ItemType.Goods, 1250, 4306, 6793, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13080000, 4307, 70001003, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 7130000, 4308, 70001004, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 14090000, 4309, 70001005, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13140000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13210000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13220000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13230000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13240000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Weapon, 13250000, 4310, 6794, 74000996);
    InitializeCrowTrade(ItemType.Goods, 351, 4311, 70001006, 74000996);
    InitializeCrowTrade(ItemType.Goods, 294, 4320, 6790, 74000997);
    InitializeCrowTrade(ItemType.Goods, 456, 4321, 70001020, 74000997);
    InitializeCrowTrade(ItemType.Goods, 292, 4322, 70001021, 74000997);
    InitializeCrowTrade(ItemType.Goods, 299, 4322, 70001021, 74000997);
    InitializeCrowTrade(ItemType.Goods, 297, 4323, 70001022, 74000997);
    InitializeCrowTrade(ItemType.Goods, 302, 4323, 70001022, 74000997);
    InitializeCrowTrade(ItemType.Goods, 300, 4324, 70001023, 74000997);
    InitializeCrowTrade(ItemType.Goods, 370, 4325, 70001024, 74000997);
    InitializeCrowTrade(ItemType.Goods, 440, 4326, 70001025, 74000997);
    InitializeCrowTrade(ItemType.Armor, 23500000, 4327, 70001026, 74000997);
    InitializeCrowTrade(ItemType.Weapon, 20040000, 4328, 70001027, 74000997);
    InitializeCrowTrade(ItemType.Weapon, 22050000, 4329, 70001028, 74000997);
    InitializeCrowTrade(ItemType.Weapon, 8280000, 4330, 70001029, 74000997);
    InitializeCrowTradeArea(4002796);
    InitializeCrowTradeArea(4002797);
    SetEventFlag(2040, OFF);
    SetEventFlag(2041, OFF);
    SetEventFlag(2042, OFF);
    SetEventFlag(74000990, OFF);
});

$Event(14000491, Default, function() {
    EndIf(PlayerIsNotInOwnWorld());
    SetEventFlag(74000995, OFF);
    WaitFor(InArea(10000, 4002795));
    SetEventFlag(74000995, ON);
    WaitFixedTimeSeconds(1);
    WaitFor(!InArea(10000, 4002795));
    SetEventFlag(74000995, OFF);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

// Iudex Gundyr - 
$Event(14005800, Default, function() {
    EndIf(EventFlag(14000800));
    WaitFor(HPRatio(4000800) <= 0);
    WaitFixedTimeSeconds(1);
    PlaySE(4000800, SoundType.s_SFX, 777777777);
    WaitFixedTimeSeconds(4);
    HandleBossDefeat(4000800);
    SetEventFlag(14000800, ON);
    SetEventFlag(9319, ON);
    SetEventFlag(6319, ON);
});

// Iudex Gundyr - 
$Event(14005810, Restart, function() {
    if (EventFlag(14000800)) {
        ForceCharacterDeath(4000800, false);
        ChangeCharacterEnableState(4000800, Disabled);
        SetCharacterAnimationState(4000800, Disabled);
        ActivateHit(4004150, Disabled);
        EndEvent();
    }
L0:
    SetCharacterAIState(4000800, Disabled);
    SetCharacterHPBarDisplay(4000800, Disabled);
    SetCharacterInvincibility(4000800, Enabled);
    SetLockOnPoint(4000800, 221, Disabled);
    ChangeCharacterHitmask(4000800, 0, ON);
    ForceAnimationPlayback(4000800, 30002, true, false, false, 0, 1);
    if (!EventFlag(14000802)) {
        WaitFor(EventFlag(14000802));
    } else {
L1:
        WaitFor(EventFlag(14005805) && InArea(10000, 4002800));
        ForceAnimationPlayback(4000800, 20002, false, false, false, 0, 1);
    }
L2:
    SetCharacterInvincibility(4000800, Disabled);
    ChangeCharacterHitmask(4000800, 0, ON);
    WaitFor(CharacterHasEventMessage(4000800, 40) || ThisEventSlot());
    SetCharacterAIState(4000800, Enabled);
    SetSpEffect(4000800, 5800);
    SetCharacterHPBarDisplay(4000800, Enabled);
    SetNetworkUpdateRate(4000800, true, CharacterUpdateFrequency.AlwaysUpdate);
    DisplayBossHealthBar(Enabled, 4000800, 0, 905110);
    SetEventFlag(14000801, ON);
    EndEvent();
});

// Iudex Gundyr - 
$Event(14005811, Default, function() {
    EndIf(EventFlag(14000800));
    if (EventFlag(14000802)) {
        WaitFor(CharacterBackreadStatus(4000800));
        ChangeCharacterDispmask(4000800, 0, ON);
        ChangeCharacterDispmask(4000800, 2, OFF);
        ChangeCharacterDispmask(4000800, 3, ON);
        ChangeCharacterDispmask(4000800, 4, ON);
        EndEvent();
    }
L0:
    WaitFor(EventFlag(14000802) || ActionButtonInArea(8900, 4000800));
    EndIf(EventFlag(14000802));
    IssueShortWarpRequest(10000, TargetEntityType.Character, 4000800, 100);
    ForceAnimationPlayback(10000, 60750, false, false, false, 0, 1);
    ForceAnimationPlayback(4000800, 20003, false, false, false, 0, 1);
    WaitFor(EventFlag(14000802) || CharacterHasEventMessage(4000800, 20));
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetNetworkconnectedEventFlag(14000802, ON);
    }
});

// Iudex Gundyr - 
$Event(14005812, Restart, function() {
    EndIf(EventFlag(14000800));
    WaitFor(CharacterHasEventMessage(4000800, 10));
    ChangeCharacterHitmask(4000800, 0, OFF);
    SetLockOnPoint(4000800, 221, Enabled);
    SetEventFlag(14005802, ON);
});

// Iudex Gundyr - 
$Event(14005813, Restart, function() {
    SetNetworkSyncState(Disabled);
    EndIf(EventFlag(14000800));
    WaitFor(EventFlag(14005805) && EventFlag(14005802));
    WaitFixedTimeSeconds(1.5);
    ChangeCamera(5110, 5110);
    WaitFor(HPRatio(4000800) <= 0);
    ChangeCamera(-1, -1);
});

// Iudex Gundyr - 
$Event(14000816, Restart, function() {
    SetObjactState(4001260, -1, Disabled);
    SetObjactState(4001261, -1, Disabled);
    EndIf(EventFlag(64000260));
    WaitFor(EventFlag(14000800));
    SetObjactState(4001260, 400005, Enabled);
});

// Iudex Gundyr - Common Setup
$Event(14005820, Restart, function() {
    InitializeCommonEvent(20005800, 14000800, 4001800, 4002800, 14005805, 4001800, 4000800, 14000801, 4002800);
    InitializeCommonEvent(20005801, 14000800, 4001800, 4002800, 14005805, 4001800, 14005822);
    InitializeCommonEvent(20005820, 14000800, 4001800, 3, 14000801);
    if (EventFlag(14000801)) {
        InitializeCommonEvent(20005831, 14000800, 14005805, 14005822, 4002800, 4004800, 4004801, 14005802);
        EndEvent();
    }
    InitializeCommonEvent(20001836, 14000800, 14005805, 14005822, 14000801, 4004800, 4004801, 14005802);
});


