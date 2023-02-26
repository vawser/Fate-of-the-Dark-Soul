# -*- coding: utf-8 -*-
def t400250_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400250_x12()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t400250_x13()
        assert not IsClientPlayer()

def t400250_x0(actionbutton1=6000, flag4=1275, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
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

def t400250_x1():
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

def t400250_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400250_x3(text3=_, z2=_, flag3=0, mode3=1):
    """State 0,5"""
    assert t400250_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t400250_x4(text2=_, z1=_, flag2=0, mode2=1):
    """State 0,5"""
    assert t400250_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventState(z1, 1)
    """State 6"""
    return 0

def t400250_x5(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t400250_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t400250_x6(goods1=2130, goods2=2131, goods3=2144, goods4=2145):
    """State 0,11"""
    SetEventState(74000532, 0)
    """State 12"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 2"""
        # action:15015000:"Learn Dark Sorceries"
        AddTalkListData(1, 15015000, -1)
        # goods:2130:Quelana Pyromancy Tome, goods:2131:Grave Warden Pyromancy Tome, action:15015020:"Give Pyromancy Tome"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1 or ComparePlayerInventoryNumber(3, goods2, 2, 0, 0) == 1,
                          3, 15015020, -1)
        # goods:2144:Deep Braille Divine Tome, goods:2145:Londor Braille Divine Tome, action:15015030:"Give Divine Tome"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods3, 2, 0, 0) == 1 or ComparePlayerInventoryNumber(3, goods4, 2, 0, 0) == 1,
                          4, 15015030, -1)
        # action:15000000:"Talk"
        AddTalkListData(5, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 4,9"""
            OpenRegularShop(150100, 159999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 5,14"""
            OpenRegularShop(150000, 150099)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 7,16"""
            assert t400250_x14(goods1=goods1, goods2=goods2)
        elif GetTalkListEntryResult() == 4:
            """State 13,18"""
            assert t400250_x21(goods3=goods3, goods4=goods4)
        elif GetTalkListEntryResult() == 5:
            """State 6,15"""
            assert t400250_x15()
        else:
            """State 10,17"""
            assert t400250_x18()
            """State 19"""
            return 0

def t400250_x7():
    """State 0,1"""
    if not GetEventStatus(74000501):
        """State 2"""
        if not GetEventStatus(74000500):
            """State 3,20"""
            # talk:25000900:"Ahh, there you are."
            assert t400250_x5(text1=25000900, flag1=0, mode1=1)
        else:
            """State 5,18"""
            # talk:25001200:"Ahh, hello there. I'm sorry to say..."
            assert t400250_x5(text1=25001200, flag1=0, mode1=1)
        """State 7"""
        ClearTalkListData()
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 8"""
        # action:14015002:"Ask to learn dark sorceries"
        AddTalkListData(1, 14015002, -1)
        # action:14015003:"Decline"
        AddTalkListData(2, 14015003, -1)
        """State 9"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 10"""
        if GetTalkListEntryResult() == 1:
            """State 11,22"""
            # talk:25001000:" "
            assert t400250_x4(text2=25001000, z1=74000501, flag2=0, mode2=1)
            """State 14"""
            SetEventState(74000500, 1)
            """State 19"""
            Label('L0')
            # goods:2130:Quelana Pyromancy Tome, goods:2131:Grave Warden Pyromancy Tome, goods:2144:Deep Braille Divine Tome, goods:2145:Londor Braille Divine Tome
            assert t400250_x6(goods1=2130, goods2=2131, goods3=2144, goods4=2145)
        elif GetTalkListEntryResult() == 2:
            """State 12,21"""
            # talk:25001100:" "
            assert t400250_x5(text1=25001100, flag1=0, mode1=1)
            """State 13"""
            SetEventState(74000500, 1)
        else:
            pass
    else:
        """State 6"""
        if GetEventStatus(74000531) == 1:
            """State 15"""
            ShuffleRNGSeed(2)
            if CompareRNGValue(0, 0) == 1:
                """State 16,23"""
                # talk:25001400:"Ahh, hello again. Thank goodness."
                assert t400250_x5(text1=25001400, flag1=0, mode1=1)
                Goto('L0')
            else:
                pass
        else:
            pass
        """State 4,17"""
        # talk:25001300:"Ahh, hello again. Thank goodness."
        assert t400250_x5(text1=25001300, flag1=0, mode1=1)
        Goto('L0')
    """State 24"""
    return 0

def t400250_x8():
    """State 0,6"""
    assert t400250_x1()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1,2"""
    if GetDistanceToPlayer() < 10:
        """State 5,7"""
        call = t400250_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 8"""
            assert t400250_x1()
    else:
        """State 4"""
        pass
    """State 9"""
    return 0

def t400250_x9():
    """State 0,1"""
    if GetEventStatus(1278) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            # talk:25002700:"You're a fickle one..."
            call = t400250_x5(text1=25002700, flag1=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t400250_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t400250_x10():
    """State 0,2,1,3"""
    return 0

def t400250_x11():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2,5"""
        call = t400250_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t400250_x1()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t400250_x12():
    """State 0"""
    while True:
        """State 1"""
        call = t400250_x16()
        assert not GetEventStatus(1261)
        """State 2"""
        call = t400250_x17()
        assert GetEventStatus(1261) == 1
    """Unused"""
    """State 3"""
    return 0

def t400250_x13():
    """State 0,1"""
    assert t400250_x1()
    """State 2"""
    return 0

def t400250_x14(goods1=2130, goods2=2131):
    """State 0,1"""
    ClearTalkListData()
    """State 2"""
    # goods:2130:Quelana Pyromancy Tome, action:15015021:"Give <?gdsparam@2130?> "
    AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1, 1, 15015021, -1)
    # goods:2131:Grave Warden Pyromancy Tome, action:15015022:"Give <?gdsparam@2131?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods2, 2, 0, 0) == 1, 2, 15015022, -1)
    # action:15000180:"Quit"
    AddTalkListData(99, 15000180, -1)
    """State 3"""
    ShowShopMessage(0)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 6"""
    if GetTalkListEntryResult() == 1:
        """State 4"""
        SetEventState(70000300, 1)
        # goods:2130:Quelana Pyromancy Tome
        PlayerEquipmentQuantityChange(3, goods1, -1)
        if GetEventStatus(70000301) == 1:
            """State 8"""
            # talk:25001900:"Ohh, another pyromancy tome, have we?"
            assert t400250_x5(text1=25001900, flag1=0, mode1=1)
        else:
            """State 10"""
            # talk:25001800:"Oh, a pyromancy tome, have we?"
            assert t400250_x5(text1=25001800, flag1=0, mode1=1)
    elif GetTalkListEntryResult() == 2:
        """State 5"""
        SetEventState(70000301, 1)
        # goods:2131:Grave Warden Pyromancy Tome
        PlayerEquipmentQuantityChange(3, goods2, -1)
        if GetEventStatus(70000300) == 1:
            """State 9"""
            # talk:25002100:"Oh, another pyromancy tome, have we?"
            assert t400250_x5(text1=25002100, flag1=0, mode1=1)
        else:
            """State 11"""
            # talk:25002000:"Oh, a pyromancy tome, have we?"
            assert t400250_x5(text1=25002000, flag1=0, mode1=1)
    else:
        """State 7"""
        pass
    """State 12"""
    return 0

def t400250_x15():
    """State 0,1"""
    if GetEventStatus(9210) == 1:
        """State 3"""
        # talk:25003000:"Oh, are you lost on your journey?"
        assert t400250_x5(text1=25003000, flag1=0, mode1=1)
    else:
        """State 2"""
        # talk:25001700:"There is one thing that you should know."
        assert t400250_x5(text1=25001700, flag1=0, mode1=1)
    """State 4"""
    return 0

def t400250_x16():
    """State 0,1"""
    call = t400250_x20()
    assert CheckSelfDeath() == 1
    """State 2"""
    t400250_x9()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t400250_x17():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t400250_x18():
    """State 0,1"""
    if GetEventStatus(74000532) == 1:
        """State 2"""
        # talk:25001600:"Don't stir up any trouble."
        assert t400250_x5(text1=25001600, flag1=0, mode1=1)
    else:
        """State 3"""
        # talk:25001500:"Do stay safe."
        assert t400250_x5(text1=25001500, flag1=0, mode1=1)
    """State 4"""
    return 0

def t400250_x19():
    """State 0,2"""
    if not GetEventStatus(74000521):
        """State 3"""
        # talk:25002400:" "
        assert t400250_x3(text3=25002400, z2=74000521, flag3=0, mode3=1)
    elif not GetEventStatus(74000522):
        """State 4"""
        # talk:25002500:" "
        assert t400250_x3(text3=25002500, z2=74000522, flag3=0, mode3=1)
    else:
        """State 1"""
        SetEventState(74000521, 0)
        SetEventState(74000522, 0)
        """State 5"""
        # talk:25002600:"What's wrong?"
        assert t400250_x5(text1=25002600, flag1=0, mode1=1)
    """State 6"""
    return 0

def t400250_x20():
    """State 0"""
    while True:
        """State 5"""
        call = t400250_x0(actionbutton1=6000, flag4=1275, flag5=6000, flag6=6000, flag7=6000, flag8=6000)
        if call.Done():
            """State 3"""
            call = t400250_x7()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1:
                """State 1"""
                Label('L0')
                call = t400250_x8()
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
                call = t400250_x11()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1:
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t400250_x10()
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t400250_x21(goods3=2144, goods4=2145):
    """State 0,1"""
    ClearTalkListData()
    """State 2"""
    # goods:2144:Deep Braille Divine Tome, action:15015023:"Give <?gdsparam@2144?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods3, 2, 0, 0) == 1, 3, 15015023, -1)
    # goods:2145:Londor Braille Divine Tome, action:15015024:"Give <?gdsparam@2145?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(3, goods4, 2, 0, 0) == 1, 4, 15015024, -1)
    # action:15000180:"Quit"
    AddTalkListData(99, 15000180, -1)
    """State 3"""
    ShowShopMessage(0)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 3 or GetTalkListEntryResult() == 4:
        """State 7"""
        if not GetEventStatus(74000502):
            """State 8,13"""
            # talk:25002200:"Oh, is this a Divine Tome?"
            assert t400250_x4(text2=25002200, z1=74000502, flag2=0, mode2=1)
        else:
            """State 9"""
            if GetTalkListEntryResult() == 3:
                """State 4"""
                SetEventState(70000302, 1)
                # goods:2144:Deep Braille Divine Tome
                PlayerEquipmentQuantityChange(3, goods3, -1)
            else:
                """State 10"""
                SetEventState(70000303, 1)
                # goods:2145:Londor Braille Divine Tome
                PlayerEquipmentQuantityChange(3, goods4, -1)
            """State 11"""
            if not GetEventStatus(70000302) or not GetEventStatus(70000303):
                """State 12"""
                # talk:25002300:"Ahh, you, how could you..."
                assert t400250_x5(text1=25002300, flag1=0, mode1=1)
            else:
                """State 14"""
                # talk:25002350:"Ahh, you, how could you..."
                assert t400250_x5(text1=25002350, flag1=0, mode1=1)
    else:
        """State 6"""
        pass
    """State 15"""
    return 0

