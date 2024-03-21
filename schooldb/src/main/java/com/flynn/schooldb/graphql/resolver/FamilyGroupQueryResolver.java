package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.FamilyGroup;
import com.flynn.schooldb.service.FamilyGroupService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.Set;

@Controller
public class FamilyGroupQueryResolver {

    @Autowired
    private FamilyGroupService familyGroupService;

    @QueryMapping
    public Set<FamilyGroup> familyGroupListAllFamilyMembersByStudentId(@Argument Long studentId) {
        return familyGroupService.listAllFamilyMembersByStudentId(studentId);
    }

    @QueryMapping
    public Set<FamilyGroup> familyGroupFindByStudentIdAndParentGuardianTrue(@Argument Long studentId) {
        return familyGroupService.findByStudentStudentIdAndParentGuardianTrue(studentId);
    }

    @QueryMapping
    public Set<FamilyGroup> familyGroupFindByStudentIdAndEmergencyPickupTrue(@Argument Long studentId) {
        return familyGroupService.findByStudentStudentIdAndEmergencyPickupTrue(studentId);
    }

    @QueryMapping
    public Set<FamilyGroup> familyGroupFindByFamilyMemberId(@Argument Long familyMemberId) {
        return familyGroupService.findByFamilyMemberFamilyMemberId(familyMemberId);
    }

}
