package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.FamilyMember;

import java.util.List;
import java.util.Set;

public interface FamilyMemberService {
    List<FamilyMember> familyMemberListAll();

    Set<FamilyMember> familyMemberSearchByKeyword(String keyword);

    Set<FamilyMember> familyMemberFindByLastName(String lastName);

    Set<FamilyMember> familyMemberFindByFirstName(String firstName);

    Set<FamilyMember> familyMemberFindByMiddleName(String middleName);

    Set<FamilyMember> familyMemberFindByPhoneNumber(String phoneNumber);



}
