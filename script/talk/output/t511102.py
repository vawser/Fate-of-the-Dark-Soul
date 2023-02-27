# -*- coding: utf-8 -*-
def t511102_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t511102_x14()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t511102_x15()
        assert not IsClientPlayer()

def t511102_x0(action2=_):
    """State 0,1"""
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t511102_x1(actionbutton1=6120, flag4=1015, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
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

def t511102_x2():
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

def t511102_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t511102_x4(text3=12002600, z3=74000115, flag3=0, mode3=1):
    """State 0,5"""
    assert t511102_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z3, 1)
    """State 1"""
    # talk:12002600:" "
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

def t511102_x5(text2=_, z2=_, flag2=0, mode2=0):
    """State 0,5"""
    assert t511102_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t511102_x6(text1=_, flag1=0, mode1=_):
    """State 0,4"""
    assert t511102_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t511102_x7(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t511102_x8(goods1=2138, goods2=390):
    """State 0,8"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15002000:"Level Up"
        AddTalkListData(1, 15002000, -1)
        # action:15002004:"Heal the Dark Sigil"
        AddTalkListData(4, 15002004, 74000125)
        # goods:2138:Eyes of a Fire Keeper, action:15002001:"Give <?gdsparam@2138?>"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1, 10, 15002001, -1)
        # goods:390:Fire Keeper Soul, action:15002005:"Give <?gdsparam@390?>"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods2, 2, 0, 0) == 1, 11, 15002005, -1)
        # action:15000000:"Talk"
        AddTalkListData(20, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 3"""
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 4"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                pass
            else:
                """State 13"""
                # talk:12000200:"Very well."
                assert t511102_x6(text1=12000200, flag1=0, mode1=0)
                """State 11"""
                def WhilePaused():
                    SetTalkTime(0.1)
                assert not GetEventStatus(74000137) and not GetEventStatus(74000138)
                """State 19"""
                SetEventState(74000135, 1)
                call = t511102_x25()
                def ExitPause():
                    SetEventState(74000135, 0)
                    SetEventState(74000136, 0)
                if call.Get() == 1:
                    """State 21"""
                    Label('L0')
                    return 0
                elif call.Done():
                    continue
        elif GetTalkListEntryResult() == 11:
            """State 5,17"""
            assert t511102_x22(goods2=goods2)
            continue
        elif GetTalkListEntryResult() == 20:
            """State 7,15"""
            assert t511102_x20()
            continue
        elif not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6,14"""
            assert t511102_x19()
            Goto('L0')
        elif GetTalkListEntryResult() == 10:
            """State 9,16"""
            def ExitPause():
                SetEventState(74000122, 0)
            assert t511102_x21(goods1=goods1)
            continue
        elif GetTalkListEntryResult() == 4:
            """State 10"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                pass
            else:
                """State 18"""
                # goods:490:Dark Sigil
                assert t511102_x23(goods3=490, z1=0)
                continue
        """State 12,20"""
        assert t511102_x7(action1=13002040)

def t511102_x9():
    assert t511102_x50()
    """State 24"""
    return 0

def t511102_x10():
    """State 0,6"""
    assert t511102_x2()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    assert not GetEventStatus(1016) and not GetEventStatus(1017)
    """State 2"""
    if GetDistanceToPlayer() < 10:
        """State 4,8"""
        call = t511102_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 7"""
            assert t511102_x2()
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t511102_x11():
    """State 0,1"""
    if GetEventStatus(1018) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4"""
            if GetEventStatus(50006020) == 1:
                """State 6,9"""
                # talk:12002900:" "
                call = t511102_x6(text1=12002900, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            else:
                """State 7,10"""
                # talk:12002950:" "
                call = t511102_x6(text1=12002950, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            """State 8"""
            assert t511102_x2()
        else:
            """State 5"""
            pass
    """State 11"""
    Label('L0')
    return 0

def t511102_x12():
    """State 0,1,2"""
    assert t511102_x2()
    """State 3"""
    return 0

def t511102_x13():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2,5"""
        call = t511102_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t511102_x2()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t511102_x14():
    """State 0"""
    while True:
        """State 1"""
        call = t511102_x16()
        assert not GetEventStatus(1000) and not GetEventStatus(1001) and not GetEventStatus(1002)
        """State 2"""
        call = t511102_x17()
        assert GetEventStatus(1000) == 1 or GetEventStatus(1001) == 1 or GetEventStatus(1002) == 1
    """Unused"""
    """State 3"""
    return 0

def t511102_x15():
    """State 0,1"""
    assert t511102_x2()
    """State 2"""
    return 0

def t511102_x16():
    """State 0,1"""
    call = t511102_x26()
    assert CheckSelfDeath() == 1
    """State 2"""
    t511102_x11()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t511102_x17():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t511102_x18():
    """State 0,1"""
    if not GetEventStatus(74000115):
        """State 2,5"""
        # talk:12002600:" "
        assert t511102_x4(text3=12002600, z3=74000115, flag3=0, mode3=1)
    else:
        """State 3,6"""
        # talk:12002700:" "
        assert t511102_x6(text1=12002700, flag1=0, mode1=1)
        """State 4"""
        SetEventState(74000115, 0)
    """State 7"""
    return 0

def t511102_x19():
    
    return 0

def t511102_x20():
    """State 0,1"""
    if GetEventStatus(50006020) == 1:
        """State 2"""
        if GetEventStatus(9300) == 1 and not GetEventStatus(1002):
            """State 4,20"""
            # talk:12000700:"Ashen one, may I pose thee a question?"
            assert t511102_x6(text1=12000700, flag1=0, mode1=0)
        else:
            """State 3,19"""
            # talk:12000600:"Ashen one, to be unkindled is to be a vessel for souls."
            assert t511102_x6(text1=12000600, flag1=0, mode1=0)
    else:
        """State 5"""
        if not GetEventStatus(74000130) and not GetEventStatus(74000131):
            """State 7,21"""
            # talk:12000800:"Ashen one, my thanks for the eyes thou'st given."
            assert (t511102_x6(text1=12000800, flag1=0, mode1=0) and (not CheckSpecificPersonGenericDialogIsOpen(2)
                    and not (CheckSpecificPersonMenuIsOpen(-1, 2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2))))
            """State 14"""
            ClearTalkListData()
            """State 15"""
            # action:14002000:"Wish for a world without flame"
            AddTalkListData(1, 14002000, -1)
            # action:14002001:"Decline"
            AddTalkListData(2, 14002001, -1)
            """State 13"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 17"""
            if GetTalkListEntryResult() == 1:
                """State 12,24"""
                # talk:12000900:"Of course."
                assert t511102_x5(text2=12000900, z2=74000130, flag2=0, mode2=0)
            elif GetTalkListEntryResult() == 2:
                """State 16,25"""
                # talk:12001100:"Of course not."
                assert t511102_x5(text2=12001100, z2=74000131, flag2=0, mode2=0)
            else:
                """State 18"""
                pass
        else:
            """State 6"""
            if GetEventStatus(74000130) == 1:
                """State 8"""
                if not GetEventStatus(74000132) or GetEventStatus(74000110) == 1:
                    """State 10,23"""
                    # talk:12001000:"Ashen one, if thine heart should bend..."
                    assert t511102_x6(text1=12001000, flag1=0, mode1=0)
                else:
                    """State 11,26"""
                    # talk:12001900:"Ashen one, forgive me if this soundeth strange."
                    assert t511102_x5(text2=12001900, z2=74000110, flag2=0, mode2=0)
            else:
                """State 9,22"""
                # talk:12001200:"Ashen one, kill me, and take these eyes away."
                assert t511102_x6(text1=12001200, flag1=0, mode1=0)
    """State 27"""
    return 0

def t511102_x21(goods1=2138):
    """State 0,6"""
    # action:12002000:"Give <?gdsparam@2138?>?"
    call = t511102_x0(action2=12002000)
    if call.Get() == 0:
        """State 2,1"""
        # goods:2138:Eyes of a Fire Keeper
        PlayerEquipmentQuantityChange(3, goods1, -1)
        """State 3"""
        SetEventState(50006020, 0)
        """State 5"""
        SetEventState(74000122, 1)
        """State 7"""
        # talk:12003300:"...Ashen one, are these..."
        assert t511102_x6(text1=12003300, flag1=0, mode1=0)
    elif call.Done():
        """State 4"""
        pass
    """State 8"""
    return 0

def t511102_x22(goods2=390):
    """State 0,5"""
    # action:12002001:"Give <?gdsparam@390?>?"
    call = t511102_x0(action2=12002001)
    if call.Get() == 0:
        """State 2,1"""
        # goods:390:Fire Keeper Soul
        PlayerEquipmentQuantityChange(3, goods2, -1)
        """State 3"""
        SetEventState(74000125, 1)
        """State 6"""
        # talk:12003400:"...Ashen one, this is..."
        assert (t511102_x6(text1=12003400, flag1=0, mode1=0) and (not CheckSpecificPersonGenericDialogIsOpen(2)
                and not (CheckSpecificPersonMenuIsOpen(-1, 2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2))))
        """State 7"""
        # action:13002030:"The Fire Keeper is now able to heal the dark sigil"
        assert t511102_x7(action1=13002030)
        """State 8"""
        # talk:12003500:"Forgive me, sister."
        assert t511102_x6(text1=12003500, flag1=0, mode1=0)
    elif call.Done():
        """State 4"""
        pass
    """State 9"""
    return 0

def t511102_x23(goods3=490, z1=0):
    """State 0,1"""
    # goods:490:Dark Sigil
    if ComparePlayerInventoryNumber(3, goods3, 0, 0, 0) == 1:
        """State 3,20"""
        # action:13002021:"You have no dark sigil"
        assert t511102_x7(action1=13002021)
    else:
        """State 2,24"""
        assert t511102_x24(goods3=goods3, z1=z1)
        """State 10"""
        SetMessageTagValue(0, GetLevelUpSoulCost(GetStatus(33), GetStatus(33) + GetWorkValue(z1)))
        """State 21"""
        # action:12002002:"Requires <?evntAcquittalPrice?> souls. \nWill you choose to heal the dark sigil?"
        call = t511102_x0(action2=12002002)
        if call.Get() == 0:
            """State 6"""
            if ComparePlayerStatus(8, 2, GetLevelUpSoulCost(GetStatus(33), GetStatus(33) + GetWorkValue(z1))):
                """State 4,13"""
                TurnCharacterToFaceEntity(-1, 10000, -1)
                assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 12"""
                TurnCharacterToFaceEntity(69010, 10000, -1)
                assert GetCurrentStateElapsedTime() > 1.5
                """State 8"""
                # goods:490:Dark Sigil
                PlayerEquipmentQuantityChange(3, goods3, -1 * GetWorkValue(z1))
                """State 9"""
                ChangePlayerStats(8, 1, GetLevelUpSoulCost(GetStatus(33), GetStatus(33) + GetWorkValue(z1)))
                """State 11"""
                SetEventState(74000124, 1)
                """State 14"""
                if GetPlayerChrType() == 8:
                    """State 15,18"""
                    GiveSpEffectToPlayer(3093)
                else:
                    """State 16,17"""
                    ChangePlayerStats(31, 5, 0)
                """State 19"""
                assert GetCurrentStateElapsedTime() > 3
                """State 23"""
                # action:13002020:"Dark sigil has been healed"
                assert t511102_x7(action1=13002020) and GetWhetherChrEventAnimHasEnded(10000) == 1
            else:
                """State 5,22"""
                # action:13000050:"Insufficient souls"
                assert t511102_x7(action1=13000050)
        elif call.Done():
            """State 7"""
            pass
    """State 25"""
    return 0

def t511102_x24(goods3=490, z1=0):
    """State 0,1"""
    # goods:490:Dark Sigil
    SetWorkValue(z1, GetItemHeldNumLimit(3, goods3))
    while True:
        """State 5"""
        # goods:490:Dark Sigil
        if ComparePlayerInventoryNumber(3, goods3, 0, GetWorkValue(z1), 0) or GetWorkValue(z1) <= 0:
            break
        else:
            """State 3,2"""
            SetWorkValue(z1, GetWorkValue(z1) - 1)
    """State 4,6"""
    return 0

def t511102_x25():
    """State 0,3"""
    if DoesSelfHaveSpEffect(150) == 1 or DoesSelfHaveSpEffect(152) == 1:
        """State 4"""
        SetEventState(74000136, 1)
        """State 2"""
        if not GetEventStatus(74000135):
            pass
        elif GetEventStatus(74000137) == 1 and GetEventStatus(74000138) == 1:
            """State 1"""
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            return 0
    elif not GetEventStatus(74000135):
        pass
    """State 6"""
    return 1

def t511102_x26():
    """State 0"""
    while True:
        """State 5"""
        call = t511102_x1(actionbutton1=6120, flag4=1015, flag5=6000, flag6=6000, flag7=6000, flag8=6000)
        if call.Done():
            """State 3"""
            call = t511102_x9()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t511102_x10()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead() == 1:
                    break
            elif IsPlayerDead() == 1:
                break
            elif GetDistanceToPlayer() > 3 or GetPlayerYDistance() > 0.25:
                """State 4"""
                call = t511102_x13()
                if call.Done() and (GetDistanceToPlayer() < 2.5 and GetPlayerYDistance() < 0.249):
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t511102_x12()
    Quit()
    """Unused"""
    """State 6"""
    return 0

#-------------------------------------
# Journey Menu
#-------------------------------------
def t511102_x50():
    MainBonfireMenuFlag()
    
    while True:
        ClearTalkListData()
        
        # Select Journey Type
        AddTalkListDataIf(GetEventStatus(25000100) == 0, 10, 80000100, -1)
        
        # Build Loadout
        AddTalkListDataIf(GetEventStatus(25000100) == 0, 11, 80000101, -1)
        
        # Commit
        AddTalkListDataIf(GetEventStatus(25000100) == 0 and GetEventStatus(25000101) == 1 or GetEventStatus(25000100) == 0 and GetEventStatus(25000102) == 1 or GetEventStatus(25000100) == 0 and GetEventStatus(25000103) == 1 or GetEventStatus(25000100) == 0 and GetEventStatus(25000104) == 1, 20, 80000102, -1)
        
        # Leave
        AddTalkListData(99, 80000999, -1)
        
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Select Journey Type
        if GetTalkListEntryResult() == 10:
            assert t511102_x51()
            continue
        # Build Loadout
        elif GetTalkListEntryResult() == 11:
            assert t511102_x52()
            continue
        # Commit
        elif GetTalkListEntryResult() == 20:
            assert t511102_x60(80000140)
            
            c1_110()
    
            ClearTalkListData()
            
            # Yes
            AddTalkListData(1, 80000103, -1)
            
            # No
            AddTalkListData(2, 80000104, -1)
            
            OpenConversationChoicesMenu(0)
            
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

            # Yes
            if GetTalkListEntryResult() == 1:
                SetEventState(25000100, 1)
                return 0
            # Cancel
            elif GetTalkListEntryResult() == 2:
                return 1
            else:
                return 2
   
            return 0
        else:
            return 0
            
        assert CheckSpecificPersonTalkHasEnded(0) == 1
        
# Journey Type
def t511102_x51():
    MainBonfireMenuFlag()
    
    while True:
        ClearTalkListData()
        
        # Hollow
        AddTalkListDataIf(GetEventStatus(25000101) == 0, 1, 80000110, -1)
        # Hollow (Selected)
        AddTalkListDataIf(GetEventStatus(25000101) == 1, 10, 80000120, -1)
        
        # Explorer
        AddTalkListDataIf(GetEventStatus(25000102) == 0, 2, 80000111, -1)
        # Explorer (Selected)
        AddTalkListDataIf(GetEventStatus(25000102) == 1, 11, 80000121, -1)
        
        # Conqueror
        AddTalkListDataIf(GetEventStatus(25000103) == 0, 3, 80000112, -1)
        # Conqueror (Selected)
        AddTalkListDataIf(GetEventStatus(25000103) == 1, 12, 80000122, -1)
        
        # Accursed
        AddTalkListDataIf(GetEventStatus(25000104) == 0, 4, 80000113, -1)
        # Accursed (Selected)
        AddTalkListDataIf(GetEventStatus(25000104) == 1, 13, 80000123, -1)
        
        # Leave
        AddTalkListData(99, 80000999, -1)
        
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Tarnished
        if GetTalkListEntryResult() == 1:
            assert t511102_x61(80000130, 25000101, 1)
            continue
        # Explorer
        elif GetTalkListEntryResult() == 2:
            assert t511102_x61(80000131, 25000102, 1)
            continue
        # Conqueror
        elif GetTalkListEntryResult() == 3:
            assert t511102_x61(80000132, 25000103, 1)
            continue
        # Accursed
        elif GetTalkListEntryResult() == 4:
            assert t511102_x61(80000133, 25000104, 1)
            continue
        # Tarnished (selected)
        elif GetTalkListEntryResult() == 10:
            assert t511102_x60(80000130)
            return 0
        # Explorer (selected)
        elif GetTalkListEntryResult() == 11:
            assert t511102_x60(80000131)
            return 0
        # Conqueror (selected)
        elif GetTalkListEntryResult() == 12:
            assert t511102_x60(80000132)
            return 0
        # Accursed (selected)
        elif GetTalkListEntryResult() == 13:
            assert t511102_x60(80000133)
            return 0
        else:
            return 0
        assert CheckSpecificPersonTalkHasEnded(0) == 1
        
# Custom Loadout
def t511102_x52():
    MainBonfireMenuFlag()
    
    while True:
        ClearTalkListData()

        # Weapons
        AddTalkListData(1, 80000200, -1)
        
        # Spells
        AddTalkListData(2, 80000201, -1)
        
        # Armor
        AddTalkListData(3, 80000202, -1)
        
        # Accessories
        AddTalkListData(4, 80000203, -1)
        
        # Ammunition
        AddTalkListData(5, 80000204, -1)

        # Items
        # AddTalkListData(8, 80000205, -1)
        
        # Souls
        AddTalkListDataIf(GetEventStatus(25000112) == 0 and ComparePlayerInventoryNumber(3, 2160, 4, 1, 0) == 1 , 9, 80000206, -1)
        
        # Level Up
        AddTalkListData(10, 80000207, -1)
        
        # Leave
        AddTalkListData(99, 80000999, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Weapons
        if GetTalkListEntryResult() == 1:
            OpenTranspositionShop(9100000, 9109999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spells
        elif GetTalkListEntryResult() == 2:
            OpenTranspositionShop(9120000, 9129999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Armor
        elif GetTalkListEntryResult() == 3:
            OpenTranspositionShop(9110000, 9119999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Accessories
        elif GetTalkListEntryResult() == 4:
            OpenTranspositionShop(9130000, 9139999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ammunition
        elif GetTalkListEntryResult() == 5:
            OpenTranspositionShop(9140000, 9149999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Items
        elif GetTalkListEntryResult() == 8:
            OpenTranspositionShop(9150000, 9159999)
            assert not (CheckSpecificPersonMenuIsOpen(18, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Souls
        elif GetTalkListEntryResult() == 9:
            assert t511102_x62()
            return 0
        # Level up
        elif GetTalkListEntryResult() == 10:
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Description Prompt
def t511102_x60(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Difficulty - YES/NO Choice
def t511102_x61(text=_, flag=_, value=_):
    assert t511102_x60(text)
            
    MainBonfireMenuFlag()

    ClearTalkListData()
    
    # Yes
    AddTalkListData(1, 80000103, -1)
    
    # No
    AddTalkListData(2, 80000104, -1)
    
    OpenConversationChoicesMenu(0)
    
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

    # Yes
    if GetTalkListEntryResult() == 1:
        SetEventState(25000101, 0)
        SetEventState(25000102, 0)
        SetEventState(25000103, 0)
        SetEventState(25000104, 0)
        
        SetEventState(flag, value)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2
        
# Souls - YES/NO Choice
def t511102_x62():
    assert t511102_x60(80000210)
            
    MainBonfireMenuFlag()

    ClearTalkListData()
    
    # Yes
    AddTalkListData(1, 80000103, -1)
    
    # No
    AddTalkListData(2, 80000104, -1)
    
    OpenConversationChoicesMenu(0)
    
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

    # Yes
    if GetTalkListEntryResult() == 1:
        SetEventState(25000112, 1)
        GiveSpEffectToPlayer(200000100)
        PlayerEquipmentQuantityChange(3, 2160, -1)
        assert t511102_x60(80000211)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2