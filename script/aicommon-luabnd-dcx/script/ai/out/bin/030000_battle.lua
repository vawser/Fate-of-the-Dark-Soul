RegisterTableGoal(GOAL_NPC_Pact_Fighter, "GOAL_NPC_Pact_Fighter")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_NPC_Pact_Fighter, true)

-------------------------------
-- Setup
-------------------------------
-- Initialize
Goal.Initialize = function (self, ai, goal, arg3)
    return 
end

-- Activate
Goal.Activate = function (self, ai, goal)
    Init_Pseudo_Global(ai, goal)
    
    -- Distance at which to roll
    ai:SetStringIndexedNumber("Dist_Rolling", 5.0)           
    -- Distance at which to backstep
    ai:SetStringIndexedNumber("Dist_BackStep", 2.0)          
    -- Distance to add during walk
    ai:SetStringIndexedNumber("AddDistWalk", 0)
    -- Distance to add during run
    ai:SetStringIndexedNumber("AddDistRun", 0.2)             
    -- Distance at which to end an approach at
    ai:SetStringIndexedNumber("End_Approach_Dist", 1.0)     
    -- Distance at which to end a backwalk at
    ai:SetStringIndexedNumber("End_Backwalk_Dist", 3.0)     
    -- Distance at which to switch to quick backwalk
    ai:SetStringIndexedNumber("Quick_Backwalk_Dist", 5.0)   
    -- Distance at which to switch to quick strafe
    ai:SetStringIndexedNumber("Quick_Strafe_Dist", 5.0)     
    -- Distance at which to end front rolling for approach
    ai:SetStringIndexedNumber("Front_Roll_Approach_Dist", 3.0)
    -- Distance at which to end backstep for retreat
    ai:SetStringIndexedNumber("Backstep_Retreat_Dist", 6.0)
    
    local actChanceList = {}
    local actFuncList = {}
    local actTblList = {}
    
    Common_Clear_Param(actChanceList, actFuncList, actTblList)
    
    -- Values
    local roll_a                = ai:GetRandam_Int(1, 100)
    
    -- Self
    local self_stamina          = ai:GetSp(TARGET_SELF)
    local self_hp_rate          = ai:GetHpRate(TARGET_SELF)
    local self_is_2h            = ai:IsBothHandMode(TARGET_SELF)
    
    -- Enemy
    local enemy_distance        = ai:GetDist(TARGET_ENE_0)
    local enemy_stamina         = ai:GetSp(TARGET_ENE_0)
    local enemy_hp_rate         = ai:GetHpRate(TARGET_ENE_0)
    local enemy_is_guard        = ai:IsTargetGuard(TARGET_ENE_0)
    local enemy_is_2h           = ai:IsBothHandMode(TARGET_ENE_0)

    -- Act Distribution
    actChanceList[1] = 100 -- Light Attack
    actChanceList[2] = 100 -- Heavy Attack
    actChanceList[3] = 20 -- Kick
    actChanceList[4] = 20 -- Heavy Attack (Basic)
    actChanceList[5] = 50 -- Skill
    actChanceList[6] = 20 -- Running Attack
    actChanceList[10] = 0 -- Approach
    actChanceList[11] = 0 -- Retreat
    actChanceList[12] = 0 -- Strafe
    actChanceList[13] = 0 -- Forward Roll
    actChanceList[14] = 0 -- Backstep

    -- Distance Modifiers
    if enemy_distance >= 5 then
        actChanceList[1] = 0 -- Light Attack
        actChanceList[2] = 0 -- Heavy Attack
        actChanceList[3] = 0 -- Kick
        actChanceList[4] = 0 -- Heavy Attack (Basic)
        actChanceList[5] = 0 -- Skill
        actChanceList[6] = 40 -- Running Attack
        actChanceList[10] = 100 -- Approach
        actChanceList[11] = 0 -- Retreat
        actChanceList[12] = 0 -- Strafe
        actChanceList[13] = 0 -- Forward Roll
        actChanceList[14] = 0 -- Backstep
    end
    
    -- Stop chasing once hurt significantly
    if self_hp_rate <= 0.33 then
        actChanceList[10] = 0 -- Approach
    end
    
    -- Boost Kick and Skill if enemy is guarding and we are close
    if enemy_is_guard == true and enemy_distance <= 1 then
        actChanceList[3] = actChanceList[3] + 25 -- Kick
        actChanceList[5] = actChanceList[5] + 10 -- Skull
    
        -- Try and guard break if enemy stamina is low whilst guarding
        if enemy_stamina <= 50 then
            actChanceList[2] = 100 -- Heavy Attack
        end
    end
    
    -- Block the following if stamina when low on stamina
    if self_stamina < 30 then
        actChanceList[5] = 0 -- Skill
        actChanceList[13] = 0 -- Forward Roll
        actChanceList[14] = 0 -- Backstep
    end
    
    -- Block backstep if there is an obstacle behind the AI within 2.6 meters
    if SpaceCheck(ai, goal, 180, ai:GetStringIndexedNumber("Dist_BackStep")) == false then
        actChanceList[14] = 0 -- Backstep
    end
    
    -- Block forward roll if there is an obstacle +/- 45 degrees in front the AI within 4.4 meters
    if SpaceCheck(ai, goal, -45, ai:GetStringIndexedNumber("Dist_Rolling")) == false and 
       SpaceCheck(ai, goal, 45, ai:GetStringIndexedNumber("Dist_Rolling")) == false then
        actChanceList[13] = 0 -- Forward Roll
    end
    
    -- Block backstep walk if there is an obstacle behind the AI within 1 meters
    if SpaceCheck(ai, goal, 180, 1) == false then
        actChanceList[11] = 0 -- Retreat
    end
    
    -- Block strafe if there is an obstacle +/- 90 degrees to the side of the AI within 1 meters
    if SpaceCheck(ai, goal, -90, 1) == false and SpaceCheck(ai, goal, 90, 1) == false then
        actChanceList[12] = 0 -- Strafe
    end
    
    -- Acts
    actFuncList[1] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act01) -- Light Attack
    actFuncList[2] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act02) -- Heavy Attack
    actFuncList[3] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act03) -- Kick
    actFuncList[4] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act04) -- Heavy Attack (Basic)
    actFuncList[5] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act05) -- Skill
    actFuncList[6] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act06) -- Running Attack
    
    actFuncList[10] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act10) -- Approach
    actFuncList[11] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act11) -- Retreat
    actFuncList[12] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act12) -- Strafe
    actFuncList[13] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act13) -- Forward Roll
    actFuncList[14] = REGIST_FUNC(ai, goal, NPC_Pact_Fighter_Act14) -- Backstep 
    
    Common_Battle_Activate(ai, goal, actChanceList, actFuncList, REGIST_FUNC(ai, goal, NPC_Pact_Fighter_ActAfter_AdjustSpace), actTblList)
    return 
end

-------------------------
-- Functions
-------------------------
-- Right Light Attack + Approach
function NPC_Pact_Fighter_Act01(self, ai, goal)
    -- Script
    local roll_A             = self:GetRandam_Int(1, 100)
    local roll_B             = self:GetRandam_Int(1, 100)
    
    -- Self
    local self_Is2H          = self:IsBothHandMode(TARGET_SELF)
    local self_RightWeapon   = self:GetEquipWeaponIndex(ARM_R)
    local self_LeftWeapon    = self:GetEquipWeaponIndex(ARM_L)
    
    -- Enemy
    local enemy_Distance     = self:GetDist(TARGET_ENE_0)
    local enemy_Stamina      = self:GetSp(TARGET_ENE_0)
    local enemy_hp_percent   = self:GetHpRate(TARGET_ENE_0)
    local enemy_IsGuarding   = self:IsTargetGuard(TARGET_ENE_0)
    local enemy_Is2H         = self:IsBothHandMode(TARGET_ENE_0)

    -- Act
    local approachDistance_Minimum  = 2.1
    local approachDistance_Middle   = 2.1
    local approachDistance_Maximum  = 2.1
    
    local approachWeight_Run        = 100
    local approachWeight_WithGuard  = 100
    
    local approachLifetime_Walk     = 1.8
    local approachLifetime_Run      = 2.0
    
    local chance_SwitchHand = 0
    
    -- Switch to Primary Left Weapon
    if self_LeftWeapon ~= WEP_Primary then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0)
    end
    
    -- Vary up weapon hand on approach
    if enemy_Distance >= 1 then
        if not self_Is2H then
            chance_SwitchHand = 25
           
            if enemy_IsGuarding then
                chance_SwitchHand = chance_SwitchHand + 25
            end
            
            if chance_SwitchHand >= roll_A then
                approachWeight_WithGuard = 0
                
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0)
            end
        elseif self_Is2H then
            chance_SwitchHand = 50
            
            if enemy_IsGuarding then
                chance_SwitchHand = chance_SwitchHand - 25
            end
            
            if chance_SwitchHand >= roll_A then
                approachWeight_WithGuard = 100
                
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0)
            end
        end
    end
    
    -- Remove Guard approach if 2H
    if self:IsBothHandMode(TARGET_SELF) then
        approachWeight_WithGuard = 0
    end
    
    -- Remove Guard approach if stamina is low
    if stamina < 60 then
        approachWeight_WithGuard = 0
    end
    
    -- Approach
    NPC_Approach_Act_Flex(self, ai, approachDistance_Minimum, approachDistance_Middle, approachDistance_Maximum, approachWeight_Run, approachWeight_WithGuard, approachLifetime_Walk, approachLifetime_Run)
    
    -- Action
    if roll_B <= 50 then
        if approachWeight_WithGuard > 0 then
            if enemy_Distance >= approachDistance_Maximum then
                -- Strafe around the enemy with Guard up
                if self:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                    ai:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, self:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
                else
                    ai:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, self:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
                end
            end
        end
    end
    
    -- 3 R1s
    if stamina >= 120 then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R1, TARGET_ENE_0, approachDistance_Minimum, 0, 0)
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
    -- 2 R1s
    elseif stamina >= 60 then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R1, TARGET_ENE_0, approachDistance_Minimum, 0, 0)
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
    -- 1 R1
    else
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, approachDistance_Minimum, 0, 0)
    end
    
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Right Heavy Attack + Approach
function NPC_Pact_Fighter_Act02(self, ai, goal)
    local roll_a = self:GetRandam_Int(1, 100)
    local roll_b = self:GetRandam_Int(1, 100)
    local distance = self:GetDist(TARGET_ENE_0)
    local stamina = self:GetSp(TARGET_SELF)
    local max_attack_distance = 2.2
    local roll_c = 100
    
    if self:IsBothHandMode(TARGET_SELF) then
        max_attack_distance = 2.2
        roll_c = 0
    end
    
    if self:GetEquipWeaponIndex(ARM_L) ~= WEP_Primary then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0) -- Switch Weapon (Left)
    end
    
    if 1 <= distance then
        if not self:IsBothHandMode(TARGET_SELF) then
            local roll_d = 25
            
            if self:IsTargetGuard(TARGET_ENE_0) then
                roll_d = roll_d + 25
            end
            
            if roll_a <= roll_d then
                roll_c = 0
                max_attack_distance = 2.2
                
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0) -- Toggle 2H state of Weapon
            end
        elseif self:IsBothHandMode(TARGET_SELF) then
            local roll_d = 50

            if self:IsTargetGuard(TARGET_ENE_0) then
                roll_d = roll_d - 25
            end
            
            if roll_a <= roll_d then
                roll_c = 100
                max_attack_distance = 2.2
                
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0) -- Toggle 2H state of Weapon
            end
        end
    end
    
    if stamina < 60 then
        roll_c = 0
    end
    
    -- Approach
    NPC_Approach_Act_Flex(self, ai, max_attack_distance, max_attack_distance + 0, max_attack_distance + 2, 100, roll_c, 1.8, 2)
    
    if roll_b <= 50 and 0 < roll_c and max_attack_distance <= distance then
        if self:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
            ai:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, self:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold) -- Move and Guard
        else
            ai:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, self:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold) -- Move and Guard
        end
    end
    
    if 60 <= stamina and 67 < roll_a then
        if roll_b <= 50 then
            ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R2, TARGET_ENE_0, max_attack_distance, 0, 0) -- Right Heavy Attack + Approach
            ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 0) -- Right Heavy Attack + Approach
        elseif roll_b <= 75 then
            ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R2, TARGET_ENE_0, max_attack_distance, 0, 0) -- Right Heavy Attack + Approach
            ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2_Hold, TARGET_ENE_0, 999, 0, 0) -- Right Heavy Attack + Approach
        else
            ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_R2_Hold, TARGET_ENE_0, max_attack_distance, 0, 0) -- Right Heavy Attack + Approach
            ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 0) -- Right Heavy Attack + Approach
        end
    elseif roll_b <= 50 then
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2_Hold, TARGET_ENE_0, max_attack_distance, 0, 0)
    else
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2, TARGET_ENE_0, max_attack_distance, 0, 0)
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Kick + Approach
function NPC_Pact_Fighter_Act03(self, ai, goal)
    local roll_a = self:GetRandam_Int(1, 100)
    local roll_b = self:GetRandam_Int(1, 100)
    local distance = self:GetDist(TARGET_ENE_0)
    local max_attack_distance = 1.6
    local roll_c = 0
    
    if self:IsBothHandMode(TARGET_SELF) then
        max_attack_distance = 1.6
        roll_c = 0
    end
    
    if self:GetEquipWeaponIndex(ARM_L) ~= WEP_Primary then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0) -- Switch Weapon (Left)
    end
    
    if self:GetSp(TARGET_SELF) < 50 then
        roll_c = 0
    end
    
    -- Approach
    NPC_Approach_Act_Flex(self, ai, max_attack_distance, max_attack_distance + 0, max_attack_distance + 2, 100, roll_c, 1.8, 2)
    
    ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_Up_R1, TARGET_ENE_0, 999, 0, 0) -- Kick
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Simple Heavy Attack + Approach
function NPC_Pact_Fighter_Act04(self, ai, goal)
    local roll_a = self:GetRandam_Int(1, 100)
    local roll_b = self:GetRandam_Int(1, 100)
    local distance = self:GetDist(TARGET_ENE_0)
    local max_attack_distance = 4.8
    local roll_c = 100
    
    if self:IsBothHandMode(TARGET_SELF) then
        max_attack_distance = 5.6
        roll_c = 0
    end
    
    if self:GetEquipWeaponIndex(ARM_L) ~= WEP_Primary then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0) -- Switch Weapon (Left)
    end
    
    if self:GetSp(TARGET_SELF) < 60 then
        roll_c = 0
    end
    
    -- Approach
    NPC_Approach_Act_Flex(self, ai, max_attack_distance, max_attack_distance + 0, max_attack_distance + 2, 100, roll_c, 1.8, 2)
    
    ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_Up_R2, TARGET_ENE_0, 999, 0, 0) -- Heavy Attack + Approach
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Skill
function NPC_Pact_Fighter_Act05(self, ai, goal)
    local roll_a = self:GetRandam_Int(1, 100)
    local roll_b = self:GetRandam_Int(1, 100)
    local roll_c = self:GetRandam_Int(1, 100)
    local max_attack_distance = 2.6
    local distance = self:GetDist(TARGET_ENE_0)
    
    if not self:IsBothHandMode(TARGET_SELF) then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0) -- Toggle 2H state of Weapon
    end
    
    -- Approach
    NPC_Approach_Act_Flex(self, ai, max_attack_distance, max_attack_distance + 0, max_attack_distance + 2, 100, 100, 1.8, 2)
    
    if roll_a >= 50 then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_L2, TARGET_ENE_0, max_attack_distance, 0, 0) -- WA Start
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, max_attack_distance, 0, 0)  -- WA Right Light Attack + Approach
        
        -- Follow up: WA Right Light Attack + Approach
        if roll_b >= 25 then
            ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, max_attack_distance, 0, 0)  -- WA Right Light Attack + Approach
        end
        
        -- Follow up: WA Right Light Attack + Approach
        if roll_c >= 25 then
            ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, max_attack_distance, 0, 0)  -- WA Right Light Attack + Approach
        end
    else
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_L2, TARGET_ENE_0, max_attack_distance, 0, 0) -- WA Start
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2, TARGET_ENE_0, max_attack_distance, 0, 0)  -- WA Right Heavy Attack + Approach
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Running Attack
function NPC_Pact_Fighter_Act06(self, ai, goal)
    local roll_a = self:GetRandam_Int(1, 100)
    local roll_b = self:GetRandam_Int(1, 100)
    local max_attack_distance = 2.8
    local const_a = 4
    
    if self:IsBothHandMode(TARGET_SELF) then
        max_attack_distance = 3.2
        const_a = -1
    end
    
    if self:GetEquipWeaponIndex(ARM_L) ~= WEP_Primary then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0) -- Switch Weapon (Left)
    end
    
    if 1 <= self:GetDist(TARGET_ENE_0) then
        if not self:IsBothHandMode(TARGET_SELF) then
            local roll_c = 25
            if self:IsTargetGuard(TARGET_ENE_0) then
                roll_c = roll_c + 25
            end
            if roll_a <= roll_c then
                const_a = -1
                max_attack_distance = 3.2
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0) -- Toggle 2H state of Weapon
            end
        elseif self:IsBothHandMode(TARGET_SELF) then
            local roll_c = 50
            if self:IsTargetGuard(TARGET_ENE_0) then
                roll_c = roll_c - 25
            end
            if roll_a <= roll_c then
                const_a = 4
                max_attack_distance = 2.8
                ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonTriangle, TARGET_ENE_0, 999, 0, 0) -- Toggle 2H state of Weapon
            end
        end
    end
    
    if self:GetSp(TARGET_SELF) < 60 then
        const_a = -1
    end
    
    if roll_a <= 50 then
        ai:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, max_attack_distance, TARGET_SELF, const_a)   -- Dash to Enemy
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)               -- Right Light Attack + Approach
    else
        ai:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, max_attack_distance, TARGET_SELF, const_a)   -- Dash to Enemy
        ai:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 0)               -- Right Heavy Attack + Approach
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Approach
function NPC_Pact_Fighter_Act10(self, ai, goal)
    if self:IsBothHandMode(TARGET_SELF) then
        ai:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, TARGET_ENE_0, self:GetStringIndexedNumber("End_Approach_Dist"), TARGET_SELF, false, -1)
    else
        ai:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, TARGET_ENE_0, self:GetStringIndexedNumber("End_Approach_Dist"), TARGET_SELF, false, NPC_ATK_L1Hold)
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Retreat
function NPC_Pact_Fighter_Act11(self, ai, goal)
    local distance = self:GetDist(TARGET_ENE_0)
    local duration = 1.8
    local animation = -1
    
    if distance >= self:GetStringIndexedNumber("Quick_Backwalk_Dist") then
        ai:AddSubGoal(GOAL_COMMON_LeaveTarget, duration, TARGET_ENE_0, self:GetStringIndexedNumber("End_Backwalk_Dist"), TARGET_ENE_0, false, animation) -- Backstep
    else
        ai:AddSubGoal(GOAL_COMMON_LeaveTarget, duration, TARGET_ENE_0, self:GetStringIndexedNumber("End_Backwalk_Dist"), TARGET_ENE_0, true, animation) -- Backstep
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Strafe
function NPC_Pact_Fighter_Act12(self, ai, goal)
    local distance = self:GetDist(TARGET_ENE_0)
    local stamina = self:GetSp(TARGET_SELF)
    local duration = 1.8
    local animation = NPC_ATK_L1Hold
    
    local quick_strafe_distance = 5.0
    
    -- Change to no guard if stamina is low
    if stamina <= 30 then
        animation = -1
    end
    
    local direction = 0
    
    -- Adjust direction based on location, or end early if colliding
    if SpaceCheck(self, ai, -90, 1) == true then
        if SpaceCheck(self, ai, 90, 1) == true then
            if self:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
                direction = 0
            else
                direction = 1
            end
        else
            direction = 0
        end
    elseif SpaceCheck(self, ai, 90, 1) == true then
        direction = 1
    else
        GetWellSpace_Odds = 100
        return GetWellSpace_Odds
    end
    
    if distance >= self:GetStringIndexedNumber("Quick_Strafe_Dist") then
        ai:AddSubGoal(GOAL_COMMON_SidewayMove, duration, TARGET_ENE_0, direction, self:GetRandam_Int(75, 90), false, true, animation) -- Guard with Left Weapon
    else
        ai:AddSubGoal(GOAL_COMMON_SidewayMove, duration, TARGET_ENE_0, direction, self:GetRandam_Int(75, 90), true, true, animation)  -- Guard with Left Weapon
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Forward Roll
function NPC_Pact_Fighter_Act13(self, ai, goal)
    local distance = self:GetDist(TARGET_ENE_0)
    local stamina = self:GetSp(TARGET_SELF)
    
    -- Skip if already next to the target
    if distance <= 1.0 then
        GetWellSpace_Odds = 100
        return GetWellSpace_Odds
    end
    
    if distance >= self:GetStringIndexedNumber("Front_Roll_Approach_Dist") and SpaceCheck(self, ai, 0, self:GetStringIndexedNumber("Dist_Rolling")) == true then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_Up_ButtonXmark, TARGET_ENE_0, 3.0, 0, 0) -- Forward Roll
    end
    
    if stamina >= 60 and distance <= 3.0 then
        local max_attack_distance = 5.8
        local spin_time = 5.4
        
        if self:GetEquipWeaponIndex(ARM_R) == WEP_Primary and self:IsBothHandMode(TARGET_SELF) then
            max_attack_distance = 5.4
            spin_time = 4.6
        end
        
        ai:AddSubGoal(GOAL_COMMON_NPCStepAttack, 10, TARGET_ENE_0, max_attack_distance, spin_time, 50) -- Roll Attack
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-- Backstep
function NPC_Pact_Fighter_Act14(self, ai, goal)
    local distance = self:GetDist(TARGET_ENE_0)
    local stamina = self:GetSp(TARGET_SELF)
    
    -- Skip if already distant from the target
    if distance >= self:GetStringIndexedNumber("Backstep_Retreat_Dist") then
        GetWellSpace_Odds = 100
        return GetWellSpace_Odds
    end
    
    if SpaceCheck(self, ai, 180, self:GetStringIndexedNumber("Dist_BackStep")) == true then
        ai:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 10, NPC_ATK_ButtonXmark, TARGET_ENE_0, 999, 0, 0) -- Roll
    end
    
    if stamina >= 60 and distance <= 2.0 then
        local max_attack_distance = 2.8
        local spin_time = 0.8
        
        if self:GetEquipWeaponIndex(ARM_R) == WEP_Primary and self:IsBothHandMode(TARGET_SELF) then
            max_attack_distance = 3.2
            spin_time = 1
        end
        
        ai:AddSubGoal(GOAL_COMMON_NPCStepAttack, 10, TARGET_ENE_0, max_attack_distance, spin_time, 50) -- Roll Attack
    end
    
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

-------------------------
-- Act After
-------------------------
function NPC_Pact_Fighter_ActAfter_AdjustSpace(self, ai, goal)
    return 
end

-------------------------
-- Update
-------------------------
Goal.Update = function (self, ai, goal)
    return Update_Default_NoSubGoal(self, ai, goal)
end

-------------------------
-- Terminate
-------------------------
Goal.Terminate = function (self, ai, goal)
    return 
end

-------------------------
-- Interrupt
-------------------------
Goal.Interrupt = function (self, ai, goal)
    local stamina   = ai:GetSp(TARGET_SELF)
    local distance  = ai:GetDist(TARGET_ENE_0)
    local roll      = ai:GetRandam_Int(1, 100)
    
    if ai:IsInterupt(INTERUPT_GuardBreak) and distance < 3 then
        goal:ClearSubGoal()
        
        local subgoal = goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, -1, TARGET_SELF, false, 0)
        subgoal:SetLifeEndSuccess(true)
        
        goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, NPC_ATK_R1, TARGET_ENE_0, 999, 0, -1) -- Right Light Attack + Approach
        
        return true
    elseif ai:IsInterupt(INTERUPT_FindAttack) then
        goal:ClearSubGoal()
        if roll >= 75 then
            NPC_Pact_Fighter_Act12(ai, goal, paramTbl) -- Strafe
        else
            NPC_Pact_Fighter_Act13(ai, goal, paramTbl) -- Forward Roll
        end
    end
    
    if ai:IsInterupt(INTERUPT_Shoot) and roll <= 33 and stamina >= 20 then
        goal:ClearSubGoal()
        NPC_Pact_Fighter_Act13(ai, goal, paramTbl) -- Forward Roll
        return true
    else
        return false
    end
end

-------------------------
-- End
-------------------------
return 
