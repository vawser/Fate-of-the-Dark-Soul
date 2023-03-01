# -*- coding: utf-8 -*-
def t510751_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t510751_x20()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t510751_x21()
        assert not IsClientPlayer()

def t510751_x0(flag6=75000261, text2=85000200, text3=85000100):
    """State 0,1"""
    if not GetEventStatus(flag6):
        """State 3"""
        assert t510751_x18(text2=text2, flag6=flag6, flag12=0, mode2=1)
    else:
        """State 4"""
        assert t510751_x19(text7=text3, flag11=0, mode1=1)
        """State 2"""
        SetEventState(flag6, 0)
    """State 5"""
    return 0

def t510751_x1(flag1=75000262, flag2=75000263, flag3=75000264, flag4=75000265, text4=85001000, text5=85001010,
               text6=85001020, text7=85001030, flag8=1846, flag9=1847):
    """State 0,9"""
    assert t510751_x15()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if not GetEventStatus(flag8) and not GetEventStatus(flag9):
        """State 2"""
        if GetDistanceToPlayer() < 10:
            """State 5,11"""
            call = t510751_x8(flag2=flag2, flag3=flag3, flag4=flag4, text4=text4, text5=text5, text6=text6,
                              text7=text7)
            if call.Done():
                pass
            elif GetEventStatus(flag8) == 1 or GetEventStatus(flag9) == 1:
                """State 6"""
                Label('L0')
                if GetDistanceToPlayer() < 10:
                    """State 7,12"""
                    # talk:85000700:"Ahh, yes, yes, I remember now!"
                    call = t510751_x9(flag1=flag1, text8=85000700)
                    if call.Done():
                        pass
                    elif GetDistanceToPlayer() > 12 or GetPlayerYDistance() > 5:
                        """State 10"""
                        Label('L1')
                        assert t510751_x15()
                elif not GetEventStatus(flag8) and not GetEventStatus(flag9):
                    """State 8"""
                    pass
            elif GetDistanceToPlayer() > 12:
                Goto('L1')
        else:
            """State 4"""
            pass
    else:
        Goto('L0')
    """State 13"""
    return 0

def t510751_x2(flag10=1848):
    """State 0,1"""
    if GetEventStatus(flag10) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            call = t510751_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t510751_x15()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t510751_x3(flag8=1846, flag9=1847):
    """State 0,3"""
    if GetEventStatus(flag8) == 1 or GetEventStatus(flag9) == 1:
        """State 1"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            call = t510751_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t510751_x15()
        else:
            """State 5"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t510751_x4():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2"""
        pass
    else:
        """State 3,4"""
        assert t510751_x15()
    """State 5"""
    return 0

def t510751_x5(flag5=75000260, text1=85000100):
    """State 0,1"""
    assert t510751_x17(text8=text1, flag1=flag5, flag13=0, mode3=1)
    """State 2"""
    return 0

def t510751_x6(flag1=75000262, flag2=75000263, flag3=75000264, flag4=75000265, z1=85001000, z2=85001010,
               z3=85001020, z4=85001030, flag5=75000260, text1=85000100, flag6=75000261, text2=85000200,
               text3=85000100, flag7=1845, flag8=1846, flag9=1847, flag10=1848, val1=10, val2=12):
    """State 0,2"""
    # talk:85001000:" ", talk:85001010:" ", talk:85001020:" ", talk:85001030:" "
    call = t510751_x10(flag1=flag1, flag2=flag2, flag3=flag3, flag4=flag4, text4=85001000, text5=85001010,
                       text6=85001020, text7=85001030, flag5=flag5, text1=text1, flag6=flag6, text2=text2,
                       text3=text3, flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, val1=val1,
                       val2=val2)
    assert CheckSelfDeath() == 1
    """State 1"""
    t510751_x2(flag10=flag10)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t510751_x7():
    """State 0,1"""
    assert t510751_x15()
    """State 2"""
    return 0

def t510751_x8(flag2=75000263, flag3=75000264, flag4=75000265, text4=85001000, text5=85001010, text6=85001020,
               text7=85001030):
    """State 0,1"""
    if not GetEventStatus(flag2):
        """State 3"""
        assert t510751_x17(text8=text4, flag1=flag2, flag13=0, mode3=1)
    elif not GetEventStatus(flag3):
        """State 5"""
        assert t510751_x17(text8=text5, flag1=flag3, flag13=0, mode3=1)
    elif not GetEventStatus(flag4):
        """State 6"""
        assert t510751_x17(text8=text6, flag1=flag4, flag13=0, mode3=1)
    else:
        """State 2"""
        SetEventState(flag2, 0)
        SetEventState(flag3, 0)
        SetEventState(flag4, 0)
        """State 4"""
        assert t510751_x19(text7=text7, flag11=0, mode1=1)
    """State 7"""
    return 0

def t510751_x9(flag1=75000262, text8=85000700):
    """State 0,3"""
    if not GetEventStatus(flag1):
        """State 1,4"""
        assert t510751_x17(text8=text8, flag1=flag1, flag13=0, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t510751_x10(flag1=75000262, flag2=75000263, flag3=75000264, flag4=75000265, text4=85001000, text5=85001010,
                text6=85001020, text7=85001030, flag5=75000260, text1=85000100, flag6=75000261, text2=85000200,
                text3=85000100, flag7=1845, flag8=1846, flag9=1847, flag10=1848, val1=10, val2=12):
    """State 0"""
    while True:
        """State 5"""
        call = t510751_x14(actionbutton1=6000, flag7=flag7, flag14=6000, flag15=6000, flag16=6000, flag17=6000)
        if call.Done():
            """State 3"""
            call = t510751_x0(flag6=flag6, text2=text2, text3=text3)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
            elif GetDistanceToPlayer() > 5:
                """State 4"""
                Label('L0')
                call = t510751_x4()
                if call.Done():
                    pass
                elif IsAttackedBySomeone() == 1 or (GetEventStatus(flag8) == 1 and not GetEventStatus(flag1)):
                    """State 1"""
                    Label('L1')
                    call = t510751_x1(flag1=flag1, flag2=flag2, flag3=flag3, flag4=flag4, text4=text4,
                                      text5=text5, text6=text6, text7=text7, flag8=flag8, flag9=flag9)
                    def ExitPause():
                        RemoveMyAggro()
                    if call.Done():
                        pass
                    elif IsPlayerDead() == 1:
                        break
            elif GetDistanceToPlayer() < val1 and not GetEventStatus(flag5):
                """State 6"""
                Label('L2')
                call = t510751_x5(flag5=flag5, text1=text1)
                if call.Done():
                    pass
                elif IsAttackedBySomeone() == 1 or (GetEventStatus(flag8) == 1 and not GetEventStatus(flag1)):
                    Goto('L1')
                elif GetDistanceToPlayer() > val2:
                    Goto('L0')
            elif IsAttackedBySomeone() == 1 or (GetEventStatus(flag8) == 1 and not GetEventStatus(flag1)):
                Goto('L1')
        elif IsAttackedBySomeone() == 1 or (GetEventStatus(flag8) == 1 and not GetEventStatus(flag1)):
            Goto('L1')
        elif IsPlayerDead() == 1:
            break
        elif GetDistanceToPlayer() < val1 and not GetEventStatus(flag5):
            Goto('L2')
        elif DoesSelfHaveSpEffect(16338) == 1:
            """State 7"""
            assert t510751_x13() and not DoesSelfHaveSpEffect(16338)
    """State 2"""
    t510751_x3(flag8=flag8, flag9=flag9)
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t510751_x11():
    """State 0,1,2"""
    # talk:85001100:" "
    assert t510751_x19(text7=85001100, flag11=0, mode1=1)
    """State 3"""
    return 0

def t510751_x12():
    """State 0,1,2"""
    # talk:85001200:"Search thine own self. Fear not the dark."
    assert t510751_x19(text7=85001200, flag11=0, mode1=1)
    """State 3"""
    return 0

def t510751_x13():
    """State 0,1"""
    # talk:85000800:"I shall partake!"
    call = t510751_x19(text7=85000800, flag11=0, mode1=1)
    if call.Done():
        pass
    elif GetDistanceToPlayer() > 12 or GetPlayerYDistance() > 5:
        """State 2"""
        assert t510751_x15()
    """State 3"""
    return 0

def t510751_x14(actionbutton1=6000, flag7=1845, flag14=6000, flag15=6000, flag16=6000, flag17=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag7) == 1 or GetEventStatus(flag14) == 1 or GetEventStatus(flag15) ==
                1 or GetEventStatus(flag16) == 1 or GetEventStatus(flag17) == 1)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
            and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag7) and not GetEventStatus(flag14) and not GetEventStatus(flag15)
              and not GetEventStatus(flag16) and not GetEventStatus(flag17)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t510751_x15():
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

def t510751_x16():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t510751_x17(text8=_, flag1=_, flag13=0, mode3=1):
    """State 0,5"""
    assert t510751_x16() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(flag1, 1)
    """State 1"""
    TalkToPlayer(text8, -1, -1, flag13)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t510751_x18(text2=85000200, flag6=75000261, flag12=0, mode2=1):
    """State 0,5"""
    assert t510751_x16() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:85000200:"One poor girl slew her own kin, but even so, was embraced, enveloped by the Abyss."
    TalkToPlayer(text2, -1, -1, flag12)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(flag6, 1)
    """State 6"""
    return 0

def t510751_x19(text7=_, flag11=0, mode1=1):
    """State 0,4"""
    assert t510751_x16() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text7, -1, -1, flag11)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t510751_x20():
    """State 0,1"""
    # talk:85000100:"One met the dark with learning. But in the end, learned his knowledge was wanting.", talk:85000200:"One poor girl slew her own kin, but even so, was embraced, enveloped by the Abyss."
    t510751_x6(flag1=75000262, flag2=75000263, flag3=75000264, flag4=75000265, z1=85001000, z2=85001010,
               z3=85001020, z4=85001030, flag5=75000260, text1=85000100, flag6=75000261, text2=85000200,
               text3=85000100, flag7=1845, flag8=1846, flag9=1847, flag10=1848, val1=10, val2=12)
    Quit()
    """Unused"""
    """State 2"""
    t510751_x7()
    Quit()
    """State 3"""
    return 0

def t510751_x21():
    """State 0,1"""
    assert t510751_x15()
    """State 2"""
    return 0

