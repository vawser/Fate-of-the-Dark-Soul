# -*- coding: utf-8 -*-
def t510021_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t510021_x8()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t510021_x9()
        assert not IsClientPlayer()

def t510021_x0(action2=_):
    """State 0,1"""
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t510021_x1(actionbutton1=6031, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag2) == 1 or GetEventStatus(flag3) == 1 or GetEventStatus(flag4) ==
                1 or GetEventStatus(flag5) == 1 or GetEventStatus(flag6) == 1)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
            and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag2) and not GetEventStatus(flag3) and not GetEventStatus(flag4) and
              not GetEventStatus(flag5) and not GetEventStatus(flag6)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t510021_x2():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t510021_x3(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t510021_x4():
    """State 0,6"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15000500:"Request Absolution"
        AddTalkListData(1, 15000500, -1)
        # action:15000510:"Request Dissolution"
        AddTalkListData(2, 15000510, -1)
        AddTalkListDataIf(GetEventStatus(15100800) == 1 and not GetEventStatus(9610), 3, 15000520, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 4,11"""
            assert t510021_x13(z4=1000, z5=1, flag1=9001, z6=9003)
        elif GetTalkListEntryResult() == 2:
            """State 7,10"""
            assert t510021_x12(z7=100, z8=1)
        elif GetTalkListEntryResult() == 3:
            """State 9,12"""
            assert t510021_x14(z1=500, z2=1, z3=9610)
        else:
            """State 5,13"""
            return 0

def t510021_x5():
    """State 0,1,2"""
    SetEventState(75100233, 1)
    """State 3"""
    assert t510021_x4()
    """State 4"""
    return 0

def t510021_x6():
    """State 0,1"""
    assert t510021_x2()
    """State 2"""
    return 0

def t510021_x7():
    """State 0,1"""
    assert t510021_x2()
    """State 2"""
    return 0

def t510021_x8():
    """State 0"""
    while True:
        """State 1"""
        call = t510021_x10()
        assert not GetEventStatus(6001)
        """State 2"""
        call = t510021_x11()
        assert GetEventStatus(6001) == 1
    """Unused"""
    """State 3"""
    return 0

def t510021_x9():
    """State 0,1"""
    assert t510021_x2()
    """State 2"""
    return 0

def t510021_x10():
    """State 0"""
    while True:
        """State 4"""
        assert t510021_x1(actionbutton1=6031, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000)
        """State 2"""
        call = t510021_x5()
        if call.Done():
            pass
        elif IsPlayerDead() == 1:
            break
        elif GetDistanceToPlayer() > 5:
            """State 3"""
            assert t510021_x7()
    """State 1"""
    t510021_x6()
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t510021_x11():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t510021_x12(z7=100, z8=1):
    """State 0,1"""
    if ComparePlayerStatus(31, 2, 0) == 1:
        """State 2,8"""
        SetAquittalCostMessageTag(z7, z8)
        """State 19"""
        # action:12000110:"Your curse can be lifted for <?evntAcquittalPrice?> souls.\nWill you request to reverse hollowing?"
        call = t510021_x0(action2=12000110)
        if call.Get() == 0:
            """State 6"""
            if ComparePlayerAcquittalPrice(z7, z8, 2) == 1:
                """State 4,18"""
                # action:13000050:"Insufficient souls"
                assert t510021_x3(action1=13000050)
            else:
                """State 9,10"""
                TurnCharacterToFaceEntity(-1, 10000, -1)
                assert GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 11"""
                TurnCharacterToFaceEntity(69010, 10000, -1)
                assert GetCurrentStateElapsedTime() > 1.5
                """State 5"""
                SubtractAcquittalCostFromPlayerSouls(z7, z8)
                """State 14"""
                if GetPlayerChrType() == 8:
                    """State 15,12"""
                    GiveSpEffectToPlayer(3093)
                else:
                    """State 16,13"""
                    ChangePlayerStats(31, 5, 0)
                """State 17"""
                assert GetCurrentStateElapsedTime() > 3
                """State 21"""
                # action:13000111:"Your curse has been lifted"
                assert t510021_x3(action1=13000111) and GetWhetherChrEventAnimHasEnded(10000) == 1
        elif call.Get() == 1:
            """State 7"""
            pass
    else:
        """State 3,20"""
        # action:13000110:"You are not cursed"
        assert t510021_x3(action1=13000110)
    """State 22"""
    return 0

def t510021_x13(z4=1000, z5=1, flag1=9001, z6=9003):
    """State 0,1"""
    if GetEventStatus(flag1) == 1:
        """State 2,9"""
        SetAquittalCostMessageTag(z4, z5)
        """State 14"""
        # action:12000100:"Your sins can be forgiven for <?evntAcquittalPrice?> souls. \nWill you request to be pardoned? "
        call = t510021_x0(action2=12000100)
        if call.Get() == 0:
            """State 7"""
            if ComparePlayerAcquittalPrice(z4, z5, 2) == 1:
                """State 4,13"""
                # action:13000050:"Insufficient souls"
                assert t510021_x3(action1=13000050)
            else:
                """State 10,11"""
                TurnCharacterToFaceEntity(-1, 10000, -1)
                assert GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 12"""
                TurnCharacterToFaceEntity(69010, 10000, -1)
                assert GetCurrentStateElapsedTime() > 3
                """State 5"""
                SubtractAcquittalCostFromPlayerSouls(z4, z5)
                """State 6"""
                SetEventState(z6, 1)
                """State 16"""
                # action:13000101:"You were cleansed of sin"
                assert t510021_x3(action1=13000101) and GetWhetherChrEventAnimHasEnded(10000) == 1
        elif call.Get() == 1:
            """State 8"""
            pass
    else:
        """State 3,15"""
        # action:13000100:"You have not sinned"
        assert t510021_x3(action1=13000100)
    """State 17"""
    return 0

def t510021_x14(z1=500, z2=1, z3=9610):
    """State 0,1,2,8"""
    SetAquittalCostMessageTag(z1, z2)
    """State 13"""
    call = t510021_x0(action2=12000120)
    if call.Get() == 0:
        """State 6"""
        if ComparePlayerAcquittalPrice(z1, z2, 2) == 1:
            """State 3,12"""
            # action:13000050:"Insufficient souls"
            assert t510021_x3(action1=13000050)
        else:
            """State 9,15"""
            call = t510021_x0(action2=12000121)
            if call.Get() == 0:
                """State 10"""
                TurnCharacterToFaceEntity(-1, 10000, -1)
                assert GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 11"""
                TurnCharacterToFaceEntity(69010, 10000, -1)
                assert GetCurrentStateElapsedTime() > 3
                """State 4"""
                SubtractAcquittalCostFromPlayerSouls(z1, z2)
                """State 5"""
                SetEventState(z3, 1)
                """State 14"""
                assert t510021_x3(action1=13000121) and GetWhetherChrEventAnimHasEnded(10000) == 1
            elif call.Get() == 1:
                """State 7"""
                Label('L0')
    elif call.Get() == 1:
        Goto('L0')
    """State 16"""
    return 0

