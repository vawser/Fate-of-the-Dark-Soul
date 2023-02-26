# -*- coding: utf-8 -*-
def t400792_1():
    """State 0"""
    while True:
        """State 1"""
        Label('L0')
        DebugEvent('待機')
        if not GetEventStatus(1901) and CheckActionButtonArea(6000) and not CheckSelfDeath():
            """State 4"""
            DebugEvent('会話')
            call = t400792_x2()
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                break
            elif GetDistanceToPlayer() >= 5:
                """State 5"""
                Label('L1')
                DebugEvent('会話範囲外')
                call = t400792_x1()
                if call.Get() == 1:
                    pass
                elif call.Get() == 0:
                    continue
                elif IsAttackedBySomeone() == 1:
                    break
        elif IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            break
        """State 2"""
        Label('L2')
        DebugEvent('死亡状態')
        Quit()
    """State 3"""
    DebugEvent('被攻撃')
    call = t400792_x0()
    if call.Get() == 1:
        Goto('L2')
    elif call.Get() == 0:
        Goto('L0')
    elif GetDistanceToPlayer() >= 5:
        Goto('L1')
    """Unused"""
    """State 6"""
    t400792_x2()
    Quit()

def t400792_x0():
    """State 0,1"""
    DisplayOneLineHelp(-1)
    """State 2"""
    ClearTalkProgressData()
    ForceEndTalk(0)
    CloseShopMessage()
    CloseMenu()
    ClearTalkListData()
    """State 6"""
    def ExitPause():
        RemoveMyAggro()
    if CheckSelfDeath() == 1:
        """State 19"""
        ClearTalkProgressData()
        ForceEndTalk(0)
        CloseShopMessage()
        CloseMenu()
        """State 9"""
        DebugEvent('死亡')
        if GetDistanceToPlayer() <= 5:
            """State 8"""
            ClearTalkProgressData()
            ForceEndTalk(0)
            CloseShopMessage()
            CloseMenu()
            """State 3"""
            TalkToPlayer(90000080, -1, -1)
            assert HasTalkEnded() == 1
        else:
            pass
        """State 21"""
        return 1
    elif IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
        """State 18"""
        DebugEvent('プレイヤーに攻撃された')
        if GetSelfHP() <= 0 and not GetEventStatus(70000320):
            """State 10,4"""
            # talk:33000700:" "
            TalkToPlayer(33000700, -1, -1)
            assert HasTalkEnded() == 1
            """State 5"""
            SetEventState(70000320, 1)
            """State 7"""
            Label('L0')
            ClearTalkDisabledState()
        elif not GetEventStatus(70000320):
            """State 11"""
            if not GetEventStatus(70000310):
                """State 12,13"""
                TalkToPlayer(90000060, -1, -1)
                assert HasTalkEnded() == 1
                """State 14"""
                SetEventState(70000310, 1)
                Goto('L0')
            elif not GetEventStatus(70000311):
                """State 15,16"""
                TalkToPlayer(90000070, -1, -1)
                assert HasTalkEnded() == 1
                """State 17"""
                SetEventState(70000311, 1)
                Goto('L0')
            else:
                pass
        else:
            pass
    else:
        pass
    """State 20"""
    return 0

def t400792_x1():
    """State 0,1"""
    ClearTalkProgressData()
    ForceEndTalk(0)
    CloseMenu()
    CloseShopMessage()
    ClearTalkListData()
    if CheckSelfDeath() == 1:
        """State 5"""
        return 1
    elif GetEventStatus(1902) == 1:
        pass
    else:
        """State 2"""
        TalkToPlayer(90000030, -1, -1)
        if HasTalkEnded() == 1:
            """State 3"""
            SetEventState(72000004, 1)
        elif IsAttackedBySomeone() == 1:
            pass
    """State 4"""
    return 0

def t400792_x2():
    """State 0,2"""
    DisplayOneLineHelp(-1)
    """State 1"""
    DebugEvent('会話状態')
    """State 11"""
    DebugEvent('会話状態')
    if not GetEventStatus(74009200):
        """State 9"""
        DebugEvent('初回挨拶')
        """State 6"""
        TalkToPlayer(99004000, -1, -1)
        assert HasTalkEnded() == 1
        """State 7"""
        SetEventState(74009200, 1)
        ClearTalkListData()
    else:
        """State 8"""
        DebugEvent('挨拶')
        """State 3"""
        TalkToPlayer(99004000, -1, -1)
        DebugEvent('会話：挨拶')
        assert HasTalkEnded() == 1
        """State 10"""
        ClearTalkListData()
    while True:
        """State 4"""
        # action:15000010:"Purchase Item"
        AddTalkListData(5, 15000010, -1)
        # action:15000005:"Leave"
        AddTalkListData(7, 15000005, -1)
        """State 5"""
        ShowShopMessage(0, 0, 0)
        DebugEvent('会話リスト表示')
        def ExitPause():
            ClearTalkListData()
        if GetTalkListEntryResult() == 5:
            """State 17"""
            DebugEvent('アイテムを買う')
            """State 18"""
            OpenRegularShop(-1, -1)
            assert not GetShopCondition()
        elif GetTalkListEntryResult() == 7:
            """State 12"""
            Label('L0')
            DebugEvent('立ち去る')
            ClearTalkListData()
            """State 13"""
            TalkToPlayer(99004000, -1, -1)
            DebugEvent('会話：雑談')
            assert HasTalkEnded() == 1
            break
        elif not GetTalkListEntryResult():
            Goto('L0')
    """State 20"""
    Label('L1')
    return 0
    """Unused"""
    """State 14"""
    OpenRepairShop()
    DebugEvent('修理ショップ')
    assert not IsMenuOpen(11)
    Goto('L1')
    """State 15"""
    OpenEnhanceShop(0)
    DebugEvent('武器強化')
    assert not IsMenuOpen(11)
    Goto('L1')
    """State 16"""
    OpenEnhanceShop(10)
    DebugEvent('防具強化')
    assert not IsMenuOpen(11)
    Goto('L1')
    """State 19"""
    DebugEvent('武器進化')
    OpenEquipmentChangeOfPurposeShop()
    CombineMenuFlagAndEventFlag(253, 331)
    assert not IsMenuOpen(11)
    Goto('L1')

