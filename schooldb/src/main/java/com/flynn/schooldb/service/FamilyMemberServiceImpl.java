package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.FamilyMember;
import com.flynn.schooldb.repository.FamilyMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Set;

@Service
public class FamilyMemberServiceImpl implements FamilyMemberService {

    private final FamilyMemberRepository familyMemberRepository;

    @Autowired
    public FamilyMemberServiceImpl(FamilyMemberRepository familyMemberRepository) {
        this.familyMemberRepository = familyMemberRepository;
    }
    @Override
    public List<FamilyMember> familyMemberListAll() {
        return familyMemberRepository.findAll();
    }

    @Override
    public Set<FamilyMember> familyMemberSearchByKeyword(String keyword) {
        return familyMemberRepository.searchByKeyword(keyword);
    }

    @Override
    public Set<FamilyMember> familyMemberFindByLastName(String lastName) {
        return familyMemberRepository.findByLastNameIgnoreCase(lastName);
    }

    @Override
    public Set<FamilyMember> familyMemberFindByFirstName(String firstName) {
        return familyMemberRepository.findByFirstNameIgnoreCase(firstName);
    }

    @Override
    public Set<FamilyMember> familyMemberFindByMiddleName(String middleName) {
        return familyMemberRepository.findByMiddleNameIgnoreCase(middleName);
    }

    @Override
    public Set<FamilyMember> familyMemberFindByPhoneNumber(String phoneNumber) {
        return familyMemberRepository.findByPhoneNumberContains(phoneNumber);
    }
    
}
