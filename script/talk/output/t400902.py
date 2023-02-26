# -*- coding: utf-8 -*-
def t400902_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400902_x13()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t400902_x14()
        assert not IsClientPlayer()

def t400902_x0(actionbutton1=6000, flag4=1040, flag5=6000, flag6=6000, flag7=6000, flag8=6000, flag9=6000,
               flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag15=6000, flag16=6000,
               flag17=6000, flag18=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag4) == 1 or GetEventStatus(flag5) == 1 or GetEventStatus(flag6) ==
                1 or GetEventStatus(flag7) == 1 or GetEventStatus(flag8) == 1 or GetEventStatus(flag9)
                == 1 or GetEventStatus(flag10) == 1 or GetEventStatus(flag11) == 1 or GetEventStatus(flag12)
                == 1 or GetEventStatus(flag13) == 1)
        """State 4"""
        assert (GetEventStatus(flag14) == 1 or GetEventStatus(flag15) == 1 or GetEventStatus(flag16)
                == 1 or GetEventStatus(flag17) == 1 or GetEventStatus(flag18) == 1)
        """State 2"""
        if (not GetEventStatus(flag4) and not GetEventStatus(flag5) and not GetEventStatus(flag6) and
            not GetEventStatus(flag7) and not GetEventStatus(flag8) and not GetEventStatus(flag9) and
            not GetEventStatus(flag10) and not GetEventStatus(flag11) and not GetEventStatus(flag12)
            and not GetEventStatus(flag13)):
            pass
        elif (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
              and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag14) and not GetEventStatus(flag15) and not GetEventStatus(flag16)
              and not GetEventStatus(flag17) and not GetEventStatus(flag18)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t400902_x1():
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
    if not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1:
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t400902_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400902_x3(text3=_, z2=_, flag3=0):
    """State 0,4"""
    assert t400902_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z2, 1)
    """State 1"""
    TalkToPlayer(text3, -1, -1, flag3)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t400902_x4(text2=90003000, z1=74009040, flag2=0):
    """State 0,4"""
    assert t400902_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z1, 1)
    """State 5"""
    return 0

def t400902_x5(text1=_, flag1=0):
    """State 0,3"""
    assert t400902_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag1)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    ReportConversationEndToHavokBehavior()
    """State 4"""
    return 0

def t400902_x6():
    """State 0,1,2"""
    if not GetEventStatus(74009040):
        """State 3,7"""
        assert t400902_x4(text2=90003000, z1=74009040, flag2=0)
    elif GetEventStatus(74009041) == 1:
        """State 5,6"""
        SetEventState(74009041, 0)
        """State 9"""
        assert t400902_x5(text1=90003020, flag1=0)
        """State 10"""
        Label('L0')
        assert t400902_x12()
    else:
        """State 4,8"""
        assert t400902_x5(text1=90003010, flag1=0)
        Goto('L0')
    """State 11"""
    return 0

def t400902_x7():
    """State 0,9"""
    SetEventState(74009045, 1)
    """State 14"""
    assert t400902_x1()
    """State 10"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if GetEventStatus(1056) == 1 or GetEventStatus(1057) == 1:
        """State 3"""
        if not GetEventStatus(74009043):
            """State 6"""
            Label('L0')
            """State 12"""
            assert t400902_x3(text3=90003090, z2=74009043, flag3=0)
        elif not GetEventStatus(74009044) and GetSelfHP() < 50:
            """State 7,13"""
            assert t400902_x3(text3=90003100, z2=74009044, flag3=0)
        else:
            """State 8"""
            pass
    else:
        """State 2"""
        if not GetEventStatus(74009042):
            """State 4,11"""
            call = t400902_x3(text3=90003080, z2=74009042, flag3=0)
            if call.Done():
                pass
            elif GetEventStatus(1056) == 1 or GetEventStatus(1057) == 1:
                Goto('L0')
        else:
            """State 5"""
            pass
    """State 15"""
    return 0

def t400902_x8():
    """State 0,1"""
    if GetEventStatus(1058) == 1:
        """State 2"""
        pass
    else:
        """State 3,5"""
        call = t400902_x5(text1=90003110, flag1=0)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            assert t400902_x1()
    """State 6"""
    return 0

def t400902_x9():
    """State 0,3"""
    if not GetEventStatus(1056) and not GetEventStatus(1057):
        """State 2"""
        pass
    else:
        """State 1,5"""
        call = t400902_x5(text1=90003120, flag1=0)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            assert t400902_x1()
    """State 6"""
    return 0

def t400902_x10():
    """State 0,1"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1:
        """State 2,4"""
        SetEventState(74009041, 1)
        """State 6"""
        call = t400902_x5(text1=90003070, flag1=0)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 5"""
            Label('L0')
            assert t400902_x1()
    else:
        """State 3"""
        Goto('L0')
    """State 7"""
    return 0

def t400902_x11():
    """State 0,4"""
    assert t400902_x2() and (GetEventStatus(1056) == 1 or GetEventStatus(1057) == 1)
    """State 2,7"""
    call = t400902_x3(text3=90003130, z2=74009045, flag3=0)
    if call.Done():
        pass
    elif GetDistanceToPlayer() > 12:
        """State 5"""
        assert t400902_x1()
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L2')
    """State 3"""
    Label('L1')
    assert t400902_x1()
    Goto('L0')
    """State 6"""
    Label('L2')
    call = t400902_x4(text2=90003000, z1=74009040, flag2=0)
    if call.Done():
        Goto('L0')
    elif GetDistanceToPlayer() > 12:
        Goto('L1')

def t400902_x12():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        AddTalkListData(1, 15000120, -1)
        AddTalkListData(2, 15000111, -1)
        AddTalkListData(3, 15000190, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 3"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 4,11"""
            assert t400902_x5(text1=90003050, flag1=0)
            """State 8"""
            OpenRepairShop()
            assert not CheckSpecificPersonMenuIsOpen(8, 0)
        elif GetTalkListEntryResult() == 2:
            """State 5,12"""
            assert t400902_x5(text1=90003030, flag1=0)
            """State 9"""
            OpenEnhanceShop(0)
            assert not CheckSpecificPersonMenuIsOpen(9, 0)
        elif GetTalkListEntryResult() == 3:
            """State 7,13"""
            assert t400902_x5(text1=90003040, flag1=0)
            """State 10"""
            OpenEquipmentChangeOfPurposeShop()
            assert not CheckSpecificPersonMenuIsOpen(7, 0)
        elif not CheckSpecificPersonMenuIsOpen(1, 0):
            """State 6,14"""
            assert t400902_x5(text1=90003060, flag1=0)
            """State 15"""
            return 0

def t400902_x13():
    """State 0"""
    while True:
        """State 7"""
        call = t400902_x0(actionbutton1=6000, flag4=1040, flag5=6000, flag6=6000, flag7=6000, flag8=6000,
                          flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag14=6000,
                          flag15=6000, flag16=6000, flag17=6000, flag18=6000)
        if call.Done():
            """State 4"""
            call = t400902_x6()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t400902_x7()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif CheckSelfDeath() == 1:
                    """State 2"""
                    t400902_x8()
                    Quit()
                elif IsPlayerDead() == 1:
                    break
                elif GetDistanceToPlayer() > 12:
                    """State 5"""
                    Label('L1')
                    assert t400902_x10() and GetDistanceToPlayer() < 4.9
            elif IsPlayerDead() == 1:
                break
            elif GetDistanceToPlayer() > 5:
                Goto('L1')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
        elif (GetDistanceToPlayer() < 10 and not GetEventStatus(74009045) and (GetEventStatus(1056) ==
              1 or GetEventStatus(1057) == 1)):
            """State 6"""
            call = t400902_x11()
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
            elif IsAttackedBySomeone() == 1:
                Goto('L0')
            elif GetDistanceToPlayer() > 12:
                Goto('L1')
    """State 3"""
    t400902_x9()
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t400902_x14():
    """State 0,1"""
    assert t400902_x1()
    """State 2"""
    return 0

