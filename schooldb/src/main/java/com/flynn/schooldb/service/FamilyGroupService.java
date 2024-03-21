package com.flynn.schooldb.service;

import com.flynn.schooldb.entity.AttendanceType;
import com.flynn.schooldb.entity.FamilyGroup;

import java.util.List;
import java.util.Set;

public interface FamilyGroupService {

    Set<FamilyGroup> listAllFamilyMembersByStudentId(Long studentId);


}
