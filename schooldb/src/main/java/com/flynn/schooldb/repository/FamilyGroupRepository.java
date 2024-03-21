package com.flynn.schooldb.repository;

import com.flynn.schooldb.entity.FamilyGroup;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Set;

@Repository
public interface FamilyGroupRepository extends JpaRepository<FamilyGroup, Long> {

    public Set<FamilyGroup> findByStudentStudentId(Long studentId);

    public Set<FamilyGroup> findByStudentStudentIdAndParentGuardianTrue(Long studentId);

    public Set<FamilyGroup> findByStudentStudentIdAndEmergencyPickupTrue(Long studentId);

    public Set<FamilyGroup> findByFamilyMemberFamilyMemberId(Long familyMemberId);

}
