// ==EMEVD==
// @docs    ds3-common.emedf.json
// @compress    DCX_DFLT_10000_44_9
// @game    DarkSouls3
// @string    N:\FDP\data\Param\event\common_func.emevd       
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    //RegisterBonfire(13900000, 3901950, 5, 180, 0);
    //RegisterBonfire(13900002, 3901952, 5, 180, 0);
    //InitializeCommonEvent(20005500, 13900800, 13900001, 3900951, 3901951);
    
    // Bonfires - Skip if in Flameless
    if(!EventFlag(25000141))
    {
        RegisterBonfire(13900800, 3901951, 5, 180, 0); // Yhorm
    }
    else
    {
        DeactivateObject(3901951, Disabled);
    }
    
    // Penetrator - Penetrating Sword
    InitializeCommonEvent(20005341, 13900235, 3900235, 3900830);
    
    // Khen the Depraved - Reward
    InitializeCommonEvent(20005341, 13910235, 3910235, 70070); 
    
    InitializeCommonEvent(20005780, 3901780, 2);
    InitializeCommonEvent(20005750, 13900800, 13900192, 13904192, 13905192, 3900192, 3902192, 3902193, 0, 0);
    InitializeCommonEvent(20005721, 13904192, 13905192, 13900192, 3900192);
    InitializeCommonEvent(20005760, 13900192, 13904192, 13905192, 3900192);
    InitializeCommonEvent(20005341, 13900192, 3900192, 58600);
    InitializeEvent(0, 13905900, 0);
    InitializeCommonEvent(20005119, 3900200, 3902200, 3902201, 3902206, 0, 0, 0, 0);
    InitializeCommonEvent(20005110, 3900203, 3902202);
    InitializeCommonEvent(20005110, 3900206, 3902202);
    InitializeCommonEvent(20005110, 3900207, 3902202);
    InitializeCommonEvent(20005203, 3900220, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0);
    InitializeCommonEvent(20005203, 3900221, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0);
    InitializeCommonEvent(20005203, 3900222, 30000, 20000, 3902220, 3902221, 3902222, 0, 0, 0);
    InitializeCommonEvent(20005210, 3900223, 30000, 20000, 1077936128);
    InitializeCommonEvent(20005110, 3900225, 3902228);
    InitializeCommonEvent(20005110, 3900226, 3902228);
    InitializeEvent(0, 13905220, 3900225, 3902227, 13905225);
    InitializeEvent(1, 13905220, 3900226, 3902227, 13905226);
    InitializeEvent(0, 13905225, 3900225, 3902228, 13905220);
    InitializeEvent(1, 13905225, 3900226, 3902228, 13905221);
    InitializeEvent(0, 13905230, 3900204, 3904240, 53900510);
    InitializeEvent(1, 13905230, 3900205, 3904240, 53900510);
    InitializeCommonEvent(20005119, 3900390, 3902390, 3902391, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005119, 3900391, 3902390, 3902391, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005119, 3900392, 3902392, 3902391, 3902390, 0, 0, 0, 0);
    InitializeCommonEvent(20005119, 3900393, 3902392, 3902391, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005119, 3900394, 3902392, 3902391, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005120, 3900395, 1089470464);
    InitializeCommonEvent(20005290, 3900230, 30001, -1);
    InitializeCommonEvent(20005212, 3900231, 30000, 20003, 1084227584, 3902231);
    InitializeCommonEvent(20005111, 3900233, 3008, 3902233);
    InitializeCommonEvent(20005133, 3900234, 3001, 1077936128, 3902234);
    InitializeCommonEvent(20005220, 3900240, 30000, 20003);
    InitializeCommonEvent(20005220, 3900241, 702, 1702);
    InitializeCommonEvent(20005260, 3900242, 700, 1700, 3900241);
    InitializeCommonEvent(20005260, 3900243, 700, 1700, 3900241);
    InitializeCommonEvent(20005220, 3900244, 30000, 20003);
    InitializeCommonEvent(20005134, 3900250, 3006, 1069547520, 3902253);
    InitializeEvent(0, 13905251, 0);
    InitializeEvent(0, 13905255, 3900257, 700, 1700, 1069547520, 0, 3901200, 3901201, 3901205, 0, 0);
    InitializeEvent(1, 13905255, 3900267, 701, 3001, 1069547520, 0, 3901202, 3901203, 3901204, 3901206, 0);
    InitializeEvent(2, 13905255, 3900268, 702, 1702, 1069547520, 1045220557, 3901202, 3901203, 3901204, 3901206, 0);
    InitializeEvent(3, 13905255, 3900269, 700, 1700, 1069547520, 0, 3901202, 3901203, 3901204, 3901206, 0);
    InitializeCommonEvent(20005210, 3900252, 702, 1702, 1069547520);
    InitializeCommonEvent(20005213, 3900253, 700, 1700, 1069547520, 3902258);
    InitializeCommonEvent(20005213, 3900255, 702, 1702, 1069547520, 3902258);
    InitializeCommonEvent(20005213, 3900256, 700, 1700, 1069547520, 3902258);
    InitializeCommonEvent(20005114, 3900257, 3902256, 1065353216);
    InitializeCommonEvent(20005121, 3900258, 1084227584, 1086324736);
    InitializeCommonEvent(20005119, 3900260, 3902252, 3902260, 0, 0, 0, 0, 0);
    InitializeCommonEvent(20005204, 3900261, 700, 1700, 3902250, 1073741824, 1700, 3902252, 1073741824);
    InitializeCommonEvent(20005132, 3900262, 1084227584, 3902257);
    InitializeCommonEvent(20005210, 3900263, 702, 1702, 1077936128);
    InitializeCommonEvent(20005114, 3900264, 3902257, 1090519040);
    InitializeCommonEvent(20005120, 3900264, 1077936128);
    InitializeCommonEvent(20005210, 3900265, 702, 1702, 1077936128);
    InitializeCommonEvent(20005213, 3900266, 700, 1700, 1082130432, 3902254);
    InitializeCommonEvent(20005110, 3900268, 3902255);
    InitializeEvent(0, 13900260, 3900254, 703, 1703);
    InitializeCommonEvent(20005350, 3900259, 20601010, 53900920);
    InitializeCommonEvent(20005122, 3900270, 3000, 1073741824);
    InitializeCommonEvent(20005122, 3900271, 3000, 1073741824);
    InitializeCommonEvent(20005122, 3900272, 3000, 1069547520);
    InitializeCommonEvent(20005122, 3900273, 3000, 1077936128);
    InitializeCommonEvent(20005122, 3900274, 3000, 1077936128);
    InitializeCommonEvent(20005122, 3900275, 3000, 1077936128);
    InitializeCommonEvent(20005131, 3900276, 3000, 1075838976, 3902270);
    InitializeCommonEvent(20005131, 3900277, 3000, 1073741824, 3902270);
    InitializeCommonEvent(20005114, 3900280, 3902291, 1086324736);
    InitializeCommonEvent(20005190, 3900290, 1101529088);
    InitializeCommonEvent(20005220, 3900291, 706, 1706);
    InitializeCommonEvent(20005110, 3900292, 3902291);
    InitializeCommonEvent(20005110, 3900293, 3902291);
    InitializeCommonEvent(20005130, 3900294, 1106247680, 3902291);
    InitializeCommonEvent(20005110, 3900296, 3902291);
    InitializeCommonEvent(20005110, 3900297, 3902291);
    InitializeCommonEvent(20005114, 3900298, 3902291, 1086324736);
    InitializeCommonEvent(20005110, 3900299, 3902290);
    DeactivateGenerator(3904300, Enabled);
    InitializeCommonEvent(20005320, 3900310, 3902310, 3904310);
    InitializeCommonEvent(20005330, 3900311, 3902311, 13905300);
    InitializeCommonEvent(20005330, 3900312, 3902311, 13905301);
    InitializeCommonEvent(20005330, 3900313, 3902311, 13905302);
    InitializeCommonEvent(20005330, 3900314, 3902311, 13905303);
    InitializeCommonEvent(20005110, 3900315, 3902312);
    InitializeCommonEvent(20005110, 3900316, 3902312);
    InitializeCommonEvent(20005192, 3900317, 3902310);
    InitializeCommonEvent(20005192, 3900318, 3902310);
    InitializeEvent(0, 13905320, 3900321, 13905325);
    InitializeEvent(1, 13905320, 3900322, 13905326);
    InitializeEvent(2, 13905320, 3900323, 13905327);
    InitializeEvent(3, 13905320, 3900324, 13905328);
    InitializeEvent(4, 13905320, 3900325, 13905329);
    InitializeCommonEvent(20005111, 3900321, 20000, 3902321);
    InitializeCommonEvent(20005111, 3900322, 20000, 3902321);
    InitializeCommonEvent(20005111, 3900323, 20000, 3902321);
    InitializeCommonEvent(20005111, 3900324, 20000, 3902321);
    InitializeCommonEvent(20005111, 3900325, 20000, 3902321);
    InitializeCommonEvent(20005212, 3900330, 700, 1700, 1090519040, 3902330);
    InitializeCommonEvent(20005212, 3900331, 700, 1700, 1090519040, 3902330);
    InitializeCommonEvent(20005212, 3900332, 700, 1700, 1085276160, 3902330);
    InitializeCommonEvent(20005211, 3900333, 700, 1700, 1088421888, 0);
    InitializeCommonEvent(20005211, 3900334, 700, 1700, 1085276160, 0);
    InitializeCommonEvent(20005211, 3900335, 700, 20000, 1090519040, 0);
    InitializeCommonEvent(20005211, 3900336, 700, 1700, 1087373312, 1065353216);
    InitializeCommonEvent(20005211, 3900337, 700, 20000, 1082130432, 1065353216);
    InitializeCommonEvent(20005211, 3900338, 700, 20000, 1094713344, 1065353216);
    InitializeCommonEvent(20005211, 3900339, 700, 1700, 1090519040, 1065353216);
    InitializeCommonEvent(20005341, 13900340, 3900340, 21508000);
    InitializeCommonEvent(20005341, 13900341, 3900341, 21508010);
    InitializeCommonEvent(20005341, 13900342, 3900342, 21508020);
    InitializeCommonEvent(20005341, 13900343, 3900343, 21508030);
    InitializeCommonEvent(20005400, 3900350);
    InitializeCommonEvent(20005400, 3900351);
    InitializeCommonEvent(20005400, 3900352);
    InitializeCommonEvent(20005400, 3900353);
    InitializeCommonEvent(20005400, 3900354);
    InitializeCommonEvent(20005400, 3900355);
    InitializeCommonEvent(20005400, 3900356);
    InitializeCommonEvent(20000343, 13900350, 3900350, 53900940);
    InitializeCommonEvent(20000343, 13900351, 3900351, 53900990);
    InitializeCommonEvent(20000343, 13900352, 3900352, 53900970);
    InitializeCommonEvent(20000343, 13900353, 3900353, 53900950);
    InitializeCommonEvent(20000343, 13900354, 3900354, 53900960);
    InitializeCommonEvent(20000343, 13900355, 3900355, 53900980);
    InitializeCommonEvent(20000343, 13900356, 3900356, 53900995);
    InitializeEvent(0, 13905360, 0);
    InitializeEvent(0, 13905361, 0);
    InitializeEvent(0, 13905363, 0);
    InitializeEvent(0, 13905364, 0);
    InitializeCommonEvent(20005132, 3900362, 1101004800, 3902362);
    InitializeCommonEvent(20005220, 3900370, 700, 1700);
    InitializeCommonEvent(20005220, 3900371, 700, 1700);
    InitializeCommonEvent(20005220, 3900372, 700, 1700);
    InitializeCommonEvent(20005340, 13900370, 3900370);
    InitializeCommonEvent(20005340, 13900371, 3900371);
    InitializeCommonEvent(20005340, 13900372, 3900372);
    InitializeCommonEvent(20005341, 13900373, 3900373, 20400020);
    InitializeEvent(0, 13905380, 0);
    InitializeEvent(0, 13905381, 0);
    InitializeCommonEvent(20005340, 13900380, 3900380);
    InitializeCommonEvent(20005110, 3900399, 3902280);
    InitializeCommonEvent(20005342, 13900360, 3900399);
    InitializeEvent(0, 13905810, 0);
    InitializeEvent(0, 13905811, 0);
    InitializeEvent(0, 13905815, 0);
    InitializeEvent(0, 13905816, 0);
    InitializeEvent(0, 13905820, 0);
    InitializeEvent(0, 13905840, 0);
    InitializeEvent(0, 13905850, 0);
    InitializeEvent(0, 13905860, 0);
    InitializeEvent(0, 13905861, 0);
    InitializeEvent(0, 13905830, 196618, 400, 10, 20000);
    InitializeEvent(1, 13905830, 393236, 400, 20, 20002);
    InitializeEvent(0, 13905835, 0);
    InitializeEvent(0, 13905870, 3901651, 3901650);
    InitializeEvent(0, 13905500, 13900500, 3901500, 3903500, 3903600);
    InitializeEvent(2, 13905500, 13900502, 3901502, 3903502, 3903602);
    InitializeEvent(3, 13905500, 13900503, 3901503, 3903503, 3903603);
    InitializeEvent(4, 13905500, 13900504, 3901504, 3903504, 3903604);
    InitializeEvent(5, 13905500, 13900505, 3901505, 3903505, 3903605);
    InitializeEvent(6, 13905500, 13900510, 3901510, 3903510, 3903610);
    InitializeEvent(7, 13905500, 13900511, 3901511, 3903511, 3903611);
    InitializeEvent(8, 13905500, 13900512, 3901512, 3903512, 3903612);
    InitializeEvent(9, 13905500, 13900513, 3901513, 3903513, 3903613);
    InitializeEvent(10, 13905500, 13900514, 3901514, 3903514, 3903614);
    InitializeEvent(11, 13905500, 13900515, 3901515, 3903515, 3903615);
    InitializeEvent(12, 13905500, 13900516, 3901516, 3903516, 3903616);
    InitializeEvent(13, 13905500, 13900517, 3901517, 3903517, 3903617);
    InitializeEvent(16, 13905500, 13900520, 3901520, 3903520, 3903620);
    InitializeEvent(17, 13905500, 13900521, 3901521, 3903521, 3903621);
    InitializeEvent(18, 13905500, 13900522, 3901522, 3903522, 3903622);
    InitializeEvent(21, 13905500, 13900525, 3901525, 3903525, 3903625);
    InitializeEvent(22, 13905500, 13900526, 3901526, 3903526, 3903626);
    InitializeEvent(24, 13905500, 13900528, 3901528, 3903528, 3903628);
    InitializeEvent(25, 13905500, 13900530, 3901530, 3903530, 3903630);
    InitializeEvent(27, 13905500, 13900532, 3901532, 3903532, 3903632);
    InitializeEvent(28, 13905500, 13900533, 3901533, 3903533, 3903633);
    InitializeEvent(29, 13905500, 13900534, 3901534, 3903534, 3903634);
    InitializeEvent(30, 13905500, 13900535, 3901535, 3903535, 3903635);
    InitializeEvent(0, 13905420, 0);
    InitializeEvent(0, 13905425, 0);
    InitializeEvent(0, 13905430, 0);
    InitializeEvent(0, 13905435, 0);
    InitializeEvent(0, 13905440, 0);
    InitializeEvent(0, 13905445, 0);
    InitializeEvent(0, 13905450, 0);
    InitializeEvent(0, 13905460, 0);
    InitializeEvent(0, 13905480, 0);
    InitializeCommonEvent(20005613, 13900550, 3903550, 3901550, 390350, 10010868);
    InitializeCommonEvent(20005613, 13900551, 3903551, 3901551, 390350, 10010868);
    InitializeEvent(0, 13905415, 13900552, 3903552, 3903557, 3901552, 390350, 390360, 10010868);
    InitializeEvent(1, 13905415, 13900553, 3903553, 3903558, 3901553, 390350, 390360, 10010868);
    InitializeEvent(0, 13905470, 0);
    InitializeEvent(0, 13905471, 0);
    InitializeEvent(0, 13905475, 0);
    InitializeCommonEvent(20005620, 13900400, 13900402, 3901400, 3901401, 3901402, 13901400);
    InitializeCommonEvent(20005628, 13900401, 3901401, 3902402);
    InitializeEvent(0, 13900411, 0);
    InitializeCommonEvent(20005622, 13900405, 13900407, 3901405, 3901406, 3901407, 13901405);
    InitializeCommonEvent(20005628, 13900406, 3901406, 3902407);
    InitializeEvent(0, 13900412, 0);
    InitializeCommonEvent(20005520, 13900609, 3901609, 3904609);
    InitializeCommonEvent(20005520, 13900611, 3901611, 3904611);
    InitializeCommonEvent(20005520, 13900613, 3901613, 3904613);
    InitializeEvent(0, 13905620, 3901620, 53900450, 13905620);
    InitializeEvent(1, 13905620, 3901621, 53900460, 13905621);
    InitializeEvent(2, 13905620, 3901625, 53900510, 13905625);
    InitializeCommonEvent(20005524, 3901622, 13900192);
    InitializeCommonEvent(20005523, 3901624, 1);
    InitializeCommonEvent(20005523, 3901627, 1);
    InitializeCommonEvent(20005523, 3901628, 2);
    InitializeEvent(0, 13900900, 0);
    InitializeCommonEvent(20006002, 3900705, 1398, 1395, 1399);
    InitializeCommonEvent(20006002, 3900706, 1398, 1395, 1399);
    InitializeCommonEvent(20006000, 3900705, 1396, 1397, 73900190, 1059481190, 1395, 1399, 0);
    InitializeCommonEvent(20006001, 3900705, 1396, 1397, 73900190, 3);
    InitializeEvent(0, 13900721, 0);
    InitializeEvent(0, 13900723, 3900706, 1108869120);
    InitializeEvent(0, 13900726, 0);
    InitializeEvent(0, 13905727, 0);
    InitializeEvent(0, 13905728, 0);
    InitializeEvent(0, 13900729, 3900705);
    InitializeCommonEvent(20006030, 3901706, 4000, 1, 62140, 50006215, 50006216, 1390);
});

$Event(50, Default, function() {
    InitializeEvent(0, 13900465, 0);
    InitializeEvent(0, 13900410, 0);
    InitializeEvent(0, 13905720, 3900705, 3900706);
    SetMapSoundState(3904801, Disabled);
    SetMapSoundState(3904802, Disabled);
});

$Event(13905220, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    WaitFor(
        ((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.Hollow)
            || CharacterType(10000, TargetType.WhitePhantom))
            && InArea(10000, X4_4)
            && !EventFlag(X8_4));
    SetSpEffect(X0_4, 11890);
    ClearSpEffect(X0_4, 11900);
    ClearSpEffect(X0_4, 11901);
    ClearSpEffect(X0_4, 11902);
    ClearSpEffect(X0_4, 11903);
    ClearSpEffect(X0_4, 11899);
});

$Event(13905225, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    WaitFor(
        (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.Hollow)
            || CharacterType(10000, TargetType.WhitePhantom))
            && InArea(10000, X4_4)
            && EventFlag(X8_4))
            || CharacterDamagedBy(X0_4, 10000));
    SetCharacterAIState(X0_4, Enabled);
    ClearSpEffect(X0_4, 11890);
    SetSpEffect(X0_4, 11899);
});

$Event(13905230, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    EndIf(EventFlag(X8_4));
    WaitFor(EventFlag(X8_4));
    RequestCharacterAIReplan(X0_4);
    SetSpEffect(X0_4, 5000);
    ChangeCharacterPatrolBehavior(X0_4, X4_4);
    WaitFor(ThisEventSlot() || CharacterAIState(X0_4, AIStateType.Combat));
    ClearSpEffect(X0_4, 5000);
});

$Event(13905251, Restart, function() {
    EndIf(ThisEventSlot());
    ForceAnimationPlayback(3900251, 702, true, false, false, 0, 1);
    WaitFor(
        EventFlagState(CHANGE, TargetEventFlagType.EventFlag, 53900450)
            || (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
                || CharacterType(10000, TargetType.Alive)
                || CharacterType(10000, TargetType.WhitePhantom)
                || CharacterType(10000, TargetType.Hollow))
                && EntityInRadiusOfEntity(10000, 3902254, 1.5, 1))
            || CharacterDamagedBy(3900251, 10000));
    EndIf(!CharacterHasSpEffect(3900251, 5450));
    ForceAnimationPlayback(3900251, 1702, false, false, false, 0, 1);
    RequestCharacterAIReplan(3900251);
});

$Event(13905255, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    EndIf(ThisEventSlot());
    RequestObjectRestoration(X20_4);
    RequestObjectRestoration(X24_4);
    RequestObjectRestoration(X28_4);
    RequestObjectRestoration(X32_4);
    RequestObjectRestoration(X36_4);
    ForceAnimationPlayback(X0_4, X4_4, true, false, false, 0, 1);
    chrSpAreaObjDmg |= ((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.WhitePhantom)
        || CharacterType(10000, TargetType.Hollow))
        && EntityInRadiusOfEntity(10000, X0_4, X12_4, 1);
    obj |= ObjectDestroyed(X20_4);
    if (X24_4 != 0) {
        obj |= ObjectDestroyed(X24_4);
    }
    if (X28_4 != 0) {
        obj |= ObjectDestroyed(X28_4);
    }
    if (X32_4 != 0) {
        obj |= ObjectDestroyed(X32_4);
    }
    if (X36_4 != 0) {
        obj |= ObjectDestroyed(X36_4);
    }
    chrSpAreaObjDmg |= obj || CharacterDamagedBy(X0_4, 10000);
    WaitFor(chrSpAreaObjDmg);
    WaitFixedTimeSeconds(X16_4);
    SetCharacterAIState(X0_4, Enabled);
    ForceAnimationPlayback(X0_4, X8_4, false, false, false, 0, 1);
    RequestCharacterAIReplan(X0_4);
});

$Event(13900260, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    ForceAnimationPlayback(X0_4, X4_4, false, false, false, 0, 1);
    WaitFor(ObjActEventFlag(3903515) || ObjActEventFlag(3903615));
    ForceAnimationPlayback(X0_4, X8_4, false, false, false, 0, 1);
});

$Event(13905320, Restart, function(X0_4, X4_4) {
    EndIf(ThisEventSlot());
    if (!EventFlag(X4_4)) {
        SetCharacterAIState(X0_4, Disabled);
        WaitFor(
            (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
                || CharacterType(10000, TargetType.Alive)
                || CharacterType(10000, TargetType.WhitePhantom)
                || CharacterType(10000, TargetType.Hollow))
                && InArea(10000, 3902320)
                && EventFlag(53900610))
                || EventFlagState(CHANGE, TargetEventFlagType.EventFlag, 53900610)
                || CharacterDamagedBy(X0_4, 10000));
    }
L0:
    SetCharacterAIState(X0_4, Enabled);
    SetSpEffect(X0_4, 5000);
    SetEventFlag(X4_4, ON);
    WaitFor(CharacterAIState(X0_4, AIStateType.Combat));
    ClearSpEffect(X0_4, 5000);
});

$Event(13905360, Restart, function() {
    EndIf(ThisEventSlot());
    SetCharacterAIState(3900360, Disabled);
    SetCharacterGravity(3900360, Disabled);
    SetCharacterMaphit(3900360, true);
    ForceAnimationPlayback(3900360, 30001, true, false, false, 0, 1);
    WaitFor(
        (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.WhitePhantom)
            || CharacterType(10000, TargetType.Hollow))
            && InArea(10000, 3902360)
            && CharacterBackreadStatus(3900360)
            && CharacterHasSpEffect(3900360, 5450))
            || CharacterDamagedBy(3900360, 10000));
    SetNetworkUpdateRate(3900360, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetSpEffect(3900360, 640);
    SetCharacterAIState(3900360, Enabled);
    SetCharacterHome(3900360, 3902365);
    SetCharacterGravity(3900360, Enabled);
    SetCharacterMaphit(3900360, false);
    ForceAnimationPlayback(3900360, 20000, false, true, false, 0, 1);
    SetNetworkUpdateRate(3900360, false, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(13905361, Restart, function() {
    EndIf(ThisEventSlot());
    SetCharacterAIState(3900361, Disabled);
    SetCharacterGravity(3900361, Disabled);
    SetCharacterMaphit(3900361, true);
    ForceAnimationPlayback(3900361, 30001, true, false, false, 0, 1);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.WhitePhantom)
        || CharacterType(10000, TargetType.Hollow);
    areaChrSpDmg = InArea(10000, 3902361)
        || (chrSp
            && areaChrSpDmg
            && CharacterBackreadStatus(3900361)
            && CharacterHasSpEffect(3900361, 5450))
        || CharacterDamagedBy(3900361, 10000);
    WaitFor(areaChrSpDmg);
    SetNetworkUpdateRate(3900361, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetSpEffect(3900361, 640);
    SetCharacterAIState(3900361, Enabled);
    SetCharacterHome(3900361, 3902366);
    SetCharacterGravity(3900361, Enabled);
    SetCharacterMaphit(3900361, false);
    ForceAnimationPlayback(3900361, 20005, false, true, false, 0, 1);
    SetNetworkUpdateRate(3900361, false, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(13905363, Restart, function() {
    EndIf(ThisEventSlot());
    SetCharacterAIState(3900363, Disabled);
    SetCharacterGravity(3900363, Disabled);
    SetCharacterMaphit(3900363, true);
    ForceAnimationPlayback(3900363, 30001, true, false, false, 0, 1);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.WhitePhantom)
        || CharacterType(10000, TargetType.Hollow);
    areaChrSpDmgHp = InArea(10000, 3902363)
        || InArea(10000, 3902364)
        || (chrSp
            && areaChrSpDmgHp
            && CharacterBackreadStatus(3900363)
            && CharacterHasSpEffect(3900363, 5450))
        || CharacterDamagedBy(3900363, 10000)
        || CharacterDead(3905390)
        || HPRatio(3900364) <= 0.5;
    WaitFor(areaChrSpDmgHp);
    SetNetworkUpdateRate(3900363, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetSpEffect(3900363, 640);
    SetCharacterHome(3900363, 3902368);
    SetCharacterGravity(3900363, Enabled);
    SetCharacterMaphit(3900363, false);
    ForceAnimationPlayback(3900363, 20007, false, true, false, 0, 1);
    SetNetworkUpdateRate(3900363, false, CharacterUpdateFrequency.AlwaysUpdate);
    SetCharacterAIState(3900363, Enabled);
    if (InArea(10000, 3902364)) {
        SetSpEffect(3900363, 5000);
        ChangeCharacterPatrolBehavior(3900363, 3904360);
    }
L0:
    RequestCharacterAIReplan(3900363);
});

$Event(13905364, Restart, function() {
    EndIf(ThisEventSlot());
    SetCharacterAIState(3900364, Disabled);
    SetCharacterGravity(3900364, Disabled);
    SetCharacterMaphit(3900364, true);
    ForceAnimationPlayback(3900364, 30001, true, false, false, 0, 1);
    WaitFor(
        (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.WhitePhantom)
            || CharacterType(10000, TargetType.Hollow))
            && InArea(10000, 3902364))
            || CharacterDamagedBy(3900364, 10000));
    SetNetworkUpdateRate(3900363, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetSpEffect(3900364, 640);
    SetCharacterAIState(3900364, Enabled);
    SetCharacterHome(3900364, 3902369);
    SetCharacterGravity(3900364, Enabled);
    SetCharacterMaphit(3900364, false);
    ForceAnimationPlayback(3900364, 20006, false, true, false, 0, 1);
    SetNetworkUpdateRate(3900363, false, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(13905380, Restart, function() {
    SetCharacterAIState(3900380, Disabled);
    ForceAnimationPlayback(3900380, 30000, true, false, false, 0, 1);
    WaitFor(
        ((CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.WhitePhantom)
            || CharacterType(10000, TargetType.Hollow))
            && InArea(10000, 3902380))
            || CharacterDamagedBy(3900380, 10000));
    ForceAnimationPlayback(3900380, 20000, false, true, false, 0, 1);
    SetCharacterAIState(3900380, Enabled);
});

$Event(13905381, Restart, function() {
    SetNetworkSyncState(Disabled);
    SetNetworkUpdateRate(3900380, false, CharacterUpdateFrequency.Every5Frames);
    WaitFor(CharacterBackreadStatus(3900380) && !CharacterDead(3900380));
    SetNetworkUpdateRate(3900380, true, CharacterUpdateFrequency.AlwaysUpdate);
    WaitFor(!CharacterBackreadStatus(3900380) || CharacterDead(3900380));
    RestartEvent();
});

$Event(13905415, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    EndIf(PlayerIsNotInOwnWorld());
    if (!EventFlag(X0_4)) {
        WaitFor(!PlayerIsNotInOwnWorld() && (ObjActEventFlag(X4_4) || ObjActEventFlag(X8_4)));
        DisplayGenericDialog(X24_4, PromptType.OKCANCEL, NumberofOptions.NoButtons, X12_4, 3);
        SetEventFlag(X0_4, ON);
    }
L0:
    SetObjactState(X12_4, X16_4, Disabled);
    SetObjactState(X12_4, X20_4, Disabled);
});

$Event(13900900, Default, function() {
    SetNetworkSyncState(Disabled);
    EndIf(PlayerIsNotInOwnWorld());
    EndIf(ThisEventSlot());
    CreateObjectfollowingSFX(3901250, 90, 61);
    WaitFor(ActionButtonInArea(4200, 3901250));
    ForceAnimationPlayback(10000, 60070, false, false, true, 0, 1);
    if (!EventFlag(6073)) {
        AwardGestureItem(23, ItemType.Goods, 9024);
    }
    AwardItemLot(3900900);
    DeleteObjectfollowingSFX(3901250, true);
    SetEventFlag(6073, ON);
});

$Event(13900410, Default, function() {
    EndIf(ThisEventSlot());
    SetEventFlag(13900400, ON);
    SetEventFlag(13900405, ON);
    SetEventFlag(13900410, ON);
});

$Event(13900411, Restart, function() {
    InitializeCommonEvent(20005621, 13900400, 13900402, 3901400, 3901401, 3904401, 3901402, 3904402, 3902401, 3902402, 13901400, 13904400, 13900401);
});

$Event(13900412, Restart, function() {
    InitializeCommonEvent(20005623, 13900405, 13900407, 3901405, 3901406, 3904406, 3901407, 3904407, 3902406, 3902407, 13901405, 13904405, 13900406);
});

$Event(13905420, Default, function() {
    InitializeCommonEvent(20005610, 13900420, 3902420, 3902421);
    InitializeCommonEvent(20005611, 13900420, 3903420, 3901420, 390305);
});

$Event(13905425, Default, function() {
    InitializeCommonEvent(20005613, 13900425, 3903425, 3901425, 390340, 10010872);
});

$Event(13905430, Default, function() {
    InitializeCommonEvent(20005610, 13900430, 3902430, 3902431);
    InitializeCommonEvent(20005611, 13900430, 3903430, 3901430, 390305);
});

$Event(13905435, Default, function() {
    InitializeCommonEvent(20005610, 13900435, 3902435, 3902436);
    InitializeCommonEvent(20005611, 13900435, 3903435, 3901435, 390300);
});

$Event(13905440, Default, function() {
    InitializeCommonEvent(20005610, 13900440, 3902440, 3902441);
    InitializeCommonEvent(20005611, 13900440, 3903440, 3901440, 390305);
});

$Event(13905445, Default, function() {
    ReproduceObjectAnimation(3901445, 0);
});

$Event(13905450, Default, function() {
    InitializeCommonEvent(20005613, 13900450, 3903450, 3901450, 390320, 10010867);
});

$Event(13905460, Default, function() {
    InitializeCommonEvent(20005614, 3901460, 63900460);
});

$Event(13900465, Default, function() {
    EndIf(ThisEventSlot());
    SetEventFlag(13900500, ON);
    SetEventFlag(13900502, ON);
    SetEventFlag(13900504, ON);
    SetEventFlag(13900505, ON);
    SetEventFlag(13900511, ON);
    SetEventFlag(13900512, ON);
    SetEventFlag(13900514, ON);
    SetEventFlag(13900516, ON);
    SetEventFlag(13900517, ON);
    SetEventFlag(13900518, ON);
    SetEventFlag(13900521, ON);
    SetEventFlag(13900522, ON);
    SetEventFlag(13900526, ON);
    SetEventFlag(13900528, ON);
    SetEventFlag(13900535, ON);
});

$Event(13905470, Restart, function() {
    DeleteObjectfollowingSFX(3901470, false);
    CreateObjectfollowingSFX(3901470, 200, 839020);
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetNetworkUpdateAuthority(3900470, AuthorityLevel.Forced);
    }
});

$Event(13905471, Restart, function() {
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SetNetworkconnectedEventFlag(13900471, OFF);
    }
    if (!EventFlag(13905479)) {
        SetNetworkUpdateRate(3900470, true, CharacterUpdateFrequency.AlwaysUpdate);
        WaitFor(
            EventFlag(13900472)
                || (!EventFlag(13900471)
                    && (CharacterType(10000, TargetType.Alive)
                        || CharacterType(10000, TargetType.WhitePhantom)
                        || CharacterType(10000, TargetType.Hollow))
                    && (InArea(10000, 3902471) || InArea(10000, 3902472) || InArea(10000, 3902473))));
        if (NumberOfClientsOfType(ClientType.Invader) != 0) {
            SetNetworkconnectedEventFlag(13900471, ON);
            SetNetworkconnectedEventFlag(13900472, ON);
        }
        SetEventFlag(13900472, OFF);
        if (!EventFlag(13905479)) {
            SpawnOneshotSFX(TargetEntityType.Area, 3902470, -1, 524112);
            if (EventFlag(50)) {
                ShootBullet(3900470, 3902470, -1, 5900, 0, 0, 0);
            }
            if (EventFlag(51)) {
                ShootBullet(3900470, 3902470, -1, 5901, 0, 0, 0);
            }
            if (EventFlag(52)) {
                ShootBullet(3900470, 3902470, -1, 5902, 0, 0, 0);
            }
            if (EventFlag(53)) {
                ShootBullet(3900470, 3902470, -1, 5903, 0, 0, 0);
            }
            if (EventFlag(54)) {
                ShootBullet(3900470, 3902470, -1, 5904, 0, 0, 0);
            }
            if (EventFlag(55)) {
                ShootBullet(3900470, 3902470, -1, 5905, 0, 0, 0);
            }
            if (EventFlag(56)) {
                ShootBullet(3900470, 3902470, -1, 5906, 0, 0, 0);
            }
            WaitFixedTimeSeconds(5);
            RestartEvent();
        }
    }
L0:
    SetNetworkUpdateRate(3900470, true, CharacterUpdateFrequency.NoUpdate);
    SetCharacterAIState(3900470, Disabled);
    EndEvent();
});

$Event(13905475, Restart, function() {
    WaitFor(
        !(!CharacterDead(3900223)
            && CharacterAIState(3900223, AIStateType.Combat, ComparisonType.NotEqual, 1)
            && InArea(3900223, 3902475)));
    SetEventFlag(13905479, ON);
});

$Event(13905480, Restart, function() {
    RegisterLadder(13900480, 13900481, 3901480);
    RegisterLadder(13900482, 13900483, 3901481);
    RegisterLadder(13900484, 13900485, 3901482);
    RegisterLadder(13900486, 13900487, 3901483);
    RegisterLadder(13900488, 13900489, 3901484);
    RegisterLadder(13900490, 13900491, 3901485);
    RegisterLadder(13900492, 13900493, 3901486);
    RegisterLadder(13900494, 13900495, 3901487);
    RegisterLadder(13900496, 13900497, 3901488);
    RegisterLadder(13900498, 13900499, 3901489);
});

$Event(13905500, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    if (!EventFlag(X0_4)) {
        SetObjactState(X4_4, 390301, Enabled);
        SetObjactState(X4_4, 390302, Enabled);
        WaitFor(ObjActEventFlag(X8_4) || ObjActEventFlag(X12_4));
        SetNetworkconnectedEventFlag(X0_4, ON);
        SetObjactState(X4_4, 390301, Disabled);
        SetObjactState(X4_4, 390302, Disabled);
        EndEvent();
    }
L0:
    ReproduceObjectAnimation(X4_4, 0);
    SetObjactState(X4_4, 390301, Disabled);
    SetObjactState(X4_4, 390302, Disabled);
    EndEvent();
});

$Event(13905620, Restart, function(X0_4, X4_4, X8_4) {
    if (!EventFlag(X4_4)) {
        ForceAnimationPlayback(X0_4, 200, true, false, true, 0, 1);
        WaitFor(EventFlag(X4_4) && !PlayerIsNotInOwnWorld());
        WaitFixedTimeSeconds(0.1);
        ForceAnimationPlayback(X0_4, 201, false, true, false, 0, 1);
        SetEventFlag(X8_4, ON);
    }
L0:
    ForceAnimationPlayback(X0_4, 202, true, false, false, 0, 1);
    EndEvent();
});

$Event(13905700, Default, function(X0_4, X4_4) {
    if (!PlayerIsNotInOwnWorld()) {
        if (!AnyBatchEventFlags(1275, 1279)) {
            BatchSetNetworkconnectedEventFlags(1275, 1279, OFF);
            SetNetworkconnectedEventFlag(1275, ON);
        }
        if (EventFlag(1276) && EventFlag(70000065)) {
            BatchSetNetworkconnectedEventFlags(1275, 1279, OFF);
            SetNetworkconnectedEventFlag(1275, ON);
        }
        if (!AnyBatchEventFlags(1260, 1274)) {
            BatchSetNetworkconnectedEventFlags(1260, 1274, OFF);
            SetNetworkconnectedEventFlag(1260, ON);
        }
        if (!EventFlag(1275)) {
        }
L9:
        SetEventFlag(70000065, OFF);
    }
L10:
    if (!EventFlag(1260)) {
        ChangeCharacterEnableState(X0_4, Disabled);
        SetCharacterBackreadState(X0_4, true);
        EndEvent();
    }
L0:
    if (!EventFlag(1278)) {
        ForceAnimationPlayback(X0_4, X4_4, true, false, true, 0, 1);
        EndEvent();
    }
L1:
    ForceCharacterTreasure(X0_4);
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterBackreadState(X0_4, true);
    EndEvent();
});

$Event(13905720, Default, function(X0_4, X4_4) {
    if (!PlayerIsNotInOwnWorld()) {
        if (!AnyBatchEventFlags(1395, 1399)) {
            BatchSetNetworkconnectedEventFlags(1395, 1399, OFF);
            SetNetworkconnectedEventFlag(1395, ON);
        }
        if (EventFlag(1396) && EventFlag(70000071)) {
            BatchSetNetworkconnectedEventFlags(1395, 1399, OFF);
            SetNetworkconnectedEventFlag(1395, ON);
        }
        if (EventFlag(1395) && EventFlag(73900164)) {
            BatchSetNetworkconnectedEventFlags(1395, 1399, OFF);
            SetNetworkconnectedEventFlag(1398, ON);
        }
        if (!AnyBatchEventFlags(1380, 1394)) {
            BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
            SetNetworkconnectedEventFlag(1380, ON);
        }
        if (EventFlag(1395)) {
            if ((EventFlag(1384) || EventFlag(1385)) && EventFlag(140) && EventFlag(73700201)) {
                BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
                SetNetworkconnectedEventFlag(1386, ON);
            }
            if (((EventFlag(1386) && EventFlag(73900152)) || EventFlag(1387))
                && EventFlag(73100364)
                && EventFlag(73700203)
                && EventFlag(73500105)
                && !EventFlag(9318)) {
                BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
                SetNetworkconnectedEventFlag(1388, ON);
            }
            if (EventFlag(1386) && EventFlag(9318) && EventFlag(73900152)) {
                BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
                SetNetworkconnectedEventFlag(1390, ON);
            }
            if (EventFlag(1388) && EventFlag(9318)) {
                BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
                SetNetworkconnectedEventFlag(1389, ON);
            }
        }
L19:
        SetEventFlag(70000071, OFF);
        if (EventFlag(1395)) {
            SetEventFlag(73900199, OFF);
        }
    }
L20:
    GotoIf(L0, EventFlag(1386));
    GotoIf(L1, EventFlag(1388));
    GotoIf(L2, EventFlag(1389));
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterBackreadState(X0_4, true);
    ChangeCharacterEnableState(X4_4, Disabled);
    SetCharacterBackreadState(X4_4, true);
    EndEvent();
L0:
    ChangeCharacterEnableState(X4_4, Disabled);
    SetCharacterBackreadState(X4_4, true);
    GotoIf(L16, EventFlag(1396));
    GotoIf(L18, EventFlag(1398));
    ForceAnimationPlayback(X0_4, 90890, false, false, true, 0, 1);
    EndEvent();
L16:
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    EndEvent();
L18:
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterBackreadState(X0_4, true);
    ForceCharacterTreasure(X0_4);
    EndEvent();
L1:
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterBackreadState(X0_4, true);
    if (!EventFlag(13900722)) {
        ChangeCharacterEnableState(X4_4, Disabled);
        SetCharacterBackreadState(X4_4, true);
        EndEvent();
    }
L20:
    if (!EventFlag(1398)) {
        SetCharacterTeamType(X4_4, TeamType.WhitePhantom);
        SetCharacterAIState(X4_4, Disabled);
        EndEvent();
    }
L18:
    ForceCharacterTreasure(X4_4);
    ChangeCharacterEnableState(X4_4, Disabled);
    SetCharacterBackreadState(X4_4, true);
    EndEvent();
L2:
    ChangeCharacterEnableState(X0_4, Disabled);
    SetCharacterBackreadState(X0_4, true);
    if (!EventFlag(1398)) {
        SetCharacterTeamType(X4_4, TeamType.WhitePhantom);
        ForceAnimationPlayback(X4_4, 90850, false, false, true, 0, 1);
        EndEvent();
    }
L18:
    ChangeCharacterEnableState(X4_4, Disabled);
    SetCharacterBackreadState(X4_4, true);
    ForceCharacterTreasure(X4_4);
    EndEvent();
});

$Event(13900721, Restart, function() {
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(
        !AnyBatchEventFlags(1396, 1398)
            && EventFlag(1386)
            && EventFlag(73900152)
            && EventFlag(73100364)
            && EventFlag(73700203)
            && EventFlag(73500105)
            && InArea(10000, 3902710));
    BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
    SetNetworkconnectedEventFlag(1388, ON);
    ChangeCharacterEnableState(3900705, Disabled);
    SetCharacterBackreadState(3900705, true);
});

$Event(13900723, Restart, function(X0_4, X4_4) {
    EndIf(PlayerIsNotInOwnWorld());
    EndIf(ThisEventSlot());
    WaitFor(
        EventFlag(73900164)
            && !EntityInRadiusOfEntity(10000, X0_4, X4_4, 1)
            && HPRatio(X0_4) != 0
            && EventFlag(1395));
    ForceCharacterDeath(X0_4, true);
    BatchSetNetworkconnectedEventFlags(1380, 1399, OFF);
    SetNetworkconnectedEventFlag(1389, ON);
    SetNetworkconnectedEventFlag(1398, ON);
});

$Event(13905725, Restart, function() {
    WaitFor(EventFlag(9318));
    ClearCharactersAITarget(3900706);
    RequestCharacterAIReplan(3900706);
    SetCharacterAIState(3900706, Disabled);
});

$Event(13900726, Restart, function() {
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(HPRatio(3900800) == 0 && EventFlag(1388));
    if (!ThisEventSlot()) {
        RequestCharacterAICommand(3900706, 20, 1);
        RequestCharacterAIReplan(3900706);
        WaitFixedTimeSeconds(2);
    }
    WaitFor(!CharacterHasSpEffect(3900706, 150) || EventFlag(1396));
    EndIf(EventFlag(1396));
    EzstateInstructionRequest(3900706, 2100, 1);
    WaitFor(EventFlag(1396) || CharacterHasSpEffect(3900706, 150) || ElapsedSeconds(0.5));
    EndIf(EventFlag(1396));
    RestartEvent();
});

$Event(13905727, Restart, function() {
    EndIf(PlayerIsNotInOwnWorld());
    SetEventFlag(73900180, ON);
    WaitFor(!CharacterHasSpEffect(3900706, 153));
    SetEventFlag(73900180, OFF);
    WaitFor(CharacterHasSpEffect(3900706, 153));
    RestartEvent();
});

$Event(13905728, Restart, function() {
    EndIf(PlayerIsNotInOwnWorld());
    SetEventFlag(73900155, OFF);
    WaitFor(InArea(10000, 3902712) || InArea(10000, 3902713));
    SetEventFlag(73900155, ON);
    WaitFor(!(InArea(10000, 3902712) || InArea(10000, 3902713)));
    SetEventFlag(73900155, OFF);
    RestartEvent();
});

$Event(13900729, Restart, function(X0_4) {
    EndIf(ThisEventSlot());
    WaitFor(
        ((EventFlag(1383) && EventFlag(73500105)) || EventFlag(1385))
            && EventFlag(1395)
            && EventFlag(140)
            && EventFlag(73700201)
            && !CharacterBackreadStatus(3700715));
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        BatchSetNetworkconnectedEventFlags(1380, 1394, OFF);
        SetNetworkconnectedEventFlag(1386, ON);
    }
    ChangeCharacterEnableState(3700715, Disabled);
    SetCharacterBackreadState(3700715, true);
    ChangeCharacterEnableState(X0_4, Enabled);
    SetCharacterBackreadState(X0_4, false);
    ForceAnimationPlayback(X0_4, 90890, false, false, true, 0, 1);
});

$Event(13905810, Restart, function() {
    if (EventFlag(13900800)) {
        ChangeCharacterEnableState(3900800, Disabled);
        ForceCharacterDeath(3900800, false);
        EndEvent();
    }
L0:
    SetCharacterAIState(3900800, Disabled);
    SetCharacterMaphit(3900800, true);
    SetCharacterGravity(3900800, Disabled);
    SetCharacterAnimationState(3900706, Disabled);
    if (!(EventFlag(1388) && EventFlag(1395) && EventFlag(13900722))) {
        ForceAnimationPlayback(3900800, 30000, false, false, false, 0, 1);
    }
    WaitFor(EventFlag(13905805) && InArea(10000, 3902800));
    SetEventFlag(13900801, ON);
    if (NumberOfClientsOfType(ClientType.Invader) != 0) {
        SendInvadingPhantomsHome(0);
    }
    EndIf(
        CharacterInvadeType(10000, 4)
            || CharacterInvadeType(10000, 7)
            || CharacterInvadeType(10000, 21)
            || CharacterType(10000, TargetType.BlackPhantom));
    if (!(EventFlag(1388) && EventFlag(1395))) {
        WaitFixedTimeSeconds(1.5);
        ForceAnimationPlayback(3900800, 20010, false, false, false, 0, 1);
        SetCharacterMaphit(3900800, false);
        SetCharacterGravity(3900800, Enabled);
        SetCharacterAIState(3900800, Enabled);
        SetNetworkUpdateRate(3900800, true, CharacterUpdateFrequency.AlwaysUpdate);
        DisplayBossHealthBar(Enabled, 3900800, 0, 905260);
        SetEventFlag(13905812, ON);
        SetNetworkconnectedEventFlag(13905730, ON);
        EndEvent();
    }
L2:
    if (!EventFlag(13900722)) {
        if (!EventFlag(13905730)) {
            WaitFixedTimeSeconds(1);
            PlayCutsceneToPlayer(39000020, CutscenePlayMode.Skippable, 10000);
            WaitFixedTimeFrames(1);
            if (NumberOfClientsOfType(ClientType.Invader) != 0) {
                SetEventFlag(13900722, ON);
            }
        }
    }
L1:
    IssueShortWarpRequest(3900800, TargetEntityType.Area, 3902711, -1);
    SetCharacterMaphit(3900800, false);
    SetCharacterGravity(3900800, Enabled);
    ForceAnimationPlayback(3900800, 20, true, false, false, 0, 1);
    SetCharacterAIState(3900800, Enabled);
    SetNetworkUpdateRate(3900800, true, CharacterUpdateFrequency.AlwaysUpdate);
    DisplayBossHealthBar(Enabled, 3900800, 0, 905260);
    SetEventFlag(13905812, ON);
    SetNetworkconnectedEventFlag(13905730, ON);
    ChangeCharacterEnableState(3900706, Enabled);
    SetCharacterBackreadState(3900706, false);
    SetCharacterTeamType(3900706, TeamType.WhitePhantom);
    SetCharacterTalkRange(3900706, 100);
    SetCharacterAIState(3900706, Enabled);
    SetCharacterEventTarget(3900706, 3900800);
    RequestCharacterAIReplan(3900706);
    SetCharacterAnimationState(3900706, Enabled);
    EndIf(PlayerIsNotInOwnWorld());
    SetNetworkUpdateRate(3900706, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetNetworkUpdateAuthority(3900706, AuthorityLevel.Forced);
});

$Event(13905811, Restart, function() {
    EndIf(EventFlag(13900800));
    WaitFor(HPRatio(3900800) <= 0);
    WaitFixedTimeSeconds(1);
    PlaySE(3900800, SoundType.s_SFX, 777777777);
    WaitFor(CharacterDead(3900800));
    WaitFixedTimeSeconds(4.5);
    HandleBossDefeatAndDisplayBanner(3900800, TextBannerType.LordofCinderFallen);
    SetEventFlag(13900800, ON);
    SetEventFlag(9318, ON);
    SetEventFlag(6318, ON);
    ChangeCamera(-1, -1);
});

$Event(13905815, Restart, function() {
    EndIf(EventFlag(13900800));
    WaitFor(CharacterHasEventMessage(3900800, 500));
    SetEventFlag(13905815, ON);
    EndEvent();
});

$Event(13905816, Restart, function() {
    DeleteMapSFX(3904810, false);
    EndIf(EventFlag(13900800));
    WaitFor(EventFlag(13905815));
    SpawnMapSFX(3904810);
    WaitFor(EventFlag(13900800));
    DeleteMapSFX(3904810, true);
});

$Event(13905820, Restart, function() {
    InitializeCommonEvent(20005800, 13900800, 3901800, 3902800, 13905805, 3901800, 3900800, 0, 0);
    InitializeCommonEvent(20005801, 13900800, 3901800, 3902800, 13905730, 3901800, 13905806);
    InitializeCommonEvent(20005820, 13900800, 3901800, 3, 0);
    InitializeCommonEvent(20001836, 13900800, 13905805, 13905806, 13905812, 3904801, 3904802, 13905815);
    InitializeCommonEvent(20005837, 13900800, 3900800, 1088421888, 5260, 5260, 13905805, 13905806);
    InitializeCommonEvent(20005810, 13900800, 3901800, 3902800, 10000);
});

$Event(13905830, Restart, function(X0_2, X2_2, X4_4, X8_4, X12_4) {
    EndIf(EventFlag(13900800));
    CreateNPCPart(3900800, X0_2, X2_2, X4_4, 1, 1, false, false);
    WaitFor(NPCPartHP(3900800, X8_4) <= 0);
    if (!CharacterHasSpEffect(3900800, 5034)) {
        ForceAnimationPlayback(3900800, X12_4, false, false, true, 0, 1);
    }
L0:
    WaitFixedTimeFrames(10);
    RestartEvent();
});

$Event(13905835, Restart, function() {
    EndIf(EventFlag(13900800));
    WaitFor(CharacterHasSpEffect(3900800, 6071) && CharacterBackreadStatus(3900800));
    if (!CharacterHasSpEffect(3900800, 5034)) {
        ForceAnimationPlayback(3900800, 20002, false, false, true, 0, 1);
    }
L0:
    WaitFixedTimeFrames(10);
    RestartEvent();
});

$Event(13905840, Restart, function() {
    EndIf(EventFlag(13900800));
    SetNetworkSyncState(Disabled);
    WaitFor(InArea(10000, 3902800));
    SetSpEffect(10000, 4510);
    SetSpEffect(3900706, 4510);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(13905850, Restart, function() {
    EndIf(EventFlag(13900800));
    WaitFor(
        ((HasDamageType(3900800, -1, DamageType.Unspecified) && HPRatio(3900800) <= 0.6)
            || (HPRatio(3900800) <= 0.79 && CharacterHasSpEffect(3900800, 11421)))
            && !CharacterHasSpEffect(3900800, 5404)
            && !CharacterHasSpEffect(3900800, 5034));
    WaitFixedTimeFrames(1);
    ForceAnimationPlayback(3900800, 20005, false, false, true, 0, 1);
});

$Event(13905860, Restart, function() {
    EndIf(EventFlag(13900800));
    dmg = HasDamageType(3900800, 10000, DamageType.Unspecified);
    dmg2 = HasDamageType(3900800, 3900706, DamageType.Unspecified);
    WaitFor(CharacterHasSpEffect(3900800, 11421) && (dmg || dmg2));
    GotoIf(L0, dmg2.Passed);
    GotoIf(L1, CharacterType(10000, TargetType.Alive) || CharacterType(10000, TargetType.Hollow));
    GotoIf(L2, EventFlag(13905862));
    GotoIf(L3, EventFlag(13905863));
    GotoIf(L4, EventFlag(13905864));
    GotoIf(L4, EventFlag(13905865));
    Goto(L4);
L2:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11444);
    } else {
        SetSpEffect(3900800, 11445);
    }
    Goto(L20);
L3:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11446);
    } else {
        SetSpEffect(3900800, 11447);
    }
    Goto(L20);
L4:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11448);
    } else {
        SetSpEffect(3900800, 11449);
    }
    Goto(L20);
L0:
    GotoIf(L5, EventFlag(13905862));
    GotoIf(L6, EventFlag(13905863));
    GotoIf(L7, EventFlag(13905864));
    GotoIf(L7, EventFlag(13905865));
    Goto(L7);
L5:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11438);
    } else {
        SetSpEffect(3900800, 11439);
    }
    Goto(L20);
L6:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11440);
    } else {
        SetSpEffect(3900800, 11441);
    }
    Goto(L20);
L7:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11442);
    } else {
        SetSpEffect(3900800, 11443);
    }
    Goto(L20);
L1:
    GotoIf(L8, EventFlag(13905862));
    GotoIf(L9, EventFlag(13905863));
    GotoIf(L10, EventFlag(13905864));
    GotoIf(L10, EventFlag(13905865));
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11430);
    } else {
        SetSpEffect(3900800, 11431);
    }
    Goto(L20);
L8:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11432);
    } else {
        SetSpEffect(3900800, 11433);
    }
    Goto(L20);
L9:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11434);
    } else {
        SetSpEffect(3900800, 11435);
    }
    Goto(L20);
L10:
    if (CharacterHasSpEffect(3900800, 5032)) {
        SetSpEffect(3900800, 11436);
    } else {
        SetSpEffect(3900800, 11437);
    }
    Goto(L20);
L20:
    WaitFixedTimeFrames(15);
    RestartEvent();
});

$Event(13905861, Restart, function() {
    EndIf(EventFlag(13900800));
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(EventFlag(13905805) && !PlayerIsNotInOwnWorld());
    GotoIf(L0, NumberOfCoopClients() == 0);
    GotoIf(L1, NumberOfCoopClients() == 1);
    GotoIf(L2, NumberOfCoopClients() == 2);
    GotoIf(L3, NumberOfCoopClients() == 3);
L0:
    if (EventFlag(1388)) {
        SetNetworkconnectedEventFlag(13905862, ON);
    }
    Goto(L20);
L1:
    if (EventFlag(1388)) {
        SetNetworkconnectedEventFlag(13905863, ON);
    } else {
        SetNetworkconnectedEventFlag(13905862, ON);
    }
    Goto(L20);
L2:
    if (EventFlag(1388)) {
        SetNetworkconnectedEventFlag(13905864, ON);
    } else {
        SetNetworkconnectedEventFlag(13905863, ON);
    }
    Goto(L20);
L3:
    if (EventFlag(1388)) {
        SetNetworkconnectedEventFlag(13905865, ON);
    } else {
        SetNetworkconnectedEventFlag(13905864, ON);
    }
    Goto(L20);
L20:
    EndEvent();
});

$Event(13905870, Restart, function(X0_4, X4_4) {
    SetNetworkSyncState(Disabled);
    DeactivateObject(X0_4, Disabled);
    SetObjectTreasureState(X0_4, Disabled);
    EndIf(PlayerIsNotInOwnWorld());
    EndIf(EventFlag(13900800));
    WaitFor(InArea(10000, 3902890));
    EndIf(
        PlayerHasItemIncludingBBox(ItemType.Weapon, 6370000)
            || PlayerHasItemIncludingBBox(ItemType.Weapon, 6370001)
            || PlayerHasItemIncludingBBox(ItemType.Weapon, 6370002)
            || PlayerHasItemIncludingBBox(ItemType.Weapon, 6370003)
            || PlayerHasItemIncludingBBox(ItemType.Weapon, 6370004)
            || PlayerHasItemIncludingBBox(ItemType.Weapon, 6370005));
    EndIf(!EventFlag(53900810));
    DeactivateObject(X4_4, Disabled);
    DeactivateObject(X0_4, Enabled);
    SetObjectTreasureState(X0_4, Enabled);
});

$Event(13905900, Restart, function() {
    SetNetworkSyncState(Disabled);
    EndIf(PlayerIsNotInOwnWorld());
    WaitFor(
        (CharacterType(10000, TargetType.Alive) || CharacterType(10000, TargetType.Hollow))
            && InArea(10000, 3902900)
            && CharacterHasSpEffect(10000, 4400));
    WaitFor(ElapsedSeconds(6) || !CharacterHasSpEffect(10000, 4400));
    RestartIf(!CharacterHasSpEffect(10000, 4400));
    RestartIf(HasMultiplayerState(MultiplayerState.TryingtoCreateSession));
    RestartIf(HasMultiplayerState(MultiplayerState.TryingtoJoinSession));
    PlayCutsceneAndWarpPlayer(39000010, CutscenePlayMode.Skippable, 3202900, 32, 0, 10000);
    SetPlayerRespawnPoint(3202900);
    SaveRequest(0);
    WaitFixedTimeFrames(1);
    RestartEvent();
});
