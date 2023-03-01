# -*- coding: utf-8 -*-
def t330008_1():
    """State 0,1"""
    t330008_x4()
    Quit()

def t330008_x0():
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

def t330008_x1(gesture1=17, z1=9019, flag3=6067):
    """State 0,1"""
    if GetEventStatus(flag3) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        OpenItemAcquisitionMenu(3, z1, 1)
        SetEventState(flag3, 1)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t330008_x2(actionbutton1=_, flag1=6001, flag2=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 2"""
        assert CompareBonfireState(1)
        """State 4"""
        assert GetEventStatus(flag1) == 1 and not GetEventStatus(flag2)
        """State 3"""
        if CompareBonfireState(0):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
        elif (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
              and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif not GetEventStatus(flag1) or GetEventStatus(flag2) == 1:
            pass
    """State 5"""
    return 0

def t330008_x3(action1=10010713):
    """State 0,1"""
    # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
    OpenGenericDialog(1, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t330008_x4():
    """State 0"""
    while True:
        """State 1"""
        call = t330008_x5()
        assert IsMultiplayerInProgress() == 1
        """State 2"""
        call = t330008_x8()
        assert not IsMultiplayerInProgress()
    """Unused"""
    """State 3"""
    return 0

def t330008_x5():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1:
        """State 2"""
        Label('L0')
    else:
        """State 3,15"""
        call = t330008_x2(actionbutton1=6100, flag1=6001, flag2=6000)
        if call.Done():
            """State 7"""
            TurnCharacterToFaceEntity(-1, 10000, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 4"""
            OfferHumanity()
            assert CompareBonfireLevel(5, 0) == 1
            """State 11"""
            RequestUnlockTrophy(41)
            """State 9"""
            UpdatePlayerRespawnPoint()
            Goto('L0')
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 14"""
    assert t330008_x2(actionbutton1=6101, flag1=6001, flag2=6000)
    """State 5"""
    ClearPlayerDamageInfo()
    """State 6"""
    SetTalkTime(1)
    """State 8"""
    TurnCharacterToFaceEntity(-1, 10000, -1)
    assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
    """State 10"""
    UpdatePlayerRespawnPoint()
    """State 12"""
    StartBonfireAnimLoop()
    call = t330008_x9()
    def ExitPause():
        EndBonfireKindleAnimLoop()
    if call.Done():
        Goto('L0')
    elif HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0):
        """State 13"""
        assert t330008_x10()
        Goto('L0')
    """Unused"""
    """State 16"""
    return 0

def t330008_x6():
    """State 0,6"""
    call = t330008_x0()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,7"""
        call = t330008_x2(actionbutton1=6100, flag1=6001, flag2=6000)
        if call.Done():
            """State 4"""
            TurnCharacterToFaceEntity(-1, 10000, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 3"""
            OfferHumanity()
            """State 5"""
            UpdatePlayerRespawnPoint()
            assert CompareBonfireLevel(5, 0) == 1
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 1"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t330008_x7():
    """State 0,1"""
    assert t330008_x0()
    """State 2"""
    return 0

def t330008_x8():
    """State 0"""
    while True:
        """State 1"""
        call = t330008_x6()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t330008_x7()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t330008_x9():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 2
    """State 21"""
    assert t330008_x1(gesture1=17, z1=9019, flag3=6067)
    """State 17"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15000150:"Travel"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 1, 15000150, -1)
        # action:15000130:"Attune Spell"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 2, 15000130, -1)
        # action:15000220:"Organize Storage Box"
        AddTalkListDataIf(GetEventStatus(14000101) == 1 or GetEventStatus(2050) == 1, 3, 15000220, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 4"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 3"""
            if GetEventStatus(2030) == 1:
                """State 18,8"""
                StartWarpMenuInit(-1)
                assert GetCurrentStateElapsedFrames() > 1
                """State 12"""
                if WasWarpMenuDestinationSelected() == 1:
                    break
                elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
                    """State 13"""
                    pass
            else:
                """State 16,20"""
                # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
                assert t330008_x3(action1=10010713)
        elif GetTalkListEntryResult() == 2:
            """State 6,7"""
            OpenMagicEquip(1000, 1000)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 14,15"""
            OpenRepository()
            assert not (CheckSpecificPersonMenuIsOpen(3, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif (GetTalkListEntryResult() == 99 or not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not
              CheckSpecificPersonGenericDialogIsOpen(0))):
            """State 5,22"""
            return 0
    """State 11,19"""
    SetEventState(74000013, 1)
    """State 9"""
    Quit()

def t330008_x10():
    """State 0,1"""
    assert t330008_x0()
    """State 2"""
    return 0

