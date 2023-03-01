# -*- coding: utf-8 -*-
def t470000_1():
    """State 0,1"""
    t470000_x4()
    Quit()

def t470000_x0():
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

def t470000_x1(gesture1=17, z1=9019, flag3=6067):
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

def t470000_x2(actionbutton1=_, flag1=6001, flag2=6000):
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

def t470000_x3(action1=10010713):
    """State 0,1"""
    # action:10010713:"Game installation incomplete.\nCannot travel between bonfires."
    OpenGenericDialog(1, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t470000_x4():
    """State 0"""
    while True:
        """State 1"""
        call = t470000_x5()
        assert IsMultiplayerInProgress() == 1
        """State 2"""
        call = t470000_x8()
        assert not IsMultiplayerInProgress()

def t470000_x5():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1:
        """State 2"""
        Label('L0')
    else:
        """State 3,15"""
        call = t470000_x2(actionbutton1=6100, flag1=6001, flag2=6000)
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
    assert t470000_x2(actionbutton1=6101, flag1=6001, flag2=6000)
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
    call = t470000_x9()
    def ExitPause():
        EndBonfireKindleAnimLoop()
    if call.Done():
        Goto('L0')
    elif (HasPlayerBeenAttacked() == 1 or GetDistanceToPlayer() > 3 or CompareBonfireState(0) or GetEventStatus(25009600)
          == 1):
        """State 13"""
        assert t470000_x10()
        Goto('L0')

def t470000_x6():
    """State 0,6"""
    call = t470000_x0()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,7"""
        call = t470000_x2(actionbutton1=6100, flag1=6001, flag2=6000)
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

def t470000_x7():
    """State 0,1"""
    assert t470000_x0()
    """State 2"""
    return 0

def t470000_x8():
    """State 0"""
    while True:
        """State 1"""
        call = t470000_x6()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t470000_x7()
        assert not IsClientPlayer()

def t470000_x9():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 2
    """State 21"""
    assert t470000_x1(gesture1=17, z1=9019, flag3=6067)
    """State 17"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        AddTalkListData(30, 99090001, -1)
        # action:15000150:"Travel"
        AddTalkListData(1, 15000150, -1)
        # action:15002000:"Level Up"
        AddTalkListData(10, 15002000, -1)
        # action:15000130:"Attune Spell"
        AddTalkListData(2, 15000130, -1)
        # action:15010002:"Reinforce Weapon"
        AddTalkListDataIf(not GetEventStatus(25000055), 18, 15010002, -1)
        # action:15010001:"Infuse Weapon"
        AddTalkListData(17, 15010001, -1)
        # action:15010003:"Repair Equipment"
        AddTalkListData(19, 15010003, -1)
        # action:15010005:""
        AddTalkListData(20, 15010005, -1)
        # action:15010006:""
        AddTalkListData(21, 15010006, -1)
        # action:15000220:"Organize Storage Box"
        AddTalkListData(3, 15000220, -1)
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
                assert t470000_x3(action1=10010713)
        elif GetTalkListEntryResult() == 2:
            """State 6,7"""
            OpenMagicEquip(1000, 1000)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 14,15"""
            OpenRepository()
            assert not (CheckSpecificPersonMenuIsOpen(3, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 10:
            """State 70,71"""
            OpenSoul()
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 22:
            """State 97,98"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 17:
            """State 84,85"""
            CombineMenuFlagAndEventFlag(6001, 344)
            CombineMenuFlagAndEventFlag(6001, 337)
            CombineMenuFlagAndEventFlag(6001, 334)
            CombineMenuFlagAndEventFlag(300, 332)
            CombineMenuFlagAndEventFlag(300, 333)
            CombineMenuFlagAndEventFlag(300, 342)
            CombineMenuFlagAndEventFlag(301, 335)
            CombineMenuFlagAndEventFlag(301, 345)
            CombineMenuFlagAndEventFlag(301, 340)
            CombineMenuFlagAndEventFlag(302, 336)
            CombineMenuFlagAndEventFlag(302, 338)
            CombineMenuFlagAndEventFlag(302, 339)
            CombineMenuFlagAndEventFlag(303, 341)
            CombineMenuFlagAndEventFlag(303, 343)
            CombineMenuFlagAndEventFlag(303, 346)
            CombineMenuFlagAndEventFlag(6000, 347)
            CombineMenuFlagAndEventFlag(6001, 331)
            CombineMenuFlagAndEventFlag(6001, 232)
            CombineMenuFlagAndEventFlag(6001, 233)
            CombineMenuFlagAndEventFlag(6001, 234)
            CombineMenuFlagAndEventFlag(6001, 235)
            """State 86"""
            OpenEquipmentChangeOfPurposeShop()
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 18:
            """State 87,88"""
            CombineMenuFlagAndEventFlag(6001, 232)
            CombineMenuFlagAndEventFlag(6001, 233)
            CombineMenuFlagAndEventFlag(6001, 234)
            CombineMenuFlagAndEventFlag(6001, 235)
            """State 89"""
            OpenEnhanceShop(0)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 19:
            """State 90"""
            OpenRepairShop()
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 20:
            """State 91,92"""
            OpenRegularShop(36000, 36999)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 21:
            """State 93,94"""
            OpenSellShop(-1, -1)
            assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                    2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        elif GetTalkListEntryResult() == 30:
            """State 23"""
            assert t470000_x20()
        elif (GetTalkListEntryResult() == 99 or not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not
              CheckSpecificPersonGenericDialogIsOpen(0))):
            """State 5,22"""
            return 0
    """State 11,19"""
    SetEventState(74000013, 1)
    """State 9"""
    Quit()

def t470000_x10():
    """State 0,1"""
    assert t470000_x0()
    """State 2"""
    return 0

def t470000_x20():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99090011, -1)
        AddTalkListData(2, 99090012, -1)
        AddTalkListData(3, 99090013, -1)
        AddTalkListData(4, 99090014, -1)
        AddTalkListData(5, 99090015, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            assert t470000_x21()
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            assert t470000_x22()
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            assert t470000_x23()
        elif GetTalkListEntryResult() == 4:
            """State 5"""
            assert t470000_x24()
        elif GetTalkListEntryResult() == 5:
            """State 6"""
            assert t470000_x25()
        elif GetTalkListEntryResult() == 99:
            """State 7"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 8"""
            return 0

def t470000_x21():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99060001, -1)
        AddTalkListDataIf(not GetEventStatus(25009610), 2, 99060002, -1)
        AddTalkListDataIf(GetEventStatus(25009610) == 1, 3, 99090010, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenGenericDialog(1, 99090021, 0, 0, 0)
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            SetEventState(25009610, 1)
            SetEventState(25009611, 0)
            SetEventState(25009612, 0)
            SetEventState(25009613, 0)
            SetEventState(25009614, 0)
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            SetEventState(25009600, 1)
            return 0
        elif GetTalkListEntryResult() == 99:
            """State 5"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6"""
            return 0

def t470000_x22():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99060001, -1)
        AddTalkListDataIf(not GetEventStatus(25009611), 2, 99060002, -1)
        AddTalkListDataIf(GetEventStatus(25009611) == 1, 3, 99090010, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenGenericDialog(1, 99090022, 0, 0, 0)
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            SetEventState(25009610, 0)
            SetEventState(25009611, 1)
            SetEventState(25009612, 0)
            SetEventState(25009613, 0)
            SetEventState(25009614, 0)
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            SetEventState(25009600, 1)
            return 0
        elif GetTalkListEntryResult() == 99:
            """State 5"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6"""
            return 0

def t470000_x23():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99060001, -1)
        AddTalkListDataIf(not GetEventStatus(25009612), 2, 99060002, -1)
        AddTalkListDataIf(GetEventStatus(25009612) == 1, 3, 99090010, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenGenericDialog(1, 99090023, 0, 0, 0)
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            SetEventState(25009610, 0)
            SetEventState(25009611, 0)
            SetEventState(25009612, 1)
            SetEventState(25009613, 0)
            SetEventState(25009614, 0)
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            SetEventState(25009600, 1)
            return 0
        elif GetTalkListEntryResult() == 99:
            """State 5"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6"""
            return 0

def t470000_x24():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99060001, -1)
        AddTalkListDataIf(not GetEventStatus(25009613), 2, 99060002, -1)
        AddTalkListDataIf(GetEventStatus(25009613) == 1, 3, 99090010, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenGenericDialog(1, 99090024, 0, 0, 0)
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            SetEventState(25009610, 0)
            SetEventState(25009611, 0)
            SetEventState(25009612, 0)
            SetEventState(25009613, 1)
            SetEventState(25009614, 0)
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            SetEventState(25009600, 1)
            return 0
        elif GetTalkListEntryResult() == 99:
            """State 5"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6"""
            return 0

def t470000_x25():
    while True:
        """State 0"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        AddTalkListData(1, 99060001, -1)
        AddTalkListDataIf(not GetEventStatus(25009614), 2, 99060002, -1)
        AddTalkListDataIf(GetEventStatus(25009614) == 1, 3, 99090010, -1)
        AddTalkListData(99, 15000190, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 1"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenGenericDialog(1, 99090025, 0, 0, 0)
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            SetEventState(25009610, 0)
            SetEventState(25009611, 0)
            SetEventState(25009612, 0)
            SetEventState(25009613, 0)
            SetEventState(25009614, 1)
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            SetEventState(25009600, 1)
            return 0
        elif GetTalkListEntryResult() == 99:
            """State 5"""
            ReportConversationEndToHavokBehavior()
            return 0
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6"""
            return 0

