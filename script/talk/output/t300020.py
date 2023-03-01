# -*- coding: utf-8 -*-
def t300020_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t300020_x3()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t300020_x4()
        assert not IsClientPlayer()

def t300020_x0():
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

def t300020_x1(gesture1=29, z1=9030, flag2=6079):
    """State 0,1"""
    if GetEventStatus(flag2) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        OpenItemAcquisitionMenu(3, z1, 1)
        SetEventState(flag2, 1)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t300020_x2(gesture1=29, z1=9030, flag1=13000900, flag2=6079):
    """State 0"""
    while True:
        """State 2"""
        assert GetEventStatus(flag1) == 1
        """State 3"""
        assert t300020_x1(gesture1=gesture1, z1=z1, flag2=flag2)
        """State 1"""
        SetEventState(flag1, 0)
    """Unused"""
    """State 4"""
    return 0

def t300020_x3():
    """State 0"""
    while True:
        """State 1"""
        call = t300020_x5()
        assert not GetEventStatus(6001)
        """State 2"""
        call = t300020_x6()
        assert GetEventStatus(6001) == 1
    """Unused"""
    """State 3"""
    return 0

def t300020_x4():
    """State 0,1"""
    assert t300020_x0()
    """State 2"""
    return 0

def t300020_x5():
    """State 0,1"""
    t300020_x2(gesture1=29, z1=9030, flag1=13000900, flag2=6079)
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t300020_x6():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

