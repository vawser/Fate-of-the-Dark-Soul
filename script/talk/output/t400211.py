# -*- coding: utf-8 -*-
def t400211_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400211_x11()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t400211_x12()
        assert not IsClientPlayer()

def t400211_x0(actionbutton1=6210, flag4=1615, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag4) == 1 or GetEventStatus(flag5) == 1 or GetEventStatus(flag6) ==
                1 or GetEventStatus(flag7) == 1 or GetEventStatus(flag8) == 1)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
            and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag4) and not GetEventStatus(flag5) and not GetEventStatus(flag6) and
              not GetEventStatus(flag7) and not GetEventStatus(flag8)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t400211_x1():
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

def t400211_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400211_x3(text3=_, z2=_, flag3=0, mode3=1):
    """State 0,5"""
    assert t400211_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z2, 1)
    """State 1"""
    TalkToPlayer(text3, -1, -1, flag3)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t400211_x4(text2=21001500, z1=74000260, flag2=0, mode2=0):
    """State 0,5"""
    assert t400211_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:21001500:"Well, fancy that. "
    TalkToPlayer(text2, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z1, 1)
    """State 6"""
    return 0

def t400211_x5(text1=_, flag1=0, mode1=_):
    """State 0,4"""
    assert t400211_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t400211_x6():
    """State 0,1"""
    if not GetEventStatus(74000260):
        """State 2,5"""
        # talk:21001500:"Well, fancy that. "
        assert t400211_x4(text2=21001500, z1=74000260, flag2=0, mode2=0)
    else:
        """State 3,4"""
        # talk:21001600:"Well, thou'rt exceeding lost indeed."
        assert t400211_x5(text1=21001600, flag1=0, mode1=0)
    """State 6"""
    assert t400211_x14()
    """State 7"""
    return 0

def t400211_x7():
    """State 0,5"""
    assert t400211_x1()
    """State 2"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 3,7"""
        call = t400211_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 6"""
            assert t400211_x1()
    else:
        """State 4"""
        pass
    """State 8"""
    return 0

def t400211_x8():
    """State 0,1"""
    if GetEventStatus(1618) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            # talk:21001250:" "
            call = t400211_x5(text1=21001250, flag1=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t400211_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t400211_x9():
    """State 0,2,1,3"""
    return 0

def t400211_x10():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2,5"""
        call = t400211_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t400211_x1()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t400211_x11():
    """State 0"""
    while True:
        """State 1"""
        call = t400211_x15()
        assert not GetEventStatus(1600)
        """State 2"""
        call = t400211_x16()
        assert GetEventStatus(1600) == 1
    """Unused"""
    """State 3"""
    return 0

def t400211_x12():
    """State 0,1"""
    assert t400211_x1()
    """State 2"""
    return 0

def t400211_x13():
    """State 0,1"""
    # talk:21001800:"To skirt the curse's grasp..."
    assert t400211_x5(text1=21001800, flag1=0, mode1=0)
    """State 2"""
    return 0

def t400211_x14():
    """State 0,11"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 10"""
        # action:15011020:"Purchase Item"
        AddTalkListData(1, 15011020, -1)
        # action:15000012:"Sell Item"
        AddTalkListData(2, 15000012, -1)
        # action:15000000:"Talk"
        AddTalkListData(4, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 2"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 9"""
        if GetTalkListEntryResult() == 1:
            """State 3,7"""
            OpenRegularShop(119900, 119999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 4,8"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 4:
            """State 5,12"""
            assert t400211_x13()
        else:
            """State 6,13"""
            assert t400211_x18()
            """State 14"""
            return 0

def t400211_x15():
    """State 0,2"""
    call = t400211_x19()
    assert CheckSelfDeath() == 1
    """State 1"""
    t400211_x8()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t400211_x16():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t400211_x17():
    """State 0,2"""
    if not GetEventStatus(74000276):
        """State 1,6"""
        # talk:21000900:" "
        assert t400211_x3(text3=21000900, z2=74000276, flag3=0, mode3=1)
    elif not GetEventStatus(74000277):
        """State 3,7"""
        # talk:21001000:" "
        assert t400211_x3(text3=21001000, z2=74000277, flag3=0, mode3=1)
    else:
        """State 4,5"""
        SetEventState(74000276, 0)
        SetEventState(74000277, 0)
        """State 8"""
        # talk:21001100:"Stop that!"
        assert t400211_x5(text1=21001100, flag1=0, mode1=1)
    """State 9"""
    return 0

def t400211_x18():
    """State 0,1"""
    # talk:21001700:"Best not tarry long."
    assert t400211_x5(text1=21001700, flag1=0, mode1=1)
    """State 2"""
    return 0

def t400211_x19():
    """State 0"""
    while True:
        """State 5"""
        call = t400211_x0(actionbutton1=6210, flag4=1615, flag5=6000, flag6=6000, flag7=6000, flag8=6000)
        if call.Done():
            """State 3"""
            call = t400211_x6()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t400211_x7()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead() == 1:
                    break
            elif IsPlayerDead() == 1:
                break
            elif GetDistanceToPlayer() > 5:
                """State 4"""
                call = t400211_x10()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsPlayerDead() == 1:
            break
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
    """State 2"""
    t400211_x9()
    Quit()
    """Unused"""
    """State 6"""
    return 0

