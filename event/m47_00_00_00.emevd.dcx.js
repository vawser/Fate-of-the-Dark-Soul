// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    GotoIf(L0, HasHollowArenaMatchType(HollowArenaMatchType.Duel));
    GotoIf(L1, HasHollowArenaMatchType(HollowArenaMatchType.TwoPlayerBrawl));
    GotoIf(L2, HasHollowArenaMatchType(HollowArenaMatchType.FourPlayerBrawl));
    GotoIf(L3, HasHollowArenaMatchType(HollowArenaMatchType.SixPlayerBrawl));
    GotoIf(L4, HasHollowArenaMatchType(HollowArenaMatchType.TwoVersusThree));
    GotoIf(L5, HasHollowArenaMatchType(HollowArenaMatchType.ThreeVersusThree));
L0:
    InitializeCommonEvent(20005920, 0, 14705300, 10020000, 10020010);
    InitializeCommonEvent(20005930, 14705300);
    InitializeCommonEvent(20005941, 14705300);
    EndEvent();
L1:
    InitializeCommonEvent(20005920, 1, 14705300, 10020001, 10020011);
    Goto(L9);
L2:
    InitializeCommonEvent(20005920, 2, 14705300, 10020002, 10020012);
    Goto(L9);
L3:
    InitializeCommonEvent(20005920, 3, 14705300, 10020003, 10020013);
    Goto(L9);
L4:
    InitializeCommonEvent(20005920, 4, 14705300, 10020004, 10020014);
    Goto(L9);
L5:
    InitializeCommonEvent(20005920, 5, 14705300, 10020005, 10020015);
    Goto(L9);
L9:
    InitializeCommonEvent(20005940, 14705300);
});


