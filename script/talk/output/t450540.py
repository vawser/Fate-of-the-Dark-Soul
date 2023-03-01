# -*- coding: utf-8 -*-
def t450540_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t450540_x12()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t450540_x13()
        assert not IsClientPlayer()

def t450540_x0(actionbutton1=6640, flag4=1695, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
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

def t450540_x1():
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

def t450540_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t450540_x3(text3=_, z3=_, flag3=0, mode3=1):
    """State 0,5"""
    assert t450540_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z3, 1)
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

def t450540_x4(text2=_, z2=_, flag2=0, mode2=1):
    """State 0,5"""
    assert t450540_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventState(z2, 1)
    """State 6"""
    return 0

def t450540_x5(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t450540_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t450540_x6(lot1=65400):
    """State 0,1"""
    # lot:65400:Titanite Slab
    GetItemFromItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t450540_x7():
    """State 0,13"""
    if GetEventStatus(9322) == 1:
        """State 14"""
        if not GetEventStatus(74500203):
            """State 21"""
            # talk:64000600:"Ohhh, my, thank you."
            assert t450540_x4(text2=64000600, z2=74500203, flag2=0, mode2=1)
            """State 23"""
            # lot:65400:Titanite Slab
            assert t450540_x6(lot1=65400)
        else:
            """State 22"""
            # talk:64000700:"When the world rots, we set it afire. For the sake of the next world."
            assert t450540_x5(text1=64000700, flag1=0, mode1=1)
    else:
        """State 1"""
        if not GetEventStatus(74500201):
            """State 2"""
            if GetEventStatus(74500200) == 1:
                """State 16"""
                # talk:64000500:"Ahh, yes, well..."
                assert t450540_x5(text1=64000500, flag1=0, mode1=1)
            else:
                """State 15"""
                # talk:64000000:"Hmm, well, there's nothing forlorn about you."
                assert t450540_x5(text1=64000000, flag1=0, mode1=1)
            """State 4"""
            ClearTalkListData()
            """State 5"""
            AddTalkListDataIf(not GetEventStatus(74500200), 1, 14054000, -1)
            AddTalkListDataIf(not GetEventStatus(74500200), 2, 14054001, -1)
            AddTalkListDataIf(GetEventStatus(74500200) == 1, 1, 14054002, -1)
            AddTalkListDataIf(GetEventStatus(74500200) == 1, 4, 14054003, -1)
            """State 3"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 6"""
            if GetTalkListEntryResult() == 1:
                """State 7,17"""
                # talk:64000100:"Ohh, ohh, finally, you've come!"
                assert t450540_x5(text1=64000100, flag1=0, mode1=1)
                """State 11"""
                SetEventState(74500201, 1)
            elif GetTalkListEntryResult() == 2:
                """State 8,18"""
                # talk:64000400:"Well, that's a rotten shame."
                assert t450540_x5(text1=64000400, flag1=0, mode1=1)
            else:
                """State 9"""
                Goto('L0')
            """State 10"""
            SetEventState(74500200, 1)
        else:
            """State 12"""
            if not GetEventStatus(74500202):
                """State 19"""
                # talk:64000200:"Surely you've seen. The rot that afflicts our world."
                assert t450540_x4(text2=64000200, z2=74500202, flag2=0, mode2=1)
            else:
                """State 20"""
                # talk:64000300:"Oh, please, it must be you."
                assert t450540_x5(text1=64000300, flag1=0, mode1=1)
    """State 24"""
    Label('L0')
    return 0

def t450540_x8():
    """State 0,6"""
    assert t450540_x1()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1,2"""
    if GetDistanceToPlayer() < 10:
        """State 4,8"""
        call = t450540_x16()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 7"""
            assert t450540_x1()
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t450540_x9():
    """State 0,1"""
    if GetEventStatus(1698) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            call = t450540_x18()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t450540_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t450540_x10():
    """State 0,3"""
    if GetEventStatus(1696) == 1 or GetEventStatus(1697) == 1:
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
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 6"""
    assert t450540_x1()
    Goto('L0')

def t450540_x11():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2"""
        pass
    else:
        """State 3,4"""
        assert t450540_x1()
    """State 5"""
    return 0

def t450540_x12():
    """State 0"""
    while True:
        """State 1"""
        call = t450540_x14(actionbutton1=6640)
        assert not GetEventStatus(1680)
        """State 2"""
        call = t450540_x15()
        assert GetEventStatus(1680) == 1
    """Unused"""
    """State 3"""
    return 0

def t450540_x13():
    """State 0,1"""
    assert t450540_x1()
    """State 2"""
    return 0

def t450540_x14(actionbutton1=6640):
    """State 0,2"""
    call = t450540_x17(z1=-1, actionbutton1=actionbutton1)
    assert CheckSelfDeath() == 1
    """State 1"""
    t450540_x9()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t450540_x15():
    """State 0,1"""
    assert t450540_x1()
    """State 2"""
    return 0

def t450540_x16():
    """State 0,1"""
    if not GetEventStatus(74500221):
        """State 4"""
        # talk:64000810:" "
        assert t450540_x3(text3=64000810, z3=74500221, flag3=0, mode3=1)
    elif not GetEventStatus(74500222):
        """State 5"""
        # talk:64000820:" "
        assert t450540_x3(text3=64000820, z3=74500222, flag3=0, mode3=1)
    elif not GetEventStatus(74500223):
        """State 6"""
        # talk:64000830:" "
        assert t450540_x3(text3=64000830, z3=74500223, flag3=0, mode3=1)
    else:
        """State 2"""
        SetEventState(74500221, 0)
        SetEventState(74500222, 0)
        SetEventState(74500223, 0)
        """State 3"""
        # talk:64000840:" "
        assert t450540_x5(text1=64000840, flag1=0, mode1=1)
    """State 7"""
    return 0

def t450540_x17(z1=-1, actionbutton1=6640):
    """State 0"""
    while True:
        """State 5"""
        call = t450540_x0(actionbutton1=actionbutton1, flag4=1695, flag5=6000, flag6=6000, flag7=6000,
                          flag8=6000)
        if call.Done():
            """State 3"""
            call = t450540_x7()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t450540_x8()
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
                call = t450540_x11()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t450540_x10()
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t450540_x18():
    """State 0,1"""
    # talk:64001000:"Yes, of course, as a burner of worlds should..."
    assert t450540_x5(text1=64001000, flag1=0, mode1=1)
    """State 2"""
    return 0

