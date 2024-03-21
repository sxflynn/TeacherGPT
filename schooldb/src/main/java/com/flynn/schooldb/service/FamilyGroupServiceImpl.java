package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.FamilyGroup;
import com.flynn.schooldb.repository.DailyAttendanceRepository;
import com.flynn.schooldb.repository.FamilyGroupRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Set;

@Service
public class FamilyGroupServiceImpl implements FamilyGroupService {

    private final FamilyGroupRepository familyGroupRepository;

    @Autowired
    public FamilyGroupServiceImpl(FamilyGroupRepository familyGroupRepository){
        this.familyGroupRepository = familyGroupRepository;
    }

    @Override
    public Set<FamilyGroup> listAllFamilyMembersByStudentId(Long studentId) {
        return familyGroupRepository.findByStudentStudentId(studentId);
    }
}
