# -*- coding: utf-8 -*-
def t310240_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t310240_x11()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t310240_x12()
        assert not IsClientPlayer()

def t310240_x0(actionbutton1=6000, flag4=1255, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
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

def t310240_x1():
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

def t310240_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t310240_x3(text3=_, z2=_, flag3=0, mode3=1):
    """State 0,5"""
    assert t310240_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t310240_x4(text2=24000200, z1=73100201, flag2=0, mode2=1):
    """State 0,5"""
    assert t310240_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:24000200:" "
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

def t310240_x5(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t310240_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t310240_x6():
    """State 0,1,2"""
    if not GetEventStatus(73100200):
        """State 3"""
        if not GetEventStatus(74000465):
            """State 19,23"""
            # talk:24000000:"Ah-hah, Unkindled are we?"
            assert t310240_x5(text1=24000000, flag1=0, mode1=1)
        else:
            """State 20,27"""
            # talk:24000050:"Ah-hah, Unkindled are we?"
            assert t310240_x5(text1=24000050, flag1=0, mode1=1)
    else:
        """State 5"""
        if GetEventStatus(73100211) == 1:
            """State 4,22"""
            # talk:24000300:"Well, hello, That was certainly quick."
            assert t310240_x5(text1=24000300, flag1=0, mode1=1)
        else:
            """State 6,21"""
            # talk:24000350:"Well, hello. You certainly took your time."
            assert t310240_x5(text1=24000350, flag1=0, mode1=1)
    """State 8"""
    ClearTalkListData()
    """State 9"""
    # action:14014000:"Ask to learn pyromancy"
    AddTalkListData(1, 14014000, -1)
    # action:14014001:"Decline"
    AddTalkListData(2, 14014001, -1)
    """State 7"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 13"""
    if GetTalkListEntryResult() == 1:
        """State 10,24"""
        # talk:24000100:" "
        assert t310240_x5(text1=24000100, flag1=0, mode1=1)
        """State 17"""
        SetEventState(73100212, 1)
        """State 16"""
        Label('L0')
        SetEventState(73100200, 1)
        """State 18"""
        SetEventState(73100211, 1)
    elif GetTalkListEntryResult() == 2:
        """State 11"""
        if not GetEventStatus(73100201):
            """State 14,25"""
            # talk:24000200:" "
            assert t310240_x4(text2=24000200, z1=73100201, flag2=0, mode2=1)
            Goto('L0')
        else:
            """State 15,26"""
            # talk:24000203:"I will not rush you. You will return, once you are enlightened."
            assert t310240_x5(text1=24000203, flag1=0, mode1=1)
            Goto('L0')
    else:
        """State 12"""
        pass
    """State 28"""
    return 0

def t310240_x7():
    """State 0,9"""
    assert t310240_x1() and GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2"""
        if not GetEventStatus(73100205):
            """State 6,14"""
            # talk:24000400:" "
            call = t310240_x3(text3=24000400, z2=73100205, flag3=0, mode3=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 10"""
                assert t310240_x1()
        elif not GetEventStatus(73100206):
            """State 7,15"""
            # talk:24000500:" "
            call = t310240_x3(text3=24000500, z2=73100206, flag3=0, mode3=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 11"""
                assert t310240_x1()
        else:
            """State 8,4"""
            SetEventState(73100206, 0)
            """State 5"""
            SetEventState(73100207, 0)
            """State 13"""
            # talk:24000600:"What are you doing?"
            call = t310240_x5(text1=24000600, flag1=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 12"""
                assert t310240_x1()
    else:
        """State 3"""
        pass
    """State 16"""
    return 0

def t310240_x8():
    """State 0,1"""
    if GetEventStatus(1258) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            # talk:24000801:"Little bird, what's to be gained?"
            call = t310240_x5(text1=24000801, flag1=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t310240_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t310240_x9():
    """State 0,3"""
    if GetEventStatus(1256) == 1 or GetEventStatus(1257) == 1:
        """State 1"""
        if GetDistanceToPlayer() < 10:
            """State 4"""
            pass
        else:
            """State 5"""
            pass
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t310240_x10():
    """State 0,1,2"""
    assert t310240_x1()
    """State 3"""
    return 0

def t310240_x11():
    """State 0"""
    while True:
        """State 1"""
        call = t310240_x13()
        assert not GetEventStatus(1240)
        """State 2"""
        call = t310240_x14()
        assert GetEventStatus(1240) == 1
    """Unused"""
    """State 3"""
    return 0

def t310240_x12():
    """State 0,1"""
    assert t310240_x1()
    """State 2"""
    return 0

def t310240_x13():
    """State 0,2"""
    call = t310240_x15()
    assert CheckSelfDeath() == 1
    """State 1"""
    t310240_x8()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t310240_x14():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t310240_x15():
    """State 0"""
    while True:
        """State 5"""
        call = t310240_x0(actionbutton1=6000, flag4=1255, flag5=6000, flag6=6000, flag7=6000, flag8=6000)
        if call.Done():
            """State 3"""
            call = t310240_x6()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t310240_x7()
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
                call = t310240_x10()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t310240_x9()
    Quit()
    """Unused"""
    """State 6"""
    return 0

