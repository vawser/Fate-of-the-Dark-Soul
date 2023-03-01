# -*- coding: utf-8 -*-
def t370006_1():
    """State 0,1"""
    t370006_x4()
    Quit()

def t370006_x0():
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

def t370006_x1(gesture1=17, z1=9019, flag3=6067):
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

def t370006_x2(actionbutton1=_, flag1=6001, flag2=6000):
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

def t370006_x3(action1=10010713):
    """State 0,1"""
    # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
    OpenGenericDialog(1, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t370006_x4():
    """State 0"""
    while True:
        """State 1"""
        call = t370006_x5()
        assert IsMultiplayerInProgress() == 1
        """State 2"""
        call = t370006_x8()
        assert not IsMultiplayerInProgress()
    """Unused"""
    """State 3"""
    return 0

def t370006_x5():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1:
        """State 2"""
        Label('L0')
    else:
        """State 3,15"""
        call = t370006_x2(actionbutton1=6100, flag1=6001, flag2=6000)
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
    assert t370006_x2(actionbutton1=6101, flag1=6001, flag2=6000)
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
    call = t370006_x9()
    def ExitPause():
        EndBonfireKindleAnimLoop()
    if call.Done():
        Goto('L0')
    elif HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0):
        """State 13"""
        assert t370006_x10()
        Goto('L0')
    """Unused"""
    """State 16"""
    return 0

def t370006_x6():
    """State 0,6"""
    call = t370006_x0()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,7"""
        call = t370006_x2(actionbutton1=6100, flag1=6001, flag2=6000)
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

def t370006_x7():
    """State 0,1"""
    assert t370006_x0()
    """State 2"""
    return 0

def t370006_x8():
    """State 0"""
    while True:
        """State 1"""
        call = t370006_x6()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t370006_x7()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t370006_x9():
    assert GetCurrentStateElapsedTime() > 2

    assert t370006_x1(gesture1=17, z1=9019, flag3=6067)

    MainBonfireMenuFlag()
    while True:
    
        ClearTalkListData()
        
        # Level Up
        AddTalkListData(4, 15002000, -1)
        
        # Attune Spell
        AddTalkListData(1, 15000130, -1)
        
        # Organize Storage Box
        AddTalkListData(2, 15000220, -1)
        
        # Allot Estus
        AddTalkListData(3, 15002002, -1)
        
        # Leave
        AddTalkListData(99, 15000005, -1)
        
        ShowShopMessage(1)
        
        # Organize Storage Box
        if GetTalkListEntryResult() == 2:
            ForceCloseMenu()
            OpenRepository()
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
            continue
         # Attune Spell
        elif GetTalkListEntryResult() == 1:
            OpenMagicEquip(1000, 1000)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
            continue
        # Allot Estus
        elif GetTalkListEntryResult() == 3:
            assert (t370006_x21() and not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)))
            continue
        # Level up
        elif GetTalkListEntryResult() == 4:
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Leave
        elif GetTalkListEntryResult() == 99 or not GetTalkListEntryResult():
            pass
            
    SetEventState(74000013, 1)

    Quit()

def t370006_x10():
    """State 0,1"""
    assert t370006_x0()
    """State 2"""
    return 0


def t370006_x21():
    """State 0,6"""
    call = t370006_x22(0)
    if call.Get() == 1:
        """State 1,7"""
        call = t370006_x22(1)
        if call.Get() == 1:
            """State 3,4"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif call.Done():
            """State 5,9"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t370006_x23(action1=13002014)
    elif call.Done():
        """State 2,8"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t370006_x23(action1=13002013)
    """State 10"""
    return 0
    
def t370006_x22(offset=_):
    """State 0,1"""
    if (not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
        150 + 1 + offset * 40 + 1 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 +
        2 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 3 * 2) and not IsEquipmentIDObtained(3,
        150 + 1 + offset * 40 + 4 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 +
        5 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 6 * 2) and not IsEquipmentIDObtained(3,
        150 + 1 + offset * 40 + 7 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 +
        8 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 9 * 2)):
        """State 2"""
        if (not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
            150 + 1 + offset * 40 + 11 * 2) and not IsEquipmentIDObtained(3, 150 + 12 + offset
            * 40 + 12 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 13 * 2) and not
            IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 14 * 2) and not IsEquipmentIDObtained(3,
            150 + 1 + offset * 40 + 15 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset *
            40 + 16 * 2) and not IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 17 * 2) and not
            IsEquipmentIDObtained(3, 150 + 1 + offset * 40 + 18 * 2) and not IsEquipmentIDObtained(3,
            150 + 1 + offset * 40 + 19 * 2)):
            """State 3"""
            if (not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
                150 + 0 + offset * 40 + 1 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset
                * 40 + 2 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 3 * 2) and
                not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 4 * 2) and not IsEquipmentIDObtained(3,
                150 + 0 + offset * 40 + 5 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset
                * 40 + 6 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 7 * 2) and
                not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 8 * 2) and not IsEquipmentIDObtained(3,
                150 + 0 + offset * 40 + 9 * 2)):
                """State 4"""
                if (not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
                    150 + 0 + offset * 40 + 11 * 2) and not IsEquipmentIDObtained(3, 150 + 0 +
                    offset * 40 + 12 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 +
                    13 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 14 * 2) and not
                    IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 15 * 2) and not IsEquipmentIDObtained(3,
                    150 + 0 + offset * 40 + 16 * 2) and not IsEquipmentIDObtained(3, 150 + 0 +
                    offset * 40 + 17 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 +
                    18 * 2) and not IsEquipmentIDObtained(3, 150 + 0 + offset * 40 + 19 * 2)):
                    """State 5"""
                    return 0
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    """State 6"""
    return 1

def t370006_x23(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0