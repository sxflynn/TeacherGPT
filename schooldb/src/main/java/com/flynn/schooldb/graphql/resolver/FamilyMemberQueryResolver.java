package com.flynn.schooldb.graphql.resolver;

import com.flynn.schooldb.entity.FamilyMember;
import com.flynn.schooldb.service.FamilyMemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.List;
import java.util.Set;

@Controller
public class FamilyMemberQueryResolver {

    @Autowired
    private FamilyMemberService familyMemberService;

    @QueryMapping
    public List<FamilyMember> familyMemberListAll() {
        return familyMemberService.familyMemberListAll();
    }

    @QueryMapping
    public Set<FamilyMember> familyMemberSearchByKeyword(@Argument String keyword){
        return familyMemberService.familyMemberSearchByKeyword(keyword);
    }

    @QueryMapping
    public Set<FamilyMember> familyMemberFindByLastName(@Argument String lastName){
        return familyMemberService.familyMemberFindByLastName(lastName);
    }

    @QueryMapping
    public Set<FamilyMember> familyMemberFindByFirstName(@Argument String firstName){
        return familyMemberService.familyMemberFindByFirstName(firstName);
    }

    @QueryMapping
    public Set<FamilyMember> familyMemberFindByMiddleName(@Argument String middleName){
        return familyMemberService.familyMemberFindByMiddleName(middleName);
    }

    @QueryMapping
    public Set<FamilyMember> familyMemberFindByPhoneNumber(@Argument String phoneNumber){
        return familyMemberService.familyMemberFindByPhoneNumber(phoneNumber);
    }

}
