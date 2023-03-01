# -*- coding: utf-8 -*-
def t450552_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t450552_x5()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t450552_x6()
        assert not IsClientPlayer()

def t450552_x0():
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

def t450552_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t450552_x2(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t450552_x1() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t450552_x3():
    """State 0,8"""
    assert t450552_x0()
    """State 9"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    if GetEventStatus(1718) == 1:
        pass
    else:
        Goto('L1')
    """State 2"""
    Goto('L0')
    """State 3"""
    Label('L1')
    if GetDistanceToPlayer() < 10:
        pass
    else:
        Goto('L2')
    """State 4"""
    Goto('L4')
    """State 5"""
    Label('L2')
    Goto('L0')
    """State 6"""
    Label('L3')
    assert t450552_x0()
    Goto('L0')
    """State 7"""
    Label('L4')
    call = t450552_x10()
    if call.Done():
        Goto('L0')
    elif GetDistanceToPlayer() > 12:
        Goto('L3')

def t450552_x4():
    """State 0,2,1"""
    if GetDistanceToPlayer() < 70:
        """State 3,6"""
        call = t450552_x11()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 72:
            """State 5"""
            assert t450552_x0()
    else:
        """State 4"""
        pass
    """State 7"""
    return 0

def t450552_x5():
    """State 0"""
    while True:
        """State 1"""
        call = t450552_x7()
        assert not GetEventStatus(14505810) or not GetEventStatus(14505802)
        """State 2"""
        call = t450552_x8()
        assert GetEventStatus(14505810) == 1 and GetEventStatus(14505802) == 1
    """Unused"""
    """State 3"""
    return 0

def t450552_x6():
    """State 0,1"""
    assert t450552_x0()
    """State 2"""
    return 0

def t450552_x7():
    """State 0,1"""
    call = t450552_x9(z1=-1)
    assert CheckSelfDeath() == 1 or GetEventStatus(9322) == 1
    """State 2"""
    t450552_x3()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t450552_x8():
    """State 0,1"""
    assert t450552_x0()
    """State 2"""
    return 0

def t450552_x9(z1=-1):
    """State 0"""
    while True:
        """State 1"""
        if IsPlayerDead() == 1:
            """State 2"""
            call = t450552_x4()
            assert DoesSelfHaveSpEffect(13133) == 1 and not GetEventStatus(14505813)
        elif DoesSelfHaveSpEffect(13133) == 1 and not GetEventStatus(14505813):
            pass
        """State 3"""
        call = t450552_x12()
        assert not DoesSelfHaveSpEffect(13133) or GetEventStatus(14505813) == 1
    """Unused"""
    """State 4"""
    return 0

def t450552_x10():
    """State 0,1"""
    # talk:65000900:"Be forewarned, eager Ash."
    assert t450552_x2(text1=65000900, flag1=0, mode1=1)
    """State 2"""
    return 0

def t450552_x11():
    """State 0,2"""
    if not GetEventStatus(14505802):
        """State 3"""
        if (((GetEventStatus(1041) == 1 and GetEventStatus(1055) == 1) or GetEventStatus(1042) == 1 or
            GetEventStatus(1045) == 1) and not GetEventStatus(74000124)):
            """State 7"""
            # talk:65001700:"Return from whence thou cam'st."
            assert t450552_x2(text1=65001700, flag1=0, mode1=1)
        else:
            """State 6"""
            # talk:65001500:"Return from whence thou cam'st."
            assert t450552_x2(text1=65001500, flag1=0, mode1=1)
    else:
        """State 1"""
        if (((GetEventStatus(1041) == 1 and GetEventStatus(1055) == 1) or GetEventStatus(1042) == 1 or
            GetEventStatus(1045) == 1) and not GetEventStatus(74000124)):
            """State 5"""
            # talk:65001800:"Leave us be, Ashen One,"
            assert t450552_x2(text1=65001800, flag1=0, mode1=1)
        else:
            """State 4"""
            # talk:65001600:"Leave us be, Ashen One."
            assert t450552_x2(text1=65001600, flag1=0, mode1=1)
    """State 8"""
    return 0

def t450552_x12():
    """State 0,1"""
    assert t450552_x0()
    """State 2"""
    return 0

