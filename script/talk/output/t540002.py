# -*- coding: utf-8 -*-
def t540002_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t540002_x14()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t540002_x15()
        assert not IsClientPlayer()

def t540002_x0(z9=_):
    """State 0,1"""
    OpenGenericDialog(8, z9, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t540002_x1(actionbutton1=6120, flag3=1015, flag4=6000, flag5=6000, flag6=6000, flag7=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag3) == 1 or GetEventStatus(flag4) == 1 or GetEventStatus(flag5) ==
                1 or GetEventStatus(flag6) == 1 or GetEventStatus(flag7) == 1)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
            and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag3) and not GetEventStatus(flag4) and not GetEventStatus(flag5) and
              not GetEventStatus(flag6) and not GetEventStatus(flag7)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t540002_x2():
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

def t540002_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t540002_x4(text2=12002600, z8=74000115, flag2=0, mode2=1):
    """State 0,5"""
    assert t540002_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z8, 1)
    """State 1"""
    # talk:12002600:" "
    TalkToPlayer(text2, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t540002_x5(z4=_, z5=_, z6=_, z7=_):
    """State 0,5"""
    assert t540002_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(z4, -1, -1, z6)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not z7:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z5, 1)
    """State 6"""
    return 0

def t540002_x6(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t540002_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag1)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t540002_x7(z3=_):
    """State 0,1"""
    OpenGenericDialog(7, z3, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t540002_x8():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 15003003, -1)
        AddTalkListDataIf(not GetEventStatus(25000207), 6, 15003019, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenTranspositionShop(210000, 210999)
        elif GetTalkListEntryResult() == 6:
            """State 3"""
            SetEventState(25000207, 1)
            GetItemFromItemLot(800001110)
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 4"""
            return 0

def t540002_x9():
    """State 0,1"""
    assert t540002_x8()
    """State 24"""
    return 0

def t540002_x10():
    """State 0,6"""
    assert t540002_x2()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    assert not GetEventStatus(1016) and not GetEventStatus(1017)
    """State 2"""
    if GetDistanceToPlayer() < 10:
        """State 4,8"""
        call = t540002_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 7"""
            assert t540002_x2()
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t540002_x11():
    """State 0,1"""
    if GetEventStatus(1018) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4"""
            if GetEventStatus(50006020) == 1:
                """State 6,9"""
                # talk:12002900:" "
                call = t540002_x6(text1=12002900, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            else:
                """State 7,10"""
                # talk:12002950:" "
                call = t540002_x6(text1=12002950, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            """State 8"""
            assert t540002_x2()
        else:
            """State 5"""
            pass
    """State 11"""
    Label('L0')
    return 0

def t540002_x12():
    """State 0,1,2"""
    assert t540002_x2()
    """State 3"""
    return 0

def t540002_x13():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2"""
        assert GetDistanceToPlayer() > 12
    else:
        """State 3"""
        pass
    """State 4"""
    assert t540002_x2()
    """State 6"""
    return 0

def t540002_x14():
    """State 0"""
    while True:
        """State 1"""
        call = t540002_x16()
        assert not GetEventStatus(1000) and not GetEventStatus(1001) and not GetEventStatus(1002)
        """State 2"""
        call = t540002_x17()
        assert GetEventStatus(1000) == 1 or GetEventStatus(1001) == 1 or GetEventStatus(1002) == 1

def t540002_x15():
    """State 0,1"""
    assert t540002_x2()
    """State 2"""
    return 0

def t540002_x16():
    """State 0,1"""
    call = t540002_x26()
    assert CheckSelfDeath() == 1
    """State 2"""
    t540002_x11()
    Quit()

def t540002_x17():
    """State 0"""
    Quit()

def t540002_x18():
    """State 0,1"""
    if not GetEventStatus(74000115):
        """State 2,5"""
        # talk:12002600:" "
        assert t540002_x4(text2=12002600, z8=74000115, flag2=0, mode2=1)
    else:
        """State 3,6"""
        # talk:12002700:" "
        assert t540002_x6(text1=12002700, flag1=0, mode1=1)
        """State 4"""
        SetEventState(74000115, 0)
    """State 7"""
    return 0

def t540002_x26():
    """State 0"""
    while True:
        """State 5"""
        call = t540002_x1(actionbutton1=6120, flag3=1015, flag4=6000, flag5=6000, flag6=6000, flag7=6000)
        if call.Done():
            """State 3"""
            SetEventState(74000139, 1)
            call = t540002_x9()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t540002_x10()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead() == 1:
                    break
            elif IsPlayerDead() == 1:
                break
            elif GetDistanceToPlayer() > 3 or GetPlayerYDistance() > 0.25:
                """State 4"""
                call = t540002_x13()
                if call.Done() and (GetDistanceToPlayer() < 2.5 and GetPlayerYDistance() < 0.249):
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t540002_x12()
    Quit()

def t540002_x27(z2=_):
    """State 0,1"""
    OpenGenericDialog(8, z2, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t540002_x28(z1=_):
    """State 0,1"""
    OpenGenericDialog(8, z1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

