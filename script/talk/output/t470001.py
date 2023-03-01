# -*- coding: utf-8 -*-
def t470001_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t470001_x7()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t470001_x8()
        assert not IsClientPlayer()

def t470001_x0():
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

def t470001_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t470001_x2(z1=_, z2=_, z3=_, z4=_):
    """State 0,5"""
    assert t470001_x1() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z2, 1)
    """State 1"""
    TalkToPlayer(z1, -1, -1, z3)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not z4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t470001_x3(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t470001_x1() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t470001_x4():
    """State 0,1"""
    Quit()

def t470001_x7():
    """State 0,1"""
    t470001_x9()
    Quit()

def t470001_x8():
    """State 0,1"""
    assert t470001_x0()
    """State 2"""
    return 0

def t470001_x9():
    """State 0,2"""
    t470001_x12()
    Quit()

def t470001_x12():
    """State 0"""
    while True:
        """State 3"""
        call = t470001_x4()
        if GetEventStatus(25009680) == 1:
            """State 2"""
            SetEventState(25009680, 0)
            call = t470001_x13(text1=88003000)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009681) == 1:
            """State 4"""
            SetEventState(25009681, 0)
            call = t470001_x13(text1=88003010)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009682) == 1:
            """State 5"""
            SetEventState(25009682, 0)
            call = t470001_x13(text1=88003020)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009683) == 1:
            """State 6"""
            SetEventState(25009683, 0)
            call = t470001_x13(text1=88003030)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009684) == 1:
            """State 7"""
            SetEventState(25009684, 0)
            call = t470001_x13(text1=88003040)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009685) == 1:
            """State 8"""
            SetEventState(25009685, 0)
            call = t470001_x13(text1=88003050)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif GetEventStatus(25009686) == 1:
            """State 9"""
            SetEventState(25009686, 0)
            call = t470001_x13(text1=88003060)
            if call.Done():
                pass
            elif IsPlayerDead() == 1:
                break
        elif IsPlayerDead() == 1:
            break
    """State 1"""
    t470001_x13(text1=88002010)
    Quit()

def t470001_x13(text1=_):
    """State 0,2,3"""
    if GetDistanceToPlayer() < 9999:
        """State 4,7"""
        call = t470001_x3(text1=text1, flag1=0, mode1=1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 9999:
            """State 6"""
            assert t470001_x0()
    else:
        """State 5"""
        pass
    """State 8"""
    return 0

