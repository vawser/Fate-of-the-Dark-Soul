# -*- coding: utf-8 -*-
def t400140_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400140_x15()
        assert IsClientPlayer() == 1
        """State 3"""
        call = t400140_x16()
        assert not IsClientPlayer()

def t400140_x0(action1=12004000):
    """State 0,1"""
    # action:12004000:"Give <?gdsparam@2112?>?"
    OpenGenericDialog(8, action1, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t400140_x1(actionbutton1=6000, flag5=1055, flag6=6000, flag7=6000, flag8=6000, flag9=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
                and not IsPlayerDead() and not IsCharacterDisabled())
        """State 3"""
        assert (GetEventStatus(flag5) == 1 or GetEventStatus(flag6) == 1 or GetEventStatus(flag7) ==
                1 or GetEventStatus(flag8) == 1 or GetEventStatus(flag9) == 1)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer()
            and not IsPlayerDead() and not IsCharacterDisabled())):
            pass
        elif (not GetEventStatus(flag5) and not GetEventStatus(flag6) and not GetEventStatus(flag7) and
              not GetEventStatus(flag8) and not GetEventStatus(flag9)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t400140_x2():
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

def t400140_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400140_x4(text3=_, z3=_, flag4=0, mode3=1):
    """State 0,5"""
    assert t400140_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventState(z3, 1)
    """State 1"""
    TalkToPlayer(text3, -1, -1, flag4)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t400140_x5(text2=_, z2=_, flag3=0, mode2=1):
    """State 0,5"""
    assert t400140_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, flag3)
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

def t400140_x6(text1=_, flag2=0, mode1=1):
    """State 0,4"""
    assert t400140_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t400140_x7(lot1=60400):
    """State 0,1"""
    # lot:60400:Morion Blade
    GetItemFromItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t400140_x8(gesture1=19, z1=9021, flag1=6069):
    """State 0,1"""
    if GetEventStatus(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        OpenItemAcquisitionMenu(3, z1, 1)
        SetEventState(flag1, 1)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t400140_x9():
    """State 0,12"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1,
                2) == 1 and not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 2"""
        # action:15011020:"Purchase Item"
        AddTalkListData(1, 15011020, -1)
        # goods:2112:Orbeck's Ashes, action:15004020:"Tell of Orbeck's death"
        AddTalkListDataIf(GetEventStatus(74000601) == 1 and ComparePlayerInventoryNumber(3, 2112, 4, 1, 0) == 1,
                          3, 15004020, -1)
        # action:15000000:"Talk"
        AddTalkListData(4, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 4,9"""
            OpenRegularShop(40000, 59999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 5,11"""
            CombineMenuFlagAndEventFlag(6001, 233)
            """State 10"""
            OpenEnhanceShop(0)
            assert not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 13,20"""
            # action:12004000:"Give <?gdsparam@2112?>?"
            call = t400140_x0(action1=12004000)
            if call.Get() == 0:
                """State 15,7"""
                SetEventState(74000603, 1)
                # goods:2112:Orbeck's Ashes
                PlayerEquipmentQuantityChange(3, 2112, -1)
                """State 19"""
                # talk:14001400:"Ahh, I see Orbeck's claim is proven false."
                assert t400140_x6(text1=14001400, flag2=0, mode1=1)
                """State 17"""
                # lot:60400:Morion Blade
                assert t400140_x7(lot1=60400)
            elif call.Done():
                """State 14"""
                pass
        elif GetTalkListEntryResult() == 4:
            """State 6,16"""
            assert t400140_x17()
        else:
            """State 18"""
            assert t400140_x20()
            """State 21"""
            return 0

def t400140_x10():
    """State 0,1"""
    if GetEventStatus(1041) == 1:
        """State 5"""
        if GetEventStatus(74000603) == 1 and not GetEventStatus(50006040):
            """State 13"""
            Label('L0')
            """State 26"""
            # talk:14001400:"Ahh, I see Orbeck's claim is proven false."
            assert t400140_x6(text1=14001400, flag2=0, mode1=1)
            """State 27"""
            # lot:60400:Morion Blade
            assert t400140_x7(lot1=60400)
        elif not GetEventStatus(74000600) or not GetEventStatus(6069):
            """State 2,29"""
            # talk:14000000:"...Oh, prithee...art thou good Yoel's master?"
            assert t400140_x6(text1=14000000, flag2=0, mode1=1)
            """State 28"""
            assert t400140_x8(gesture1=19, z1=9021, flag1=6069)
            """State 19"""
            # talk:14000050:"Another matter."
            assert t400140_x5(text2=14000050, z2=74000600, flag3=0, mode2=1)
            """State 20"""
            Label('L1')
            assert t400140_x9()
        else:
            """State 3"""
            if ((GetEventStatus(74500250) == 1 or GetEventStatus(14500801) == 1) and not GetEventStatus(9322)
                and not GetEventStatus(74000607)):
                """State 14,30"""
                # talk:14005000:"Ahh, thy scent beseems most familiar."
                assert t400140_x5(text2=14005000, z2=74000607, flag3=0, mode2=1)
                Goto('L1')
            elif GetEventStatus(9322) == 1 and not GetEventStatus(74000608):
                """State 15,31"""
                # talk:14005200:"Might that soul be..."
                assert t400140_x5(text2=14005200, z2=74000608, flag3=0, mode2=1)
                Goto('L1')
            elif GetEventStatus(9210) == 1:
                """State 6,22"""
                # talk:14000300:"Away to link the fire, I presume?"
                assert t400140_x6(text1=14000300, flag2=0, mode1=1)
                Goto('L1')
            else:
                """State 7,18"""
                # talk:14000100:"Speak thy desire,"
                assert t400140_x6(text1=14000100, flag2=0, mode1=1)
                Goto('L1')
    elif GetEventStatus(1042) == 1:
        """State 8"""
        if GetEventStatus(74000603) == 1 and not GetEventStatus(50006040):
            Goto('L0')
        elif not GetEventStatus(74000606):
            """State 9,24"""
            # talk:14001500:"Ahh, our Lord and Liege."
            assert t400140_x5(text2=14001500, z2=74000606, flag3=0, mode2=1)
            Goto('L1')
        else:
            """State 10"""
            if ((GetEventStatus(74500250) == 1 or GetEventStatus(14500801) == 1) and not GetEventStatus(9322)
                and not GetEventStatus(74000607)):
                """State 16,32"""
                # talk:14005100:"Ahh, our Lord and rightful Liege."
                assert t400140_x5(text2=14005100, z2=74000607, flag3=0, mode2=1)
                Goto('L1')
            elif GetEventStatus(9322) == 1 and not GetEventStatus(74000608):
                """State 17,33"""
                # talk:14005300:"Ahh, our Lord and Liege."
                assert t400140_x5(text2=14005300, z2=74000608, flag3=0, mode2=1)
                Goto('L1')
            elif GetEventStatus(9210) == 1:
                """State 11,25"""
                # talk:14000400:"Ahh, our Lord and Liege."
                assert t400140_x6(text1=14000400, flag2=0, mode1=1)
                Goto('L1')
            else:
                """State 12,23"""
                # talk:14000200:"Ahh, our Lord and rightful Liege."
                assert t400140_x6(text1=14000200, flag2=0, mode1=1)
                Goto('L1')
    else:
        """State 4,21"""
        # talk:14001600:"Thou'st forsworn the Lord's Mark."
        assert t400140_x5(text2=14001600, z2=74000619, flag3=0, mode2=1)
    """State 34"""
    return 0

def t400140_x11():
    """State 0,9"""
    assert t400140_x2()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if not GetEventStatus(1056) and not GetEventStatus(1057):
        """State 2"""
        if GetDistanceToPlayer() < 10:
            """State 8,11"""
            call = t400140_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 10"""
                Label('L0')
                assert t400140_x2()
            elif GetEventStatus(1056) == 1 or GetEventStatus(1057) == 1:
                """State 5"""
                Label('L1')
                if GetDistanceToPlayer() < 10:
                    """State 6,12"""
                    call = t400140_x22()
                    if call.Done():
                        pass
                    elif GetDistanceToPlayer() > 12:
                        Goto('L0')
                elif not GetEventStatus(1056) and not GetEventStatus(1057):
                    """State 7"""
                    pass
        else:
            """State 4"""
            pass
    else:
        Goto('L1')
    """State 13"""
    return 0

def t400140_x12():
    """State 0,1"""
    if GetEventStatus(1058) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            call = t400140_x23()
            if call.Done():
                Goto('L0')
            elif GetDistanceToPlayer() > 12:
                pass
        else:
            """State 5"""
            pass
        """State 6"""
        assert t400140_x2()
    """State 8"""
    Label('L0')
    return 0

def t400140_x13():
    """State 0,2"""
    if GetEventStatus(1056) == 1 or GetEventStatus(1057) == 1:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            # talk:14002600:"Peasant, at least thy cadavder shall a little kindling make..."
            call = t400140_x6(text1=14002600, flag2=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t400140_x2()
        else:
            """State 5"""
            pass
    else:
        """State 1"""
        pass
    """State 8"""
    return 0

def t400140_x14():
    """State 0,1"""
    if (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonMenuIsOpen(12, 0) and not
        CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 2,5"""
        call = t400140_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t400140_x2()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t400140_x15():
    """State 0"""
    while True:
        """State 1"""
        call = t400140_x18()
        assert not GetEventStatus(1041) and not GetEventStatus(1042) and not GetEventStatus(1043)
        """State 2"""
        call = t400140_x19()
        assert GetEventStatus(1041) == 1 or GetEventStatus(1042) == 1 or GetEventStatus(1043) == 1
    """Unused"""
    """State 3"""
    return 0

def t400140_x16():
    """State 0,1"""
    assert t400140_x2()
    """State 2"""
    return 0

def t400140_x17():
    """State 0,1"""
    if GetEventStatus(1221) == 1 and not GetEventStatus(1238) and not GetEventStatus(74000601):
        """State 4"""
        # talk:14001000:"Oh, good Hollow. I'm afraid I must say..."
        assert t400140_x5(text2=14001000, z2=74000601, flag3=0, mode2=1)
    elif GetEventStatus(1042) == 1:
        """State 2"""
        # talk:14003300:"Our Lord and Liege."
        assert t400140_x6(text1=14003300, flag2=0, mode1=1)
    elif GetEventStatus(1348) == 1 and GetEventStatus(74000604) == 1:
        """State 6"""
        # talk:14001300:"Ahh, greetings, our Lord and Liege."
        assert t400140_x5(text2=14001300, z2=74000605, flag3=0, mode2=1)
    elif GetEventStatus(136) == 1:
        """State 5"""
        # talk:14001200:"Our Lord and Liege."
        assert t400140_x5(text2=14001200, z2=74000604, flag3=0, mode2=1)
    elif GetEventStatus(50006040) == 1:
        """State 8"""
        # talk:14001403:"Lord of Hollows, may the dark sigil guide thy way."
        assert t400140_x6(text1=14001403, flag2=0, mode1=1)
    elif GetEventStatus(74000601) == 1:
        """State 3"""
        # talk:14001100:"Orbeck of Vinheim is a cause of much consternation."
        assert t400140_x6(text1=14001100, flag2=0, mode1=1)
    else:
        """State 7"""
        # talk:14000051:"Thou'rt a Lord, art thou not?"
        assert t400140_x6(text1=14000051, flag2=0, mode1=1)
    """State 9"""
    return 0

def t400140_x18():
    """State 0,2"""
    call = t400140_x24()
    assert CheckSelfDeath() == 1
    """State 1"""
    t400140_x12()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t400140_x19():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t400140_x20():
    """State 0,1"""
    if GetEventStatus(1042) == 1:
        """State 2"""
        if GetEventStatus(9210) == 1:
            """State 4,8"""
            # talk:14000800:"Honourable usurper, I prithee wrest the flame from its mantle."
            assert t400140_x6(text1=14000800, flag2=0, mode1=1)
        else:
            """State 5,9"""
            # talk:14000600:"Be safe, our Lord and Liege."
            assert t400140_x6(text1=14000600, flag2=0, mode1=1)
    else:
        """State 3"""
        if GetEventStatus(9210) == 1:
            """State 7,10"""
            # talk:14000700:"Link the fire, our Lord of Hollows."
            assert t400140_x6(text1=14000700, flag2=0, mode1=1)
        else:
            """State 6,11"""
            # talk:14000500:"Till we meet again."
            assert t400140_x6(text1=14000500, flag2=0, mode1=1)
    """State 12"""
    return 0

def t400140_x21():
    """State 0,5"""
    if GetEventStatus(1042) == 1:
        """State 1"""
        if not GetEventStatus(74000623):
            """State 8"""
            # talk:14003000:"Thy Lordship, what is the matter?"
            assert t400140_x4(text3=14003000, z3=74000623, flag4=0, mode3=1)
        else:
            """State 2"""
            SetEventState(74000621, 0)
            SetEventState(74000622, 0)
            SetEventState(74000623, 0)
            """State 9"""
            # talk:14003100:"Please, stop."
            assert t400140_x6(text1=14003100, flag2=0, mode1=1)
    else:
        """State 3"""
        if not GetEventStatus(74000623):
            """State 12"""
            # talk:14002000:"Where are thy wits!"
            assert t400140_x4(text3=14002000, z3=74000623, flag4=0, mode3=1)
        else:
            """State 4"""
            SetEventState(74000621, 0)
            SetEventState(74000622, 0)
            SetEventState(74000623, 0)
            """State 13"""
            # talk:14002100:"Cease this at once!"
            assert t400140_x6(text1=14002100, flag2=0, mode1=1)
    """State 14"""
    Label('L0')
    return 0
    """Unused"""
    """State 6"""
    # talk:14002700:" "
    assert t400140_x4(text3=14002700, z3=74000621, flag4=0, mode3=1)
    Goto('L0')
    """State 7"""
    # talk:14002800:" "
    assert t400140_x4(text3=14002800, z3=74000622, flag4=0, mode3=1)
    Goto('L0')
    """State 10"""
    # talk:14001700:" "
    assert t400140_x4(text3=14001700, z3=74000621, flag4=0, mode3=1)
    Goto('L0')
    """State 11"""
    # talk:14001800:" "
    assert t400140_x4(text3=14001800, z3=74000622, flag4=0, mode3=1)
    Goto('L0')

def t400140_x22():
    """State 0,3"""
    if not GetEventStatus(74000620):
        """State 1,4"""
        # talk:14002200:"Hmph, Yoel knows not of thy folly."
        assert t400140_x4(text3=14002200, z3=74000620, flag4=0, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t400140_x23():
    """State 0,1"""
    if GetEventStatus(1042) == 1:
        """State 2,4"""
        # talk:14003200:"Brave usurper, I beseech thee claim the fire..."
        assert t400140_x6(text1=14003200, flag2=0, mode1=1)
    else:
        """State 3,5"""
        # talk:14002500:"Kaathe, I have failed thee..."
        assert t400140_x6(text1=14002500, flag2=0, mode1=1)
    """State 6"""
    return 0

def t400140_x24():
    """State 0"""
    while True:
        """State 5"""
        call = t400140_x1(actionbutton1=6000, flag5=1055, flag6=6000, flag7=6000, flag8=6000, flag9=6000)
        if call.Done():
            """State 3"""
            call = t400140_x10()
            if call.Done():
                pass
            elif IsAttackedBySomeone() == 1 or (GetEventStatus(1056) == 1 and not GetEventStatus(74000620)):
                """State 1"""
                Label('L0')
                call = t400140_x11()
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
                call = t400140_x14()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone() == 1:
                    Goto('L0')
        elif IsAttackedBySomeone() == 1 or (GetEventStatus(1056) == 1 and not GetEventStatus(74000620)):
            Goto('L0')
        elif IsPlayerDead() == 1:
            break
    """State 2"""
    t400140_x13()
    Quit()
    """Unused"""
    """State 6"""
    return 0

